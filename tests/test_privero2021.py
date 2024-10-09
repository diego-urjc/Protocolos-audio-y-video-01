import unittest
from mysound import Sound


class Testvalues(unittest.TestCase):

    def testValues(self):
        sound = Sound(1)
        sound.sin(440, 10000)

        # Comprobar que los valores de la onda sin están dentro de un rango
        self.assertLessEqual(max(sound.buffer), 10000)  # Valor obtenido menor o igual al maximo
        self.assertGreaterEqual(min(sound.buffer), -10000)  # Valor obtenido mayor o igual al minimo

    def testSilence(self):
        sound = Sound(1)
        sound.sin(0, 10000)

        # Comprobar que cuando la frecuencia es 0 se genere una onda silenciosa
        self.assertEqual(max(sound.buffer), 0)
        self.assertEqual(min(sound.buffer), 0)

if __name__ == '__main__':
    unittest.main()
