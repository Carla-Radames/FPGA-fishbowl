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
// CREATED		"Wed Sep 02 11:41:07 2020"

module UART(
	clk,
	rst_n,
	din,
	rdy,
	dout
);


input wire	clk;
input wire	rst_n;
input wire	din;
output wire	rdy;
output wire	dout;

wire	SYNTHESIZED_WIRE_0;
wire	[7:0] SYNTHESIZED_WIRE_1;





uart_rx	b2v_inst(
	.clk(clk),
	.rst_n(rst_n),
	.din(din),
	.dout_vld(SYNTHESIZED_WIRE_0),
	.dout(SYNTHESIZED_WIRE_1));
	defparam	b2v_inst.BPS = 50;


uart_tx	b2v_inst1(
	.clk(clk),
	.rst_n(rst_n),
	.din_vld(SYNTHESIZED_WIRE_0),
	.din(SYNTHESIZED_WIRE_1),
	.rdy(rdy),
	.dout(dout));
	defparam	b2v_inst1.BPS = 50;


endmodule
