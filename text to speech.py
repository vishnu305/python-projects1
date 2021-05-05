from gtts import gTTS
import os
mytext="hi there i am using whatsapp"
language='en'
output=gTTS(text=mytext,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")
os.system("start syeraa.mp3")
