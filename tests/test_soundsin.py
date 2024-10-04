# Ejercicio 6

import unittest

from mysoundsin import SoundSin


class TestSoundSin(unittest.TestCase):

    def test_val(self):
        sound = SoundSin(2, 440, 1000)

        self.assertTrue(sound.duration > 0)
        self.assertTrue(sound.nsamples >= sound.samples_second)
        self.assertTrue(sound.nsamples > sound.duration)

    def test_buffer(self):
        sound = SoundSin(3, 440, 1000)
        self.assertEqual(len(sound.buffer), sound.nsamples)

    def test_type(self):
        sound = SoundSin(3, 440, 1000)
        self.assertIsInstance(sound.buffer, list)
        self.assertIsInstance(sound.nsamples, int)


if __name__ == '__main__':
    unittest.main()
