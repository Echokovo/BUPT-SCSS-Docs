library ieee;
use ieee.std_logic_1164.all;

entity String_Detector is
	port(z,clock,reset: in bit;
	     f: out bit);
end String_Detector;

architecture arch of String_Detector is
	type state is (s0,s1,s2,s3,s4,s5,s6,s7);
	signal pr_state,nx_state: state;
begin
	process(reset,clock)
	begin
		if (reset = '1') then
			pr_state <= s0;
		elsif (clock'event and clock = '1') then
			pr_state <= nx_state;
		end if;
	end process;
	process(z,pr_state)
	begin
		case pr_state is
			when s0 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s0;
				else
					nx_state <= s1;
				end if;
			when s1 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s0;
				else
					nx_state <= s2;
				end if;
			when s2 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s0;
				else
					nx_state <= s3;
				end if;
			when s3 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s4;
				else
					nx_state <= s3;
				end if;
			when s4 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s5;
				else
					nx_state <= s1;
				end if;
			when s5 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s0;
				else
					nx_state <= s6;
				end if;
			when s6 =>
				f <= '0';
				if (z = '0') then
					nx_state <= s7;
				else
					nx_state <= s2;
				end if;
			when s7 =>
				f <= '1';
				if (z = '0') then
					nx_state <= s0;
				else
					nx_state <= s1;
				end if;
		end case;
	end process;
end arch;