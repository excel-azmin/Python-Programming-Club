# pip install googletrans==3.1.0a0
from googletrans import Translator
translator = Translator()

user_input_language = input()
print(translator.translate(user_input_language, dest='bn').text)