library verilog;
use verilog.vl_types.all;
entity Decoder3to8_vlg_sample_tst is
    port(
        A               : in     vl_logic;
        B               : in     vl_logic;
        C               : in     vl_logic;
        G1              : in     vl_logic;
        G2A             : in     vl_logic;
        G2B             : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end Decoder3to8_vlg_sample_tst;
