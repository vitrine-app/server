from ctypes import *

games_catcher = cdll.LoadLibrary('./lib/games_catcher.so')


class GoString(Structure):
    _fields_ = [('p', c_char_p), ('n', c_longlong)]


games_catcher.GetGame.argtypes = [c_int, GoString]
games_catcher.GetGame.restype = c_char_p
