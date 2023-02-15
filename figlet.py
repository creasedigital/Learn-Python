import pyfiglet
from termcolor import colored

text = input("Enter the text to display: \n")
text_color = input("Pick your fav color: \n")

col = colored(pyfiglet.figlet_format(text), color=text_color,
              on_color="on_magenta", attrs={'blink': 3})

print(col)
