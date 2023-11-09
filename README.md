# Patrones-creacionales

El link al repositorio es el siguiente: https://github.com/Germiprogramer/Patrones-creacionales.git

# Ejercicio 1

De cara a este ejercicio, se ha decidido implementar el abstract factory en un archivo, debido a problemas de importaciones mutuas al intentar separar el código en distintos archivos.

**Limpieza de datos**

Conversión de Meses de Texto a Números:

En muchos conjuntos de datos, los nombres de los meses se almacenan como texto (por ejemplo, 'ENERO', 'FEBRERO', etc.).
Convertir los nombres de los meses de texto a números facilita su manipulación y análisis. Los algoritmos y análisis estadísticos suelen trabajar mejor con datos numéricos que con texto.
La conversión de meses a números también permite realizar análisis de series temporales o comparaciones de datos en diferentes meses de una manera más efectiva.
Conversión de Horas de Formato de 24 Horas a Minutos del Día:

En algunos conjuntos de datos, las horas se almacenan en formato de 24 horas (por ejemplo, '14:30', '18:45', etc.).
Convertir las horas a minutos del día permite una representación numérica más compacta y fácil de manejar. Por ejemplo, '14:30' se convierte a 870 minutos (14 horas * 60 minutos/hora + 30 minutos).

Se ha decidido crear una fábrica para realizar análisis estadísticos. Los resultados se presentan a continuación, considerando que las horas se han expresado en minutos:

**Para la variable "Hora Solicitud":**
- **Moda:** La moda es 785.0 minutos, lo que indica que este valor es el más común o frecuente en las horas de solicitud. En otras palabras, la mayoría de las solicitudes se realizaron aproximadamente a las 13 horas y 5 minutos (785 minutos desde el inicio del día, considerando 60 minutos en una hora).
- **Media:** La media es aproximadamente 818.92 minutos, lo que equivale a aproximadamente 13 horas y 38 minutos. Este valor representa el punto medio de todas las horas de solicitud registradas.

**Para la variable "Hora Intervención":**
- **Moda:** La moda es 814.0 minutos, lo que sugiere que este valor es el más frecuente en las horas de intervención. La mayoría de las intervenciones ocurrieron alrededor de las 13 horas y 34 minutos (814 minutos desde el inicio del día).
- **Media:** La media es aproximadamente 821.27 minutos, equivalente a aproximadamente 13 horas y 41 minutos. Esta cifra muestra el punto medio entre todas las horas de intervención registradas.

**Para la variable "Mes":**
- **Moda:** La moda es 5, lo que indica que el mes número 5 es el más común en los datos. En términos calendario, esto podría referirse a mayo, dependiendo del sistema de numeración de meses que se esté utilizando (por ejemplo, si se empieza a contar desde enero como 1).
- **Media:** La media es aproximadamente 6.66, indicando un promedio de 6 meses y 19 días. Dado que los meses son valores discretos y se expresan como números enteros, este valor podría representar una media ponderada en algún contexto específico, pero sin más información, es difícil interpretar su significado exacto.

La información sobre las horas y meses de mayor frecuencia puede ser útil para la planificación y gestión de recursos en función de los momentos de mayor demanda. Además, cabe destacar un punto extraño, y es que la hora media de intervención es antes que la hora media de solicitud. Esto se debe a que algunas solictudes nocturnas son intervenidasen la madrugada del día siguiente, causando un malente,dido en nuestro análisis.

Los graficos son los siguientes:

<img width="478" alt="Captura de pantalla 2023-11-09 223938" src="https://github.com/Germiprogramer/Patrones-creacionales/assets/91720991/6041021d-3c2f-44c2-889d-2966381c5a0b">
<img width="480" alt="Captura de pantalla 2023-11-09 223949" src="https://github.com/Germiprogramer/Patrones-creacionales/assets/91720991/3c1a534c-ed8e-4dcf-ac73-94f68d0d26f5">
<img width="477" alt="Captura de pantalla 2023-11-09 223959" src="https://github.com/Germiprogramer/Patrones-creacionales/assets/91720991/0cf9bdc4-a552-4b98-903e-cc72f94c27b1">

Desgraciadamente, parece que los gráficos se han guardado como imágenes en blanco en el proyecto, pero esto es lo que debería salir.

# Ejercicio 2

**Justificación patron builder**

El patrón Builder es un patrón creacional que se utiliza para construir objetos complejos paso a paso. En el caso de una pizzería, este patrón se adapta perfectamente para crear pizzas con diferentes combinaciones de ingredientes, masa, salsa, cocción, presentación, maridaje y extras. Vamos a justificar el uso del patrón Builder en este contexto.

1. **Separación de la construcción y la representación:** Uno de los principios clave del patrón Builder es separar la construcción de un objeto complejo de su representación. En el contexto de una pizzería, hay muchas formas diferentes de combinar ingredientes, tipos de masa, salsas, y demás. Usando el patrón Builder, puedes encapsular todo ese proceso complejo en una clase PizzaBuilder separada, permitiendo que la pizzería construya pizzas de manera flexible y sin necesidad de conocer los detalles internos de cómo se ensamblan las pizzas. Además, permite separar las pizzas en distintos tipos, creando distintas clases creadoras y distintos directores.

2. **Facilita la creación de objetos complejos:** Imagina una pizzería que ofrece pizzas con una amplia gama de ingredientes y opciones personalizables. Al utilizar el patrón Builder, puedes tener diferentes constructores para diferentes tipos de pizzas (por ejemplo, PizzaMargheritaBuilder, PizzaHawaianaBuilder, etc.). Cada constructor sabe cómo ensamblar una pizza específica, simplificando el proceso de creación de pizzas complejas.

3. **Código fácil de extender:** Con el patrón builder, puedes crear un código más simple y coomprensible. Teniendo en cuenta que builder construye por partes, resulta fácil de entender la elaboración de una pizza como un paso a paso.

4. **Encapsulación de la lógica de construcción:** Al encapsular la lógica de construcción dentro de la clase PizzaBuilder, puedes ocultar los detalles de implementación de cómo se ensamblan las pizzas. Esto proporciona una capa de abstracción que protege el código cliente de cambios en la forma en que se construyen las pizzas. Si en el futuro cambias la forma en que se preparan ciertos ingredientes, solo necesitas actualizar el código dentro del builder sin afectar al resto de la aplicación.

En resumen, el patrón Builder es una elección sólida para el diseño de una pizzería porque proporciona una forma estructurada y flexible de construir pizzas complejas con numerosas combinaciones posibles de ingredientes y opciones, al mismo tiempo que mejora la legibilidad, la mantenibilidad y la extensibilidad del código.

___________________________________________________________________________________________________________________________________________________________________
**Explicacion planteamiento**

Al principio hemos realizado el patron builder para realizar la pizza. La interfaz Pizza proporciona una estructura común para construir diferentes tipos de pizzas. Los métodos abstractos garantizan que todas las clases concretas que implementan esta interfaz deben proporcionar una implementación específica para cada uno de estos métodos. Cada método representa un componente esencial de la pizza final, y al implementar la interfaz, se pueden crear pizzas personalizadas y específicas utilizando diferentes combinaciones de estos componentes. El código tiene una clase Director que orquesta el proceso de construcción del objeto y varios constructores (clases que implementan la interfaz Pizza) que implementan los pasos específicos para construir diferentes tipos de pizzas.

Además, se ha realizado un pseudo gestor de clientes usando una interfaz gráfica de tkinter. Para ello hemos creado dos csv, clientes y pedidos. 

La interfaz gráfica tiene 4 pantallas. La primera pide el registro para usuarios no pertecientes al dataset, y el inicio de sesión para usuarios que ya están registrados. Si se registran, se escriben sus datos en el dataset.

La segunda interfaz permite elegir entre pizzas de menú o pizzas personalizadas. Además, permite recibir al usuario recomendaciones en función de las pizzas que más ha pedido. 

La otras dos interfaces son para pedir pizza de menu o personalizada. Lo que pida el usuario se almacena en la base de datos de pedidos. Desgraciadamente, la pizza de menu no se almacena correctamente, no estoy seguro de por qué dado que al ser implementada al inicio no daba ningún tipo de error.
