# init
from machine import Pin, ADC

# LOOP
while True:
    counter = 0
    # setar pino I/O 1 Para OUT.
    GPIO1 = Pin(16, mode=Pin.OUT)
    # Quem é o I/O-2 ??
    #GPIO2 = Pin(17, mode=Pin.IN)
    GPIO2 = ADC(28)
    
    # IS I/O-pin 2 HIGH?
    # HIGH >= 3.3V/2
    value_GPIO2 = GPIO2.read_u16() 
    if GPIO2 == True:
        GPIO1 = Vol
        loop_interno_gpio2_high = True
        while loop_interno_gpio2_high:
            if GPIO2 == True:
                counter = counter + 1
            else:
                ADC_out = counter
                loop_interno_gpio2_high = False
            print("counter", counter)
    else: # GPIO2 == FALSE
        GPIO1 = Voh
        loop2_interno_gpio2_high = True
        while loop2_interno_gpio2_high:
            if GPIO2 == True:
                ADC_out = counter
                loop_interno_gpio2_high = False
            else:
                counter = counter - 1
            print("counter", counter)

