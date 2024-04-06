import sys

from time import time

class PID:
    def __init__(self): 
        self.kp = 0.4 #Vinkelregulering
        self.ki = 6
        self.kd =  1.5
        self.windup = 0
        self.winduptime = 0
        self.accWindup = []
        self.windupLim = 2
        self.lastIntegral = 0
        self.lastError = 0
        self.lastVal = 0
        self.useWindup = False

    def checkWindup(self):
        for i in self.accWindup:
            if self.accWindup[i] * 0.98 > self.windup or self.accWindup[i] * 1.02 < self.windup: # Reset windup if prev windup between these vals
                break
            else:
                self.accWindup = []
                self.windup = 0

    def resetWindup(self):
        self.windup = 0

    def regulate(self, target, currentVal, dt):
        # Implement controller using this function
        print("Angle:", currentVal)
        error = target - currentVal # Proportional Calculation

        derivative = dt * (self.lastVal - error) # Derivative calculation

        self.accWindup.append(self.windup)
        if len(self.accWindup) > 10:
            self.accWindup.pop(0)

        #PID.checkWindup(self)

        self.windup += error * dt # Integral calculation trapezoidal methode

        self.lastVal = error
        print("Windup:", self.windup)
        #print("Error:", error)
        pid = self.kp * error + self.ki * self.windup + self.kp * derivative

        return pid

    def copy(self, pid):
        self.kp = pid.kp
        self.ki = pid.ki
        self.kd = pid.kd
        self.windup = pid.windup
        self.useWindup = pid.useWindup