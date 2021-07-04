from googletrans import Translator
# taking some text in spanish language
text = "me encanta python.hub"
translator = Translator()
dt = translator.detect(text)
translated = translator.translate(text)
print(translated.text)
