text = input("Enter a string:")
original_string = print(text)
#replace
old = input("Enter a character want to replace:")
new = input("Enter new character to replace:")
print("Replaced string:",  text.replace(old,new))
#revese
reverse = print ("Reversed string:",text[::-1])
#palindrome
if text[::-1] == text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#count character
count =list(text)
print("character count:",len(count))

#word frequency
freq = {}
for freq in text:
    frequency =text.split()
print("word cound:",len(frequency))
