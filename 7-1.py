import RPi.GPIO as G
import time
import matplotlib.pyplot as plt

leds = [2,3,4,17,27,22,10,9]
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
maxVolts = 3.28
levels = 256

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def binary2decimal(value):
    s = ''
    for x in value:
        s += str(x)
    return int(s, 2)

def val2led(value):
    ledsignal = [0]*8
    for i in range(8):
        if value >= maxVolts*(i+1)/8:
            ledsignal[i] = 1
    return ledsignal

G.setmode(G.BCM)
G.setwarnings(False)
G.setup(dac,G.OUT, initial=G.LOW)
G.setup(troyka,G.OUT, initial = G.HIGH)
G.setup(comp,G.IN)
G.setup(leds,G.OUT, initial = G.HIGH)

measure = []

try:
    begining_time = time.time()
    val = 0
    volts = 0
    while (volts < 2.67):
        signal = [0,0,0,0,0,0,0,0]
        for i in range (8):
            signal[i] = 1
            G.output(dac, signal)
            time.sleep(0.005)
            compval = G.input(comp)
            if compval == 1:
                signal[i] = 0
            else:
                signal[i] = 1
        val = binary2decimal(signal)
        volts = val/levels * 3.3
        measure.append(volts)
        print("ADC val = {:^3} -> {}, voltage = {:.2f}".format(val, signal, volts))
        G.output(leds,0)
        G.output(leds,val2led(volts))

    G.output(troyka, 0)

    while (volts > 0.06):
        signal = [0,0,0,0,0,0,0,0]
        for i in range (8):
            signal[i] = 1
            G.output(dac, signal)
            time.sleep(0.005)
            compval = G.input(comp)
            if compval == 1:
                signal[i] = 0
            else:
                signal[i] = 1
        val = binary2decimal(signal)
        volts = val/levels * 3.3
        measure.append(volts)
        print("ADC val = {:^3} -> {}, voltage = {:.2f}".format(val, signal, volts))
        G.output(leds,0)
        G.output(leds,val2led(volts))

    ending_time = time.time()
    print('Mesuaring duration:', ending_time - begining_time, 'sec')
    print('Mesuaring period:', (ending_time - begining_time)/len(measure), 'sec')
    print('Discretization fequency:', len(measure)/(ending_time - begining_time), 'hz')
    print('Quantization step:', maxVolts/levels, 'V')
    plt.plot(measure)
    plt.show()
except KeyboardInterrupt:
    print('Stop')
else:
    print('No exception')

finally:
    G.output(dac, 0)
    G.output(troyka, 0)
    G.cleanup

    
