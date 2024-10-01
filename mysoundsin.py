from mysound import Sound


class SoundSin(Sound):
    def __init__(self, duration, frequency, amplitude):
        super().__init__(duration)
        self.duration = duration
        self.frequency = frequency
        self.amplitude = amplitude
        self.nsamples = int(self.samples_second * self.duration)
        self.buffer = [0] * self.nsamples



