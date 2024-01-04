import random
from string import ascii_lowercase
first_array=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(first_array)
print("The array gets shuffled to become:",first_array)

second_array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=input("Enter the word:")
encrypt = []
for i in word:
    # Find the index of the element
    letter1=second_array.index(i)
    #put the index in first_array (to print each letter)
    letter2=first_array[letter1]
    encrypt.append(letter2)
    print(i,letter1,letter2)
for j in encrypt:
    print(second_array[j], end='')
    
