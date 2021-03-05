//应当有一个高频clk捕获和一个内部的小时钟 自定义编码长度 默认发送0 发出信号开始时刻先发送1
//统一起见也给个rst_n?这样方便定义初始状态……
//input [3:0] instruct 4位编码的按钮信息 这里就不需要一个data_vld了
module irda_out(
	input clk,
	input rst_n,
	input [3:0] Iin,
	input  Iin_vld,
	output reg Iout
	);
parameter DIV=/*100000*/50;//计数满100000 传输1bit
parameter FRA=6;//发送4帧数据,但是注意要预留出开头和结尾
	
reg   [3:0]       icache	  ;//暂时存储指令
reg               flag  	  ;
reg   [16:0]      cnt0       ;//1e5个晶振周期发射1个数据,"波特率"为500
wire              add_cnt0   ;
wire              end_cnt0   ;

reg   [ 3:0]      cnt1       ;//4位数据
wire              add_cnt1   ;
wire              end_cnt1   ;

wire  [ 5:0]      data       ;//data应当注意预留够起始位和结束位！！！

always@(posedge clk or negedge rst_n)
	begin
		if (!rst_n)	flag<=0;
		else if (!flag&&Iin_vld) flag<=1;
		else if (end_cnt1) flag<=0;
	end
	
always@(posedge clk or negedge rst_n)
	begin
		if (!rst_n) cnt0<=0;
		else if (add_cnt0) 
			begin
				if(end_cnt0) cnt0<=0;
				else cnt0<=cnt0+1;
			end
	end

assign add_cnt0=flag;
assign end_cnt0=add_cnt0&&(cnt0==DIV-1);

always@(posedge clk or negedge rst_n)
	begin
		if (!rst_n) cnt1<=0;
		else if (add_cnt1) 
			begin
				if(end_cnt1) cnt1<=0;
				else cnt1<=cnt1+1;
			end
	end
	
assign add_cnt1=end_cnt0;
assign end_cnt1=add_cnt1&&(cnt1==FRA-1);

always @ (posedge clk or negedge rst_n) 
	begin
		if(!rst_n) icache<=4'd0;
		else if(!flag&&Iin_vld) icache<=Iin;	//end_cnt1!=0,因此会耐心地等待新信号到达前前一条信号发完
	end	

	
always @ (posedge clk or negedge rst_n) 
	begin
		if(!rst_n) Iout<=1'b0;//默认输出低电平
		else if(add_cnt0&&(cnt0==1-1)) Iout<= data[cnt1];  //使得在rst_n已经使能的情况下，能够在周期的起始位置发送数据
   end	

assign  data = {1'b0,icache,1'b1}; //传输时是从低到高 data = {停止位，数据[7],数据[6] ~ 数据[0],起始位};
endmodule

	
	