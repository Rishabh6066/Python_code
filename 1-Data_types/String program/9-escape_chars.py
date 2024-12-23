# \,\n,\t,\r,\b,\ooo,\xhh

# \"
txt=" I am \"jeff\" from pune"
print(txt)

# \\
txt=" I am \"jeff\" from pune I like Python \\JS"
print(txt)

# \n: newline

txt=" I am \"jeff\" from pune \n I like Python JS"
print(txt)

# \t: tab

txt=" I am \"jeff\" from pune.\tI like Python JS"
print(txt)

#\r : Carriage Return: Will pint the txt after \r

txt=" I am \"jeff\" from pune.\rI like Python JS"
print(txt)

#\b : backspace

txt=" I am \"jeff\" from pune.\bI like Python JS"
print(txt)

# \ooo : Octals

txt="\110\145\154\154\157"
print(txt)

# \xhh : hexa

txt="\x48\x65\x6c\x6c\x6f"
print(txt)

txt="Hello\rWor\rld"
print(txt)

'''

"Hello" is written

\r will move cursor to start

"Worlo" : Hel to Wor 

\r will move cursor to start

"ldrlo" : Wo to ld

o/p : "ldrlo"

'''