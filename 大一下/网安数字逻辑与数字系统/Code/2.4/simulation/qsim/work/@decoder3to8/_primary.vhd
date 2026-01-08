library verilog;
use verilog.vl_types.all;
entity Decoder3to8 is
    port(
        G1              : in     vl_logic;
        G2A             : in     vl_logic;
        G2B             : in     vl_logic;
        A               : in     vl_logic;
        B               : in     vl_logic;
        C               : in     vl_logic;
        Y               : out    vl_logic_vector(7 downto 0)
    );
end Decoder3to8;
