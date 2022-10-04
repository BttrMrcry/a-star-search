"""
INTELIGENCIA ARTIFICIAL
METODO DE BUSQUEDA UNIFORME
"""
# Importando bibliotecas
import pandas as pd
 # VARIABLES GLOBALES (Accesibles para cualquier funcion)
info_ciudades = None          # Utilizado en DataFrame para vertices entre ciudades: ciudad1 - ciudad2 - costo
lista_prioridad_frontera = [] # Lista FIFO cuyo costo de ruta más bajo sera el Head
  
# AGREGANDO LAS CIUDADES DE ROMANIA
def agregar_ciudades():
    global info_ciudades
    data = [{'ciudad1': 'Timisoara',      'ciudad2': 'Lugoj',          'costo_ruta': 111},
            {'ciudad1': 'Lugoj',          'ciudad2': 'Mehadia',        'costo_ruta': 70},
            {'ciudad1': 'Mehadia',        'ciudad2': 'Dobreta',        'costo_ruta': 75},
            {'ciudad1': 'Dobreta',        'ciudad2': 'Craiova',        'costo_ruta': 120},
            {'ciudad1': 'Oradea',         'ciudad2': 'Zerind',         'costo_ruta': 71},
            {'ciudad1': 'Oradea',         'ciudad2': 'Sibiu',          'costo_ruta': 151},
            {'ciudad1': 'Zerind',         'ciudad2': 'Arad',           'costo_ruta': 75},
            {'ciudad1': 'Arad',           'ciudad2': 'Sibiu',          'costo_ruta': 140},
            {'ciudad1': 'Arad',           'ciudad2': 'Timisoara',      'costo_ruta': 118},   
            {'ciudad1': 'Sibiu',          'ciudad2': 'Fagaras',        'costo_ruta': 99},
            {'ciudad1': 'Sibiu',          'ciudad2': 'Rimnicu Vilcea', 'costo_ruta': 80},
            {'ciudad1': 'Rimnicu Vilcea', 'ciudad2': 'Craiova',        'costo_ruta': 146},
            {'ciudad1': 'Rimnicu Vilcea', 'ciudad2': 'Pitesti',        'costo_ruta': 97},
            {'ciudad1': 'Craiova',        'ciudad2': 'Pitesti',        'costo_ruta': 138},
            {'ciudad1': 'Fagaras',        'ciudad2': 'Bucharest',      'costo_ruta': 211},
            {'ciudad1': 'Pitesti',        'ciudad2': 'Bucharest',      'costo_ruta': 101},
            {'ciudad1': 'Neamt',          'ciudad2': 'Iasi',           'costo_ruta': 87},
            {'ciudad1': 'Iasi',           'ciudad2': 'Vaslui',         'costo_ruta': 92},
            {'ciudad1': 'Bucharest',      'ciudad2': 'Giurgiu',        'costo_ruta': 90},
            {'ciudad1': 'Bucharest',      'ciudad2': 'Urziceni',       'costo_ruta': 85},
            {'ciudad1': 'Urziceni',       'ciudad2': 'Vaslui',         'costo_ruta': 142},
            {'ciudad1': 'Urziceni',       'ciudad2': 'Hirsova',        'costo_ruta': 98},
            {'ciudad1': 'Hirsova',        'ciudad2': 'Eforie',         'costo_ruta': 86}]
    info_ciudades = pd.DataFrame(data, columns=['ciudad1', 'ciudad2', 'costo_ruta'])
# print(info_ciudades)      # despliega el dataFrame info_ciudades

# CLASE NODO Y SUS ATRIBUTOS
class Nodo:
    def __init__(self,ciudad,vecino,costo_ruta):
        self.ciudad = ciudad
        self.vecino = vecino
        self.costo_ruta = costo_ruta

# FUNCION MAIN, EJECUTA EL PROGRAMA
def main():
    global info_ciudades # Variable global a modificar
    agregar_ciudades()   # Agregamos los caminos de las ciudades
    menu()               # Desplegamos el menu()
    ciudad_origen = input('Ingrese Ciudad de Inicio: \n')
    ciudad_destino = input('Ingrese Ciudad Destino:\n')
    hacer_recorrido(ciudad_origen,ciudad_destino)

def menu():
    print('*--------------------------------------------*')
    print('|  METODO UNIFORME, INTELIGENCIA ARTIFICIAL  |')
    print('*--------------------------------------------*')
    print('|  MAPA DE CIUDADES DISPONIBLES PARA VIAJE   |')
    print('|                                            |')
    print('| -Arad            -Bucharest     -Craiova   |')
    print('| -Dobreta         -Eforie        -Fagaras   |')
    print('| -Giurgiu         -Hirsova       -Iasi      |')
    print('| -Lugoj           -Mehadia       -Neamt     |')
    print('| -Oradea          -Pitesti       -Sibiu     |')
    print('| -Rimnicu Vilcea  -Timisoara     -Urziceni  |')
    print('| -Vaslui          -Zerind                   |')
    print('*--------------------------------------------*')


def hacer_recorrido(ciudad_origen, ciudad_destino):
    camino, costo_total = busqueda_uniforme(ciudad_origen, ciudad_destino)
    if not camino:  # Si no se pudo llegar al destino
        print('ERROR: No se pudo recorrer de ciudad {} a la ciudad {}.\nVerifique sus entradas o las ciudades incluidas en el mapa\n' +
        ' y vuelva a ejecutar el programa.'.format(ciudad_origen, ciudad_destino))     
    else:
        print('RECORRIDO DE {} A {} COMPLETADO, RUTA:'.format(ciudad_origen,ciudad_destino).upper())
        ciudades_visitadas = []
        while True:
            ciudades_visitadas.append(camino.ciudad) # Agregando a la lista las ciudades visitadas
            if camino.vecino is None: # Cuando camino.vecino no tenga mas valores
                break
            camino = camino.vecino
        size = len(ciudades_visitadas)  # Obtenemos la longitud antes de iterar
        for i in range(size):  # IMPRIMIENDO LA TRAYECTORIA DE CIUDADES
            if i < size - 1:
                print(ciudades_visitadas.pop(), end='' + ", ")
            else:
                print(ciudades_visitadas.pop()) 
        print('COSTO DE RUTA: {} [KM]'.format(costo_total))   

 # Funcion que comprueba si la ciudad del nodo esta en la lista de prioridad_frontera
def nodo_en_frontera(frontera, nodo): 
    for i in frontera:
        if nodo.ciudad == i.ciudad:
            return True
    return False    # Si no lo encuentra, retorna falso
 
# Funcion para la busqueda uniforme
def busqueda_uniforme(c_origen, c_destino):
    #print(type(c_origen))
    global info_ciudades, lista_prioridad_frontera   # Variables que afectan a las globales
    nodo = Nodo(c_origen, None,0)                    # Creamos un nodo con la ciudad de origen
    agregar_frontera(nodo)                           # Lo agregamos a la frontera
    explorado = []                                   # Para guardar las ciudades ya exploradas
    
    while True:
        if len(lista_prioridad_frontera) == 0:  # Si ya no quedan elementos en la lista de prioridades
            return False                        # Cortamos el flujo del programa
        nodo = lista_prioridad_frontera.pop(0)  # Quitamos el primer elemento
        explorado.append(nodo.ciudad)
                 # Prueba de objetivo
        if nodo.ciudad == c_destino:            # Si ya completamos el recorrido
            return nodo, nodo.costo_ruta        # Terminamos, recojan sus cosas chicos
                                                # Sino, recorremos los nodos secundarios
        for i in range(len(info_ciudades)):     # Total de Ciudades
            ciudad_destino = ''                 #Inicializamos variable ciudad_destino
            if info_ciudades['ciudad1'][i] == nodo.ciudad:    # Si la ciudad de mapa corresponde a la de nodo
                ciudad_destino = info_ciudades['ciudad2'][i]  # Actualizamos ciudad_destino con el nuevo recorrido
            elif info_ciudades['ciudad2'][i] == nodo.ciudad:  # Comparando el nodo de la ciudad con el valor ciudad2 del DaFr
                ciudad_destino = info_ciudades['ciudad1'][i]  # Actualizamos ciudad_destino con el valor anterior
            if ciudad_destino == '':                          # Si no hubo un match en el DaFr, continuamos
                continue
            nodo_hijo = Nodo(ciudad_destino, nodo, nodo.costo_ruta + info_ciudades['costo_ruta'][i])
            
            # El siguiente conjunto de lineas nos ayuda a definir los nodos frontera del nodo actual
            # Si el nodo no ha sido explorado y no esta mapeado en frontera, se mapea
            # Si esta en la frontera, se actualiza con el nodo de menor consumo de ruta
            if nodo_hijo.ciudad not in explorado and not nodo_en_frontera(lista_prioridad_frontera, nodo_hijo):
                agregar_frontera(nodo_hijo)         # Agregamos al nodo frontera 
            elif nodo_en_frontera(lista_prioridad_frontera, nodo_hijo):
                reemplaza_frontera(nodo_hijo)        # Corrige para una frontera con menor costo
 
# Funcion que expande y actualiza las fronteras en base al costo de ruta
def agregar_frontera(nodo):
    global lista_prioridad_frontera
    size = len(lista_prioridad_frontera)
    for i in range(size):
        if nodo.costo_ruta < lista_prioridad_frontera[i].costo_ruta: # Si el costo del nodo nuevo es menor al de lista de priodad, se inserta
            lista_prioridad_frontera.insert(i, nodo)
            return
    lista_prioridad_frontera.append(nodo) # Caso contrario, el costo es mayor y lo agregamos al FINAL de la cola
 
# Funcion que reemplaza las fronteras en base al costo de ruta
def reemplaza_frontera(nodo):
    global lista_prioridad_frontera
    size = len(lista_prioridad_frontera)
    for i in range(size): # Por cada elemento de la lista_prioridad_frontera
        # Si la ciudad de frontera es la misma que el nodo y el costo de frontera es mayor al del nodo
        if lista_prioridad_frontera[i].ciudad == nodo.ciudad and lista_prioridad_frontera[i].costo_ruta > nodo.costo_ruta:
            lista_prioridad_frontera[i] = nodo # Se actualiza la frontera con el nodo para tener el costo mas bajo
            return
 
#Inicia el programa
main()

