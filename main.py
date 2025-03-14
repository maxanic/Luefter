def on_button_pressed_a():
    global PWM
    PWM += -10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global PWM
    PWM += 10
input.on_button_pressed(Button.B, on_button_pressed_b)

PWM = 0
pins.servo_set_pulse(AnalogPin.P0, 5000)

def on_forever():
    pins.servo_write_pin(AnalogPin.P0, PWM)
    basic.pause(200)
basic.forever(on_forever)
