#Tello Drone Litter Hunter
This project is working on making a drone that can 
sweep an area and identify litter.

## -- Setup -- 

1. Clone repository
2. Make sure Python 3.9 is installed
3. Using a terminal, run `python main.py`

Commands can be typed in once the drone has connected via wifi
I recommend using an external wifi adapter, otherwise you'll lose internet access

Once connected, start by typing `command` into the terminal, and after that you can type in the tello commands. 
The drone will reply with `ok` when it receives the command correctly

Tello commands can be found in the `Tello 2.0 SDK User Guide.pdf` in this repo

#### *_Example command sequence typed one at a time once connected_*:
 
```command > takeoff > forward 50 > up 40 > ccw 200 > forward 50 > land   ```

This will have it move twice, spin, then move again, then land.

## -- Credits --

The seed program came from the Tello SDK, 
but then I built off it from there