# ask the user about his/ her thoughts
prompt = input(f' what\'s on your mind today? \n')

# put the user answer in a string
string=' '
prompt_string= string.replace(string, prompt)

# convert string into a list
word_list = prompt_string.split(' ')

# count the words in the list
count = len(word_list)
    
# tell the user the count of the words
print(f'oh nice, you just told me what\'s on your mind in {count} words!')

