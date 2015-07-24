Diseño de datos
===============

Objetos de datos
----------------

El sistema utiliza un único tipo de estructura de datos, instancias de :class:`MarcoPoloManager <marcopolomanager.marcopolomanager.MarcoPoloManager>` para representar los diferentes servicios a gestionar.


Estructuras de archivo
----------------------

Se consultan varias fuentes de datos en la aplicación:

- Ficheros de configuración ``/etc/marcopolomanager/marcopolomanager.cfg``, que permiten modificar el comportamiento de la aplicación.
- Ficheros de *log*, que permiten analizar *a posteriori* el comportamiento del programa, en particular ante algún tipo de situación irregular, sitos en ``/var/log/marcopolo/marcomanagerd.log``.
- Ficheros con los diferentes servicios, situados en ``/etc/marcopolomanager/managers/``. Deben ser *scripts* de python (ver :doc:`ejemplo </managers>`).