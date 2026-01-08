library verilog;
use verilog.vl_types.all;
entity String_Detector_vlg_sample_tst is
    port(
        clock           : in     vl_logic;
        reset           : in     vl_logic;
        z               : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end String_Detector_vlg_sample_tst;
