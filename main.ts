input.onButtonPressed(Button.A, function () {
    PWM += -20
})
input.onButtonPressed(Button.AB, function () {
    PWM = 0
})
input.onButtonPressed(Button.B, function () {
    PWM += 20
})
let PWM = 0
pins.analogSetPeriod(AnalogPin.P0, 40)
PWM = 0
basic.forever(function () {
    pins.analogWritePin(AnalogPin.P0, PWM)
})
