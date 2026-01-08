library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity Count4 IS
	port(clock,reset: IN STD_LOGIC;
		  f          : OUT STD_LOGIC_VECTOR(3 downto 0));
end Count4;

architecture arch of Count4 is
	signal temp:STD_LOGIC_VECTOR(3 downto 0);
begin
	process(clock,reset)
	begin
		if (clock'event AND clock='1') then 
			if (reset='1') then
				temp<=(OTHERS=>'0');
			else
				temp<=temp+1;
			end if;
		end if;
	end process;
	f<=temp;
end arch;