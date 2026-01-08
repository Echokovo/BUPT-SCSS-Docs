library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity Encoder8421toGray is
	port (z:IN STD_LOGIC_VECTOR(3 downto 0);
			f:OUT STD_LOGIC_VECTOR(3 downto 0));
end Encoder8421toGray;

architecture arch of Encoder8421toGray is
	signal temp:STD_LOGIC_VECTOR(3 downto 0);
	begin
	process(z)
	begin
		temp(3)<=z(3);
		for i in 2 downto 0 loop
			temp(i)<=z(i+1) xor z(i);
		end loop;
		f<=temp;
	end process;
end arch;