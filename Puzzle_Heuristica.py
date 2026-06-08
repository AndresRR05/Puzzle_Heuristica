# Puzzle Lineal con heurística
from arbol import Nodo

def buscar_solucion_heuristica(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        dato_nodo = nodo_inicial.get_datos()
        
        # Hijo Izquierdo: Intercambia los dos primeros elementos
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        
        # Hijo Central: Intercambia los elementos centrales
        hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo)
        
        # Hijo Derecho: Intercambia los dos últimos elementos
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo)
        
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

        for nodo_hijo in nodo_inicial.get_hijos():
            # Definimos la función de mejora dentro para que sea accesible
            def mejora(nodo_padre, nodo_hijo):
                calidad_padre = 0
                calidad_hijo = 0
                dato_padre = nodo_padre.get_datos()
                dato_hijo = nodo_hijo.get_datos()
                
                for n in range(1, len(dato_padre)):
                    # Corregido: se usan corchetes [] para índices, no paréntesis ()
                    if dato_padre[n] > dato_padre[n-1]:
                        calidad_padre = calidad_padre + 1
                    if dato_hijo[n] > dato_hijo[n-1]:
                        calidad_hijo = calidad_hijo + 1
                
                return calidad_hijo >= calidad_padre

            # Validación: no visitado y que mejore la calidad
            if not nodo_hijo.get_datos() in visitados and mejora(nodo_inicial, nodo_hijo):
                # Llamada recursiva
                sol = buscar_solucion_heuristica(nodo_hijo, solucion, visitados)
                if sol is not None:
                    return sol
        
        # Si el bucle termina sin encontrar solución en esta rama
        return None

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    
    nodo_solucion = buscar_solucion_heuristica(nodo_inicial, solucion, visitados)

    # Mostrar resultado
    if nodo_solucion is not None:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            # Corregido: Solo avanzamos un padre a la vez para no saltar pasos
            nodo = nodo.get_padre()
        
        resultado.reverse()
        print(resultado)
    else:
        print("No se encontró una solución.")