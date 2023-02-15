from pyfiglet import figlet_format
from termcolor import colored

text = input("Enter the text to display: \n")
text_color = input("Pick your fav color: \n")

ascii_art = figlet_format(text)

col = colored(ascii_art, color=text_color,
              on_color="on_magenta", attrs={'blink': 3})

print(col)
