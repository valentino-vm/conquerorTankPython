global tiempo
global velocidad

import sys
import glob
import pyduinocli

import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result




def inicio():
    prueba = open ('comandosArduino//comandosArduino.ino','w')
    prueba.write("""
    #include <avr/wdt.h>
    #include "DeviceDriverSet_xxx0.h"
    #include "ApplicationFunctionSet_xxx0.cpp"

    DeviceDriverSet_Motor AppMotor;
    Application_xxx Application_ConquerorCarxxx0;

    void setup() {
        int segundos = 5;
        int velocidad = 255;

    Serial.begin(9600);
    """)

    prueba.close()

def final():
  control = open('comandosArduino//comandosArduino.ino','a')
  control.write("""}
    
    void loop() { 
                
    } 
    """)
  control.close()



def avanza(tiempo,velocidad):
  
  control = open('comandosArduino//comandosArduino.ino','a')
  control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(0 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """
  )

def reversa(tiempo,velocidad):
  
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(1 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)

 

def izquierda(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(2 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)


def derecha(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(3 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)


def avanzaIzquierda(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(4 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)


def reversaIzquierda(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(5 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)


def avanzaDerecha(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(6 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)


def reversaDerecha(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(7 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)

    return reversaDerecha

def alto(tiempo,velocidad):
    control = open('comandosArduino//comandosArduino.ino','a')
    control.write("""
      for(int i = 0; i < """+str(tiempo)+"""; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == """+str(tiempo)+"""-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, """+str(velocidad)+""" /*speed*/);
      }
      }
    """)
    
    
def cargar ():
  arduino = pyduinocli.Arduino("./arduino-cli")

  puerto = serial_ports()
  print (puerto)

  arduino.compile(fqbn="arduino:avr:uno",sketch="comandosArduino//comandosArduino.ino")

  arduino.upload(fqbn="arduino:avr:uno", sketch="comandosArduino//comandosArduino.ino", port=puerto[0])
