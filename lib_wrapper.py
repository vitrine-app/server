from ctypes import *

lib = cdll.LoadLibrary("./games-catcher.so")

lib.get_game.argtypes = [c_int]
lib.get_game.restype = c_char_p
