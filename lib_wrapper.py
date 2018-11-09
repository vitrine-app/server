from ctypes import *

lib = cdll.LoadLibrary("./lib/games_catcher.so")

lib.GetGame.argtypes = [c_int, c_char_p]
lib.GetGame.restype = c_char_p
