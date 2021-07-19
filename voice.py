import gtts
import os
from playsound import playsound


def speak(string):
    '''
    :param string: The text that will be converted into audio
    :return: Returns the audio
    '''
    # converts the parameter into a string (if from a different type)
    if isinstance(string, str) is False:
        string = str(string)

    # make request to google to get synthesis
    tts = gtts.gTTS(string, lang="de", slow=False)

    # save the audio file
    audio_file = "number.mp3"
    tts.save(audio_file)

    # play the audio file
    playsound(audio_file)

    # remove the audio file
    if os.path.exists(audio_file):
        os.remove(audio_file)
