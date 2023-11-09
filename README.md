# Patrones-creacionales

El link al repositorio es el siguiente: https://github.com/Germiprogramer/Patrones-creacionales.git

# Ejercicio 1

De cara a este ejercicio, se ha decidido implementar el abstract factory en un archivo, debido a problemas de importaciones mutuas al intentar separar el código en distintos archivos.

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

# Ejercicio 2

**Justificación patron builder**

El patrón Builder es un patrón creacional que se utiliza para construir objetos complejos paso a paso. En el caso de una pizzería, este patrón se adapta perfectamente para crear pizzas con diferentes combinaciones de ingredientes, masa, salsa, cocción, presentación, maridaje y extras. Vamos a justificar el uso del patrón Builder en este contexto.

1. **Separación de la construcción y la representación:** Uno de los principios clave del patrón Builder es separar la construcción de un objeto complejo de su representación. En el contexto de una pizzería, hay muchas formas diferentes de combinar ingredientes, tipos de masa, salsas, y demás. Usando el patrón Builder, puedes encapsular todo ese proceso complejo en una clase PizzaBuilder separada, permitiendo que la pizzería construya pizzas de manera flexible y sin necesidad de conocer los detalles internos de cómo se ensamblan las pizzas. Además, permite separar las pizzas en distintos tipos, creando distintas clases creadoras y distintos directores.

2. **Facilita la creación de objetos complejos:** Imagina una pizzería que ofrece pizzas con una amplia gama de ingredientes y opciones personalizables. Al utilizar el patrón Builder, puedes tener diferentes constructores para diferentes tipos de pizzas (por ejemplo, PizzaMargheritaBuilder, PizzaHawaianaBuilder, etc.). Cada constructor sabe cómo ensamblar una pizza específica, simplificando el proceso de creación de pizzas complejas.

3. **Código fácil de extender:** Con el patrón builder, puedes crear un código más simple y coomprensible. Teniendo en cuenta que builder construye por partes, resulta fácil de entender la elaboración de una pizza como un paso a paso.

4. **Encapsulación de la lógica de construcción:** Al encapsular la lógica de construcción dentro de la clase PizzaBuilder, puedes ocultar los detalles de implementación de cómo se ensamblan las pizzas. Esto proporciona una capa de abstracción que protege el código cliente de cambios en la forma en que se construyen las pizzas. Si en el futuro cambias la forma en que se preparan ciertos ingredientes, solo necesitas actualizar el código dentro del builder sin afectar al resto de la aplicación.

En resumen, el patrón Builder es una elección sólida para el diseño de una pizzería porque proporciona una forma estructurada y flexible de construir pizzas complejas con numerosas combinaciones posibles de ingredientes y opciones, al mismo tiempo que mejora la legibilidad, la mantenibilidad y la extensibilidad del código.
