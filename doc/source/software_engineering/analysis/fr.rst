Requisitos funcionales
======================

RF 1: Creación de una unidad de gestión
---------------------------------------

- **Versión**: 
- **Autores**: 
- **Fuentes**: 
- **Objetivos asociados**: 
- **Requisitos asociados**: 
- **Descripción**: Un Administrador (**ACT-1**) podrá definir una nueva unidad para gestionar un servicio. 
- **Precondición**
- **Secuencia normal**:

    1. El Administrador (**ACT-1**) crea la unidad definiendo el comportamiento de la misma durante el inicio y fin del gestor, el momento en el que debe ser ejecutada y otros parámetros adicionales.
    2. Solicita al gestor que publique el servicio.
    3. El gestor procesa los datos, programa los eventos de tiempo (si los hay, en caso contrario la ejecución comienza inmediatamente al terminar este caso de uso) y en caso de que toda la información que el Administrador ha indicado sea válida, añade el servico a la lista de servicios a procesar.
- **Poscondición**: El servicio es programado para su ejecución.
- **Excepciones**: En caso de que alguno de los parámetros que el Administrador no sea válido, se registrará el incidente y el caso de uso finalizará.
- **Rendimiento**
- **Frecuencia**
- **Importancia**: Alta
- **Urgencia**: Alta
- **Estado**: Completo
- **Estabilidad**: Estable
- **Comentarios**: Los posibles errores que la ejecución o cualquier otro aspecto no evaluable en el momento de añadir el servicio puedan ocasionar serán procesados durante la ejecución (**RF-2**) o detención del servicio (**RF-3**)

RF 2: Ejecución de un servicio
------------------------------

- **Versión**: 
- **Autores**: 
- **Fuentes**: 
- **Objetivos asociados**: 
- **Requisitos asociados**: 
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
- **Comentarios**


RF 3: Detención
---------------

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


.. Detención
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
