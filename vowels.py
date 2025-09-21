vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
word = input("enter a word:")
for w in word:
    print(w)
    if w in vowels:
        vowels[w] += 1
print(vowels)
