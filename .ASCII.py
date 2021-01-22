import random
import os

ID = random.randrange(2287)

#website="https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"

f = open(".ART", "r")
lines = f.readlines()

word = str(lines[ID]) 

tail = (len(word) - 1)
word = word[0:tail]

l = str(word[0])

if l == "0" or l == "3" or l == "a" or l == "b":
	l = "ab"
elif l == "d" or l == "e" or l=="f":
	l = "def"
elif l == "g" or l == "h" or l=="i":
	l = "ghi"
elif l == "j" or l == "k" or l=="l":
	l = "jkl"
elif l == "m" or l == "n" or l=="o":
	l = "mno"
elif l == "p" or l == "q" or l=="r":
	l = "pqr"
elif l == "u" or l == "v" or l=="w":
	l = "uvw"
elif l == "x" or l == "y" or l=="z":
	l = "xyz"

website="http://www.ascii-art.de/ascii/" + l + "/" + word + ".txt"

print(website)
os.system("curl " +  website)
print("\n")

f.close()
