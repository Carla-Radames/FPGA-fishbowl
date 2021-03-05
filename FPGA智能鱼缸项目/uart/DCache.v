//这个模块应当能够读取从arduino发回来的若干组串口信号信号并且分为5个字节的形式存储到存储器中
//如果发送1.234，理论上是先发送高位1的ascii码的从低到高的序列,最后发送4的从低到高的序列，并且这个低到高的顺序保存在uart_rx的dout低到高中
//通过dout_vld确定目前接收到第几位字节，通过2位和arduino的通信线add确定写入位置
//需要一个rst_n初始化cnt……
//还需要一个4位串行数据转2位高低电平的模块
module DCache(
	input [7:0] din,			//8位数据输入
	input [1:0] add,			//2位地址输入
	input clk,			//默认时钟
	//input rst_n;		//用于初始化上电时刻cnt的状态
	input dout_vld,	//每次捕捉到 写入位置平移8
	//output reg [39:0] RF [3:0]//生成4个40位寄存器 
	output reg [39:0] temp,			//温度寄存器
	output reg [39:0] humi,			//湿度寄存器
	output reg [39:0] pres,			//压强寄存器
	output reg [39:0] forc			//压力寄存器
	);

reg [3:0] cnt;//0~4=FRA-1之间循环
//reg state;//状态机，在IDLE,
reg [39:0] cache;//用于暂时性存储数据 
reg i;//用于选择对应的寄存器号

parameter FRA=5;//接收5帧数据
//cnt初始应当为0……祈祷能？
initial cnt<=0;
initial cache<=0;
//initial state<=0;
//initial i<=0;

/*
always@(posedge clk)
	begin
		case (add)
			2'b00:i<=0;
			2'b01:i<=1;
			2'b10:i<=2;
			2'b11:i<=3;
		endcase
	end
*/	
//能否引入一个delay函数，以防止时序冲突？

always @(posedge dout_vld)
	begin
		cnt<=cnt+1;
		//这里很可能出错,如果我在执行到一半的时刻修改了add该怎么办？
		//此时高3位数据还在cache中，低2位数据会变成错误数据，但是最终写入的不是最开始的存储器，新存储器的值随着稳定一次次传输又会被不断修改直到正确
		if (cnt==FRA)//这个时候理论上数据还未传输完成，还差一位停止位，设计上add保持，异步时钟
			begin 
				case (add)
					2'b00:temp<=cache;
					2'b01:humi<=cache;
					2'b10:pres<=cache;
					2'b11:forc<=cache;
				endcase
				cnt<=0;//当计数完成后清零
			end
	end

always @(posedge dout_vld)
	begin
		//这里很有可能出错，din已经更新，cnt可能还没来得及更新
		//最好能delay一下下
		#2//竟然可以使用delay……
		case (cnt)
			0:cache[39:32]<=din;
			1:cache[31:24]<=din;
			2:cache[23:16]<=din;
			3:cache[15:8] <=din;
			4:cache[7:0]  <=din;
		endcase
	end
	
endmodule