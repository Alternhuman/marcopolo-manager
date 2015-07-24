Diseño arquitectónico
=====================

Diagrama de componentes
-----------------------

.. figure:: ../img/design_components.*
    :align: center

    En este diagrama se representan los diferentes componentes y los puntos de entrada que facilitan la interconexión entre los mismos.

Diagrama de despliegue
----------------------

.. figure:: ../img/deployment.*
    :align: center

    Vista de la interacción entre los diferentes componentes. El gestor de *daemons* se encarga del arranque y detención de la instancia de ``runner.py`` (se representa con un conector genérico).