library verilog;
use verilog.vl_types.all;
entity Fulladder_vlg_check_tst is
    port(
        Cout            : in     vl_logic;
        S               : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end Fulladder_vlg_check_tst;
