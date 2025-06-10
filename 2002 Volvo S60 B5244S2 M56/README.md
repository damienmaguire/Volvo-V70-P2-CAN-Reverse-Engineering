# 2002 Volvo S60 B5244S2 M56

## General Remarks

### Tapping into the CAN Bus (tested on LHD cars)

A good spot to tap into the CAN bus is the loom close to the CEM under the dashboard.
About 20-30cm after the CEM connector there are two intersections in the loom where the
two CAN busses are split into three (depending on the car variant) wires.

The kickpanel has to be removed to access the wiring loom. To remove the kickpanel, the
side kickpanel on the center tunnel has to be removed. A single slotted plastic screw
somewhat covered by the seat has to be turned from horizontal to vertical to unlock it.
The side panel can than be pulled back. The kickpanel is attached with two screws and
two clips close to the screws.
It makes sense to move the CEM out of the way for easier access. It can be moved to
the rear of the vehicle after the white metal locking tab is released.

<picture>
  <img src="Pictures/CEM Wire Loom Intersections.jpg" alt="CEM Wire Loom Intersections">
</picture>

<picture>
  <img src="Pictures/CEM Wire Loom Tapped.jpg" alt="CEM Wire Loom with cables attached">
</picture>

Some wrapping tape has to be removed, but the thicker, more rigid pieces of tape
that are covering the intersections can be pushed away (at least on my car).

The intersection closer to the CEM appears to be the Low Speed CAN bus and the
intersection farther away appears to be the High Speec CAN bus, but that does not have
to be universally true for all cars, model years and variants.

### Colors and Speeds

Both HISPEED and LOSPEED busses have the same wire colors, green and white.
The green cable is CANL and the white cable is CANH.

The HISPEED bus runs at 250kBaud and the LOSPEED bus at 125kBaud.

The bus voltage is 3.3V.

## CAN Communication Protocol

### Message Format

All messages are in Extended Format and are 8 Byte long.

To be continued.

### Control Unit Addresses

To be continued.


