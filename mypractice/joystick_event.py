# from sense_hat import SenseHat
# from time import sleep
#
# sense = SenseHat()
# event = sense.stick.wait_for_event()
# print("The joystick was {} {}".format(event.action, event.direction))
# sleep(0.1)
# event = sense.stick.wait_for_event()
# print("The joystick was {} {}".format(event.action, event.direction))

# from sense_hat import SenseHat
# from time import sleep
#
# sense = SenseHat()
# # event = sense.stick.wait_for_event()
# # print("The joystick was {} {}".format(event.action, event.direction))
# # sleep(0.1)
# # event = sense.stick.wait_for_event(emptybuffer=True)
# # print("The joystick was {} {}".format(event.action, event.direction))
# while True:
#     for event in sense.stick.get_events():
#         print("The joystick was {} {}".format(event.action, event.direction))

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

x = 3
y = 3
sense = SenseHat()

def disparrow(event):
    sense.set_pixels(arrow_mask)

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh
refresh()
pause()

#sense.set_pixels(arrow_mask)
#disparrow()