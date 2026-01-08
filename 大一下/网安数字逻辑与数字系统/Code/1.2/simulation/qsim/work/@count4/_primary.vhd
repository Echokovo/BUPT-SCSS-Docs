library verilog;
use verilog.vl_types.all;
entity Count4 is
    port(
        clock           : in     vl_logic;
        reset           : in     vl_logic;
        f               : out    vl_logic_vector(3 downto 0)
    );
end Count4;
