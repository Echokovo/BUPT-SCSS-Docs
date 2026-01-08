library verilog;
use verilog.vl_types.all;
entity Voter is
    port(
        z               : in     vl_logic_vector(3 downto 0);
        f               : out    vl_logic
    );
end Voter;
