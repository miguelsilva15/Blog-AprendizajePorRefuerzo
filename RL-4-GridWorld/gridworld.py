import numpy as np

def actualizar(funcion_de_valor, politica, longitud_del_mundo, recompensa,
               descuento=1):
    nueva_funcion_de_valor = np.zeros((longitud_del_mundo, longitud_del_mundo))
    #se genera una matriz con ceros, la cual remplazara a la funcion de valor
    # existente
    for posicion_en_el_mundo, valor in np.ndenumerate(funcion_de_valor):
        posicion_en_el_mundo = np.asarray(posicion_en_el_mundo)
        if not es_estado_terminal(posicion_en_el_mundo, longitud_del_mundo):
            #se confirma si el estado es terminal o no
            nuevo_valor = 0
            for _, accion_individual in politica.items():
                #se iterara por cada una de las acciones de nuestra politica
                nueva_posicion = (posicion_en_el_mundo +
                                  accion_individual['accion'])
                x, y = nueva_posicion.T
                if (x < 0 or x >= longitud_del_mundo or y < 0 or y >=
                    longitud_del_mundo):                  
                    #nos fijamos si esta dentro del mundo, si no se le devuelve
                    #a la misma posicion
                    nueva_posicion = posicion_en_el_mundo
                nuevo_valor += (accion_individual['probabilidad'] *
                                (recompensa + descuento *
                                 funcion_de_valor[tuple(nueva_posicion)]))
                    #se genera el nuevo valor que remplazara ese estado
            nueva_funcion_de_valor[tuple(posicion_en_el_mundo)] = nuevo_valor
    return nueva_funcion_de_valor

def es_estado_terminal(posicion_en_el_mundo, longitud_del_mundo):
    '''esta funcion hara que la funcion de valor no sufra ningun cambio cuando
    se encuentre en los estados terminales'''
    inicio = np.array([0,0])
    final = np.array([longitud_del_mundo-1, longitud_del_mundo-1])
    return (np.array_equal(posicion_en_el_mundo, inicio) or
            np.array_equal(posicion_en_el_mundo, final))

def mundo_cuadricula(longitud_del_mundo, politica, recompensa, k=1000):
    funcion_de_valor = np.zeros((longitud_del_mundo, longitud_del_mundo))
    #la funcion inicial arbitraria inicializa con una matriz de ceros
    for iteracion in range(k):
        #se va a actualizar la funcion de valor basado en el valor de k
        funcion_de_valor_nueva = actualizar(funcion_de_valor, politica,
                                            longitud_del_mundo, recompensa)
        if np.array_equal(funcion_de_valor_nueva, funcion_de_valor):
            #si la politica deja de cambiar significa que se habra
            #encontrado una solucion
            print("convergio! a la iteracion:", iteracion)
            break
        else:
            funcion_de_valor = funcion_de_valor_nueva
        print(funcion_de_valor)

if __name__ == '__main__':
    recompensa = -1
    longitud_del_mundo = 4 #el tamaño del mundo sera una cuadricula 4 x 4
    politica = {           #la politica es la misma que se explico en el post
        'derecha' : {
            'probabilidad': 0.25,
            'accion': np.array([0, 1])
        },
        'izquierda' : {
            'probabilidad': 0.25,
            'accion': np.array([0, -1])
        },
        'arriba' : {
            'probabilidad': 0.25,
            'accion': np.array([1, 0])
        },
        'abajo' : {
            'probabilidad': 0.25,
            'accion': np.array([-1, 0])
        }
    }
    mundo_cuadricula(longitud_del_mundo, politica, recompensa)
