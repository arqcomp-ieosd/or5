library IEEE;
use IEEE.std_logic_1164.all;

entity programcounter is
    generic (DATA_SIZE: integer :=32);
    
    port( DATA_i   : in  std_logic_vector(DATA_SIZE-1 downto 0);
          EN_i     : in  std_logic;
          RST_i  : in  std_logic;
          CLK_i    : in  std_logic;
          DATA_o   : out std_logic_vector(DATA_SIZE-1 downto 0)
          );
end programcounter;

            
architecture PC_arch of ProgramCounter is
begin

program_counter: process(RST_i, CLK_i, DATA_i, EN_i) 
begin
    if RST_i = '1' then
        DATA_o <= (others => '0'); 
    elsif rising_edge(CLK_i) then
        if EN_i = '1' then
            DATA_o <= DATA_i;
        end if;
    end if;
end process;

end PC_arch;