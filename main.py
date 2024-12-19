from RealtimeSTT import AudioToTextRecorder
from processor import initialize_lm, process
from speech import read_text

ready_status = True

def process_text(text):
    global ready_status

    ready_status = False

    print(text)
    lm_output = process(text)
    print(lm_output)
    read_text(lm_output)
    
    ready_status = True

if __name__ == '__main__':
    recorder = AudioToTextRecorder()
    read_text(initialize_lm())
    while True:
        if ready_status:
            recorder.text(process_text)
