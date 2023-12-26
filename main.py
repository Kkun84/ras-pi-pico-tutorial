from machine import PWM, Pin

led = PWM(Pin("LED"), freq=1000, duty_u16=0x8000)

while True:
    for i in range(0xFFFF):
        led.duty_u16(i)
    for i in reversed(range(0xFFFF)):
        led.duty_u16(i)
