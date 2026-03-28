import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

# HARDWARE SETUP
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D6, board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# OLED SETUP
i2c_bus = busio.I2C(board.SCL, board.SDA)

oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["Hack Club"]}
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
    i2c=i2c_bus
)
keyboard.extensions.append(oled_ext)

#  16-KEY MATRIX LAYOUT
keyboard.keymap = [
    [
        KC.N7,   KC.N8,   KC.N9,   KC.MUTE,
        KC.N4,   KC.N5,   KC.N6,   KC.VOLU,
        KC.N1,   KC.N2,   KC.N3,   KC.VOLD,
        KC.ESC,  KC.N0,   KC.ENTER, KC.MPLY
    ]
]

if __name__ == '__main__':
    keyboard.go()
