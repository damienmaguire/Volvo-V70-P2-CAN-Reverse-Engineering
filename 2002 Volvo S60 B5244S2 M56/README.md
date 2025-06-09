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


## Log History and Notes

### 09.06.2025 - First Observations

The car appears to have multiple activity modes:
1) Off (no CAN messages at all)
2) Sleepy (around 400 mps, no activity on HISPEED)
3) Awake (around 900mps, activity on HISPEED and LOSPEED)
4) Active (around 1300mps, activity on HISPEED and LOSPEED)

Unlocking the car was not tested for any bus activity yet.
Inserting the key does not cause any bus activity.
Turning the key to Position 1 brings the car to *Sleepy Mode*. It goes back to *Off Mode*
when turning the key back to off and a couple of minutes of time.
A relay can be heard clicking when it goes back to *Off Mode*.

Turning the key to Position 2 brings the car to *Active Mode* with
activity on both CAN busses. There does
not seem to be an increase of bus activity with the engine running.

The car will go to *Awake Mode* when the key is turned back to Position 1 or Off
with activity on both CAN busses. Turning the key back to Off keeps the car
in *Awake Mode* for some time, after which it turns to *Sleepy Mode* and then off.
A relay can be heard when going from *Awake Mode* to *Sleepy Mode*.

