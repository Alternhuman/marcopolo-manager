Vista estática del sistema
==========================

Se plantea la siguiente estructura: 


.. image:: ../img/analysis_marcomanager.*
	:align: center

La clase de control **manager** contendrá referencias a todos los servicios a publicar. Dichos servicios serán implementaciones de la clase abstracta **iservice**, que define el conjunto de métodos que la clase de control consumirá. **manager** será controlada por el gestor de servicios del sistema.