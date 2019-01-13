----------------------------------------------------------------------------------
-- Company:  RAT Technologies
-- Engineer:  Various RAT rats
-- 
-- Create Date:    3/10/2017
-- Module Name:    RAT_wrapper - Behavioral 
-- Target Devices: Basys3
-- Description: Wrapper for RAT CPU. This model provides a template to interfaces 
--    the RAT CPU to the Basys3 development board. 
--
-- Revision: 
-- Revision 0.01 - File Created
--          0.10 - Update to include new keyboard driver        
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity RAT_wrapper is
    Port ( LEDS     : out   STD_LOGIC_VECTOR (7 downto 0);
           CATHODES : out   STD_LOGIC_VECTOR (7 downto 0);
           ANODES   : out   STD_LOGIC_VECTOR (3 downto 0);
           SWITCHES : in    STD_LOGIC_VECTOR (7 downto 0);
           RST      : in    STD_LOGIC;
           CLK  	: in    STD_LOGIC;
           PS2D		: in  	STD_LOGIC; 						-- PS/2 data signal
           PS2C		: in	STD_LOGIC; 						-- PS/2 clock signal
end RAT_wrapper;

architecture Behavioral of RAT_wrapper is

   -- INPUT PORT IDS -------------------------------------------------------------
   -- Right now, the only possible inputs are the switches
   -- In future labs you can add more port IDs, and you'll have
   -- to add constants here for the mux below
   CONSTANT SWITCHES_ID : STD_LOGIC_VECTOR (7 downto 0) := X"20";
   CONSTANT KEYBOARD_ID : STD_LOGIC_VECTOR (7 downto 0) := X"44"; 
   -------------------------------------------------------------------------------
   
   -------------------------------------------------------------------------------
   -- OUTPUT PORT IDS ------------------------------------------------------------
   -- In future labs you can add more port IDs
   CONSTANT LEDS_ID      : STD_LOGIC_VECTOR (7 downto 0) := X"40";
   CONSTANT SSEG_ID      : STD_LOGIC_VECTOR (7 downto 0) := X"81";
   -------------------------------------------------------------------------------

   -- Declare RAT_CPU ------------------------------------------------------------
   component RAT_CPU 
       Port ( IN_PORT  : in  STD_LOGIC_VECTOR (7 downto 0);
              OUT_PORT : out STD_LOGIC_VECTOR (7 downto 0);
              PORT_ID  : out STD_LOGIC_VECTOR (7 downto 0);
              IO_STRB  : out STD_LOGIC;
              RST      : in  STD_LOGIC;
              INT_IN   : in  STD_LOGIC;
              CLK      : in  STD_LOGIC);
   end component RAT_CPU;
   -------------------------------------------------------------------------------
      
   -- Declare sseg_dec -----------------------------------------------------------  
   component sseg_dec is
       Port ( ALU_VAL  : in  std_logic_vector(7 downto 0);
              CLK 	   : in  std_logic;
              DISP_EN  : out std_logic_vector(3 downto 0);
              SEGMENTS : out std_logic_vector(7 downto 0));
   end component sseg_dec;

   -- Declare PS/2 Receiver ----------------------------------------------------	
	component KeyboardDriver
   	Port (	clk		: in  STD_LOGIC;
   			keyclk	: in  STD_LOGIC;
   			keydata	: in  STD_LOGIC;
   			keycode	: out STD_LOGIC_VECTOR (7 downto 0);
   			intrpt	: out STD_LOGIC);
   end component KeyboardDriver;
   
   -- Signals for connecting RAT_CPU to RAT_wrapper -------------------------------
   signal s_input_port  : std_logic_vector (7 downto 0);
   signal s_output_port : std_logic_vector (7 downto 0);
   signal s_port_id     : std_logic_vector (7 downto 0);
   signal s_load        : std_logic;
   signal s_interrupt   : std_logic;
   
   signal s_clk_sig     : std_logic := '0';	-- 50 MHz clock      
   
   -- Register definitions for output devices ------------------------------------
   signal r_LEDS        : std_logic_vector (7 downto 0); 
   signal r_SSEG        : std_logic_vector (7 downto 0);

   -- Keyboard signals --------------------------------------------------------------
	signal keyready   : std_logic;
	signal ps2KeyCode : std_logic_vector(7 downto 0);
	
begin	

   -- Instantiate RAT_CPU --------------------------------------------------------
   CPU: RAT_CPU
   port map(  IN_PORT  => s_input_port,
              OUT_PORT => s_output_port,
              PORT_ID  => s_port_id,
              RST      => RST,  
              IO_STRB  => s_load,
              INT_IN   => s_interrupt,
              CLK      => s_clk_sig);         
   -------------------------------------------------------------------------------
   
   -- Instantiate sseg_dec -------------------------------------------------------              
   SG: sseg_dec
   port map (     ALU_VAL  => r_SSEG,
                  CLK      => s_clk_sig,
                  DISP_EN  => ANODES,
                  SEGMENTS => CATHODES);
   ------------------------------------------------------------------------------
      
   -- Instantiate VGA Driver ---------------------------------------------------
   VGA: vgaDriverBuffer
   port map( CLK => s_clk_sig,
             WE 		=> r_vga_we,
             WA 		=> r_vga_wa,
             WD 		=> r_vga_wd,
             Rout 		=> VGA_RGB(7 downto 5),
             Gout 		=> VGA_RGB(4 downto 2),
             Bout		=> VGA_RGB(1 downto 0),
             HS 		=> VGA_HS,
             VS 		=> VGA_VS,
             pixelData 	=> r_vgaData);
   -------------------------------------------------------------------------------
   
   -- Instantiate Keyboard Driver ------------------------------------------------  
   KEYBOARD: KeyboardDriver
   port map ( clk 		=> s_clk_sig,
	    	  keyclk 	=> PS2C,
	    	  keydata 	=> PS2D,
	    	  keycode 	=> ps2KeyCode,
	    	  intrpt 	=> keyready);
   --------------------------------------------------------------------------------

   -- Clock Divider Process ------------------------------------------------------
   clkdiv: process(CLK)
    begin
        if RISING_EDGE(CLK) then
            s_clk_sig <= NOT s_clk_sig;
        end if;
    end process clkdiv;
   -------------------------------------------------------------------------------

   ------------------------------------------------------------------------------- 
   -- MUX for selecting what input to read ---------------------------------------
   -------------------------------------------------------------------------------
   inputs: process(s_clk_sig, s_port_id, SWITCHES, r_vgaData, ps2KeyCode)
   begin
      if s_port_id = SWITCHES_ID then
    	s_input_port <= SWITCHES;
      elsif s_port_id = KEYBOARD_ID then
    	s_input_port <= ps2KeyCode;
   	  else
    	s_input_port <= x"00";
      end if;
   end process inputs;
   -------------------------------------------------------------------------------

   -------------------------------------------------------------------------------
   -- MUX for updating output registers ------------------------------------------
   -- Register updates depend on rising clock edge and asserted load signal
   -------------------------------------------------------------------------------
   outputs: process(s_clk_sig) 
   begin   
      if (rising_edge(s_clk_sig)) then
         if (s_load = '1') then 
            if (s_port_id = LEDS_ID) then
               r_LEDS <= s_output_port;
            elsif(s_port_id = SSEG_ID) then
               r_SSEG <= s_output_port;
            end if;  
         end if; 
      end if;
   end process outputs;      
   -------------------------------------------------------------------------------

   -- Register Interface Assignments ---------------------------------------------
   LEDS <= r_LEDS; 
   
   -- Signal Assignments ---------------------------------------------------------
   s_interrupt <= keyready;		-- combine all interrupts

end Behavioral;
