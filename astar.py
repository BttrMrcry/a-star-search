import heapq
from os import system, name
from colorama import Fore, Back, Style

# A* Python Traversal
#https://medium.com/nerd-for-tech/graph-traversal-in-python-a-algorithm-27c30d67e0d0
mapa = {
    # now we need a list as the value to store g-score and h-score
    # list first value is the g-score, second value is the h-score,i.e., heuristic
    "Arad": {
        "Sibiu": [140, 253],
        "Timisoara": [118, 329],
        "Zerind": [75, 374]
    },
    "Bucharest": {
        "Fagaras": [211, 178],
        "Giurgiu": [90, 77],
        "Pitesti": [101, 98],
        "Urziceni": [85, 80]
    },
    "Craiova": {
        "Dobreta": [120, 242],
        "Pitesti": [138, 98],
        "Rimnicu": [146, 193]
    },
    "Dobreta": {
        "Craiova": [120, 160],
        "Mehadia": [75, 241]
    },
    "Efoire": {
        "Hirsova": [86, 151]
    },
    "Fagaras": {
        "Bucharest": [211, 0],
        "Sibiu": [99, 253]
    },
    "Giurgiu": {
        "Bucharest": [90, 0]
    },
    "Hirsova": {
        "Efoire": [86, 161],
        "Urziceni": [98, 80]
    },
    "Iasi": {
        "Neamt": [87, 234],
        "Vaslui": [92, 199]
    },
    "Lugoj": {
        "Mehadia": [70, 241],
        "Timisoara": [111, 329]
    },
    "Mehadia": {
        "Dobreta": [75, 242],
        "Lugoj": [70, 244]
    },
    "Neamt": {
        "Iasi": [87, 226]
    },
    "Oradea": {
        "Sibiu": [151, 253],
        "Zerind": [71, 374]
    },
    "Pitesti": {
        "Bucharest": [101, 0],
        "Craiova": [138, 160],
        "Rimnicu": [97, 193]
    },
    "Rimnicu": {
        "Craiova": [146, 160],
        "Pitesti": [97, 98],
        "Sibiu": [80, 253]
    },
    "Sibiu": {
        "Arad": [140, 366],
        "Fagaras": [99, 178],
        "Oradea": [151, 380],
        "Rimnicu": [80, 193]
    },
    "Timisoara": {
        "Arad": [118, 366],
        "Lugoj": [111, 244]
    },
    "Urziceni": {
        "Bucharest": [85, 0],
        "Hirsova": [98, 151],
        "Vaslui": [142,199]
    },
    "Vaslui": {
        "Iasi": [92, 226],
        "Urziceni": [142, 80]
    },
    "Zerind": {
        "Arad": [75, 366],
        "Oradea": [71, 380]
    }
}
"""

El algoritmo regresa el grafo de la siguiente manera.

graph["Arad"] # this return {'B':[2,2],'C':[3,2]}.
graph["Arad"]["Sibiu"][0]  # regresa el tamaño de la arista.
graph["Arad"]["Sibiu"][1]  # regresa la distancia del nodo inicial al nodo destino.
graph["Arad"]["Sibiu"] # esto regresa la tupla [<distancia_entre_nodos>, <distancia_heuristica>].

"""



def astar(mapa, ciudad_inicio, ciudad_fin):
    # A*: F=G+H, llamamos F como f_distance, G como g_distance, H como heurística
    distancia_f = {ciudad: float('inf') for ciudad in mapa}  # f_distance = {"Arad": ∞, "Bucharest": ...}
    distancia_f[ciudad_inicio] = 0

    # Distancia hasta el momento.
    distancia_g = {ciudad: float('inf') for ciudad in mapa}  # g_distance = {"Arad": ∞, "Bucharest": ...}
    distancia_g[ciudad_inicio] = 0

    ciudad_anterior = {ciudad: None for ciudad in mapa}  # came_from = {"Arad":None,"Bucharest":...} 
    ciudad_anterior[ciudad_inicio] = ciudad_inicio

    cola_prioridad = [(0, ciudad_inicio)]  # El primer elemento es la distancia F y el segundo es el nodo n actual

    paso = 0
    while cola_prioridad:
        _, ciudad_actual = heapq.heappop(cola_prioridad)
        print(f'Paso {paso}: La ciudad a expandir es {Back.BLUE}{ciudad_actual}{Style.RESET_ALL}')

        if ciudad_actual == ciudad_fin:
            print('La ciudad a expandir es la final, se llegó al destino!')
            print("\n")
            print('Termina')
            print("\n")
            return distancia_g, ciudad_anterior

        for siguiente_ciudad, pesos in mapa[ciudad_actual].items():  # Para cada nodo adyacente al nodo actual:
            distancia_g_temporal = distancia_g[ciudad_actual] + pesos[0]  # A la distancia hasta el nodo actual, se le suma la distancia hasta el nodo siguiente
            if distancia_g_temporal < distancia_g[siguiente_ciudad]:
                distancia_g[siguiente_ciudad] = distancia_g_temporal
                distancia_h = pesos[1]
                distancia_f[siguiente_ciudad] = distancia_g_temporal + distancia_h
                ciudad_anterior[siguiente_ciudad] = ciudad_actual
                heapq.heappush(cola_prioridad, (distancia_f[siguiente_ciudad], siguiente_ciudad))
                print(f'La función f(n) de {Back.YELLOW}{siguiente_ciudad}{Style.RESET_ALL} es f(n) = {distancia_g_temporal} + {distancia_h} = {distancia_f[siguiente_ciudad]}. Se agrega a la cola de prioridad.')
            else:
                print(f'La distancia a {Back.GREEN}{siguiente_ciudad}{Style.RESET_ALL}  pasando por {Back.BLUE}{ciudad_actual}{Style.RESET_ALL}: ({distancia_g_temporal}) es mayor\na la distancia mínima actual para llegar a {siguiente_ciudad} :({distancia_g[siguiente_ciudad]})')
        print("\n")
        paso += 1
    return distancia_g, ciudad_anterior


# define una función clear
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def menu():
    print('*--------------------------------------------*')
    print('| METODO A-Estrella, INTELIGENCIA ARTIFICIAL |')
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


if __name__ == "__main__":
    while True:
        clear()
        menu()
        ciudad_inicio = input('Ingresa el nombre de la ciudad de inicio: ') 
        if ciudad_inicio in mapa:
            break
        else:
            clear()
            print('Nombre de ciudad no válido\n\n')

    ciudad_fin = "Bucharest"
    distancia_g, ciudad_anterior = astar(mapa, ciudad_inicio, ciudad_fin)
    # Recuperar camino
    ciuidad_actual = ciudad_fin
    trayectoria_reversa = []
  # actual: Craiova , inicio: Arad
    while ciuidad_actual != ciudad_inicio:
        trayectoria_reversa.append(ciuidad_actual)
        ciuidad_actual = ciudad_anterior[ciuidad_actual]

    print(f'Costo: {distancia_g[ciudad_fin]}')
    print('Trayectoria:', end=' ')
    while len(trayectoria_reversa) > 1:
        ciudad = trayectoria_reversa.pop() 
        print(f"{ciudad}({distancia_g[ciudad]}) -> ", end = '')
    ultima_ciuidad = trayectoria_reversa.pop()
    print(f"{ultima_ciuidad}({distancia_g[ultima_ciuidad]})")
