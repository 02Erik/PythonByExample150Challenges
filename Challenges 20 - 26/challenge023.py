#023 

#Ask the user to type in the first  line of a nursery rhyme and display the length of the string.  Ask for a starting number and an  ending number and then display  just that section of the text  (remember Python starts  counting from 0 and not 1). 

rhyme = input('Enter a nursery rhyme: ')
print(len(rhyme))

s_number = int(input('Enter a starting number: '))
e_number = int(input('Énter a ending number: '))

print(rhyme[s_number:e_number])

