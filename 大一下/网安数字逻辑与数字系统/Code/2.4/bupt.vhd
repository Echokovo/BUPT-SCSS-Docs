library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity Decoder3to8 is
	port (G1,G2A,G2B,A,B,C:IN STD_LOGIC;
			Y:OUT STD_LOGIC_VECTOR (7 downto 0));
end Decoder3to8;

architecture arch of Decoder3to8 is
signal temp:STD_LOGIC_VECTOR (5 downto 0);
begin
	process(G1,G2A,G2B,A,B,C)
	begin
		temp<=G1 & G2A & G2B & C & B & A;
		case temp is
			when "100000" =>Y<="01111111";
			when "100001" =>Y<="10111111";
			when "100010" =>Y<="11011111";
			when "100011" =>Y<="11101111";
			when "100100" =>Y<="11110111";
			when "100101" =>Y<="11111011";
			when "100110" =>Y<="11111101";
			when "100111" =>Y<="11111110";
			when others=>NULL;
		end case;
	end process;
end arch;