# Challenge 1
# user =int(input("enter a number: "))
# lenght= int(input("the length of the list: "))
# multiple_list=[]
# for num in range(lenght):
#     multiple_list.append(user*(num+1))

# print(multiple_list)

# Challenge 2
user_word = input("enter a word : ")
new_word=""
for word in range(len(user_word)):
    if word == 0:
        new_word += user_word[word]
    elif user_word[word] != user_word[word - 1]:
        new_word += user_word[word]

print(f"Word without duplicate: {new_word}")

# word = input("Enter a word: ")
# new_word = ""
# for i in range(len(word)):
#   if i == 0 or word[i] != word[i-1]:
#     new_word += word[i]
# print(f"Word without duplicate: {new_word}")



