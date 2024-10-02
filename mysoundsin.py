#Ejercicio 5
from mysound import Sound
import math

class SoundSin(Sound):
    def __init__(self, duration, frequency, amplitude):
        super().__init__(duration)

        self.nsamples = int(self.samples_second * self.duration)
        self.buffer = [0] * self.nsamples

        self.sin(frequency,amplitude)

        for nsample in range(self.nsamples):
            t = nsample / self.samples_second
            self.buffer[nsample] = int(amplitude *
                                       math.sin(2 * math.pi * frequency * t))

sign = SoundSin(0.5,4400,2500)