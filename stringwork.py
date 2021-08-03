#use this code example to substring a string or slice a string

word = "krish.macdonald"

#first char in a string is 0 use the : to get to the last letter
#be aware the last position is the stop position and will not return that char

#this example creates var "kri"
word1 = word[0:3]
#this example creates var "krish"
word2 = word[0:6]
#this example creates var "macdonald"
word3 = word[7:16]

#this prints "kri"
print(word1)
#this prints "krish"
print(word2)
#this prints "Macdonald"
print(word3.capitalize())