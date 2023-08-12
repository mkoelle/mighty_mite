from time import sleep
from machine import Pin

LOW = 0
HIGH = 1

HALF_STEP = [
    [LOW, LOW, LOW, HIGH],
    [LOW, LOW, HIGH, HIGH],
    [LOW, LOW, HIGH, LOW],
    [LOW, HIGH, HIGH, LOW],
    [LOW, HIGH, LOW, LOW],
    [HIGH, HIGH, LOW, LOW],
    [HIGH, LOW, LOW, LOW],
    [HIGH, LOW, LOW, HIGH],
]

FULL_STEP = [
 [LOW, LOW, HIGH, HIGH],
 [LOW, HIGH, HIGH, LOW],
 [HIGH, HIGH, LOW, LOW],
 [HIGH, LOW, LOW, HIGH]
]
        
class Stepper():
    def __init__(self, mode, pin1, pin2, pin3, pin4, delay=2):
        self.mode = mode
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.pin3 = Pin(pin3, Pin.OUT)
        self.pin4 = Pin(pin4, Pin.OUT)
        self.delay = delay/100  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP
        
        # Initialize all to 0
        self.reset()
        
    def step(self, count, direction=1):
        """Rotate count steps. direction = -1 means backwards"""
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1.value(bit[0]) 
                self.pin2.value(bit[1]) 
                self.pin3.value(bit[2]) 
                self.pin4.value(bit[3]) 
                sleep(self.delay)
        self.reset()
        
    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1.value(0) 
        self.pin2.value(0) 
        self.pin3.value(0) 
        self.pin4.value(0) 