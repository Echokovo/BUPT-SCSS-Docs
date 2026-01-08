library verilog;
use verilog.vl_types.all;
entity Voter_vlg_sample_tst is
    port(
        z               : in     vl_logic_vector(3 downto 0);
        sampler_tx      : out    vl_logic
    );
end Voter_vlg_sample_tst;
