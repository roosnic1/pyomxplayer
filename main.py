from pyomxplayer import OMXPlayer
import time
import traceback
import sys

def main():
    global omx

    def callbackFunc():
        OMXPlayer('test.mp3', callbackFunc, start_playback=True)

    try:
        omx = OMXPlayer('test.mp3', callbackFunc)
        omx.toggle_pause()
        print("Starting omxplayer")
        # Loop forever, doing something useful hopefully:
        i = 0
        while True:
            i += 1
            time.sleep(0.5)
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
        omx.stop()
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()