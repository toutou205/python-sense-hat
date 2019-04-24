from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
X = [255,0,0]
O = [0,0,0]
arrow_mask = [
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, O, O, O, O, O,
O, X, X, X, X, X, X, X,
O, O, X, O, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

X_mask = [
O, O, O, O, O, O, O, O,
O, X, O, O, O, X, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, X, O, O, O, X, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

def disparrow(event):
    if event.direction == 'left':
        sense.rotation = 0
    elif event.direction == 'up':
        sense.rotation = 90
    elif event.direction == 'right':
        sense.rotation = 180
    else:
        sense.rotation = 270
    sense.clear()
    sense.set_pixels(arrow_mask)

sense = SenseHat()
sense.clear()
sense.set_pixels(X_mask)
while True:
    # sense.rotation = 90
    # sense.set_pixels(arrow_mask)

    for event in sense.stick.get_events():
        print("The joystick was {} {}".format(event.action, event.direction))
        print(event.action)
        print(event.direction)
        if event.action == 'pressed':
            disparrow(event)

#sense.set_pixels(arrow_mask)
# disparrow()