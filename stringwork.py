#use this code example to substring a string or slice a string

word = "krish.macdonald"

#first char in a string is 0 use the : to get to the last letter
#be aware the last position is the stop position and will not return that char

#this example creates var "kri"
word1 = word[0:3]
#this example creates var "krish"
word2 = word[0:5]
#this example creates var "macdonald"
word3 = word[6:16]

#source variable
print("This is the base data:",word)
#this prints "kri"
print("This takes the first 3 characters:",word1)
#this prints "krish"
print("This takes the first 5 characters:",word2)
#this prints "Macdonald"
print("This takes the characters 7 through 15:",word3.capitalize())