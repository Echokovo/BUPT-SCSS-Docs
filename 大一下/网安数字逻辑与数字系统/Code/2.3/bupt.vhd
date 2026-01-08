library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity Fulladder is
	port(A,B,Cin:IN STD_LOGIC;
		  S,Cout:OUT STD_LOGIC);
end Fulladder;

architecture arch of Fulladder is
begin
	process(A,B,Cin)
	begin
		S<=(A xor B)xor Cin;
		Cout<=((A xor B)and Cin)or(A and B);
	end process;
end arch;