import jetFunctions as j
import time

measure = []
try:
    numberofmesures = 900
    j.initSpiAdc()
    j.initStepMotorGpio()
    j.stepBackward(int(numberofmesures/2))
    for i in range(numberofmesures):
        time.sleep(0.01)
        measure.append(j.getAdc())
        j.stepForward(1)

finally:
    j.stepBackward(int(numberofmesures/2))
    j.deinitSpiAdc()
    j.deinitStepMotorGpio()
    j.jetsave("Desktop/Карабинцев, Исаев, Равшанов/datawithflow10.0.txt", measure)