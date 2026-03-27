print("Starting")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry, ImageEntry

kb = KMKKeyboard()

kb.row_pins = (board.D0, board.D1, board.D2)
kb.col_pins = (board.D3, board.D4, board.D5)
kb.diode_orientation = DiodeOrientation.COL2ROW

enc = EncoderHandler()
enc.pins = ((board.D6, board.D7),)
enc.map = [((KC.VOL_UP, KC.VOL_DOWN),)]
kb.modules.append(enc)

kb.keymap = [
    [KC.A, KC.B, KC.C],
    [KC.D, KC.E, KC.F],
    [KC.G, KC.H, KC.I],
]

bus = busio.I2C(board.SCL, board.SDA)
disp = Display(i2c=bus)
kb.extensions.append(disp)

if __name__ == '__main__':
    kb.go()