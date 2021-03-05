//删掉din_vld 和rdy信号之后，只需要把计数器cnt0计数条件改为add_cnt0 = 1,就可以了
//还是需要一个din_vld的，方便模拟arduino的delay(1000);
//就使用晶振自带的时钟即可
`timescale 1ns / 1ps
	
module uart_tx(
                 input             clk    ,			
                 input             rst_n  ,		 //注意，rst_n为了保证程序块的正常执行必须始终为1
                 input [7:0]       din    ,
                 input             din_vld,	 //开始发送信号，可以设计成给一个尖峰
                 output reg        rdy    ,  //类似接收的完成信号，表示完成了一个字节的传输，同din_vld信号一样，不要可以删掉
                 output reg        dout   
             );

parameter         BPS    = 5208;		//BPS bit/s这里并不是真的这个意思 5208个周期才能传输出去1bit
														//含义：多少个FPGA周期等同于arduino周期
												//arduino:9600波特率 FPGA:1/50M传输1bit数据 测试：调为1s传输

reg   [7:0]       tx_data_tmp;	

reg               flag_add   ;
reg   [14:0]      cnt0       ;
wire              add_cnt0   ;
wire              end_cnt0   ;

reg   [ 3:0]      cnt1       ;
wire              add_cnt1   ;
wire              end_cnt1   ;

wire  [ 9:0]      data       ;

always  @(posedge clk or negedge rst_n)begin
    if(rst_n==1'b0)begin
        flag_add <= 0;
    end
	 else if(flag_add==0 && din_vld)begin	//flag_add被赋值，正式开始数据的传输，
														//注意，实际上如果没有din_vld,flag_add=0,下面的并行程序块都不会进入！！！
														//同时 一旦程序块开始 div_vld本身应该不会再中断程序的执行……
        flag_add <= 1;							//flag_add=1，在end_cnt1前绝不会再回到这个分支，div_vld无意义。
    end
    else if(end_cnt1)begin
        flag_add <= 0;
    end
	 //不使用din_vld的版本
	 /*
	 else if(end_cnt1)begin
			flag_add<=0;
	 end
	 else flag_add<=1;
	 */
end

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

assign add_cnt0 = flag_add;
assign end_cnt0 = add_cnt0 && cnt0==BPS-1 ; //当且仅当cnt0计数达到所需频率时才输出1次

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
assign end_cnt1 = add_cnt1 && cnt1==10-1 ;


always @ (posedge clk or negedge rst_n) begin
	if(!rst_n) begin
		tx_data_tmp <=8'd0;
	end
	else if(flag_add==1'b0 && din_vld) begin	  //这里时序很有可能会出错，主要是抢flag_add=0且刚好rst_n=1的那个瞬间
		tx_data_tmp <= din;	
	end
end

always @ (posedge clk or negedge rst_n) begin
	if(!rst_n) begin
		dout <= 1'b1;							 //1输出，等同于拉高总线
	end
	else if(add_cnt0 && cnt0==1-1)begin  //cnt0在每个cnt0周期的最开头输出一次，这个时刻刚好rst_n=1且cnt0未更新
	//每个cnt0周期结束的时刻即end_cnt0=1时刻，在刚变化的前一个周期处cnt0=5207,后一个周期处add_cnt0=0，不会引发误差
        dout<= data[cnt1];
    end 
end

assign  data = {1'b1,tx_data_tmp,1'b0}; //传输时是从低到高 data = {停止位，数据[7],数据[6] ~ 数据[0],起始位};

always  @(*)begin
    if(din_vld||flag_add)//只是加强了条件
        rdy = 1'b0;
    else
        rdy = 1'b1;
end

endmodule
