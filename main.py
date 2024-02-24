import vosk
import sounddevice as sd
import queue
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import os
from gtts import gTTS
import azure.cognitiveservices.speech as speechsdk
import commands
from work import Aru

q = queue.Queue()
model = vosk.Model('vosk-model-small-ru-0.22')

language = 'ru'


aru = Aru()

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

def callback(indata, farmes, times, status):
    q.put(bytes(indata))

def recognize(data, vectorizer, clf):
    name_aru = commands.voice_start.intersection(data.split())
    if not name_aru:
        return
    data.replace(list(name_aru)[0], '')
    zapros = data.replace(list(name_aru)[0], '')
    print(zapros)
    text_vector = vectorizer.transform([data]).toarray()[0]
    print(text_vector)
    count_z = list(text_vector).count(0)
    print(count_z)
    answer = clf.predict([text_vector])[0]
    answer = str(answer)
    func_name = answer.split()[0]
    func = 'aru.' + func_name + '()'
    exec(func)

def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(commands.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(commands.data_set.values()))

    del commands.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device,
                           dtype='int16', channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)


if __name__ == '__main__':
    main()