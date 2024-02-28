#! python3
# BulletPoints.py - Add bulletpoints to every new line of a copied text

import pyperclip

text = pyperclip.paste()
# text = "asfsf/nsjafhsakjhf/nhghgfhg"

textList = text.split("/n")
textBullet = ""

for i in textList:
    textBullet += f"* {i}\n"

pyperclip.copy(textBullet)
print("Added bullets")
# print(text.split("/n"))
