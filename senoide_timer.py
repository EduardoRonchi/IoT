# imports
import _thread
from machine import Pin, PWM, ADC, Timer
import time
import math


def senoide():
    y = []
    fs = 128
    f = 10
    samples = 640
    for x in range(samples):
        y.append(1+math.sin(2 * math.pi * f * x / fs))
    return y

def interrupcao(t):
    global flag_interrupcao
    flag_interrupcao = True


flag_interrupcao = False
tim = Timer() # period in ms
tim.init(period=100, callback=interrupcao)

# PWM
PIN_OUT = 25
pwm_out = PWM(Pin(PIN_OUT, mode=Pin.OUT)) # Attach PWM object on the LED pin
pwm_out.freq(1000)

y = senoide()    

while True:
    
    for i in range(len(y)):
        if flag_interrupcao == True:
            #print(flag_interrupcao)
            duty_pwm = (y[i] * 39321/2) + 13107 # entre 20 e 80% do PWM
            #print("duty_pwm", duty_pwm/10000, "y", y[i])
            pwm_out.duty_u16(int(duty_pwm)) # For Pi Pico
            flag_interrupcao = False
            
        
        
