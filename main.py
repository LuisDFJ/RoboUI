import serial
import time


def encodeSerial( waist, shoulder, elbow ):
    byteArray = ( int( waist ).to_bytes( 2, 'big' ) + 
                int( shoulder ).to_bytes( 2, 'big' ) +
                int( elbow ).to_bytes( 2, 'big' ) )
    return b"<" + byteArray + b">"


def main():
    com =  serial.Serial( "COM11", 115200 )
    
    val = encodeSerial( 1023,1023,1023 )

    time.sleep( 2.0 )
    com.write( val )
    time.sleep( 0.5 )
    com.write( val )
    time.sleep( 0.4 )
    com.write( val )
    time.sleep( 0.3 )
    com.write( val )
    time.sleep( 0.2 )
    com.write( val )
    time.sleep( 0.1 )
    com.write( val )

    com.close()
            
            #com.write( b"A510B510C510S1530F\n" )


main()

#encodeSerial( 1023, 1023, 1023 )