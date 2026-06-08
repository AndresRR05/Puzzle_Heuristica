from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from Puzzle_Heuristica import buscar_solucion_heuristica
from arbol import Nodo


@require_http_methods(["GET", "POST"])
def inicio(request):
    if request.method == "POST":
        estado_inicial_str = request.POST.get("estado_inicial", "").strip()
        objetivo_str = request.POST.get("objetivo", "").strip()

        try:
            estado_inicial = [int(x.strip()) for x in estado_inicial_str.split(",")]
            objetivo = [int(x.strip()) for x in objetivo_str.split(",")]
        except ValueError:
            return render(
                request,
                "index.html",
                {
                    "error": "Los estados deben ser numeros separados por comas. Ej: 4,2,3,1",
                    "estado_inicial": estado_inicial_str,
                    "objetivo": objetivo_str,
                },
            )

        if len(estado_inicial) != 4 or len(objetivo) != 4:
            return render(
                request,
                "index.html",
                {
                    "error": "Cada estado debe tener exactamente 4 numeros",
                    "estado_inicial": estado_inicial_str,
                    "objetivo": objetivo_str,
                },
            )

        nodo_inicial = Nodo(estado_inicial)
        visitados = []
        nodo_solucion = buscar_solucion_heuristica(nodo_inicial, objetivo, visitados)

        if nodo_solucion is None:
            return render(
                request,
                "index.html",
                {
                    "error": "No se encontro solucion para ese estado inicial.",
                    "estado_inicial": estado_inicial_str,
                    "objetivo": objetivo_str,
                },
            )

        ruta = []
        nodo = nodo_solucion
        while nodo is not None:
            ruta.append(nodo.get_datos())
            nodo = nodo.get_padre()
        ruta.reverse()

        return render(
            request,
            "index.html",
            {
                "ruta": ruta,
                "estado_inicial": estado_inicial_str,
                "objetivo": objetivo_str,
                "pasos": len(ruta) - 1,
            },
        )

    return render(request, "index.html")
