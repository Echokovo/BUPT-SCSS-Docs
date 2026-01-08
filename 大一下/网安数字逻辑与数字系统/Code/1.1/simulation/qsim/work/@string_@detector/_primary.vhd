library verilog;
use verilog.vl_types.all;
entity String_Detector is
    port(
        z               : in     vl_logic;
        clock           : in     vl_logic;
        reset           : in     vl_logic;
        f               : out    vl_logic
    );
end String_Detector;
