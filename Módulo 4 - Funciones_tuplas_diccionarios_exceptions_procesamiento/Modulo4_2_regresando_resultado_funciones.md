# **Módulo 4 - Fundamentos de Python 1**
## **Regresando el resultado de una función**

## **Efectos y resultados: la instrucción `return`**
Todas las funciones presentadas anteriormente tienen algún tipo de efecto: producen un texto y lo envían a la consola.

Por supuesto, las funciones, al igual que las funciones matemáticas, pueden tener resultados.

Para lograr que las **funciones devuelvan un valor** (pero no solo para ese propósito) se utiliza la instrucción `return` (regresar o
retornar).

Esta palabra nos da una idea completa de sus capacidades. Nota: es una **palabra clave reservada** de Python.

La instrucción `return` tiene **dos variantes diferentes**: Considerémoslas por separado.


## **`return` sin una expresión**
La primera consiste en la palabra reservada en sí, sin nada que la siga.

Cuando se emplea dentro de una función, provoca la **terminación inmediata de la ejecución de la función, y un retorno**
**instantáneo (de ahí el nombre) al punto de invocación**.

Nota: si una función no está destinada a producir un resultado, **emplear la instrucción `return` no es obligatorio**, se ejecutará
implícitamente al final de la función.

De cualquier manera, se puede emplear para **terminar las actividades de una función**, antes de que el control llegue a la última
línea de la función.

---------------------------------

Consideremos la siguiente función:
```
def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    
    print("¡Feliz año nuevo!")
```

Cuando se invoca sin ningún argumento:
`happy_new_year()`

La función produce un poco de ruido; la salida se verá así:
```
Tres...
Dos...
Uno...
¡Feliz año nuevo!
```

Al proporcionar `false` como argumento:
`happy_new_year(False)`

Se modificará el comportamiento de la función; la instrucción `return` provocará su terminación justo antes de los deseos. Esta es la
salida actualizada:
```
Tres...
Dos...
Uno...
```


## **`return` con una expresión**
La segunda variante de `return` está **extendida con una expresión**:
```
def function():
    return expression
```

Existen dos consecuencias de usarla:

- Provoca la **terminación inmediata de la ejecución de la función** (nada nuevo en comparación con la primer variante).
- Además, la función **evaluará el valor de la expresión y lo devolverá (de ahí el nombre una vez más) como el resultado de la**
**función**.

Si, este ejemplo es sencillo:
```
def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)
```

El fragmento de código escribe el siguiente texto en la consola:
`La función boring_function ha devuelto su resultado. Es: 123`

Vamos a investigarlo.

Analiza la siguiente imagen:

![boring_function](../img/boring_function.jpg)

La instrucción `return`, enrriquecida con la expresión (la expresión es muy simple aquí), "transporta" el valor de la expresión al lugar
donde se ha invocado la función.

El resultado se puede usar libremente aquí, por ejemplo, para ser asignado a una variable.

También puede ignorarse por completo y perderse sin dejar rastro.

Ten en cuenta que no estamos siendo muy educados aquí: la función devuelve un valor y lo ignoramos (no lo usamos de ninguna
manera):
```
def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")
```

El programa produce el siguiente resultado:
```
¡Esta lección es interesante!
'Modo aburrimiento' ON.
Esta lección es aburrida...
```

Está mal? De ninguna manera.

La única desventaja es que el resultado se ha perdido irremediablemente.
No olvides:

- Siempre se te **permite ignorar el resultado de la función** y estar satisfecho con el efecto de la función (si la función tiene
alguno).
- Si una función intenta devolver un resultado útil, debe contener la segunda variante de la instrucción `return`.

Espera un segundo, significa esto que también hay resultados inútiles? sí, en cierto sentido.


## **Unas pocas palabras acerca de `none`**
Permítenos presentarte un valor muy curioso (para ser honestos, un valor que es ninguno) llamado `None`.

Sus datos no representan valor razonable alguno; en realidad, no es un valor en lo absoluto; por lo tanto, **no**
**debe participar en ninguna expresión**.

Por ejemplo, un fragmento de código cmo el siguiente:
`print(None + 2)`

Causará un error de tiempo de ejecución, descrito por el siguiente mensaje de diagnóstico:
`TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`

Nota: `None` es una **palabra clave reservada**.

Solo existen dos tipos de circunstancias en las que `None` se puede usar de manera segura:

- Cuando **se le asigna a una variable** (o se devuelve como **el resultado de una función**).
- Cuando **se le compara con una variable** para diagnosticar su estado interno.

Al igual que aquí: 
```
value = None
if value is None:
    print("Lo siento, no contienes ningún valor")
```

No olvides esto: si una función no devuelve un cierto valor utilizando una cláusula de expresión `return`, se
asume que **devuelve implícitamente** `none`.

Echemos un vistazo al siguiente código: 
```
def strange_function(n):
    if(n % 2 == 0):
        return True
```

Es obvio que la función `strange_function` retorna `True` cuando su argumento es par.

Qué es lo que retorna de otra manera?

Podemos usar el siguiente código para verificarlo:
```
print(strange_function(2))
print(strange_function(1))
```

Esto es lo que vemos en consola:
```
True
None
```

No te sorprendas la próxima vez que veas `None` como el resultado de la función, puede ser el síntoma de un
error sutil dentro de la función.