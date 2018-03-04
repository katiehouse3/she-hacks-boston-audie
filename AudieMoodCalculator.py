# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Written by: Katie House, Julia Antonou, Lucille Tasker, 
#                and Srilekha Nuli
#  
#               SheHacks Boston 2018
#             
#   ~~ Script Adapted from Google API Doc Examples ~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import tkinter
from tkinter import messagebox

import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

root = tkinter.Tk()

def RefreashGraph():
    # Import Libraries
    import argparse
    import io
    import shutil
    import os

    def Show_Plot():
        import datetime
        import matplotlib.pyplot as plt
        import numpy as np
        from numpy import genfromtxt

        fig = plt.figure()
        fig.suptitle('Sentiment over Time', fontsize=14, fontweight='bold')

        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)

        ax.set_ylabel('Sentimet (-1 to 1)')


        from datetime import datetime
        def c_date(dstr):
            return dt.datetime.strptime(dstr, '%Y-%m-%d %H:%M:%s')
                                                  
        data = np.genfromtxt('C:data.csv',dtype=None,names=True, \
                                 delimiter=',', converters = {'CST': c_date})

        # Timestamp and Sentiment Data
        x = data['Timestamp']
        y = data['Sentiment']

        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        import matplotlib.ticker as tkr

        # plot
        ax.plot(x,y)

        plt.gcf().autofmt_xdate()
        
        return plt.show()

    def transcribe_file(speech_file):
        """Transcribe the given audio file."""
        from google.cloud import speech
        from google.cloud.speech import enums
        from google.cloud.speech import types
        client = speech.SpeechClient()

        # [START migration_sync_request]
        # [START migration_audio_config_file]
        with io.open(speech_file, 'rb') as audio_file:
            content = audio_file.read()

        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=8192,
            language_code='en-US')

        response = client.recognize(config, audio)
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print('Transcript: {}'.format(result.alternatives[0].transcript))

        # Imports the Google Cloud client library
        from google.cloud import language
        from google.cloud.language import enums
        from google.cloud.language import types
            # Instantiates a client
        client = language.LanguageServiceClient()

        # The text to analyze
        text = format(result.alternatives[0].transcript)
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        import time
        import datetime

        ts = time.time()

        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        Mbox('Your Speach', "Audie Heard : '"'' + text + "''", 0)
        Mbox('Your Sentiment', "Your sentiment score was : " + str(sentiment.score), 0)

        # import the data into a csv
        import csv
        fd = open('data.csv','a')
        DataAsText = "\n" + str(st) + "," + str(sentiment.score)
        fd.write(DataAsText)
        fd.close()
        Mbox("upload", "Upload Complete", 0)
    
    directory = os.fsencode("audio")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".flac"): 
            Mbox('Data', "New File Detected", 0)
            path = "audio/" + filename
            complete = "audio/complete/" + filename
            transcribe_file(path)
            shutil.move(path, complete)
            Show_Plot()
            continue
        else:
            continue

w = tkinter.Label(root, text="\nCalculate your mood with Audie!\n")
B = tkinter.Button(root, text ="Click Here", command = RefreashGraph)

w.pack()
B.pack()

root.mainloop()

