<style>
body {
    text-align: justify;
}
</style>

## wordlist_comb.py

``wordlist_comb.py`` es un script en Python que crea una wordlist que resulta de la combinación de dos wordlists. Por ejemplo, si tenemos una wordlist de 'usuarios.txt' y otra de 'contraseñas.txt', ``wordlist_comb.py`` crea una tercera lista combinando 'usuarios' y 'contraseñas' con el siguiente formato: ``usuario:contraseña``

Cabe destacar que la wordlist resultante puede llegar a ser un archivo con cientos de miles, e incluso millones de combinaciones por ser un producto cartesiano entre los elementos de cada archivo. Por lo que un ataque de fuerza bruta, por ejemplo con ``hydra``, en un archivo de un elevado número de combinaciones puede consumir mucho tiempo y recursos de la máquina host. Sin embargo, para archivos de relativamente pocos elementos, esta solución se presenta como ideal. Incluso para archivos con un número muy grande de elementos, ya que se pueden ir "troceando" y crear combinaciones más razonablemente pequeñas.

Desde el directorio de descarga en una shell de Linux se ejecuta:
```bash
python3 wordlist_comb.py -u <wordlist#1> -p <wordlist#2> -o <nombre_wordlist_resultante>
```

También se puede ejecutar un pequeño asistente para recordar su uso:
```bash
python3 wordlist_comb.py -h
```