#!/usr/bin/python

import pyaudio
import wave

class Ear(object):

    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    chunk = 1024

    def __init__(self):
        audio = pyaudio.PyAudio()

    def stream(self, record_time):
        stream = audio.open(format=self.format, 
                            channels=self.channels,
                            rate=self.rate, 
                            input=True,
                            frames_per_buffer=self.chunk)
        frames = []
        for i in range(0, int(self.rate/ self.chunk* record_time)):
            frames.append(stream.read(self.chunk))
        stream.stop_stream()
        stream.close()
        audio.terminate()
        return frame



