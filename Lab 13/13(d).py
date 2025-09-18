#Bahopiya Dhaval
with open(r'C:\Users\student\Downloads\ict (1).txt', 'r') as f1, open(r'C:\Users\student\Downloads\Dhaval.txt', 'r') as f2, open('merged.txt', 'w') as fout:
    fout.write(f1.read())
    fout.write(f2.read())
