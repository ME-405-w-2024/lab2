import pyb

class EncoderDriver:
    """
    This is a driver for a quadrature encoder.
    """
    
    def __init__(self, 
                 chan_A_pin:pyb.Pin.board, 
                 chan_B_pin:pyb.Pin.board,
                 timer_num:int):


        self.pin_A = pyb.Pin(chan_A_pin, mode=pyb.Pin.AF_PP, af=pyb.Pin.AF2_TIM4)
        self.pin_B = pyb.Pin(chan_B_pin, mode=pyb.Pin.AF_PP, af=pyb.Pin.AF2_TIM4)

        self.enc_timer = pyb.Timer(timer_num, prescaler=1)
        self.timer_channelA = self.enc_timer.channel(1, pyb.Timer.ENC_AB)

    def read(self):
        # must return the current timer count
        return self.enc_timer.counter()
    

    def zero(self):
        # must set the timer count to zero
        self.enc_timer.counter(0)