from gtts import gTTS
import os

Text = "I am Emu"

output = gTTS(text=Text,lang='en', slow=False)

output.save("output.mp3")

os.system("start output.mp3")