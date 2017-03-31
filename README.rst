pyomxplayer
===========
Python wrapper module around `OMXPlayer <https://github.com/popcornmix/omxplayer>`_
for the Raspberry Pi. This fork from `jbaiter <https://github.com/jbaiter/pyomxplayer>`_
only plays audio and calls a callback function once the song has ended.


Installation:
-------------
::

    git clone https://github.com/roosnic1/pyomxplayer.git
    python pyomxplayer/setup.py install

Example:
--------
::

    >>> from pyomxplayer import OMXPlayer
    >>> from pprint import pprint
    >>> omx = OMXPlayer('test.mp3')
    >>> pprint(omx.__dict__)
    {'_position_thread': <Thread(Thread-5, started 1089234032)>,
    '_process': <pexpect.spawn object at 0x1a435d0>,
    'audio': {'bps': 16,
            'channels': 2,
            'decoder': 'mp3',
            'rate': 48000,
            'streams': 1},
    'chapters': 0,
    'current_audio_stream': 1,
    'current_volume': 0.0,
    'paused': True,
    'position': 0.0,}
    >>> omx.toggle_pause()
    >>> omx.position
    9.43
    >>> omx.stop()
