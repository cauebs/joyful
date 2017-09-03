# **joyful**: simple joystick input on Linux


## Installation
```
~ $ pip install git+https://github.com/cauebs/joyful
```


## Usage

```python
from joyful import Joystick
from joyful.mapping import dualshock4 as ds4


ds4 = Joystick(joystick_number=1, mapping=ds4.MAPPING)

for event in ds4.iter_events():
    if not event.initial and event.id == ds4.Labels.PLAYSTATION:
        break

    print(f'{event.id} = {event.value}')
```

Joystick input is read from `/dev/input/js{joystick_number}`.

This has only been tested on my Dualshock 4. If you create mappings for other controllers, I'll be glad to merge them! However, this isn't intended for serious usage and there might not be any further developments.
