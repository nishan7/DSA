'''
#### Name:  Lift
Link: [link]()

**Requirement**
1) It go UP or DOWN
2) Door opens only when it is IDLE
3) Transfer passengers from one floor to another


**Actors**
Passengers
Floor
Elevator
Doors
Buttons (Lift)
Floor Buttons


**Use Case**
Calling the lift
Setting the Direction


**Algorithm**
FCFS
SJB
Order
'''


class Lift:
    floors = 10
    capacity = 5

    state = "IDLE"  # Moving,
    direction = "UP"  # DOWN

    floors_to_got = set()
    get_current_floor()

    start()   # Got the direction and open when current floor is in floors_to_go

    request(floor)


class Button:
    pass

class LiftButton(Button):
    pass

class OutsideButton(Button):
    pass



# class Request:
#     sendRequest(floor)
