Métodos de movimiento
=====================
Los movimientos soportados por el módulo incluyen el desplazamiento hacia delante, hacia atrás y los giros.

Movimientos abiertos
--------------------
Los métodos de movimiento que se presentan a continuación son ejecutados de forma libre y personalizada, como se muestra más adelante. 

Cada uno de los movimientos puede ejecutarse de dos formas: movimiento continuo o personalizado:

 * Cuando no se indica el parámetro del tiempo (tm) el movimiento será continuo hasta que una instrucción lo detenga y usando la velocidad indicada. Si la velocidad no se indica, se ejecuta el movimiento a la velocidad predefinida (50%).
 * Cuando se indica un tiempo del movimiento, se ejecutará hasta que transcurra y luego se detendrá. Para la velocidad, se comportará de la forma indicada en el punto anterior.

Los movimientos varían de acuerdo a la dirección (hacia delante o hacia atrás) y por el motor que se moverá (izquierdo, derecho o ambos motores). Los métodos se listan a continuación:

.. autoclass:: YarpTp.YarpTp
   :members: ForwardMotorL, ForwardMotorR, ReverseMotorL, ReverseMotorR, Forward, Reverse

Movimientos cerrados
--------------------
Estos movimientos ocurren de forma limitada o definida, es decir, mueven al robot por un paso.

.. autoclass:: YarpTp.YarpTp
   :members: ForwardStep, ReverseStep

Giros
-----
Estos métodos permiten girar el robot hacia un lado. 

.. autoclass:: YarpTp.YarpTp
   :members: TurnLeft, TurnRight

Métodos de parada
-----------------
Los siguiente métodos detienen el movimiento de los motores del robot.

.. autoclass:: YarpTp.YarpTp
   :members: Stop, StopMotorL, StopMotorR
