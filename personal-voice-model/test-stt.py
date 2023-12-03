from RealtimeSTT import AudioToTextRecorder
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    recorder = AudioToTextRecorder(
        spinner=False, model="tiny.en", language="en")

    print("Say something...")
    while (True):
        print(recorder.text(), end=" ", flush=True)
