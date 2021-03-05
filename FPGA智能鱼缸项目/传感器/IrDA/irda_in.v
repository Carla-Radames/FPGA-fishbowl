module irda_in(
	input clk,
	input rst_n,
	input Iin,
	output reg [3:0] Iout,
	output reg Iout_vld
	);

parameter DIV=100000/*50*/;
parameter FRA=6;

reg   [16:0]        cnt0         ;
wire                add_cnt0     ;
wire                end_cnt0     ;

reg   [ 3:0]        cnt1         ;
wire                add_cnt1     ;
wire                end_cnt1     ;

reg                 rx0          ;	//rx0~rx2是一种校验器，用于校验01序列的到来
reg                 rx1          ;	
reg                 rx2          ;	
wire                rx_en        ;

reg                 flag	      ;

//对数据的跨时钟处理，防止出现亚稳态
always @ (posedge clk or negedge rst_n) begin
	if(!rst_n) begin
		  rx0 <= 1'b0;
        rx1 <= 1'b0;
        rx2 <= 1'b0;
	end
	else begin
		  rx0 <= Iin;
        rx1 <= rx0;
        rx2 <= rx1;
	end
end

assign rx_en = ~rx2 & rx1;//01序列检测 即检测上升沿	

always @(posedge clk or negedge rst_n)begin
    if(!rst_n)begin
        cnt0 <= 0;
    end
    else if(add_cnt0)begin
        if(end_cnt0)
            cnt0 <= 0;
        else
            cnt0 <= cnt0 + 1;
    end
end

assign add_cnt0 = flag;
assign end_cnt0 = add_cnt0&&(cnt0==DIV-1);

always @(posedge clk or negedge rst_n)begin 
    if(!rst_n)begin
        cnt1 <= 0;
    end
    else if(add_cnt1)begin
        if(end_cnt1)
            cnt1 <= 0;
        else
            cnt1 <= cnt1 + 1;
    end
end

assign add_cnt1 = end_cnt0;
assign end_cnt1 = add_cnt1&&(cnt1==FRA-2); //去掉一个起始位，一个停止位

always @ (posedge clk or negedge rst_n)begin
	if(!rst_n) begin
		flag<= 1'b0;
	end
	else if(rx_en) begin		
		flag<= 1'b1;	
	end
    else if(end_cnt1) begin		
		flag<= 1'b0;	
	end
end

always @ (posedge clk or negedge rst_n)begin
	if(!rst_n) begin
		Iout<=8'd0;
	end
	else if(add_cnt0&&(cnt0==DIV/2-1)&&(cnt1!=0)) begin		//在中间时刻采样，此时的数据比较稳定，从低位到高位依次采样
	    Iout[cnt1-1]<= rx2 ;//cnt1=0的时刻读取的为起始位，这里直接跳过,且在end_cnt1=0之前就已经完成全体dout的赋值,且在接收下一帧数据前保持
	end
end


//传输完数据信号
always @ (posedge clk or negedge rst_n)begin
	if(!rst_n) begin
		Iout_vld <= 1'b0;
	end
    else if(end_cnt1) begin		
		Iout_vld <= 1'b1;	//接收完成时，发送一个dout_vld脉冲
	end
	else begin	
      Iout_vld <= 1'b0;			
	end
end

endmodule