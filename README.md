# conquerorTankPython
Librería que te permite manipular el código de Arduino directamente desde Python. 
# Conqueror Robot Tank - Paquetería Python para Control Autónomo

Este proyecto permite programar scripts en Python para controlar autónomamente un robot tanque Conqueror. También ofrece la capacidad de manipular un módulo de sensores externos que está integrado en la configuración estándar del robot.

Al utilizar Python como lenguaje de alto nivel, se ha diseñado la interfaz (las funciones) de manera intuitiva para aquellos que desean iniciarse en el desarrollo de lógica de programación y visualizarla en hardware.

Dado que tanto el hardware como el software están en constante evolución, es posible que se requiera modificar el código en el futuro para mantener su compatibilidad con las versiones contemporáneas de Arduino.

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Dependencias de Software](#dependencias-de-software)
3. [Instalación de Librerías](#instalación-de-librerías)
4. [Lista de comandos](#lista-de-comandos)
5. [Instrucciones](#instrucciones)
6. [Ejemplo de Uso](#ejemplo-de-uso)

## Requisitos

### Dependencias de Software

Para el funcionamiento del código, se requiere la instalación del siguiente software:

- Versión Actual de Python
- Arduino IDE (opcional)

### Instalación de Librerías

Los siguientes comandos deben ser ejecutados en orden para garantizar una correcta instalación de las librerías necesarias.

#### Controlar el Robot Tanque Conqueror

Las siguientes librerías se utilizan para controlar el robot tanque:

#### Instalación (Windows)
```
pip install --upgrade setuptools
pip install pyduinocli
pip install pyserial
pip install time
pip install setuptools wheel twine
```
#### Lista de comandos 
      inicio
      final
      cargar
      avanza
      reversa
      izquierda
      derecha
      avanzaIzquierda
      reversaIzquierda
      avanzaDerecha
      reversaDerecha
      alto
### Instrucciones
  1. Conecta el robot tanque Conqueror a tu computadora.
  3. Crea un script.py en la carpeta RobotConquerorTank para enviar comandos al robot tanque y controlar sus movimientos.
  4. Asegúrate de tener importado comandos as com
  5. Asegúrate que estás trabajando en la misma carpeta
  6. Posteriormente, ten asegurado que no esté en ninguna conexión Bluetooth o con algún otro puerto físico.
  7. El orden en el que se tienen que poner los comandos es com.inicio()
  8. Posteriormente, asegúrate de tener presentes la lista de comandos a utilizar
  9. Agrega los comandos a usar.
  10. Agrega el com.final()
  11. Posteriormente el com.cargar()
  12. Ejecuta el programa

### Ejemplo de uso
```
import Comandos as com

com.inicio()

com.derecha(4,200) // com.derecha(segundos, velocidad "0-255")


com.final()

com.cargar()
```
