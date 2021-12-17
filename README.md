
# SAGv.1
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
The arithmatic logic unit of the CPU is carefully designed for specific mathematical operations needed for temperature process.
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

### 3.1 Descriptions of micro instruction units
|Micro Instruction Unit| Description |
|--|--|
| ADDR | This has 8 bits of space. This unit represents the address of the next micro instruction. |
| CTRL | 3 bits are allocated for JMPC (jump to program counter), JAMN (negetive flag check), JAMZ (zero flag check).|
|ALU| 4 bits are allocated to represent the ALU instuction (Refer topic 2). |
|EXT| Remain unused till now. (For future extensions). |
|C bus| Reserved 12 bits to provide write control signals for registers. Many registers can be written at the same time. (Refer 3.4 for further details).  |
|MEM| Reserved 3 bits for memory handling purposes. Write, Read, Fetch respectively. |
|A Bus| Reserved 4 bits to select the register to put on A bus. Only one register can access the A bus at a time. (Refer 3.2 for further details) |
|B Bus| Reserved 4 bits to select the register to put on B bus. Only one register can access the B bus at a time. (Refer 3.3 for further details) |

