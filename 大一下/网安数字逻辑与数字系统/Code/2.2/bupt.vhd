library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity compare4 is
	port (A,B:IN STD_LOGIC_VECTOR (3 downto 0);
			YA,YB,YC:OUT STD_LOGIC);
end compare4;

architecture arch of compare4 is
begin
	process(A,B)
	begin
		if (A>B) then
			YA<='1';
			YB<='0';
			YC<='0';
		elsif (A<B) then
			YA<='0';
			YB<='1';
			YC<='0';
		else
			YA<='0';
			YB<='0';
			YC<='1';
		end if;
	end process;
end arch;