from googletrans import Translator


def google_translate(text):
    translator = Translator()
    translation = translator.translate(text=text, src="en", dest="ru")

    return translation.text
