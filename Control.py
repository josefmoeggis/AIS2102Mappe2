import sys
import numpy as np

from time import time

class Control:
    def __init__(self): 
        self.k1 = 10 #Vinkelregulering
        self.k2 =  1.5

 #   def checkWindup(self):
  #      for i in range(len(self.accWindup)):
   #         if self.accWindup[i] * 0.98 > self.windup or self.accWindup[i] * 1.02 < self.windup: # Reset windup if prev windup between these vals
    #            break
     #       else:
      #          self.accWindup = []
       #         self.windup = 0


    def regulate(self, target, x1, dt, dummy):
        # Implement controller using this function
        print("Angle:", np.rad2deg(x1))
        posError = target - x1
        

        dummy += self.windup

        self.lastVal = x1
        #print("Error:", error)
        control = -self.k1 * x1

        return control, dummy


    def copy(self, control):
        self.k1 = control.k1
        self.k2 = control.k2
        self.kd = control.kd
        self.windup = control.windup
        self.useWindup = control.useWindup

    def getError(self):
        return self.lastVal