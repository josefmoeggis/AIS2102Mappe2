import sys
import numpy as np

from time import time

class PID:
    def __init__(self): 
        self.k1 = 109.8354 #Vinkelregulering
        self.k2 = 2.666
        self.lastVal = 0
        self.lastVel = 0
        self.x_hat1 = 0
        self.x_hat2 = 0

    def resetWindup(self):
        self.windup = 0


    def regulate(self, x1, currentVal, angleVelocity, dt, dummy):
    # Construct the state vector (position and velocity)
        # Calculate the error
        error = x1 - currentVal

        # Apply the K matrix
        K = np.array([self.k1, self.k2])
        u = -(self.k1 * currentVal - self.k2 * -angleVelocity)/650
        # Update the last value
        print("error:", error)
        self.lastVal = currentVal
        return u, dummy
    
    def regulateObs(self, x1, currentVal, angleVelocity, dt, dummy):
    # System dynamics matrices
        a11 = 0
        a12 = 1
        a21 = 0
        a22 = -8
        b1 = 0
        b2 = 1
        c1 = 1.56410*(10**4)
        c2 = 1

        # Observer gain values (design or tune these values)
        l1 = 0.0063
        l2 = 0.1347

        # Update the estimated state variables using the observer
        x_hat1 = self.x_hat1 + (a11 * self.x_hat1 + a12 * self.x_hat2 + b1 * currentVal - l1 * (c1 * self.x_hat1 - currentVal))
        x_hat2 = self.x_hat2 + (a21 * self.x_hat1 + a22 * self.x_hat2 + b2 * currentVal - l2 * (c2 * self.x_hat2 - angleVelocity))

        print("x_hat1:", self.x_hat1)
        print("dt:", dt)
        #print("x_hat2:", self.x_hat2)

        # Calculate the error
        error = x_hat1 - x1

        # Apply the K matrix
        u = -(self.k1 * error + self.k2 * x_hat2)/20

        # Update the estimated state variables
        self.x_hat1 = x_hat1
        self.x_hat2 = x_hat2

        return u


    def copy(self, pid):
        self.kp = pid.k2
        self.ki = pid.k2
    def getError(self):
        return self.lastVal

    def getX_hat1(self):
        return self.x_hat1