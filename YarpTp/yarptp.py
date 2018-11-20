import RPi.GPIO as GPIO
from time import sleep


class YarpTp:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.__enableA = 0
        self.__input1 = 0
        self.__input2 = 0

        self.__enableB = 0
        self.__input3 = 0
        self.__input4 = 0

        self.__frequency = 500
        self.__pwm_a = None
        self.__pwm_b = None

        self.setMotorLeft(18, 23, 24)
        self.setMotorRight(19, 6, 5)

    def __enable_pins(self, channel_list, m):
        GPIO.setup(channel_list, GPIO.OUT)
        if m:
            self.__pwm_a = GPIO.PWM(channel_list[0], self.__frequency)
            self.__pwm_a.start(0)
        else:
            self.__pwm_b = GPIO.PWM(channel_list[0], self.__frequency)
            self.__pwm_b.start(0)

    def __signals(self, inputs, signal, m, sp):
        GPIO.output(inputs, signal)
        if m == 0:
            self.__pwm_a.ChangeDutyCycle(sp)
        elif m == 1:
            self.__pwm_b.ChangeDutyCycle(sp)
        elif m == 2:
            self.__pwm_a.ChangeDutyCycle(sp)
            self.__pwm_b.ChangeDutyCycle(sp)

    def __power_off(self, lst):
        GPIO.output(lst, GPIO.LOW)

    def setMotorLeft(self, enA, in1, in2):
        """
        Personalizar los pines GPIO usados por el motor izquierdo.

        :param int enA: Código BCM del pin conectado a la entrada enA del controlador L298N.
        :param int in1: Código BCM del pin conectado a la entrada in1 del controlador L298N.
        :param int in2: Código BCM del pin conectado a la entrada in2 del controlador L298N.
        """
        self.__enableA = enA
        self.__input1 = in1
        self.__input2 = in2
        self.__enable_pins((self.__enableA, self.__input1, self.__input2), True)

    def setMotorRight(self, enB, in3, in4):
        """
        Personalizar los pines GPIO usados por el motor derecho.

        :param int enB: Código BCM del pin conectado a la entrada enB del controlador L298N.
        :param int in3: Código BCM del pin conectado a la entrada in3 del controlador L298N.
        :param int in4: Código BCM del pin conectado a la entrada in4 del controlador L298N.
        """
        self.__enableB = enB
        self.__input3 = in3
        self.__input4 = in4
        self.__enable_pins((self.__enableB, self.__input3, self.__input4), False)

    def ForwardMotorL(self, tm=0.0, speed=50):
        """Mover el motor izquierdo del robot hacia delante.

        :param tm: (opcional) Tiempo que durará el movimiento ejecutado.
        :type tm: float
        :param speed: (opcional) Velocidad del movimiento.
        :type speed: int
        """
        if tm == 0.0:
            self.__signals((self.__input1,self.__input2), (GPIO.LOW, GPIO.HIGH), 0, speed)
        else:
            self.__signals((self.__input1,self.__input2), (GPIO.LOW, GPIO.HIGH), 0, speed)
            sleep(tm)
            self.__power_off((self.__input1, self.__input2))

    def ForwardMotorR(self, tm=0.0, speed=50):
        """
        Mover el motor derecho hacia delante.

        :param tm:  Tiempo que durará el movimiento ejecutado.
        :type tm: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        if tm == 0.0:
            self.__signals((self.__input3,self.__input4), (GPIO.LOW, GPIO.HIGH), 1, speed)
        else:
            self.__signals((self.__input3,self.__input4), (GPIO.LOW, GPIO.HIGH), 1, speed)
            sleep(tm)
            self.__power_off((self.__input3, self.__input4))

    def ReverseMotorL(self, tm=0.0, speed=50):
        """
        Mover el motor izquierdo hacia atrás.

        :param tm:  Tiempo que durará el movimiento ejecutado.
        :type tm: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        if tm == 0.0:
            self.__signals((self.__input1,self.__input2), (GPIO.HIGH, GPIO.LOW), 0, speed)
        else:
            self.__signals((self.__input1,self.__input2), (GPIO.HIGH, GPIO.LOW), 0, speed)
            sleep(tm)
            self.__power_off((self.__input1, self.__input2))

    def ReverseMotorR(self, tm=0.0, speed=50):
        """
        Mover el motor derecho hacia atrás.

        :param tm:  Tiempo que durará el movimiento ejecutado.
        :type tm: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        if tm == 0.0:
            self.__signals((self.__input3,self.__input4), (GPIO.HIGH, GPIO.LOW), 1, speed)
        else:
            self.__signals((self.__input3,self.__input4), (GPIO.HIGH, GPIO.LOW), 1, speed)
            sleep(tm)
            self.__power_off((self.__input3, self.__input4))

    def Forward(self, tm=0.0, speed=50):
        """
        Mover ambos motores hacia delante.

        :param tm:  Tiempo que durará el movimiento ejecutado.
        :type tm: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        if tm == 0.0:
            self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH), 2, speed)
        else:
            self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH), 2, speed)
            sleep(tm)
            self.__power_off((self.__input1, self.__input2, self.__input3, self.__input4))

    def Reverse(self, tm=0.0, speed=50):
        """
        Mover ambos motores hacia atrás.

        :param tm:  Tiempo que durará el movimiento ejecutado.
        :type tm: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        if tm == 0.0:
            self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW), 2, speed)
        else:
            self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW), 2, speed)
            sleep(tm)
            self.__power_off((self.__input1, self.__input2, self.__input3, self.__input4))

    def ForwardStep(self):
        """
        Mueve el robot 1 paso hacia delante.
        """
        self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH), 2, 50)
        sleep(0.3)
        self.__power_off((self.__input1, self.__input2, self.__input3, self.__input4))

    def ReverseStep(self):
        """
        Mueve el robot 1 paso hacia atrás.
        """
        self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW), 2, 50)
        sleep(0.3)
        self.__power_off((self.__input1, self.__input2, self.__input3, self.__input4))

    def TurnLeft(self, tm=0.3):
        """
        Gira el robot hacia la izquierda en un ángulo de 90°.
        """
        self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH), 2, 50)
        sleep(tm)
        self.__power_off((self.__input1,self.__input2,self.__input3,self.__input4))

    def TurnRight(self, tm=0.3):
        """
        Gira el robot hacia la derecha en un ángulo de 90°.
        """
        self.__signals((self.__input1,self.__input2,self.__input3,self.__input4), (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW), 2, 50)
        sleep(tm)
        self.__power_off((self.__input1,self.__input2,self.__input3,self.__input4))

    def Stop(self):
        """
        Detiene ambos motores.
        """
        self.__power_off((self.__input1, self.__input2, self.__input3, self.__input4))

    def StopMotorL(self):
        """
        Detiene el motor izquierdo.
        """
        self.__power_off((self.__input1, self.__input2))

    def StopMotorR(self):
        """
        Detiene el motor izquierdo.
        """
        self.__power_off((self.__input3, self.__input4))

    def GoodBye(self):
        """
        Desactiva el control de los pines del robot.
        """
        GPIO.cleanup()
