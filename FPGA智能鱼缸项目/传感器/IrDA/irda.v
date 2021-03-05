// Copyright (C) 1991-2013 Altera Corporation
// Your use of Altera Corporation's design tools, logic functions 
// and other software and tools, and its AMPP partner logic 
// functions, and any output files from any of the foregoing 
// (including device programming or simulation files), and any 
// associated documentation or information are expressly subject 
// to the terms and conditions of the Altera Program License 
// Subscription Agreement, Altera MegaCore Function License 
// Agreement, or other applicable license agreement, including, 
// without limitation, that your use is for the sole purpose of 
// programming logic devices manufactured by Altera and sold by 
// Altera or its authorized distributors.  Please refer to the 
// applicable agreement for further details.

// PROGRAM		"Quartus II 64-Bit"
// VERSION		"Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Full Version"
// CREATED		"Fri Sep 04 09:34:51 2020"

module irda(
	clk,
	rst_n,
	C,
	Iout,
	pulse,
	ins,
	R
);


input wire	clk;
input wire	rst_n;
input wire	[3:0] C;
output wire	Iout;
output wire	pulse;
output wire	[3:0] ins;
output wire	[3:0] R;

wire	SYNTHESIZED_WIRE_0;
wire	SYNTHESIZED_WIRE_1;
wire	[3:0] SYNTHESIZED_WIRE_2;

assign	pulse = SYNTHESIZED_WIRE_1;
assign	ins = SYNTHESIZED_WIRE_2;




pulser	b2v_inst(
	.push(SYNTHESIZED_WIRE_0),
	.clk(clk),
	.pulse(SYNTHESIZED_WIRE_1));
	defparam	b2v_inst.DIV = 2500;


irda_out	b2v_inst10(
	.clk(clk),
	.rst_n(rst_n),
	.Iin_vld(SYNTHESIZED_WIRE_1),
	.Iin(SYNTHESIZED_WIRE_2),
	.Iout(Iout));
	defparam	b2v_inst10.DIV = 50;
	defparam	b2v_inst10.FRA = 6;


keyboard	b2v_inst7(
	.clk(clk),
	.C(C),
	.push(SYNTHESIZED_WIRE_0),
	.ins(SYNTHESIZED_WIRE_2),
	.R(R));


endmodule
