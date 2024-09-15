# Tarea 1 - Javiera Pacheco
## Preguntas Teóricas 

**Paradigma de programación:** Se les llama así a las “formas” en que se programa, es decir, a los patrones, características, métodos, etc., con ello se puede clasificar entonces las diversas formas de programar. Por ejemplo 2 paradigmas muy comunes son el imperativo donde se va diciendo a la maquina como cambiar para lograr cierta operación y el declarativo donde simplemente se dice el resultado deseado.

**Programación Orientada a Objetos:** La POO es un método para organizar de forma modular los procesos y se basa en las clases, las clases son como los modelos para sus instancias, las cuales son las funciones o atributos comunes que comparten las clases, con ello los objetos se pueden trabajar ya que se define con las instancias que se asocia a ese objeto concreto y se guarda como único, pero si se debe hacer más objetos se puede seguir con la clase que es la “plantilla, por ello se basa en las clases y es “orientado” al objeto.

**Recursividad e Iteración:** Cuando se deben realizar operaciones o instrucciones de forma reiterada hay dos enfoques principales, iterativa donde simplemente se ejecutan las instrucciones reiteradas hasta llegar a lo buscado y forma recursiva, donde una función se llama a si misma reiteradamente, es decir ahora está definido en términos de la función en sí y puede actualizarse. Son enfoques de hacerlo, por lo tanto en realidad son equivalentes y puede hacerse una transformación de una a otra, el tema es el tiempo que demorara cierta operación en ser realizada aunque se pueda hacer de ambas formas, esto extendido se relaciona con la notación Big-O ya que esta ultima es la forma en que se establece cuanto demora un algoritmo en ejecutarse, es una forma de medir la eficiencia de los algoritmos, con ello la recursión y la iteración pueden ser mas o menos eficientes para un problema dado ya que son algoritmos diferentes aunque solucionen el mismo problema.

**Rendimientos de Big-O:** Para ver el rendimiento general de un algoritmo se establece una relación entre el tiempo que demora el algoritmo en resolverse según que tan grande sean los datos de entrada. O(1) por ejemplo refiere a tiempo constante, esto porque se dice que no importa que tan grande sea la entrada, esta no tiene relación con el algoritmo y no cambia cuanto se demora, O(n) por otro lado es cuando el tiempo crece linealmente con la cantidad de datos de entrada, por ejemplo cuando se debe operar con cada elemento de entrada, en ese caso se debe operar para cada dato y por ello el tiempo crece linealmente a más datos de entrada.

**Caso Big-O para programas en etapas:** La eficiencia estará dominada por la menos eficiente de las etapas, ya que a priori sumariamos la notación big-O de cada etapa, pero el termino dominante de la menos eficiente haría casi imperceptible a las más eficientes, quedándonos así solo con esta para definir al programa en etapas. 

**Complejidad temporal de un algoritmo recursivo:** Para poder saber la complejidad de estos, se puede estimar primero por ejemplo si podemos saber cuantas veces se recorren los datos de entrada en casos de que se recorran todos en la recursión, dándonos los tiempos polinómicos según cuantas veces se recorren, en casos de otros algoritmos se puede hacer la prueba de aumentar la entrada y ver cuanto demora el tiempo de ejecución y así estimar su complejidad.

## Programación Clase que calcule el número de caminos posibles

El primer algoritmo en implementarse consiste en recorrer la grilla desde abajo para el cálculo de caminos posibles desde las casillas adyacentes a B, con esto se acumulan hacia atrás de forma que se sabe la cantidad de caminos que se genera desde un nodo (casilla), esto se va a agregando al contador de forma que se conocen los caminos totales.

Luego de implementar esta forma, se notó que se generaban sucesiones conocidas en los nodos, principalmente, los naturales, la sucesión triangular y la sucesión cuadrática, esto llevo a notar que la forma de calcularse los caminos tenía mucha relación con el triangulo de pascal, con ello usando propiedades matemáticas derivadas del mismo, se encontró una expresión matemática para el cálculo de los caminos que consiste en la doble sumatoria (ya que la dimensión de la matriz es 2) de la combinatoria que genera las sucesiones. Siendo este el segundo algoritmo implementado.

## Estudio de Complejidad Temporal

Para comparar los algoritmos y ver cuál es mejor en términos de tiempo en ejecución según el tamaño de la grilla, se decoró los métodos de la clase con la funcionalidad que calcula el tiempo que demora la ejecución, además se agregó un nuevo método que nos permite seleccionar directamente que algoritmo usar. 

Con ello se realizo un programa que muestra el tiempo de ejecución versus el tamaño de la matriz/grilla de entrada, para los casos de grillas cuadradas y ver como se comporta este tiempo de ejecución para los dos algoritmos, con ello también se grafica la línea de tendencia para visualizar de mejor forma los datos. 

Se obtuvo el siguiente gráfico:

Notamos que el algoritmo de la “función matemática” es mucho peor que el algoritmo de recorrer los nodos, aunque al inicio se creyó que la función matemática sería mejor, pero analizando vemos que hay un anidado de dos for para su formulación, dando con ello una notación big-O de O(n^2) la cual empeora el tiempo de ejecución muy rápido a medida que crece la dimensión de la grilla, en cambio el recorrer e ir sumando los caminos de la grilla logra el resultado con tan solo recorrer toda la grilla una vez (es más, no se recorre toda la grilla, las orillas no son recorridas) siendo así mucho más eficiente ya que seria aproximadamente O(n), siendo solo lineal a la dimensión de la grilla. 


