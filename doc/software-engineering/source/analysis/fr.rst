Requisitos funcionales
======================

RF 1: Creación de una unidad de gestión
---------------------------------------

- **Versión**: 1
- **Autores**: Diego Martín
- **Fuentes**: Análisis preliminar
- **Objetivos asociados**: OBJ-2
- **Requisitos asociados**: IRQ-2
- **Descripción**: Un Administrador (**ACT-1**) podrá definir una nueva unidad para gestionar un servicio. 
- **Precondición**: El administrador debe contar con permisos de modificación.
- **Secuencia normal**:

    1. El Administrador (**ACT-1**) crea la unidad definiendo el comportamiento de la misma durante el inicio y fin del gestor, el momento en el que debe ser ejecutada y otros parámetros adicionales.
    2. Solicita al gestor que publique el servicio.
    3. El gestor procesa los datos, programa los eventos de tiempo (si los hay, en caso contrario la ejecución comienza inmediatamente al terminar este caso de uso) y en caso de que toda la información que el Administrador ha indicado sea válida, añade el servico a la lista de servicios a procesar.
- **Poscondición**: El servicio es programado para su ejecución.
- **Excepciones**: En caso de que alguno de los parámetros que el Administrador no sea válido, se registrará el incidente y el caso de uso finalizará.
- **Rendimiento**: Alto
- **Frecuencia**: Alta
- **Importancia**: Alta
- **Urgencia**: Alta
- **Estado**: Completo
- **Estabilidad**: Estable
- **Comentarios**: Los posibles errores que la ejecución o cualquier otro aspecto no evaluable en el momento de añadir el servicio puedan ocasionar serán procesados durante la ejecución (**RF-2**) o detención del servicio (**RF-3**)

RF 2: Ejecución de un servicio
------------------------------

- **Versión**: 1
- **Autores**: Diego Martín
- **Fuentes**: Análisis preliminar
- **Objetivos asociados**: OBJ-2, OBJ-3
- **Requisitos asociados**: IRQ-1, IRQ-2
- **Descripción**: Una vez que el instante de tiempo en el que el servicio deba ejecutarse sea alcanzado se realizará la secuencia de acciones indicadas por el Administrador.
- **Precondición**: El servicio debe haberse definido (**RF-1**).
- **Secuencia normal**:

    1. El gestor carga todas las instrucciones y las ejecuta.
    2. Se registra la ejecución en caso de que sea necesario.
- **Poscondición**
- **Excepciones**: 

    + En caso de que aparezca algún error no contemplado por el administrador durante la ejecución, el caso de uso finalizará y se registrará el incidente.
- **Rendimiento**: Alto
- **Frecuencia**: Una vez por servicio, a menos que se registren eventos de tiempo periódicos.
- **Importancia**: Alta
- **Urgencia**: Alta
- **Estado**: Completo
- **Estabilidad**: Estable

RF 3: Detención
---------------

- **Versión**: 1
- **Autores**: Diego Martín
- **Fuentes**: Análisis preliminar
- **Objetivos asociados**: OBJ-2, OBJ-3
- **Requisitos asociados**: IRQ-2
- **Descripción**: El gestor permitirá a las diferentes unidades la ejecución de una acción destinada a la liberación de recursos, eliminar servicios publicados o cualquier otra tarea vinculada con la finalización de la ejecución del servicio antes de que el gestor sea detenido. 
- **Precondición**: El gestor debe encontrarse activado.
- **Secuencia normal**:

    1. A petición del Administrador o ante un evento de finalización (por ejemplo, el apagado del sistema), el gestor detectará esta condición.
    2. Se recorrerá la lista de servicios, invocando el método de finalización dispuesto a tal efecto.
    3. Cada uno de los servicios realizará la acción que el Administrador determinó para esta situación.
    4. Los diferentes servicios finalizan, y con ellos el gestor.
- **Poscondición**: El gestor y sus servicios se han detenido.
- **Excepciones**:

    + En caso de que la detención se realice de forma "brusca" (interrupción inesperada) no se ejecutará esta acción de limpieza.
- **Rendimiento**
- **Frecuencia**: Se espera que la frecuencia del caso de uso sea pequeña, dado que esta acción está destinada a un evento de apagado.
- **Importancia**: Media
- **Urgencia**: Media
- **Estado**: Completo
- **Estabilidad**: Estable

Vista de casos de uso
---------------------

.. toctree::
    :maxdepth: 2

    uc

.. 
    - **Versión**: 
    - **Autores**: 
    - **Fuentes**: 
    - **Objetivos asociados**: 
    - **Requisitos asociados**: 
    - **Descripción**
    - **Precondición**
    - **Secuencia normal**
    - **Poscondición**
    - **Excepciones**
    - **Rendimiento**
    - **Frecuencia**
    - **Importancia**
    - **Urgencia**
    - **Estado**
    - **Estabilidad**
    - **Comentarios**
