# Data from https://media.time4learning.com/uploads/FourthGradeSpellingWordList.pdf
# data for 9th grade https://www.spelling-words-well.com/9th-grade-spelling-words.html

#open text file in read mode
text_file = open("./all_words.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
# print(data)

answer = []
temp_word = ''

for i in data:
    if i == '\n':
        answer.append(temp_word)
        temp_word = ''
    else:
        temp_word += i
print(answer)