# **Módulo 1 - Comienza tu viaje con Python**  

## **Como obtener y utilizar Python**
Existen varias formas de obtener tu propia copia de Python 3, dependiendo del sistema operativo que utilices.

**Es probable que los usuarios de Linux tengan Pythoin ya instalado** - este es el escenario más porobable, ya que la infraestructura de
Python se usa de forma intensiva en muchos componentes del sistema operativo Linux.

Por ejemplo, algunas distribuciones pueden ensamblar herramientas específicas con el sistema y muchas de estas herramientas,
como los administradores de paquetes, a menudo están escritas en Python. Algunas partes de los entornos gráficos disponibles en el 
mundo de Linux también pueden usar Python.

Si eres un usuario de Linux, abre la terminal/consola y escribe:
```
Python3
```

En el prompt del shell, presiona Enter y espera.

Si ves algo como esto:

```
Python 3.4.5 (default, Jan 12 2017, 02:28:40)
[GCC 4.2.1 Compatible Clang 3.7.1 (tags/RELEASE_371/final)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Entonces no tienes que hacer nada más.



Si Python 3 está ausente, consulta la documentación de Linux para saber cómo utilizar tu administrador de paquetes para descargar e instalar un paquete nuevo. El que necesitas se llama python3 o su nombre comienza con eso.

Todos los usuarios que no sean de Linux pueden descargar una copia en https://www.python.org/downloads/.  

![linux_terminal_1](../img/linux_terminal_1.jpg)


## **Descargando e instalando Python**
Debido a que el navegador le dice al sitio web al que se ingresó, el sistema operativo que se utiliza, el único paso que se debe seguir es 
hacer clic en la versión de Python que se desea.

En este caso, selecciona Python 3. El sitio siempre te ofrece la última versión.

Si eres un **usuario de Windows**, utiliza el archivo .exe descargado y sigue todos los pasos.

Deja las configuraciones predeterminadas que el instalador sugiere por ahora, con una excepción: observa la casilla de verificación 
denominada **Agregar Python 3.x a PATH** y selecciónala.

Esto hará las cosas más fáciles.

Si eres un **usuario de macOS**, es posible que ya se haya preinstalado una versión de Python 2 en tu computadora, pero como estaremos trabajando con Python 3, aún deberás descargar e instalar el archivo .pkg correspondiente desde el sitio de Python.

![web_descargas_python](../img/web_descargas_python.jpg)  

## **Comenzando tu trabajo con Python**
Ahora que tienes Python 3 instalado, es hora de verificar si funciona y de utilizarlo por primera vez.

Este será un procedimiento muy simple, pero debería ser suficiente para convencerte de que el entorno de Python es completo y 
funcional.

Existen muchas formas de utilizar Python, especialmente si vas a ser un desarrollador de Python.

Para comenzar tu trabajo, necesitas las siguientes herramientas:

- Un **editor** que te ayudará a escribir el código (debe tener algunas características especiales, no disponibles en herramientas
simples); este editor dedicado te dará más que el equipo estándar del sistema operativo.

- Una **consola** en la que puedas ejecutar tu código recién escrito y detenerlo por la fuerza cuando se sale de control.

- Una herramienta llamada **depurador**, capaz de ejecutar tu código paso a paso y te permite inspeccionarlo en cada momento de
su ejecución.

Además de sus muchos componentes útiles, la instalación estándar de Python 3 contiene una aplicación muy simple pero
extremadamente útil llamada IDLE.

**IDLE** es un acrónimo de: Integrated Development and Learning Environment (Desarrollo Integrado y Entorno de Aprendizaje).

Navega por los menús de tu sistema operativo, encuentra IDLE en algún lugar debajo de Python 3.x y ejecútalo. Esto es lo que deberías 
ver:

![idle_shell_python](../img/idle_shell_python.jpg)  

## **Cómo escribir y ejecutar tu primer programa**
Ahora es el momento de escribir y ejecutar tu primer programa en Python 3. Por ahora, será muy simple.

El primer paso es crear un nuevo archivo fuente y llenarlo con el código. Haz clic en *File* en el menú del IDLE y selecciona *New File*:

![python_shell_new_file](../img/python_shell_new_file.jpg)  

Como puedes ver, IDLE abre una nueva ventana para ti. Puedes usarla para escribir y modificar tu código.

Esta es la **ventana del editor**. Su único propósito es ser un lugar de trabajo en el que se trate tu código fuente. No confundas
la ventana del editor con la ventana del shell. Realizan diferentes funciones.

La ventana del editor actualmente no tiene título, pero es una buena práctica comenzar a trabajar nombrando el archivo fuente.

Haz clic en *File* (en la nueva ventana), luego haz clic sobre *Save as ...* , selecciona una carpeta para el nuevo archivo (el escritorio es un
buen lugar para tus primeros intentos de programación) y elige un nombre para el nuevo archivo:

![python_shell_naming](../img/python_shell_naming.jpg)  

Nota: no establezcas ninguna extensión para el nombre de archivo que vas a utilizar. Python necesita que sus archivos tengan la
extensión *.py*, por lo que debes confiar en los valores predeterminados de la ventana de diálogo. El uso de la extensión *.py* permite
que el sistema operativo abra estos archivos correctamente.

## **Cómo ejecutar tu primer programa**
Ahora solo coloca una línea en tu ventana de editor recién abierta y con nombre.

La línea se ve así:
```
print("Hisssssss...")
```

Puedes utilizar el portapapeles para copiar el texto en el archivo.

No vamos a explicar el significado del programa en este momento. Encontrarás una discusión detallada en el siguiente capítulo.

Echa un vistazo más de cerca a las comillas. Estas son la forma más simple de las comillas (neutrales, rectas, etc.) que se usan
comúnmente en los archivos fuente. No intentes utilizar citas tipográficas (curvadas, rizadas, etc.), utilizadas por los procesadores de
texto avanzados, ya que Python no las acepta.

![python_shell_ejecutando_programa](../img/python_shell_ejecutando_programa.jpg)

Guarda el archivo (*File -> Save*) y ejecuta el programa (*Run -> Run Module*).

Si todo sale bien y no hay errores en el código, la ventana de la consola mostrará los efectos causados por la ejecución del programa.

En este caso, el programa se ejecutará de manera correcta y mostrará **Hisssssss...** en la consola.

Intenta ejecutarlo una vez más. Y una vez más.

Ahora cierra ambas ventanas y vuelve al escritorio.

![python_shell_ejecutando_programa_salida_consola](../img/python_shell_ejecutando_programa_salida_consola.jpg)  

## **Cómo estropear y arreglar tu código**
Ahora ejecuta IDLE nuevamente.

- Haz clic en *File*, *Open*, señala el archivo que guardaste anteriormente y deja que IDLE lo lea de nuevo.
- Intenta ejecutarlo de nuevo presionando *F5* cuando la ventana del editor esté activa.  

Como puedes ver, IDLE puede guardar tu código y recuperarlo cuando lo necesites de nuevo.

IDLE contiene una característica adicional y muy útil.

- Primero, quita el paréntesis de cierre.
- Luego ingresa el paréntesis nuevamente.
Tu código debería parecerse al siguiente:
```
Hisssssss...
```

![python_shell_ejecutando_programa_print_sin_parentesis](../img/python_shell_ejecutando_programa_print_sin_parentesis.jpg)  

Cada vez que coloques el paréntesis de cierre en tu programa, IDLE mostrará la parte del texto limitada con un par de paréntesis
correspondientes. Esto te ayuda a recordar **colocarlos en pares**.

Retira nuevamente el paréntesis de cierre. El código se vuelve erróneo. Ahora contiene un error de sintaxis. IDLE no debería dejar que
lo ejecutes.

Intenta ejecutar el programa de nuevo. IDLE te recordará que guardes el archivo modificado. Sigue las instrucciones.

Observa todas las ventanas con cuidado.

Aparece una nueva ventana, dice que el intérprete ha encontrado un EOF (*fin-de-archivo*) aunque (en su opinión) el código debería
contener algo más de texto.

La ventana del editor muestra claramente donde ocurrió:

![python_shell_error_unexpected_eoe](../img/python_shell_error_unexpected_eoe.jpg)  

Ahora arregla el código. Debe verse así:
```
print("Hisssssss...")
```

Ejecútalo para ver si sigue funcionando.

Vamos a arruinar el código una vez más. Elimina una letra de la palabra *print*. Ejecuta el código presionando *F5*. Como puedes ver,
Python no puede reconocer la instrucción.

![python_shell_prin_sin_t](../img/python_shell_prin_sin_t.jpg)  

Es posible que hayas notado que el mensaje de error generado para el error anterior es bastante diferente del primero:

![python_shell_error_funcion_mal_escrita](../img/python_shell_error_funcion_mal_escrita.jpg)  

Esto se debe a que la naturaleza del error es **diferente** y el error se descubre en una **etapa diferente** de la interpretación.

La ventana del editor no proporcionará ninguna información útil sobre el error, pero es posible que las ventanas de la consola si.

El mensaje (*en rojo*) muestra (en las siguientes líneas):

- El **rastreo** (que es la ruta que el código atraviesa a través de diferentes partes del programa, puedes ignorarlo por ahora, ya que
está vacío en un código tan simple).

- La **ubicación del error** (el nombre del archivo que contiene el error, el número de línea y el nombre del módulo); nota: el número
puede ser engañoso, ya que Python generalmente muestra el lugar donde se percata por primera vez de los efectos del error, no
necesariamente del error en sí.

- El **contenido de la línea errónea**; nota: la ventana del editor de IDLE no muestra números de línea, pero muestra la ubicación
actual del cursor en la esquina inferior derecha; utilízalo para ubicar la línea errónea en un código fuente largo.

- El **nombre del error** y una breve explicación.

Experimenta creando nuevos archivos y ejecutando tu código. Intenta enviar un mensaje diferente a la pantalla, por ejemplo,
`¡rawr!`, `¡miau!`, o incluso tal vez un `¡oink!` Intenta estropear y arreglar tu código, observa que sucede.

## **Felicidades!**
## **Has completado el módulo 1.**

¡Bien hecho! Has llegado al final del Módulo 1 y has completado una meta importante en tu educación de programación en Python.
Aquí hay un breve resumen de los objetivos cubiertos y con los que te has familiarizado en el Módulo 1:

- Los fundamentos de la programación de computadoras, es decir, cómo funciona la computadora, cómo se ejecuta el programa,
cómo se define y construye el lenguaje de programación.

- La diferencia entre compilación e interpretación.

- La información básica sobre Python y cómo se posiciona entre otros lenguajes de programación, y qué distingue a sus diferentes
versiones.

- Los recursos de estudio y los diferentes tipos de interfaces que utilizarás en el curso.

Ahora estás listo para tomar el cuestionario del módulo, el cual te ayudará a evaluar lo que has aprendido hasta ahora.