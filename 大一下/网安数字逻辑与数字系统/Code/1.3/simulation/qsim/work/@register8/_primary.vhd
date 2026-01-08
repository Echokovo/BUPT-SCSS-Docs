library verilog;
use verilog.vl_types.all;
entity Register8 is
    port(
        D               : in     vl_logic_vector(7 downto 0);
        CLK             : in     vl_logic;
        OE              : in     vl_logic;
        Q               : out    vl_logic_vector(7 downto 0)
    );
end Register8;
