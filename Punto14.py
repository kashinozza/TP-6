from graph import Graph

# Crear un grafo no dirigido
casa = Graph(is_directed=False)

# A
ambientes = [
    'cocina',
    'comedor',
    'cochera',
    'quincho',
    'baño 1',
    'baño 2',
    'habitacion 1',
    'habitacion 2',
    'sala de estar',
    'terraza',
    'patio'
]

for ambiente in ambientes:
    casa.insert_vertex(ambiente)

# B
conexiones = [
    ('cocina', 'comedor', 4),
    ('comedor', 'cochera', 6),
    ('cochera', 'quincho', 8),
    ('quincho', 'baño 1', 5),
    ('baño 1', 'baño 2', 3),
    ('baño 2', 'habitacion 1', 7),
    ('habitacion 1', 'habitacion 2', 4),
    ('habitacion 2', 'sala de estar', 6),
    ('sala de estar', 'terraza', 5),
    ('terraza', 'patio', 3),
    ('patio', 'cocina', 7),
    ('cocina', 'cochera', 2),
    ('cocina', 'baño 1', 9),
    ('cocina', 'sala de estar', 10),
    ('comedor', 'quincho', 3),
    ('comedor', 'baño 2', 8),
    ('comedor', 'terraza', 11),
    ('cochera', 'habitacion 2', 5),
    ('quincho', 'sala de estar', 4),
    ('habitacion 1', 'patio', 6)
]

for origen, destino, distancia in conexiones:
    casa.insert_edge(origen, destino, distancia)

#Mostrar
casa.show()

#C
aem = casa.kruskal('cocina')
print('\nÁrbol de expansión mínima:')
peso_total = casa.print_kruskal(aem)
print('Metros de cable necesarios:', peso_total)

#D
camino, distancia = casa.shortest_path(
    'habitacion 1',
    'sala de estar'
)

print('\nCamino más corto:')
print(' -> '.join(camino))
print('Metros de cable de red necesarios:', distancia)