# **Módulo 3 - Fundamentos de Python 1**
## **Valores booleanos, ejecución condicional, bucles, listas y su procesamiento, operadores lógicos y de bit a bit**

En este módulo, aprenderás sobre:

- Datos de tipo booleano.
- Operadores relaccionales.
- Cómo tomar decisiones en Python (if, if-else, if-elif, else)
- Cómo repetir la ejecución de código usando los bucles (while, for).
- Cómo realizar operaciones lógicas y de bit a bit en Python.
- Listas en Python (construcción, indexacioón y segmentación; manipulación 
de contenido).
- Cómo ordenar una lista usando algoritmos de clasificación de burbujas.
- Listas multidimensionales y sus aplicaciones.

## **Condiciones y ejecución condicional**
Ya sabes como hacer preguntas a Python, pero aún no sabes como hacer un uso razonable de las respuestas. Se debe tener un
mecanismo que le permita hacer algo **si se cumple una condición, y no hacerlo si no se cumple**.

Es como en la vida real: haces ciertas cosas o no cuando se cumple una condición específica,por ejemplo, sales a caminar si el clima es
bueno, o te quedas en casa si está húmedo y frío.

Para tomar tales decisiones, Python ofrece una instrucción especial. Debido a su naturaleza y su aplicación, se denomina **instrucción**
**condicional** (o sentencia condicional).

Existen varias variantes de la misma. Comenzaremos con la más simple, aumentando la dificultad lentamente.

La primera forma de una sentencia condicional, que puede ver a continuación, está escrita de manera muy informal pero figurada:

´´´
if true_or_not:
    do_this_if_true
´´´

Esta sentencia condicional consta d elos siguientes elementos, estrictamente necesarios en este orden: 

- La palabra clave reservada ´if´
- Uno o más espacios en blanco
- Una expersión (una pregunta o una respuesta) cuyo valor e interpreta únicamente en términos de ´True´ (cuando su valor no
sea cero) y ´False´ (cuando sea igual a cero)
- Unos **dos puntos** seguido de una nueva línea.
- Una instrucción **con sangría** o conjunto de instrucciones (se requiere absolutamente almenos una instrucción); la **sangría** se
puede lograr de dos maneras: insertando un número particular de espacios (la recomendación es usar **cuatro espacios de**
**sangría**), o usando el *tabulador*; nota: si hay mas de una instrucción en la parte con sangría, la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan tabuladores con espacios, es importante que todas las sangrías
**sean exactamente iguales**. Python 3 **no permite mezclar espacios y tabuladores** para la sangría.