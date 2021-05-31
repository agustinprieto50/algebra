# TRABAJO FINAL - DIFERENCIAS HACIA DELANTE

Alumno: Prieto, Agustin. Ingeniería Informática.

Ejemplo de uso:


python3 dif_adelante.py -f "(x**2)*cos(x)" -x 1 -d 0.2 -n 5


====== METODO DE DIFERENCIAS HACIA ADELANTE =======

Programa realizado por Agustin Prieto

Deltas:  [-0.018507, -0.170152, -0.049076, 0.014807, 0.005891]

Valores para Xn: [0.540302, 0.521795, 0.333136, -0.074751, -0.736135, -1.664587] 
Resultado de la derivada de x**2*cos(x) en 1.0: 0.238434. Con un error de: 0.00159166259765625




Explicacion:
    En -f debemos indicar la funcion a utilizar. Euler se utiliza con la letra "E". Las ecuaciones deben ir siempre entre parentesis.
    En -x indicamos el x0
    En -d indicamos la distancia h
    Y en -n indicamos justamente n.

Antes de correr el programa es necesario instalar el modulo sympy con el siguiente comando:
    pip3 install sympy

