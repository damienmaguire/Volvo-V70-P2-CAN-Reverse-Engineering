# Scripts

Collection of Python scripts that ease the analysis of the CAN logs.


## CAN Message Period Calculator

This script can be used to analyze the timing information of a CAN log in CSV
format (such as from SavvyCAN). The period is very important to know for
VCU development, if you want to replicate the CAN messages from for example
the ECU/ECM.

```
python "CAN Message Period Calculator.py" "..\2002 Volvo S60 B5244S2 M56\09-06-2025 20-07 --- car off, ignition on, start, idle, rev to 2000, hold at 2000, hold at 2500, back to high idle, back to low idle, off.csv"

       ID  | Count |  Mean [ms] | StdDev [ms] | Min [ms] | Max [ms] | Jitter [%]
--------------------------------------------------------------------------------
  0012C024 |  3604 |      14.04 |        1.77 |    13.36 |   119.12 |      12.59
  0022C01E |  5495 |      12.00 |        0.28 |     3.97 |    13.21 |       2.35
...
  04000002 |   146 |     459.95 |        3.73 |   449.62 |   470.27 |       0.81
  04200002 |    56 |     924.18 |      104.83 |   901.66 |  1687.26 |      11.34
--------------------------------------------------------------------------------
  42 CAN IDs analyzed, 77455 total messages

```

## CAN Message Counter Finder

This script can be used to find candidates for counters in the messages.
It prints a table with the message IDs and the Bytes where it suspects the
counter to be as well as a Match Rate.

```
python "Counter and Checksum Finder.py" "..\2002 Volvo S60 B5244S2 M56\09-06-2025 20-07 --- car off, ignition on, start, idle, rev to 2000, hold at 2000, hold at 2500, back to high idle, back to low idle, off.csv"

ID (Bus)     | Byte | Step | Start | End | Match Rate
-----------------------------------------------------
00400066 (0) |    0 |   64 |     0 | 192 |        1.0
00400066 (0) |    3 |    1 |     0 |   7 |       0.87
00608024 (1) |    0 |   64 |     0 | 192 |        1.0
00608024 (1) |    6 |    1 |     0 |   7 |       0.87
00B00002 (1) |    0 |   64 |     0 | 193 |        1.0
00C24008 (1) |    0 |  240 |    13 | 253 |        1.0
00C24008 (1) |    2 |   16 |     2 | 242 |        1.0
0102C02C (1) |    0 |   64 |     0 | 195 |        1.0
...
```

## CAN Extended ID Analyzer

Simple tool that prints all IDs it found and divides them by the busses
and shows a binary representation:

```
python '.\Extended ID Analyzer.py' '..\2002 Volvo S60 B5244S2 M56\10-06-2025\10-06-2025 15-22 --- car off, start, drive mostly around 50, accelerate to 120, around 50, shutdown, wait till car is off.csv'

=== Bus 0 ===
 ID (hex)  | ID (binary)
-------------------------------------------------
  00400066 | 0 0000 0100 0000 0000 0000 0110 0110
  00613DF8 | 0 0000 0110 0001 0011 1101 1111 1000
...
  04000002 | 0 0100 0000 0000 0000 0000 0000 0010
  04200002 | 0 0100 0010 0000 0000 0000 0000 0010
-------------------------------------------------
   23 unique extended CAN IDs found on Bus 0


=== Bus 1 ===
 ID (hex)  | ID (binary)
-------------------------------------------------
  0012C024 | 0 0000 0001 0010 1100 0000 0010 0100
  0022C01E | 0 0000 0010 0010 1100 0000 0001 1110
...
  01A00002 | 0 0001 1010 0000 0000 0000 0000 0010
-------------------------------------------------
   19 unique extended CAN IDs found on Bus 1
```