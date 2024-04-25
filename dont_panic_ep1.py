import sys
import math

# global variables
elevators = []
blocked = False
obj = None
last_floor = 0
new_floor = False

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators.append({
        "floor": elevator_floor,
        "pos": elevator_pos,
    })

# game loop
while True:
    # floor of the leading clone
    # position of the leading clone on its floor
    # direction of the leading clone: LEFT or RIGHT

    clone_floor, clone_pos, direction = input().split()
    floor = int(clone_floor)
    pos = int(clone_pos)

    # checks for a new floor, if yes, se new_floor to True
    if last_floor < floor: 
        new_floor = True
    
    closest_elevator = None
    geatable_elevator = [i for i in elevators if i["floor"] == floor]
    _closest_elevator = 99999

    if len(geatable_elevator) > 0:
        # This bucle it's getting the closest elevator
        for i in geatable_elevator:           
            if abs(pos - i["pos"]) < _closest_elevator:  
                _closest_elevator = abs(pos - i["pos"])
                closest_elevator = i      
        # Set the closest elevator as "objective" 
        obj = closest_elevator               
    else:
        # If no elevators found in the floor, set the exit as "objective"
        obj = {                                
            "floor": exit_floor, 
            "pos": exit_pos,
        }
    
    # checks for NoneType, if it's not, continues
    if obj is not None:   
        if direction == "LEFT":
            # If direction it's "LEFT" and objective it's to the right,
            if obj["pos"] > pos and not blocked:   
                #   block the leading clone to change direction.
                print("BLOCK")                      
                blocked = True
            else:
                print("WAIT")
        else:
            # If direction it's "RIGHT" and objective it's to the left,
            if obj["pos"] < pos and not blocked:   
                #   block the leading clone to change direction. 
                print("BLOCK")                      
                blocked = True  
            else:
                print("WAIT")
        
        
        # If the leading clone it's on a new floor, any clone is blocking, set <blocked> to False,
        if new_floor:
            #    and update las floor.             
            blocked = False       
            last_floor = floor
            new_floor = False
    else:
        print("error")


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # action: WAIT or BLOCK
   
