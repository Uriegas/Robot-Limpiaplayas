# Robot-Limpiaplayas
Simulador de un robot limpia playas

## Linea de Comandos
Para correr el programa solo por linea de comandos incluya los argumentos `-r` y `-p` como en el ejemplo:
```
python vcleaner.py -r "1, 0, 1" -p 2
```

La estructura es la siguiente:
```
python vcleaner.py -r <rooms in quotes> -p <agent position>
```

Para obtener ayuda ejecute:
```
python vcleaner.py -h
```

Para correr con interfaz gráfica corra el comando solo:
```
python vcleaner.py
```

## Reference
1. https://docs.python.org/dev/library/argparse.html
2. https://stackoverflow.com/questions/58976607/restrict-input-string-length-in-argparse-add-argument
