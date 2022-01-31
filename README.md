
# SAGv.1 Processor
SAGv.1 a application specific integrated circuit (ASIC) design process temperature sensor data of thousands of machines.

## 1. CPU Specifications

 - 16 - bit architecture
 - BIG endian
 - Max Clock Speed 200MHz
 - 4 General Purpose registers
 - 127 Assembly Instruction capabilities
 - 8 addressing modes
 - Use 3 data busses

## 2. ALU Capabilities and Instructions
The arithmatic logic unit of the CPU is carefully designed for specific mathematical operations needed for temperature process. And also there are two ALU flags to indicate ZERO and NEGETIVE numbers.
| Hex code | Bin representation | Operation | Descreption |
|--|--|--|--|
| 0x0 | 0000 | A + B | Put the sum of A, B to C bus |
| 0x1 | 0001 | A - B | Put the difference of A, B to C bus |
| 0x2 | 0010 | A + B + 1 | Put the result A+B+1 to C bus |
| 0x3 | 0011 | A + 1 | Increment A by one, send to C bus |
| 0x4 | 0100 | A | Pass content of A bus to C bus |
| 0x5 | 0101 | B | Pass content of B bus to C bus |
| 0x6 | 0110 | 0 | Output ZERO to C bus |
| 0xd | 1101 | sqrt(A) | Put integer sqrt of A to C bus |
| 0xe | 1110 | A / 8 | Integere Division of A to C bus |
| 0xf | 1111 | A x B | Put multiplication of A, B to C bus |


## 3. Micro Instuction format of CPU

Since the proccesor is a CISC based architechure, microprogramming is essential. Here I have given the format of the micro instructions.

|ADDR| CTRL | ALU | EXT | C bus | MEM | A bus| B bus |
|--|--|--|--|--|--|--|--|
| 8 bits | 3 bits | 4 bits | 2 bits | 12 bits | 3 bits | 4 bits | 4 bits |

### 3.1. Descriptions of micro instruction units
|Micro Instruction Unit| Description |
|--|--|
| ADDR | This has 8 bits of space. This unit represents the address of the next micro instruction. |
| CTRL | 3 bits are allocated for JMPC (jump to program counter), JAMN (negetive flag check), JAMZ (zero flag check).|
|ALU| 4 bits are allocated to represent the ALU instuction (Refer topic 2). |
|EXT| Remain unused till now. (For future extensions). |
|C bus| Reserved 12 bits to provide write control signals for registers. Many registers can be written at the same time. (Refer 3.3 for further details).  |
|MEM| Reserved 3 bits for memory handling purposes. Write, Read, Fetch respectively. |
|A Bus| Reserved 4 bits to select the register to put on A bus. Only one register can access the A bus at a time. (Refer 3.2 for further details) |
|B Bus| Reserved 4 bits to select the register to put on B bus. Only one register can access the B bus at a time. (Refer 3.2 for further details) |

### 3.2. A bus, B bus decoding Information
To restrict and save space, A, B bus output control signals should be encoded. Please refer the below table to handle register outputs.
|Hex code| Bin Code | A bus | B bus | Description|
|--|--|--|--|--|
| 0x0 | 0000 | NONE | NONE | Nothing outputs to the bus
| 0x1 | 0001 | MAR | MAR | Memory Address Register
| 0x2 | 0010 | MDR | MDR | Memory Data Register
| 0x3 | 0011 | PC | PC | Program Counter
| 0x4 | 0100 | MBR | MBR | Memory Buffer Register
| 0x5 | 0101 | SP | SP | Stack Pointer
| 0x6 | 0110 | LV| LV | Local Variable Pointer
| 0x7 | 0111 | TOS| TOS | Top Of the Stack
| 0xc | 1100 | H0| H0 | H0 General Purpose Register
| 0xd | 1101 | H1| H1 | H1 General Purpose Register
| 0xe | 1110 | H2| H2 | H2 General Purpose Register
| 0xf | 1111 | H3| H3 | H3 General Purpose Register


### 3.3. C bus Information
In the below table we have provided the order of the registers in the C bus microinstruction format.
|Bit order| Register |
|--|--|
| MSB(11) | MAR |
|10|MDR|
|9|PC|
|8|SP|
|7|LV|
|6|TOS|
|3|H0|
|2|H1|
|1|H2|
|LSB(0)|H3|


## 4. Addressing Modes in Assembly
We have provided 3 bits space to represent addressing mode. It implies we can have 8 addressing modes. But so far, we have used only one addressing mode (Reigister Direct). Refer the table for more information.
|Hex code| Bin Code  | Description
|--|--|--|
| 0x0 | 000 | Register Direct Addressing Mode

## 5. Assembly Instruction Format
The assembly instruction consists of 16 bits. 7 bits for OPCODE, 3 bits for ADDR mode, 6 bits for OPERANDS. More details will be added later.

## 6. Table of assembly instructions
|Hex Code| Instruction | Description |
|--|--|--|
| 0x00 | NOP | No Operation |
|  | LDIM [reg] [imme] | Load Immidiate value to the register. The immediate value must be in the following address |
|  | RDSENSOR | This command will update sensor address, read sensordata, calculate difference, save the difference to an array, save new value to LOCAL VARIABLE POOL |
|  | ACCMEAN | This is a special instuction to accumulate values for the mean calculation |
|  | ACCSTD | This is a special instuction to accumulate values for the std calculation |
|  | INTDIV [reg] [imme] | Integer division register value by immediate value |
|  | INTSQRT [reg1] [reg2] | Integer square root of regiter 2 saved to register 1 |
|  | JIFCOMP [mem_offset] | This is a special instuction to check if we readed 8 sensors |
|  | JUMP [mem_offset] | Unconditional jump |
|  | JIFEQ [reg] [imme] [offset] | Jump if immediate value is equals to value in the register to given offset |

