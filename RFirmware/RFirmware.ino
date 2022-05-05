#include <DynamixelSerial1.h>
#define ID1 9
#define ID2 13
#define ID3 17
#define ENPIN 20
#define SERVBAUD 1000000

bool flag = false;
typedef unsigned int uint16_t;
uint16_t joints[3];

void setup() {
  Serial.begin( 115200 );
  pinMode( 13, OUTPUT );
  digitalWrite( 13, LOW );

  Dynamixel.begin(SERVBAUD,ENPIN);
  Dynamixel.ledStatus(ID2,ON);
  delay(1000);
  Dynamixel.ledStatus(ID2,OFF);
}

void decodeSerial( uint16_t *arr )
{
  byte byteArr[8];
  uint16_t i = 0;
  while( Serial.available() > 0 ){
    char a = Serial.read();
    if ( i < 8 ) byteArr[ i++ ] = a;
    if ( a == '>' ) break;
    delay( 1 );
  }
  uint16_t *uiArr = (uint16_t*)( byteArr + 1 );
  if ( byteArr[0] == '<' && byteArr[7] == '>' )
  {
    *(arr)     = *(uiArr);
    *(arr + 1) = *(uiArr + 1);
    *(arr + 2) = *(uiArr + 2);
    flag ^= true;
    digitalWrite( 13, flag );
  }
  
}

void loop() {
  if( Serial.available() )
  {
    decodeSerial( joints );
    /*
    Serial.println( joints[0] );
    Serial.println( joints[1] );
    Serial.println( joints[2] );
    */
    Dynamixel.move(ID1,joints[0]);
    Dynamixel.move(ID2,joints[1]);
    Dynamixel.move(ID3,joints[2]);
  }
}