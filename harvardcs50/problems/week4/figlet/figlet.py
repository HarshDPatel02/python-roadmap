import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = None
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font = sys.argv[2]
    if font not in figlet.getFonts():
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")

if font:
    figlet.setFont(font=font)

print(figlet.renderText(text))
