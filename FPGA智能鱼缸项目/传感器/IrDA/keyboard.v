//键盘 当按下后能够转成4位数据且按下时会给出push信号
//注意防抖
//1.矩阵键盘模块
//此模块尚未调试
module keyboard(clk,R,push,C,ins);
input clk;
input [3:0] C;
output reg [3:0] R;
output reg [3:0] ins;
output reg push;//保证脉冲模块正常工作
//向外输出的ins是一个4位二进制数……
reg [6:0] count;//防抖计数

always @(posedge clk)
	begin
	//S0状态，跑马灯模式
		if (C==4'b1111)//倘若列线没有输入信号
			begin
				count=0;
				push=0;		//当且仅当按键松开时才能保证push归0
				ins=4'b1111;//未检测到信号向外输出1111
				//跑马灯开始
				case(R)
					4'b0111:R=4'b1011;
					4'b1011:R=4'b1101;
					4'b1101:R=4'b1110;
					4'b1110:R=4'b0111;
					default:R=4'b0111;//一定要加上这句，才能让R进入跑马灯模式
				endcase
			end
			
		else 
		//防抖按钮
			begin
				if (count<10)
					begin
						count=count+1;
						ins=4'b1111;//ins的值注意要进行维护,这句语句理论上可以不要
					end
				else 
		//开始数据输出 
		//下面选取几种特殊情况进行指令的编码即可
					begin
						if (R==4'b0111) ins=1;
						else if (R==4'b1011) ins=5;
						else if (R==4'b1101) ins=9;
						else if (R==4'b1110) ins=12;
							
						if (C==4'b1011) ins=ins+1;
						else if (C==4'b1101) ins=ins+2;
						else if (C==4'b1110) ins=ins+3;
							
						if (R==4'b1101&&C==4'b1011) ins=0;
						if (R==4'b1101&&C==4'b1101) ins=10;
						if (R==4'b1101&&C==4'b1110) ins=11;//修正第三行
						push=1;
						//FSM开始读数,先给ins置位再给push置位，防止竞争冒险;
						//如果第二次上升沿到来时按键还被按住，则push和ins依然保持不变；
					end
			end
	end	
endmodule 

