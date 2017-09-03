class Event:
    def __init__(self, time, value, code, number,
                 button_map, axis_map, normalize_axis=True):
        self.initial = bool(code & 0x80)
        self.time = time

        if code & 0x1:
            self.id = button_map[number] if button_map else number
            self.value = bool(value)

        elif code & 0x2:
            self.id = axis_map[number] if axis_map else number
            self.value = value
            if normalize_axis:
                self.value /= 2**15

    def __repr__(self):
        return f'<Event {self.id}: {self.value}>'
