from pyomxplayer import OMXPlayer


def callbackFunc():
    OMXPlayer('test.mp3', callbackFunc, start_playback=True)

omx = OMXPlayer('test.mp3', callbackFunc)
omx.toggle_pause()