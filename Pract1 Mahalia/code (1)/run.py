# Search methods

import search

print("Prueba 1 de A a B")
ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Breadth_First", search.breadth_first_graph_search(ab).path())
print("Depth_First", search.depth_first_graph_search(ab).path())
print("Recorrido y profundidad: ", search.busqueda_en_grafo_Ramif_y_Acota(ab).path())
print("Recorrido y profundidad con Subestimación:", search.busqueda_Ramif_y_Acota_Subest(ab).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

print("\nPrueba 2 de Z a G")
zg = search.GPSProblem('Z', 'G'
                       , search.romania)

print("Breadth_First", search.breadth_first_graph_search(zg).path())
print("Depth_First", search.depth_first_graph_search(zg).path())
print("Recorrido y profundidad: ", search.busqueda_en_grafo_Ramif_y_Acota(zg).path())
print("Recorrido y profundidad con Subestimación:", search.busqueda_Ramif_y_Acota_Subest(zg).path())


print("\nPrueba 3 de T a U")
tu = search.GPSProblem('T', 'U'
                       , search.romania)

print("Breadth_First", search.breadth_first_graph_search(tu).path())
print("Depth_First", search.depth_first_graph_search(tu).path())
print("Recorrido y profundidad: ", search.busqueda_en_grafo_Ramif_y_Acota(tu).path())
print("Recorrido y profundidad con Subestimación:", search.busqueda_Ramif_y_Acota_Subest(tu).path())

print("\nPrueba 4 de R a N")
rn = search.GPSProblem('R', 'N'
                       , search.romania)

print("Breadth_First", search.breadth_first_graph_search(rn).path())
print("Depth_First", search.depth_first_graph_search(rn).path())
print("Recorrido y profundidad: ", search.busqueda_en_grafo_Ramif_y_Acota(rn).path())
print("Recorrido y profundidad con Subestimación:", search.busqueda_Ramif_y_Acota_Subest(rn).path())

print("\nPrueba 5 de O a S")
os = search.GPSProblem('O', 'S'
                       , search.romania)

print("Breadth_First", search.breadth_first_graph_search(os).path())
print("Depth_First", search.depth_first_graph_search(os).path())
print("Recorrido y profundidad: ", search.busqueda_en_grafo_Ramif_y_Acota(os).path())
print("Recorrido y profundidad con Subestimación:", search.busqueda_Ramif_y_Acota_Subest(os).path())