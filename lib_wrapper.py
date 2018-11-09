from ctypes import *

lib = cdll.LoadLibrary('./lib/games_catcher.so')


class GoString(Structure):
    _fields_ = [('p', c_char_p), ('n', c_longlong)]


lib.GetGame.argtypes = [c_int, GoString]
lib.GetGame.restype = c_char_p
