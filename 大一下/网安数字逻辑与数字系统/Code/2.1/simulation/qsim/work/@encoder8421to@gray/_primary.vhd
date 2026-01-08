library verilog;
use verilog.vl_types.all;
entity Encoder8421toGray is
    port(
        z               : in     vl_logic_vector(3 downto 0);
        f               : out    vl_logic_vector(3 downto 0)
    );
end Encoder8421toGray;
