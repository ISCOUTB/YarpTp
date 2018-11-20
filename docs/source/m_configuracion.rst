Métodos de configuración
========================
Desactivar control
------------------
Cuando se finalice el uso del robot, deben liberarse los pines de la Raspberry. Para esto, es importante que al final de cada script donde se controle el robot se ejecute el siguiente movimiento.

.. autoclass:: YarpTp.YarpTp
   :members: GoodBye

Al ejecutar el método anterior, no se podrá controlar más el robot.
Sin embargo, si una nueva instancia de la clase YarpTp se crea usando la instruccion ``YarpTp()``
se podrá controlar de nuevo el robot.

Definición de los pines a usar
------------------------------
Internamente, el control de las ruedas se da desde los pines GPIO de la Raspberry, los cuales están predefinidos en el módulo siguiendo la documentación de construcción del robot YarpTp. Sin embargo, si los pines son cambiados, se pueden usar los siguientes métodos:

.. autoclass:: YarpTp.YarpTp
   :members: setMotorLeft, setMotorRight


