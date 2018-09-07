# Tulipy

Tulipy es un wrapper de python para utilizar [Tulipan Translate](https://www.tulipantranslate.com)


### Uso como libreria
```
import tulipy
```

#### Encode (mensaje > traduccion)

```
tulipy.codificar('Te voy a romper el concepto social de genero',
                       'Horacio')
```
***tulipy.codificar(Mensaje,Apodo)***
-> te devuelve una String

#### Encode (traduccion > Mensaje original)

```
tulipy.decodificar('Pasame tu cuil.', 'Horacio')
```
***tulipy.decodificar(Mensaje,Apodo)***
-> te devuelve una String

### Uso como CLI (Linea de comandos)
```
python tulypy.py -h 

CLI de Tulipan Translate

optional arguments:
  -h, --help            show this help message and exit
  --codificar CODIFICAR
                        mensaje a codificar
  --decodificar DECODIFICAR
                        mensaje a decodificar
  --apodo APODO         apodo a utilizar
```
Ejemplos:
```
$> python tulipy.py --codificar "Que Fuerte esta tu prima" --apodo Jorge
Mensaje Traducido: ¿Pasás a buscar a los chicos?
```
```
$ python tulipy.py --decodificar "¿Pasás a buscar a los chicos?" --apodo Jorge
Mensaje Original: Que Fuerte esta tu prima
```
