# Informe del Proyecto Observatorio Editorial

## Presentación

El presente documento constituye el informe final del proyecto "Observatorio Editorial", desarrollado como parte del trabajo de curso. Este sistema ha sido diseñado e implementado con el objetivo de gestionar y analizar información relacionada con el ámbito editorial, permitiendo el seguimiento de publicaciones, organizaciones, personas y otros elementos relevantes del sector.

El proyecto implementa una arquitectura moderna basada en tecnologías web, utilizando Django como framework principal y PostgreSQL como sistema gestor de base de datos, lo que garantiza robustez, escalabilidad y un alto rendimiento en el manejo de la información.

## Resumen

El Observatorio Editorial es un sistema de gestión diseñado para facilitar el seguimiento y análisis de información relacionada con el ámbito editorial. El objetivo principal del proyecto es proporcionar una plataforma centralizada que permita almacenar, consultar y analizar datos sobre publicaciones, organizaciones, personas y otros elementos del sector editorial.

La solución propuesta consiste en una aplicación web desarrollada con Django y PostgreSQL, que implementa una API REST para el acceso a los datos. El sistema cuenta con una estructura modular que facilita su mantenimiento y extensión, así como con un sistema de auditoría que permite el seguimiento de los cambios realizados en la base de datos.

Como resultado, se ha obtenido una aplicación funcional que cumple con los requisitos establecidos, proporcionando una interfaz intuitiva para la gestión de la información y garantizando la integridad y seguridad de los datos almacenados.

## Índice

1. Introducción
2. Descripción de la Solución Propuesta
   1. Requisitos
   2. Diseño
   3. Programación
   4. Pruebas
3. Conclusiones
4. Recomendaciones
5. Referencias Bibliográficas
6. Anexos

## Introducción

En el contexto actual, la gestión eficiente de la información relacionada con el ámbito editorial representa un desafío significativo para las instituciones y organizaciones del sector. La diversidad de fuentes, formatos y tipos de datos, así como la necesidad de realizar análisis complejos sobre esta información, requieren de herramientas especializadas que faciliten estas tareas.

El Observatorio Editorial surge como respuesta a esta problemática, con el objetivo de proporcionar una plataforma centralizada para la gestión y análisis de información editorial. Este sistema permite almacenar datos sobre campos de conocimiento, categorías, coberturas, códigos postales, condiciones de licencia y relaciones entre materias y ejes temáticos, entre otros elementos relevantes para el sector.

Los objetivos específicos del trabajo de curso incluyen:

1. Desarrollar una aplicación web que permita la gestión eficiente de la información editorial.
2. Implementar una API REST que facilite el acceso a los datos desde diferentes plataformas.
3. Diseñar una base de datos robusta que garantice la integridad y seguridad de la información.
4. Implementar un sistema de auditoría que permita el seguimiento de los cambios realizados en la base de datos.
5. Proporcionar una interfaz intuitiva que facilite la interacción con el sistema.

## Descripción de la Solución Propuesta

### Requisitos

#### Requisitos Funcionales

1. El sistema debe permitir la gestión (creación, lectura, actualización y eliminación) de campos de conocimiento.
2. El sistema debe permitir la gestión de categorías relacionadas con el ámbito editorial.
3. El sistema debe permitir la gestión de coberturas geográficas.
4. El sistema debe permitir la gestión de códigos postales.
5. El sistema debe permitir la gestión de condiciones de licencia.
6. El sistema debe permitir establecer relaciones entre materias y ejes temáticos.
7. El sistema debe registrar automáticamente los cambios realizados en la base de datos (auditoría).
8. El sistema debe proporcionar una API REST para el acceso a los datos.

#### Requisitos No Funcionales

1. El sistema debe ser desarrollado utilizando Python como lenguaje de programación principal.
2. El sistema debe utilizar PostgreSQL como sistema gestor de base de datos.
3. El sistema debe implementar una arquitectura modular que facilite su mantenimiento y extensión.
4. El sistema debe garantizar la integridad y seguridad de los datos almacenados.
5. El sistema debe proporcionar un rendimiento adecuado en la gestión de grandes volúmenes de información.

#### Diagrama de Casos de Uso

El diagrama de casos de uso del sistema incluye los siguientes actores y casos de uso principales:

**Actores:**
- Administrador: Encargado de la gestión del sistema y de los usuarios.
- Usuario: Persona que utiliza el sistema para consultar y gestionar la información editorial.

**Casos de Uso Principales:**
- Gestionar Campos de Conocimiento
- Gestionar Categorías
- Gestionar Coberturas
- Gestionar Códigos Postales
- Gestionar Condiciones de Licencia
- Gestionar Relaciones entre Materias y Ejes Temáticos
- Consultar Auditoría

### Diseño

#### Arquitectura del Sistema

El sistema se ha diseñado siguiendo una arquitectura de tres capas:

1. **Capa de Presentación**: Implementada mediante una API REST desarrollada con Django Rest Framework, que proporciona una interfaz para la interacción con el sistema.
2. **Capa de Lógica de Negocio**: Implementada mediante modelos y vistas de Django, que encapsulan la lógica de negocio del sistema.
3. **Capa de Datos**: Implementada mediante PostgreSQL, que almacena la información del sistema de forma persistente.

#### Diagrama de Clases

El diagrama de clases del sistema refleja la estructura de los modelos de datos utilizados. Las principales clases incluyen:

- **CampoDeConocimiento**: Representa un campo de conocimiento en el ámbito editorial.
- **Categoria**: Representa una categoría relacionada con el ámbito editorial.
- **Cobertura**: Representa una cobertura geográfica.
- **CodigoPostal**: Representa un código postal.
- **CondicionDeLaLicencia**: Representa una condición de licencia.
- **CorrespondeA**: Representa una relación entre una materia y un eje temático.
- **Auditoria**: Registra los cambios realizados en la base de datos.

Estas clases se han implementado tanto en Django (para la API REST) como en SQLAlchemy (para el acceso directo a la base de datos), siguiendo un patrón de diseño similar en ambos casos.

#### Descripción de Responsabilidades

La responsabilidad de gestionar los campos de conocimiento se implementa mediante el siguiente flujo de actividades:

1. El usuario solicita la creación, lectura, actualización o eliminación de un campo de conocimiento a través de la API REST.
2. La vista correspondiente (CampoDeConocimientoViewSet) recibe la solicitud y la procesa.
3. Si es necesario, se validan los datos utilizando el serializador correspondiente (CampoDeConocimientoSerializer).
4. Se realiza la operación solicitada en la base de datos mediante el modelo correspondiente (CampoDeConocimiento).
5. Se registra automáticamente el cambio en la tabla de auditoría mediante un trigger de PostgreSQL.
6. Se devuelve la respuesta al usuario a través de la API REST.

### Programación

#### Consideraciones para la Implementación de la Interfaz Gráfica

Aunque el sistema actual se centra en proporcionar una API REST, se han considerado los siguientes aspectos para una futura implementación de la interfaz gráfica:

1. Utilización de un framework de frontend moderno (como React o Vue.js) que consuma la API REST.
2. Diseño responsive que se adapte a diferentes dispositivos y tamaños de pantalla.
3. Implementación de componentes reutilizables que faciliten el mantenimiento y la extensión de la interfaz.
4. Utilización de bibliotecas de componentes que proporcionen una experiencia de usuario consistente.

#### Estructuras de Datos Utilizadas

Para el tratamiento de los datos en memoria interna, se han utilizado las siguientes estructuras de datos:

1. **Modelos de Django**: Utilizados para representar las entidades del sistema y facilitar su persistencia en la base de datos.
2. **Serializadores de Django Rest Framework**: Utilizados para convertir los modelos de Django en formatos que puedan ser fácilmente consumidos por la API REST (como JSON).
3. **Modelos de SQLAlchemy**: Utilizados para el acceso directo a la base de datos, proporcionando una interfaz orientada a objetos para la manipulación de los datos.

La elección de estas estructuras se fundamenta en su capacidad para representar de forma eficiente las entidades del sistema, así como en su integración con los frameworks utilizados (Django y SQLAlchemy).

#### Manual de Usuario

**Gestión de Campos de Conocimiento**

Para gestionar los campos de conocimiento, el usuario puede utilizar los siguientes endpoints de la API REST:

- `GET /api/campos/`: Obtiene la lista de todos los campos de conocimiento.
- `GET /api/campos/{id}/`: Obtiene un campo de conocimiento específico.
- `POST /api/campos/`: Crea un nuevo campo de conocimiento.
- `PUT /api/campos/{id}/`: Actualiza un campo de conocimiento existente.
- `DELETE /api/campos/{id}/`: Elimina un campo de conocimiento.

**Gestión de Categorías**

Para gestionar las categorías, el usuario puede utilizar los siguientes endpoints de la API REST:

- `GET /api/categorias/`: Obtiene la lista de todas las categorías.
- `GET /api/categorias/{id}/`: Obtiene una categoría específica.
- `POST /api/categorias/`: Crea una nueva categoría.
- `PUT /api/categorias/{id}/`: Actualiza una categoría existente.
- `DELETE /api/categorias/{id}/`: Elimina una categoría.

**Consulta de Auditoría**

Para consultar la auditoría, el usuario puede utilizar los siguientes endpoints de la API REST:

- `GET /api/auditoria/`: Obtiene la lista de todos los registros de auditoría.
- `GET /api/auditoria/{id}/`: Obtiene un registro de auditoría específico.

### Pruebas

#### Casos de Prueba

**Caso de Prueba 1: Creación de un Campo de Conocimiento**

- **Objetivo**: Verificar que se puede crear un nuevo campo de conocimiento.
- **Datos de Entrada**: Nombre del campo de conocimiento.
- **Resultado Esperado**: El campo de conocimiento se crea correctamente y se devuelve su identificador.
- **Resultado Obtenido**: El campo de conocimiento se crea correctamente y se devuelve su identificador.

**Caso de Prueba 2: Actualización de una Categoría**

- **Objetivo**: Verificar que se puede actualizar una categoría existente.
- **Datos de Entrada**: Identificador de la categoría y nuevo nombre.
- **Resultado Esperado**: La categoría se actualiza correctamente y se devuelven los datos actualizados.
- **Resultado Obtenido**: La categoría se actualiza correctamente y se devuelven los datos actualizados.

**Caso de Prueba 3: Eliminación de un Código Postal**

- **Objetivo**: Verificar que se puede eliminar un código postal existente.
- **Datos de Entrada**: Identificador del código postal.
- **Resultado Esperado**: El código postal se elimina correctamente y se devuelve un código de estado 204 (No Content).
- **Resultado Obtenido**: El código postal se elimina correctamente y se devuelve un código de estado 204 (No Content).

**Caso de Prueba 4: Consulta de Auditoría**

- **Objetivo**: Verificar que se pueden consultar los registros de auditoría.
- **Datos de Entrada**: Ninguno.
- **Resultado Esperado**: Se devuelve la lista de todos los registros de auditoría.
- **Resultado Obtenido**: Se devuelve la lista de todos los registros de auditoría.

## Conclusiones

El desarrollo del proyecto "Observatorio Editorial" ha permitido alcanzar los objetivos planteados, proporcionando una plataforma robusta y eficiente para la gestión y análisis de información relacionada con el ámbito editorial. A continuación, se presentan las principales conclusiones del trabajo realizado:

1. Se ha desarrollado una aplicación web que permite la gestión eficiente de la información editorial, cumpliendo con los requisitos funcionales y no funcionales establecidos.

2. Se ha implementado una API REST que facilita el acceso a los datos desde diferentes plataformas, proporcionando una interfaz clara y consistente para la interacción con el sistema.

3. Se ha diseñado una base de datos robusta que garantiza la integridad y seguridad de la información, utilizando PostgreSQL como sistema gestor y aprovechando sus características avanzadas, como los triggers para la implementación del sistema de auditoría.

4. Se ha implementado un sistema de auditoría que permite el seguimiento de los cambios realizados en la base de datos, facilitando la trazabilidad de las operaciones y el control de la información.

5. Se ha proporcionado una documentación detallada que facilita la comprensión del sistema y su utilización por parte de los usuarios.

El proyecto ha demostrado la viabilidad de utilizar tecnologías modernas como Django, Django Rest Framework y SQLAlchemy para el desarrollo de sistemas de gestión de información complejos, proporcionando una base sólida para futuras extensiones y mejoras.

## Recomendaciones

A partir de la experiencia adquirida durante el desarrollo del proyecto y considerando las posibilidades de mejora y extensión del sistema, se presentan las siguientes recomendaciones:

1. Implementar una interfaz gráfica de usuario que facilite la interacción con el sistema, utilizando un framework de frontend moderno como React o Vue.js.

2. Ampliar la funcionalidad del sistema para incluir la gestión de otros elementos relevantes para el ámbito editorial, como publicaciones, autores, editores, etc.

3. Implementar un sistema de autenticación y autorización más avanzado, que permita definir diferentes roles de usuario y controlar el acceso a las funcionalidades del sistema de forma más granular.

4. Desarrollar funcionalidades de análisis y visualización de datos que permitan obtener información valiosa a partir de los datos almacenados en el sistema.

5. Implementar pruebas automatizadas más exhaustivas, incluyendo pruebas unitarias, de integración y de rendimiento, para garantizar la calidad y robustez del sistema.

6. Considerar la posibilidad de desplegar el sistema en un entorno de producción utilizando contenedores (como Docker) para facilitar su instalación y mantenimiento.

## Referencias Bibliográficas

1. Django Project. (2023). Django Documentation. Recuperado de https://docs.djangoproject.com/

2. Django REST Framework. (2023). Django REST Framework Documentation. Recuperado de https://www.django-rest-framework.org/

3. PostgreSQL Global Development Group. (2023). PostgreSQL Documentation. Recuperado de https://www.postgresql.org/docs/

4. SQLAlchemy. (2023). SQLAlchemy Documentation. Recuperado de https://docs.sqlalchemy.org/

5. Sommerville, I. (2016). Software Engineering (10th ed.). Pearson Education Limited.

6. Fowler, M. (2003). Patterns of Enterprise Application Architecture. Addison-Wesley Professional.

7. Richardson, L., & Ruby, S. (2007). RESTful Web Services. O'Reilly Media.

## Anexos

### Anexo 1: Modelo Lógico de los Datos

El modelo lógico de los datos del sistema incluye las siguientes entidades principales:

- **Campo_de_conocimiento**: Almacena información sobre los campos de conocimiento.
  - campo_id: Identificador único del campo de conocimiento.
  - nombre_del_campo: Nombre del campo de conocimiento.

- **Categoria**: Almacena información sobre las categorías.
  - id_categoria: Identificador único de la categoría.
  - nombre: Nombre de la categoría.

- **Cobertura**: Almacena información sobre las coberturas geográficas.
  - id_cobertura: Identificador único de la cobertura.
  - cobertura: Descripción de la cobertura.

- **Codigo_Postal**: Almacena información sobre los códigos postales.
  - id_codigo: Identificador único del código postal.

- **Condicion_de_la_licencia**: Almacena información sobre las condiciones de licencia.
  - id_condicion_de_la_licencia: Identificador único de la condición de licencia.
  - condicion_de_la_licencia: Descripción de la condición de licencia.

- **Corresponde_A**: Almacena información sobre las relaciones entre materias y ejes temáticos.
  - materias__idem: Identificador de la materia.
  - ejetem__ideje: Identificador del eje temático.

- **auditoria**: Almacena información sobre los cambios realizados en la base de datos.
  - id_auditoria: Identificador único del registro de auditoría.
  - tabla_afectada: Nombre de la tabla afectada por el cambio.
  - operacion: Tipo de operación realizada (INSERT, UPDATE, DELETE).
  - usuario: Usuario que realizó la operación.
  - fecha_hora: Fecha y hora en que se realizó la operación.
  - datos_antiguos: Datos antes de la operación (para UPDATE y DELETE).
  - datos_nuevos: Datos después de la operación (para INSERT y UPDATE).

### Anexo 2: Diagrama Entidad-Relación

El diagrama entidad-relación del sistema muestra las entidades principales y sus relaciones:

- **Campo_de_conocimiento** es una entidad independiente.
- **Categoria** es una entidad independiente.
- **Cobertura** es una entidad independiente.
- **Codigo_Postal** es una entidad independiente.
- **Condicion_de_la_licencia** es una entidad independiente.
- **Corresponde_A** establece una relación muchos a muchos entre materias y ejes temáticos.
- **auditoria** registra los cambios realizados en las demás entidades.

### Anexo 3: Diagrama de Clases

El diagrama de clases del sistema muestra la estructura de los modelos de datos utilizados, tanto en Django como en SQLAlchemy:

- **CampoDeConocimiento**: Representa un campo de conocimiento.
  - Atributos: campo_id, nombre_del_campo
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

- **Categoria**: Representa una categoría.
  - Atributos: id_categoria, nombre
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

- **Cobertura**: Representa una cobertura geográfica.
  - Atributos: id_cobertura, cobertura
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

- **CodigoPostal**: Representa un código postal.
  - Atributos: id_codigo
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

- **CondicionDeLaLicencia**: Representa una condición de licencia.
  - Atributos: id_condicion_de_la_licencia, condicion_de_la_licencia
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

- **CorrespondeA**: Representa una relación entre una materia y un eje temático.
  - Atributos: materias__idem, ejetem__ideje
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

- **Auditoria**: Registra los cambios realizados en la base de datos.
  - Atributos: id_auditoria, tabla_afectada, operacion, usuario, fecha_hora, datos_antiguos, datos_nuevos
  - Métodos: __str__ (Django), __repr__ (SQLAlchemy)

### Anexo 4: Diagrama de Arquitectura

El diagrama de arquitectura del sistema muestra las principales componentes y su interacción:

1. **Cliente**: Aplicación o sistema que consume la API REST.
2. **Servidor Web**: Servidor que aloja la aplicación Django.
3. **Django**: Framework web que implementa la lógica de negocio y la API REST.
4. **Django Rest Framework**: Framework que facilita la implementación de la API REST.
5. **SQLAlchemy**: ORM que proporciona acceso directo a la base de datos.
6. **PostgreSQL**: Sistema gestor de base de datos que almacena la información del sistema.

La interacción entre estos componentes sigue el siguiente flujo:

1. El cliente realiza una solicitud HTTP a la API REST.
2. El servidor web recibe la solicitud y la pasa a Django.
3. Django procesa la solicitud utilizando las vistas y serializadores correspondientes.
4. Si es necesario, Django accede a la base de datos utilizando sus modelos ORM.
5. Alternativamente, se puede acceder a la base de datos directamente utilizando SQLAlchemy.
6. La respuesta se devuelve al cliente en formato JSON.