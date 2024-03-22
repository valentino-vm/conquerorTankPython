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
4. [Instrucciones](#instrucciones)
5. [Ejemplo de Uso](#ejemplo-de-uso)

## Requisitos

### Dependencias de Software

Para el funcionamiento del código, se requiere la instalación del siguiente software:

- Versión Actual de Python
- Arduino IDE

### Instalación de Librerías

Los siguientes comandos deben ser ejecutados en orden para garantizar una correcta instalación de las librerías necesarias.

#### Controlar el Robot Tanque Conqueror

Las siguientes librerías se utilizan para controlar el robot tanque:

#### Instalación (Windows)

pip install --upgrade setuptools
pip install pyduinocli
pip install pyserial
pip install time

### Instrucciones
  1. Conecta el robot tanque Conqueror a tu computadora.
  2. Ejecuta el script prueba1.py para enviar comandos al robot tanque y controlar sus movimientos.
  3. Si deseas utilizar los sensores externos, asegúrate de conectarlos adecuadamente y modificar el script según sea necesario.
