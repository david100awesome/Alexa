from time import sleep
from talk import *
from draw import *

while True:
    exit_key()
    normal_pic()
    sleep(0.4)
    text_version = recognize_voice()
        
    reply(text_version)
