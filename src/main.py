import pyb
from encoder_reader import EncoderDriver as Encoder
import micropython


micropython.alloc_emergency_exception_buf(1000)


if __name__ == "__main__":

    pinC6 = pyb.Pin.board.PC6
    pinC7 = pyb.Pin.board.PC7
    enc1_timer_num = 1

    pinB6 = pyb.Pin.board.pinB6
    pinB7 = pyb.Pin.board.pinB7
    enc2_timer_num = 2


    encoder1 = Encoder(pinC6, pinC7, enc1_timer_num)
    encoder2 = Encoder(pinB6, pinB7, enc2_timer_num)


    print("test")