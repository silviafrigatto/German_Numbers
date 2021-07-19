#   This program prompts the user to enter a number (from 0 to 99) and shows how to write/speak it in german.

from time import sleep
from voice import speak

title = "0 TO 99 IN GERMAN"
print(f'{"*-" * 32}\n{title.center(64)}\n{"*-" * 32}')
print('''Instructions:
- Enter a number from 0 to 99 to see how it's written in german.
- A number outside of this interval finishes the program.''')

list_1 = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
list_2 = ["elf", "zwölf"]
list_3 = ["zehn", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
end_is_1 = (21, 31, 41, 51, 61, 71, 81, 91)

while True:
    try:
        num = int(input("\n=> Enter a number: "))
        sleep(0.3)
    except ValueError:
        print("ERROR! You didn't enter a number.")
    else:
        if num < 0 or num >= 100:
            print("Exiting program...")
            sleep(1)
            print("Tschüss!")
            sleep(0.2)
            break
        else:
            #   Rules
            if num in end_is_1:
                list_1[1] = "ein"
            if num == 16:
                list_1[6] = "sech"
            if num == 17:
                list_1[7] = "sieb"
            if num < 10:
                print(f'{num}\n{list_1[num]}')
                speak(num)
            elif num == 11:
                print(f'{num}\n{list_2[0]}')
                speak(num)
            elif num == 12:
                print(f'{num}\n{list_2[1]}')
                speak(num)
            elif 12 < num < 19:
                print(f'{num}\n{list_1[num % 10]}{list_3[0]}')
                speak(num)
            else:
                if num % 10 == 0:
                    print(f'{num}\n{list_3[int((num - (num % 10)) / 10) - 1]}')
                    speak(num)
                else:
                    print(f'{num}\n{list_1[num % 10]}und{list_3[int((num - (num % 10)) / 10) - 1]}')
                    speak(num)
