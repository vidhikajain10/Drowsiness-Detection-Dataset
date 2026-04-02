import os
from playsound import playsound

def play_alarm():
    try:
        sound_path = os.path.join("assets", "alarm.wav")
        playsound(sound_path)
    except Exception as e:
        print("Alarm error:", e)
