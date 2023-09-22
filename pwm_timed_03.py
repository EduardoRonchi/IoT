import time
import math
from machine import Pin, PWM, Timer, ADC

AMPLITUDE=(2**15)


#*************************************************
#   Gera "samples" pontos em um período de senoide
#*************************************************

samples=12								# número de pontos 
delta_phi=2*math.pi/samples				# fração de ângulo -> 2*pi/samples  

cosint=[ 0.98*math.cos(k*delta_phi) for k in range(samples) ]								# lista global que contém as amostras de senóide
print(cosint)
#for k in range(samples):				# Gera os pontos da senóide
#  cosint.append(math.cos(k*delta_phi))
#  continue


#************************************************
#   Programa os Timers
#************************************************

timer_sample=Timer()					# cria um objeto de Timer
sigfreq=500							# frequência da senóide

sampleflag=False						# Flag que indica um disparo do Timer

def int_sample(arg):					# função que será chamada a cada interrupção
    global sampleflag
    sampleflag=True

                                        # inicializa o Timer para gerar uma interrupção por amostra da senóide
timer_sample.init(mode=Timer.PERIODIC, freq=(sigfreq*samples), callback=int_sample)


#************************************************

timer2_sample=Timer()# cria um objeto de Timer
sigfreq2=10# frequência da senóide

sampleflag2=False						# Flag que indica um disparo do Timer

def int_sample2(arg):					# função que será chamada a cada interrupção
    global sampleflag2
    sampleflag2=True

                                        # inicializa o Timer para gerar uma interrupção por amostra da senóide
timer2_sample.init(mode=Timer.PERIODIC, freq=(sigfreq2*samples), callback=int_sample2)




#************************************************
#   Programa  PWM
#************************************************

pwmfreq=1_000_000

pwm  = PWM(Pin(21))
pwm2  = PWM(Pin(20))

pwm.freq(pwmfreq)
pwm2.freq(pwmfreq)



#************************************************
#   Configura ADC0 
#************************************************

adc0=ADC(Pin(26))


#************************************************
#   Loop principal
#************************************************


k=0
l=0
while True:
    if (sampleflag == True):
       modulante=0.5+0.4*(adc0.read_u16()/2**16)
       pwm.duty_u16(round(AMPLITUDE*(1+ (modulante*cosint[k])) ))
       sampleflag=False
       k =  0 if k >= samples-1 else k+1
    if (sampleflag2 == True):
       pwm2.duty_u16(round(AMPLITUDE*(1+cosint[l])))
       sampleflag2=False
       l =  0 if l >= samples-1 else l+1
    continue

#from machine import Pin, PWM


