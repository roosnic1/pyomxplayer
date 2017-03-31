import pexpect
import re

from threading import Thread
from time import sleep

class OMXPlayer(object):

    _AUDIOPROP_REXP = re.compile(r"Audio codec (\w+) channels (\d+) samplerate (\d+) bitspersample (\d+).*")
    _STATUS_REXP = re.compile(r"V :\s*([\d.]+).*")
    _DONE_REXP = re.compile(r"have a nice day.*")

    _LAUNCH_CMD = '/usr/bin/omxplayer -s %s %s'
    _PAUSE_CMD = 'p'
    _TOGGLE_SUB_CMD = 's'
    _QUIT_CMD = 'q'

    paused = False
    subtitles_visible = True

    def __init__(self, audiofile, song_ended_callback, args=None, start_playback=False):
        if not args:
            args = ""
        cmd = self._LAUNCH_CMD % (audiofile, args)
        self._process = pexpect.spawn(cmd)

        self.audio = dict()

        self.song_ended_callback = song_ended_callback

        audio_props = self._AUDIOPROP_REXP.match(self._process.readline()).groups()
        self.audio['decoder'] = audio_props[0]
        (self.audio['channels'], self.audio['rate'],
         self.audio['bps']) = [int(x) for x in audio_props[1:]]

        self.current_audio_stream = 1
        self.current_volume = 0.0

        self._position_thread = Thread(target=self._get_position)
        self._position_thread.start()

        if not start_playback:
            self.toggle_pause()


    def _get_position(self):
        while True:
            index = self._process.expect([self._STATUS_REXP,
                                            pexpect.TIMEOUT,
                                            pexpect.EOF,
                                            self._DONE_REXP])
            if index == 1: continue
            elif index in (2, 3):
                self.stop()
                if self.song_ended_callback:
                    self.song_ended_callback()
                    break
            else:
                self.position = float(self._process.match.group(1))
            sleep(0.05)

    def toggle_pause(self):
        if self._process.send(self._PAUSE_CMD):
            self.paused = not self.paused

    def stop(self):
        self._process.send(self._QUIT_CMD)
        self._process.terminate(force=True)

    def set_speed(self):
        raise NotImplementedError

    def set_audiochannel(self, channel_idx):
        raise NotImplementedError


    def set_chapter(self, chapter_idx):
        raise NotImplementedError

    def set_volume(self, volume):
        raise NotImplementedError

    def seek(self, minutes):
        raise NotImplementedError
