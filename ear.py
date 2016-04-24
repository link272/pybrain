#!/usr/bin/python

import pyaudio
import wave

class Ear(object):

    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    chunk = 1024
    record_seconds = 0.01
 
    def __init__(self):
        audio = pyaudio.PyAudio()

    def stream(self):
        stream = audio.open(format=self.format, 
                            channels=self.channels,
                            rate=self.rate, 
                            input=True,
                            frames_per_buffer=self.chunk)
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            frames.append(stream.read(CHUNK))
        stream.stop_stream()
        stream.close()
        audio.terminate()
        return frame



