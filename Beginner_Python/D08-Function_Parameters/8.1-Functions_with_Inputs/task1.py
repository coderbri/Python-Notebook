def greet():
    print("Hello")
    print("你好")
    print("안녕하세요")

greet()


def greet_by_name(name):
    print(f"Hello {name}!")

greet_by_name("Bri")


your_lang = input("What is your language? Enter:\n"
                  " 'en' for English,\n"
                  " 'es' for Español (Spanish),\n"
                  " 'zh' for 中文 (Standard Mandarin), or\n"
                  " 'kr' for 한국어 (Korean)\n").lower()

def greet_by_language(language):
    if language == 'en':
        print("Hello! How are you?")
    elif language == 'es':
        print("¡Hola! ¿Como está?")
    elif language == 'zh':
        print("你好！你怎么样？")
    elif language == 'kr':
        print("안녕하세요!")
    else:
        "Please enter a valid language."

greet_by_language(your_lang)