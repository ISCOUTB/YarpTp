Primeros pasos
==============
Un script sencillo para moverse hacia el frente puede ser así:

::

  from YarpTp import YarpTp
  my_car = YarpTp()
  my_car.ForwardStep()
  my_car.GoodBye()

¿Qué está haciendo?

 #. En primer lugar se importa la clase YarpTp quien contiene los métodos de control.
 #. Luego, se crea una instancia de la clase, es decir, un objeto que hará las veces del robot en el código.
 #. Ahora es posible ejecutar cualquier método de movimiento, como se muestra al llamar a ``ForwardStep()``, el cual se mueve cierto paso predefinido hacia delante. Para ver los demás movimientos, ir a la sección de movimientos.
 #. Finalmente, hay que “apagar” el control del robot usando el método ``GoodBye()``.
