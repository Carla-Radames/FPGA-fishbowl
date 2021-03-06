onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /irda_vlg_tst/C
add wave -noupdate /irda_vlg_tst/clk
add wave -noupdate /irda_vlg_tst/rst_n
add wave -noupdate /irda_vlg_tst/Iout
add wave -noupdate /irda_vlg_tst/R
add wave -noupdate -expand /irda_vlg_tst/ins
add wave -noupdate /irda_vlg_tst/pulse
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {0 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 150
configure wave -valuecolwidth 100
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ps
update
WaveRestoreZoom {0 ps} {64 ns}
