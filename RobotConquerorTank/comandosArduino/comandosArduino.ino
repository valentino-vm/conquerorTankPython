
    #include <avr/wdt.h>
    #include "DeviceDriverSet_xxx0.h"
    #include "ApplicationFunctionSet_xxx0.cpp"

    DeviceDriverSet_Motor AppMotor;
    Application_xxx Application_ConquerorCarxxx0;

    void setup() {
        int segundos = 5;
        int velocidad = 255;

    Serial.begin(9600);
    
      for(int i = 0; i < 4; i++){
      // Codigo a ejecutar en cada iteracion
      //ValentinoV
      ApplicationFunctionSet_ConquerorCarMotionControl(3 /*direction*/, 200 /*speed*/);
      Serial.println(i);
      delay(1000);
      if (i == 4-1){
        ApplicationFunctionSet_ConquerorCarMotionControl(8 /*direction*/, 200 /*speed*/);
      }
      }
    }
    
    void loop() { 
                
    } 
    