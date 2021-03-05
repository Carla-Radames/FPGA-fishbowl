//需要一个这样的模块 当按下按钮的时刻 过一段时间发出一个脉冲信号以驱动红外发送模块
//push表示正在按压
module pulser(	//矩阵键盘输出到
	//input [3:0] ins,
	input push,
	input clk,//每间隔6/500s以上发出一个脉冲
	output reg pulse
	);
reg [18:0] cnt;
wire end_cnt;
parameter DIV=/*5000000*/2500;
always @(posedge clk)
	begin
		if(!push) cnt<=0;
		else if (!end_cnt) cnt<=cnt+1;
		else cnt<=0;
	end

assign end_cnt=(cnt==DIV-1);
	
always @(posedge clk)
	begin
		if(push&&end_cnt) pulse<=1;
		else pulse<=0;
	end
endmodule