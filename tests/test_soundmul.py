# Ejercicio 8
import unittest

from mysound import Sound


class Test_soundmul(unittest.TestCase):

    def test_len(self):  # aqui voy a comprobar que la longitud del buffer del
        # objeto antiguo es igual que la del nuevo buffer
        self.assertEqual(len(s.buffer), len(s2.buffer))

    def test_values(self):

        # Verificar que cada valor del buffer
        # se haya multiplicado correctamente
        for i in range(s.nsamples):
            self.assertEqual(s2.buffer[i], int(s.buffer[i])*2)

    def test_multiplication0(self):
        s = Sound(2)
        s.sin(440, 10000)
        factor = 0.0
        s2 = s.soundmul(factor)
        for sample in s2.buffer:
            self.assertEqual(sample, 0)


s = Sound(2)
s.sin(440, 10000)

s2 = s.soundmul(2)
