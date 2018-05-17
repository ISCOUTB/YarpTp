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

    def ForwardMotorA(self):
        # self.signals((self.input1,self.input2), (GPIO.LOW, GPIO.HIGH), True, 50)
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)
        self.pwm_a.ChangeDutyCycle(50)

    def ForwardMotorB(self):
        # self.signals((self.input3,self.input4), (GPIO.HIGH, GPIO.LOW), False, 50)
        GPIO.output(self.input3, GPIO.HIGH)
        GPIO.output(self.input4, GPIO.LOW)
        self.pwm_b.ChangeDutyCycle(50)

    def ReverseMotorA(self):
        # self.signals((self.input1,self.input2), (GPIO.HIGH, GPIO.LOW), True, 50)
        GPIO.output(self.input1, GPIO.HIGH)
        GPIO.output(self.input2, GPIO.LOW)
        self.pwm_a.ChangeDutyCycle(50)

    def ReverseMotorB(self):
        # self.signals((self.input3,self.input4), (GPIO.LOW, GPIO.HIGH), False, 50)
        GPIO.output(self.input3, GPIO.LOW)
        GPIO.output(self.input4, GPIO.HIGH)
        self.pwm_b.ChangeDutyCycle(50)

    def ForwardBoth(self):
        self.ForwardMotorA()
        self.ForwardMotorB()

    def ReverseBoth(self):
        self.ReverseMotorA()
        self.ReverseMotorB()

    # Move motor A - Forward - with Speed = speed
    def ForwardMotorAwSpeed(self, speed):
        # self.signals((self.input1,self.input2), (GPIO.LOW, GPIO.HIGH), True, speed)
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)
        self.pwm_a.ChangeDutyCycle(speed)

    def ForwardMotorBwSpeed(self, speed):
        # self.signals((self.input3,self.input4), (GPIO.HIGH, GPIO.LOW), False, speed)
        GPIO.output(self.input3, GPIO.HIGH)
        GPIO.output(self.input4, GPIO.LOW)
        self.pwm_b.ChangeDutyCycle(speed)

    def ReverseMotorAwSpeed(self, speed):
        # self.signals((self.input1,self.input2), (GPIO.HIGH, GPIO.LOW), True, speed)
        GPIO.output(self.input1, GPIO.HIGH)
        GPIO.output(self.input2, GPIO.LOW)
        self.pwm_a.ChangeDutyCycle(speed)

    def ReverseMotorBwSpeed(self, speed):
        # self.signals((self.input3,self.input4), (GPIO.LOW, GPIO.HIGH), False, speed)
        GPIO.output(self.input3, GPIO.LOW)
        GPIO.output(self.input4, GPIO.HIGH)
        self.pwm_b.ChangeDutyCycle(speed)

    def ForwardBothwSpeed(self, speed):
        self.ForwardMotorAwSpeed(speed)
        self.ForwardMotorBwSpeed(speed)

    def ReverseBothwSpeed(self, speed):
        self.ReverseMotorAwSpeed(speed)
        self.ReverseMotorBwSpeed(speed)

    def StopAll(self):
        GPIO.cleanup()

    def StopMotorA(self):
        GPIO.cleanup((self.input1, self.input2))

    def StopMotorB(self):
        GPIO.cleanup((self.input3, self.input4))
