



def calculateTempC(thermistorVolt, r2, sourceVoltage):
    thermistorCurent = (sourceVoltage - thermistorVolt) / r2
    #print("Thermistor current = ", thermistorCurent)
    thermistorR = thermistorVolt / thermistorCurent
    #print("Thermistor resistance = ", thermistorR)
    thermistorR = 30000
    print(thermistorR)
    thermistorTemperatureC = 94974.5413538519 - 4696.967 * thermistorR + 129.826 * thermistorR**2 - 2.6186 * thermistorR**3 + 0.042544* thermistorR**4 - 0.00059762 * thermistorR**5 + 0.00000781 * thermistorR**6 - 9.53630e-8 * thermistorR**7 + 9.691e-10 * thermistorR**8 - 7.19177773e-12 * thermistorR**9 + 3.497936e-1 * thermistorR**10 - 9.821e-17 * thermistorR**11 + 1.2e-19 * thermistorR**12
    #thermistorTemperatureC = -3e-20 * thermistorR ** 5 + 1e-17 * thermistorR ** 4 + 1e-12 * thermistorR ** 2 + thermistorR - 2  

    print(thermistorTemperatureC)

calculateTempC(4.06, 5510, 5)