# Log History and Notes: 09.06.2025 - First Observations

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