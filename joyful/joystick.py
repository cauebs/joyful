from array import array
from fcntl import ioctl
from struct import unpack

from . import mappings
from .event import Event


class Joystick:
    def __init__(self, joystick_number=0, mapping=mappings.GENERIC):
        self.path = f'/dev/input/js{joystick_number}'
        self.mapping = mapping
        self.state = {}
        with open(self.path, 'rb') as js:
            # JSIOCGNAME(len)
            buffer = array('B', [0] * 64)
            ioctl(js, 0x80006a13 + 0x10000 * len(buffer), buffer)
            self.name = buffer.tobytes().decode()

            # JSIOCGAXES
            buffer = array('B', [0])
            ioctl(js, 0x80016a11, buffer)
            num_axes = int(buffer[0])

            # JSIOCGBUTTONS
            buffer = array('B', [0])
            ioctl(js, 0x80016a12, buffer)
            num_buttons = int(buffer[0])

            # JSIOCGAXMAP
            buffer = array('B', [0] * 64)
            ioctl(js, 0x80406a32, buffer)

            self._axis_map = [self.mapping.get(axis, f'unknown(0x{axis:02x})')
                              for axis in buffer[:num_axes]]

            self.axes = {axis_name: 0
                         for axis_name in self._axis_map}

            # JSIOCGBTNMAP
            buffer = array('H', [0] * 200)
            ioctl(js, 0x80406a34, buffer)

            self._button_map = [self.mapping.get(btn, f'unknown(0x{btn:03x})')
                                for btn in buffer[:num_buttons]]

            self.buttons = {button_name: 0
                            for button_name in self._button_map}

    def iter_events(self, normalize_axes=True):
        with open(self.path, 'rb') as js:
            while True:
                buffer = js.read(8)
                if not buffer:
                    continue

                event = Event(*unpack('IhBB', buffer),
                              self._button_map, self._axis_map,
                              normalize_axis=normalize_axes)

                self.axes[event.id] = event.value
                yield event
