library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Register8 is
	port (D:IN STD_LOGIC_VECTOR(7 downto 0);
			CLK,OE:IN STD_LOGIC;
			Q:OUT STD_LOGIC_VECTOR(7 downto 0));
end Register8;

architecture arch of Register8 is
	signal temp:STD_LOGIC_VECTOR(7 downto 0);
begin
	process(CLK,OE)
	begin
		if (OE = '0') then
			if (CLK'event and CLK = '1') then
				temp<=D;
			end if;
		else
			temp<="ZZZZZZZZ";
		end if;
		Q<=temp;
	end process;
end arch;