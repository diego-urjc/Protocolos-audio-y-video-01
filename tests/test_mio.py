# Ejercicio 4

import unittest
from mysound import Sound


class Testvalues(unittest.TestCase):

    def testValues(self):
        sound = Sound(1)
        sound.sin(440, 10000)

        # comprobar que la duracion de la onda es mayor a 0 y que es un numero float o entero

        self.assertTrue(sound.duration > 0)
        self.assertTrue(type(sound.duration) == float or int)


if __name__ == '__main__':
    unittest.main()
