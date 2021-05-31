#!/usr/bin/python3

import argparse
from sympy import Symbol, sympify
from sympy import *


class Adelante():

    def __init__(self):
        self.funcion = sympify(self.parse().funcion)
        self.x = self.parse().x_zero
        self.h = self.parse().distance
    
    def __str__(self):
        return '\nResultado de la derivada de {} en {}: {}'.format(self.funcion, self.x ,self.derivada())

    def parse(self):
        parser = argparse.ArgumentParser(description='===== DIFERENCIAS HACIA ADELANTE =====')
        parser.add_argument('-f', '--funcion', action='store', metavar='FUNCION',
                            type=str, required=True, help='Ingrese la Funcion')
        parser.add_argument('-x', '--x_zero', action='store', metavar='X_ZERO',
                            type=float, required=True, help='Ingrese X cero')
        parser.add_argument('-d', '--distance', action='store', metavar='DISTANCE',
                            type=float, required=True, help='Ingrese la distancia entre puntos')

        args = parser.parse_args()
        return args

    # retorna los valores de la funcion en los x indicados
    def value(self):
        f = self.funcion
        a = self.x
        h = self.h

        x = Symbol('x')
        values = list()
        for i in range(6):
            values.append(round(f.subs(x, a), 6))
            a += h
        print(values)
        return values

    # calcula delta f
    def delta(self, value):
        df = list()

        for i in range(len(value)-1):
            df.append(value[i+1]-value[i])
        return df

    #calcula delta n de f
    def dif(self):
        deltas_definitivos = list()
        deltas = self.delta(self.value())
        deltas_definitivos.append(round(deltas[0], 6))

        while len(deltas) > 1:
            deltas = self.delta(deltas)
            deltas_definitivos.append(round(deltas[0], 6))
        print(deltas_definitivos)
        return deltas_definitivos
    
    def derivada(self):
        d = self.dif()
        f = ((1/self.h)*(d[0]-(1/2)*d[1]+(1/3)*d[2]+(1/4)*d[3]+(1/5)*d[4]))
        return round(f, 6)
    
    def error(self):
        e = ((-1)**5)*(self.h**5)*(()/())
        return 

if __name__ == '__main__':
    print('\n====== METODO DE DIFERENCIAS HACIA ADELANTE =======')
    print('\nPrograma realizado por Agustin Prieto\n')
    print(Adelante())