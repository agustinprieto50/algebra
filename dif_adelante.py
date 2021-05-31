#!/usr/bin/python3

import argparse
from sympy import Symbol, sympify, diff


class Adelante():

    def __init__(self):
        self.funcion = sympify(self.parse().funcion)
        self.x = self.parse().x_zero
        self.h = self.parse().distance
        self.n = self.parse().numero

    def __str__(self):
        return '\nValores para Xn: {} \nResultado de la derivada de {} en {}: {}. Con un error de: \
{}'.format(self.value(), self.funcion, self.x, self.derivada(), self.error())

    def parse(self):
        parser = argparse.ArgumentParser(description='===== DIFERENCIAS HACIA \
            ADELANTE =====')
        parser.add_argument('-f', '--funcion', action='store',
                            metavar='FUNCION',
                            type=str, required=True, help='Ingrese la Funcion')
        parser.add_argument('-x', '--x_zero', action='store', metavar='X_ZERO',
                            type=float, required=True, help='Ingrese X cero')
        parser.add_argument('-d', '--distance', action='store',
                            metavar='DISTANCE',
                            type=float, required=True,
                            help='Ingrese la distancia entre puntos')
        parser.add_argument('-n', '--numero', action='store', metavar='NUMERO',
                            type=int,
                            required=True, help='Ingrese el valor de n')

        args = parser.parse_args()
        return args

    # retorna los valores de la funcion en los x indicados
    def value(self):
        f = self.funcion
        a = self.x
        h = self.h

        x = Symbol('x')
        values = list()
        for i in range(self.n+1):
            values.append(round(f.subs(x, a), 6))
            a += h
        return values

    # calcula delta f
    def delta(self, value):
        df = list()

        for i in range(len(value)-1):
            df.append(value[i+1]-value[i])
        return df

    # calcula delta n de f
    def dif(self):
        deltas_definitivos = list()
        deltas = self.delta(self.value())
        deltas_definitivos.append(round(deltas[0], 6))

        while len(deltas) > 1:
            deltas = self.delta(deltas)
            deltas_definitivos.append(round(deltas[0], 6))
        print('Deltas: ', deltas_definitivos)
        return deltas_definitivos

    def derivada(self):
        f = ((1/self.h)*(self.termino()))
        return round(f, 6)

    def termino(self):
        t = (self.n)
        signo = -1
        result = 0
        d = self.dif()

        for i in range(t):
            n = d[i] * (1/(i+1))*(signo**i)
            result += n
        return result

    def error(self):
        x = Symbol('x')
        max_deriv = list()
        derivada = diff(self.funcion, x, self.n + 1)
        for i in self.value():
            max_deriv.append(derivada.subs(x, i))
        e = (((-1)**self.n)*(self.h**self.n)*((max(max_deriv))/(self.n + 1)))
        return (abs(e))


if __name__ == '__main__':
    print('\n====== METODO DE DIFERENCIAS HACIA ADELANTE =======')
    print('\nPrograma realizado por Agustin Prieto\n')
    print(Adelante())
