from ClassPCB import PCB
import time
import matplotlib.pyplot as plt
import numpy as np


def calcularTiempo(funcion):
    def funcionM(pcb,n):
        start= time.time()
        funcion(pcb,n)
        end = time.time()
        return(end-start)
    return funcionM

@calcularTiempo
def calcularCamino(pcb,n):
    pcb.routesToB_S(n)

def funcionGrafico(N,method):
    times = []
    x = []
    for n in range(2,N+1):
        pcb = PCB(n,n)
        t=calcularCamino(pcb,method)
        times.append(t)
        x.append(n)
    
    z1=np.polyfit(x,times,3)
    p1=np.poly1d(z1)

    plt.scatter(x,times,alpha=0.5,c='orange',label='Valor de la funcion')
    plt.plot(x,p1(x),c='red',label='Linea de tendencia')
    plt.title(f'Tiempo v/s Dimension de la matriz con el metodo {method}')
    plt.legend()
    plt.ylabel('Tiempo[S]')
    plt.xlabel('Dimesion de la matriz cuadrada')
    plt.grid()
    plt.savefig(fname=f'Grafico_metodo_{method}',format='svg')
    plt.show()

funcionGrafico(300,1)
funcionGrafico(300,2)