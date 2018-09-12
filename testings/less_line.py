"""
aaaa
"""
import RPi.GPIO as GPIO
from time import sleep

class Prototype:
    def __init__(self):
        # Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19
        self.enableA = 0 # Phisycal pin 12
        self.input1 = 0
        self.input2 = 0

        self.enableB = 0 # Phisycal pin 35
        self.input3 = 0
        self.input4 = 0

        GPIO.setmode(GPIO.BOARD)

        channel_list = (self.enableA, self.input1, self.input2,
                        self.enableB, self.input3, self.input4)

        GPIO.setup(channel_list, GPIO.OUT)

        frequency = 0

        self.pwm_a = GPIO.PWM(self.enableA, frequency)
        self.pwm_b = GPIO.PWM(self.enableB, frequency)

        self.pwm_a.start(0)
        self.pwm_b.start(0)

    # m = True -> Motor A
    # m = False -> Motor B
    def signals(self, inputs, signal, m, sp):
        GPIO.output(inputs, signal)
        if m:
            self.pwm_a.ChangeDutyCycle(sp)
        else:
            self.pwm_b.ChangeDutyCycle(sp)

    # Move motor A - Forward - with Speed = speed
    def ForwardMotorAwSpeed(self, speed):
        self.signals((self.input1,self.input2), (GPIO.LOW, GPIO.HIGH), True, speed)

    def ForwardMotorBwSpeed(self, speed):
        self.signals((self.input3,self.input4), (GPIO.HIGH, GPIO.LOW), False, speed)

    def ReverseMotorAwSpeed(self, speed):
        self.signals((self.input1,self.input2), (GPIO.HIGH, GPIO.LOW), True, speed)

    def ReverseMotorBwSpeed(self, speed):
        self.signals((self.input3,self.input4), (GPIO.LOW, GPIO.HIGH), False, speed)

    def ForwardBothwSpeed(self, speed):
        self.ForwardMotorAwSpeed(speed)
        self.ForwardMotorBwSpeed(speed)

    def ReverseBothwSpeed(self, speed):
        self.ReverseMotorAwSpeed(speed)
        self.ReverseMotorBwSpeed(speed)

    # Move motor X with standard speed
    def ForwardMotorA(self):
        self.ForwardMotorAwSpeed(50)

    def ForwardMotorB(self):
        self.ForwardMotorBwSpeed(50)

    def ReverseMotorA(self):
        self.ReverseMotorAwSpeed(50)

    def ReverseMotorB(self):
        self.ReverseMotorBwSpeed(50)

    # Move both motors with standard speed
    def ForwardBoth(self):
        self.ForwardMotorAwSpeed(50)
        self.ForwardMotorBwSpeed(50)

    def ReverseBoth(self):
        self.ReverseMotorAwSpeed(50)
        self.ReverseMotorBwSpeed(50)

    # Stop both motors
    def StopAll(self):
        GPIO.cleanup()

    # Stop X motor
    def StopMotorA(self):
        GPIO.cleanup((self.input1, self.input2))

    def StopMotorB(self):
        GPIO.cleanup((self.input3, self.input4))
