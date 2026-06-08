# Puzzle Heuristica - Deploy con Django y Render

Aplicacion Django para resolver el Puzzle Lineal usando busqueda heuristica.

## Ejecutar local

1. Crear y activar entorno virtual (opcional)
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Migrar base de datos:

```bash
python manage.py migrate
```

4. Iniciar servidor:

```bash
python manage.py runserver
```

Abrir `http://127.0.0.1:8000`

## Deploy en Render

1. Sube este directorio a tu repo
2. En Render crea un Web Service desde ese repo
3. Render detecta `render.yaml` automaticamente
4. La app quedara publicada en tu dominio `.onrender.com`

## Archivos clave

- `Puzzle_Heuristica.py`: logica del algoritmo
- `django_views.py`: integra formulario y algoritmo
- `templates/index.html`: frontend minimalista moderno
- `render.yaml`: configuracion de deploy
