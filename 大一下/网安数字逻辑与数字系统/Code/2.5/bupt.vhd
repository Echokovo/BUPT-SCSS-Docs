library IEEE;
use IEEE.STD_LOGIC_1164.all;
entity Voter is
	port(z:IN STD_LOGIC_VECTOR(3 downto 0);
		  f:OUT STD_LOGIC);
end Voter;

architecture arc of Voter is
begin
	process(z)
	variable count:integer range 0 to 4;
	begin
	count:=0;
	for n in 0 to 3 loop
		if z(n)='1' then      
			count:=count+1;
		end if;
	end loop;
	if(count>=3)then
		f<='1';
	else
		f<='0';
	end if;
	end process;
end arc;