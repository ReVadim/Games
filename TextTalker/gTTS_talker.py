from gtts import gTTS

text = 'Всем привет!'

obj = gTTS(text, lang='ru')

obj.save('mp3/hi_everyone.mp3')
