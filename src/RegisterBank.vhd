library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


ENTITY registerbank IS
    GENERIC (
        size_of_register     : integer := 64;  -- cantidad de bits registros
        amount_registers_dir : integer := 5
           );  -- cantidad de bits de direccionamiento a registros
    PORT(
        A_i     : IN     std_logic_vector(amount_registers_dir - 1 downto 0);
        B_i     : IN     std_logic_vector(amount_registers_dir - 1 downto 0);
        C_i     : IN     std_logic_vector(amount_registers_dir - 1 downto 0);    
        Reg_W_i : IN     std_logic;
        RST_i   : IN     std_logic;
        CLK_i   : IN     std_logic;  -- Se propone eliminar el reloj, ya que registra las entradas y no permite que el uP funcione en un solo clock por instruccion
        W_c_i   : IN     std_logic_vector(size_of_register - 1 downto 0);
        R_a_o   : OUT    std_logic_vector(size_of_register - 1 downto 0);
        R_b_o   : OUT    std_logic_vector(size_of_register - 1 downto 0)
    );
END ENTITY registerbank;

ARCHITECTURE registerbank_arch OF registerbank IS

TYPE ram_memory IS ARRAY ( 2**amount_registers_dir - 1 downto 0 ) OF std_logic_vector(size_of_register - 1 downto 0);

signal bank: ram_memory:=(others=>x"0000000000000000");
    
BEGIN

Registros : PROCESS (CLK_i,C_i,Reg_W_i,W_c_i) IS
BEGIN
    IF RST_i = '1' then
        bank <= (OTHERS=>std_logic_vector(to_unsigned(0,size_of_register)));
    ELSIF (rising_edge(CLK_i) and Reg_W_i = '1' and to_integer(unsigned(C_i))/=0)  THEN
        bank(to_integer(unsigned(C_i))) <= W_c_i; 
    END IF;
END PROCESS Registros;

R_a_o <= bank(to_integer(unsigned(A_i)));      
R_b_o <= bank(to_integer(unsigned(B_i)));

END ARCHITECTURE registerbank_arch;