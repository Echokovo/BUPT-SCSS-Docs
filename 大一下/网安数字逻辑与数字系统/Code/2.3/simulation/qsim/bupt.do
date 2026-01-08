onerror {quit -f}
vlib work
vlog -work work bupt.vo
vlog -work work bupt.vt
vsim -novopt -c -t 1ps -L cyclonev_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.Fulladder_vlg_vec_tst
vcd file -direction bupt.msim.vcd
vcd add -internal Fulladder_vlg_vec_tst/*
vcd add -internal Fulladder_vlg_vec_tst/i1/*
add wave /*
run -all
