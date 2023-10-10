
word = input('Enter word ')
print("Original String:", word)
size= len(word)
print("printing only even index charecter")
for i in range(0, size-1,2):
    print("index[",i,"]",word[i])