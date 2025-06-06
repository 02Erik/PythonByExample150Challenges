# 026  

#Pig Latin takes the first consonant of a word,  moves it to the end of the word and adds on an  “ay”. If a word begins with a vowel you just add  “way” to the end. For example, pig becomes igpay,  banana becomes ananabay, and aadvark becomes  aadvarkway. Create a program that will ask the  user to enter a word and change it into Pig Latin.  Make sure the new word is displayed in lower case

word = input('Enter a word: ').lower()

first = word[0]
length = len(word)
rest = word[1:length]

if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
    a = word + 'way'
    print(a)
else:
    a = rest + first + 'ay'
    print(a)
