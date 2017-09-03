from enum import Enum, auto


class Labels(Enum):
    DPAD_X = auto()
    DPAD_Y = auto()

    L1_BUTTON = auto()
    L2_BUTTON = auto()
    L2_TRIGGER = auto()
    L3_X_AXIS = auto()
    L3_Y_AXIS = auto()
    L3_BUTTON = auto()

    SHARE = auto()
    OPTIONS = auto()
    START = auto()
    SELECT = auto()
    PLAYSTATION = auto()

    CROSS = auto()
    CIRCLE = auto()
    SQUARE = auto()
    TRIANGLE = auto()

    R1_BUTTON = auto()
    R2_BUTTON = auto()
    R2_TRIGGER = auto()
    R3_X_AXIS = auto()
    R3_Y_AXIS = auto()
    R3_BUTTON = auto()

    ACCEL_X = auto()
    ACCEL_Y = auto()
    ACCEL_Z = auto()
    GYRO_X = auto()
    GYRO_Y = auto()
    GYRO_Z = auto()


MAPPING = {
    0x00: Labels.L3_X_AXIS,
    0x01: Labels.L3_Y_AXIS,
    0x02: Labels.L2_TRIGGER,
    0x03: Labels.R3_X_AXIS,
    0x04: Labels.R3_Y_AXIS,
    0x05: Labels.R2_TRIGGER,
    0x10: Labels.DPAD_X,
    0x11: Labels.DPAD_Y,
    0x130: Labels.CROSS,
    0x131: Labels.CIRCLE,
    0x133: Labels.TRIANGLE,
    0x134: Labels.SQUARE,
    0x136: Labels.L1_BUTTON,
    0x137: Labels.R1_BUTTON,
    0x138: Labels.L2_BUTTON,
    0x139: Labels.R2_BUTTON,
    0x13a: Labels.SHARE,
    0x13b: Labels.OPTIONS,
    0x13c: Labels.PLAYSTATION,
    0x13d: Labels.L3_BUTTON,
    0x13e: Labels.R3_BUTTON,
}

MOTION = {
    0x00: Labels.ACCEL_X,
    0x01: Labels.ACCEL_Y,
    0x02: Labels.ACCEL_Z,
    0x03: Labels.GYRO_X,
    0x04: Labels.GYRO_Y,
    0x05: Labels.GYRO_Z,
}
