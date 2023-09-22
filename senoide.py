# fazer uma senoide
# consultar o valor da senoide em x tempo
# aplicar o valor da senoide no duty cicle do pwm

# imports
import _thread
from machine import Pin, PWM, ADC
import time
import math

# PWM
PIN_OUT = 16
pwm_out = PWM(Pin(PIN_OUT, mode=Pin.OUT)) # Attach PWM object on the LED pin
pwm_out.freq(50000)
#step = 50

#pino_senoide = (Pin(14, mode=Pin.OUT))

def senoide():
    Fs = 2000
    f = 10
    y = []
    for x in range(0, Fs, 1):
        y.append(1 + math.sin(2 * math.pi * f * x / Fs))
    return y

y = senoide()
print(len(y))
#print(y)
while True:
    #break
    for i in range(len(y)):
        print("Y:", y[i])
        #pino_senoide(y[i])
        #for duty in range(0,65_535, step):
        duty_pwm = y[i] * 65535/2
        pwm_out.duty_u16(int(duty_pwm)) # For Pi Pico
        #time.sleep_ms(1)
    for i in range(len(y)):
        print("Y:", y[i])
        #pino_senoide(y[i]s)
        #for duty in range(0,65_535, step):
        duty_pwm = y[i] * 65535/2
        pwm_out.duty_u16(int(-duty_pwm)) # For Pi Pico
        #time.sleep_ms(1)