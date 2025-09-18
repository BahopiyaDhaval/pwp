#Bahopiya Dhaval
with open(r'C:\Users\student\Downloads\ict (1).txt', 'r') as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
chars = text

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(chars))
