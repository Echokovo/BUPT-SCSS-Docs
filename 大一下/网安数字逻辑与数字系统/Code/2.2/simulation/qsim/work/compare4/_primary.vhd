library verilog;
use verilog.vl_types.all;
entity compare4 is
    port(
        A               : in     vl_logic_vector(3 downto 0);
        B               : in     vl_logic_vector(3 downto 0);
        YA              : out    vl_logic;
        YB              : out    vl_logic;
        YC              : out    vl_logic
    );
end compare4;
