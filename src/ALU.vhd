library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity alu is

generic (N : integer :=64);
port (
      A_i      : in  std_logic_vector(N - 1 downto 0);
      B_i      : in  std_logic_vector(N - 1 downto 0);
      OUTPUT_o    : out std_logic_vector(N - 1 downto 0);
      ALUop_i  : in  std_logic_vector(3 downto 0);
      Zero_o   : out std_logic
      );
end entity;

architecture alu_arch of alu is

constant AND_IN : std_logic_vector(3 downto 0) := "0000";  -- As defined in the book
constant OR_IN  : std_logic_vector(3 downto 0) := "0001";  -- As defined in the book
constant ADD    : std_logic_vector(3 downto 0) := "0010";  -- As defined in the book
constant XOR_IN : std_logic_vector(3 downto 0) := "0101";
constant SUB    : std_logic_vector(3 downto 0) := "0110";  -- As defined in the book

constant SLL_IN : std_logic_vector(3 downto 0) := "1000";
constant SRL_IN : std_logic_vector(3 downto 0) := "1001";
constant SLA_IN : std_logic_vector(3 downto 0) := "1010";
constant SRA_IN : std_logic_vector(3 downto 0) := "1011";

signal output_s : std_logic_vector(N-1 downto 0);

begin
-- Se analiza el flag Z

OUTPUT_o <= output_s;

Zero_o <= '1' when output_s = std_logic_vector(to_unsigned(0,N)) else '0'; 

process(A_i, B_i, ALUop_i)

variable aux1 : std_logic;
variable aux2 : std_logic_vector(N-1 downto 0);

begin
    case ALUop_i is
        when ADD =>
            output_s <= std_logic_vector((unsigned(A_i) + unsigned(B_i)));
        when SUB =>
            output_s <= std_logic_vector((unsigned(A_i) - unsigned(B_i)));
        when AND_IN =>
            output_s <= A_i and B_i;
        when OR_IN =>
            output_s <= A_i or B_i;
        when XOR_IN =>
            output_s <= A_i xor B_i;
        when SLL_IN =>
            output_s <= std_logic_vector(shift_left(unsigned(A_i), to_integer(unsigned(B_i))));
        when SRL_IN =>
            output_s <= std_logic_vector(shift_right(unsigned(A_i), to_integer(unsigned(B_i))));
        when SLA_IN =>
            output_s <= std_logic_vector(shift_left(signed(A_i), to_integer(unsigned(B_i))));
        when SRA_IN =>
            output_s <= std_logic_vector(shift_right(signed(A_i), to_integer(unsigned(B_i))));
        when others => output_s <= (others => '0');        
    end case;
        
    end process;
end alu_arch;














