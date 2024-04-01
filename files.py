#open(filename ,mode) not recommendable
"""file_handle = open('files.txt', 'r')
print(file_handle.read())
file_handle.close()"""



#using for loop to read many lines
"""file_handle = open('files.txt', 'r')
for content in file_handle:
    print(content)"""

#recommended way
"""with open('files.txt', 'r') as file_handle:
    content = file_handle.read()
    print(content)"""

#file writting
"""with open('files.txt', 'w') as file_handle:
    file_handle.write('added text')

#read from above code
    
with open('files.txt', 'r') as file_handle:
    content = file_handle.read()
    print(content)"""
#the append mode adds text instead of deleting
"""with open('files.txt', 'a') as file_handle:
     file_handle.write('this is append text ')

with open('files.txt', 'r') as file_handle:
     content = file_handle.read()
     print(content)"""
# file seeking to a certain positon

with open('files.txt', 'w') as file_handle:
     file_handle.write('this is appended text ')
     file_handle.seek(0)
     file_handle.write('another added text')

with open('files.txt', 'r') as file_handle:
     content = file_handle.read()
     print(content)



