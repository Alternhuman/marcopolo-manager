Vista de actividad
==================

.. figure:: ../img/analysis_activity.*
    :align: center

    Cada uno de los servicios es procesado, extrayendo la información sobre las acciones a realizar y el momento en el que deben ser llevadas a cabo (así como la periodicidad). Estos datos son añadidos al bucle de eventos de Tornado, que emitirá señales al llegar a un punto en el tiempo en el que un servicio solicite ejecutar la acción a llevar a cabo. Recogiendo esas señales es posible ejecutar la acción solicitada por el nodo en el momento oportuno.