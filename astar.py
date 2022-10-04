import heapq

# A* Python Traversal
#https://medium.com/nerd-for-tech/graph-traversal-in-python-a-algorithm-27c30d67e0d0
graph = {
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



def astar(graph, start_node, end_node):
  # A*: F=G+H, llamamos F como f_distance, G como g_distance, H como heurística
  f_distance = {node: float('inf') for node in graph}  # f_distance = {"Arad": ∞, "Bucharest": ...}
  f_distance[start_node] = 0

  # Distancia hasta el momento.
  g_distance = {node: float('inf') for node in graph}  # g_distance = {"Arad": ∞, "Bucharest": ...}
  g_distance[start_node] = 0

  came_from = {node: None for node in graph}  # came_from = {"Arad":None,"Bucharest":...} 
  came_from[start_node] = start_node

  queue = [(0, start_node)]  # El primer elemento es la distancia F y el segundo es el nodo n actual

  while queue:
    current_f_distance, current_node = heapq.heappop(queue)
    if current_node == end_node:
      print('found the end_node')
      return g_distance, came_from

    for next_node, weights in graph[current_node].items():  # Para cada nodo adyacente al nodo actual:
      temp_g_distance = g_distance[current_node] + weights[0]  # A la distancia hasta el nodo actual, se le suma la distancia hasta el nodo siguiente
      if temp_g_distance < g_distance[next_node]:
        g_distance[next_node] = temp_g_distance
        heuristic = weights[1]
        f_distance[next_node] = temp_g_distance + heuristic
        came_from[next_node] = current_node
        heapq.heappush(queue, (f_distance[next_node], next_node))
  return g_distance, came_from


if __name__ == "__main__":
  inicio = "Arad" 
  fin = "Bucharest"
  g_distance, came_from = astar(graph, inicio, fin)
  # Recuperar camino
  actual = fin
  trayectoria_reversa = []
  # actual: Craiova , inicio: Arad
  while actual != inicio:
    trayectoria_reversa.append(actual)
    actual = came_from[actual]

  copia_trayectoria_reversa = trayectoria_reversa.copy()
  
  while len(trayectoria_reversa) > 1:
    ciudad = trayectoria_reversa.pop() 
    print(f"{ciudad}({g_distance[ciudad]})->", end = '')
  ultima_ciuidad = trayectoria_reversa.pop()
  print(f"{ultima_ciuidad}({g_distance[ultima_ciuidad]})")

    

  # trayectoria_reversa = [Bucharest, Pitesti, ]
  
  #print(g_distance)
  #print(came_from)]
  
  
# return {'A': 0, 'B': 4, 'C': 5, 'D': 10, 'E': 4, 'F': 4} and {'A': 'A', 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'E'}
"""
found the end_node
{'Arad': 0, 'Bucharest': 418, 'Craiova': 526, 'Dobreta': inf, 'Efoire': inf, 'Fagaras': 417, 'Giurgiu': inf, 'Hirsova': inf, 'Iasi': inf, 'Lugoj': inf, 'Mehadia': inf, 'Neamt': inf, 'Oradea': 671, 'Pitesti': 415, 'Rimnicu': 413, 'Sibiu': 393, 'Timisoara': 447, 'Urziceni': inf, 'Vaslui': inf, 'Zerind': 449}
{'Arad': 'Arad', 'Bucharest': 'Pitesti', 'Craiova': 'Rimnicu', 'Dobreta': None, 'Efoire': None, 'Fagaras': 'Sibiu', 'Giurgiu': None, 'Hirsova': None, 'Iasi': None, 'Lugoj': None, 'Mehadia': None, 'Neamt': None, 'Oradea': 'Sibiu', 'Pitesti': 'Rimnicu', 'Rimnicu': 'Sibiu', 'Sibiu': 'Arad', 'Timisoara': 'Arad', 'Urziceni': None, 'Vaslui': None, 'Zerind': 'Arad'}

"""