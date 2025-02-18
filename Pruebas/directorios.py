from pathlib import Path

# Especifica el directorio que quieres listar
directorio = Path('C:/Users/mario.rey/OneDrive - EDISA/Documentos/MARIO/PIA/pia')

# Listar el contenido del directorio
contenido = list(directorio.iterdir())

# Imprimir el contenido
print(contenido)