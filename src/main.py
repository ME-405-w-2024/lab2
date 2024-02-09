import pyb
import encoder_reader

ENCODER1_TIMER_NUMBER = 4

ENCODER2_TIMER_NUMBER = 8

if __name__ == "__main__":
    encoder1 = encoder_reader.Encoder(pyb.Pin.board.PB6,pyb.Pin.board.PB7,ENCODER1_TIMER_NUMBER,pyb.Pin.AF2_TIM4)

    encoder2 = encoder_reader.Encoder(pyb.Pin.board.PC6,pyb.Pin.board.PC7,ENCODER2_TIMER_NUMBER,pyb.Pin.AF3_TIM8)

    position1 = 0
    position2 = 0

    while 1:
        position1 = encoder1.read()
        position2 = encoder2.read()
        print( "Encoder1: " + str(position1) + " | Encoder2: " + str(position2) )