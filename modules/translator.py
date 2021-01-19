from translate import Translator
translator= Translator(to_lang="ja")
try:
    with open("translate_text.txt") as my_file:
        text = my_file.readline()
        translation = translator.translate(text)
        print(translation)

        with open("text_ja.txt", mode='w', encoding='utf-8') as t_file:
            t_file.write(translation)

except FileNotFoundError as err:
    print("File not found")
    raise err