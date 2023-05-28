"""Record a few seconds of audio and save to a WAVE file."""
import os
import time
import wave

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = 'output.wav'

aud = pyaudio.PyAudio()

stream = aud.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

if not os.path.exists('sounds'):
    os.makedirs('sounds')


def run():
    input('Speak for 20 secs after pressing \'Enter\': ')
    print('\n speak NOW whats on your mind!')
    
    time.sleep(.5)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print('\nRecording Saved.')
    stream.stop_stream()
    stream.close()

    aud.terminate()

    wf = wave.open('sounds/' + WAVE_OUTPUT_FILENAME, 'wb') # 'wb' is word binary
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(aud.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames)) # 'b' is binary empty string
    wf.close()


if __name__ == '__main__':
    run()
