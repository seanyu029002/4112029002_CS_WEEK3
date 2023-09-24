import os
import time

items = os.listdir('CS')
  
a = os.path.exists('CS/test.txt')  

print(a)
    
for item in items:
    print(item)  
        
file = open('CS/test.txt', 'r', encoding="UTF-8")
content =  file.read()
print(content)

file_size = os.path.getsize('CS/test.txt')
print(file_size)

modification_time = os.path.getmtime('CS/test.txt')
print(modification_time)

formatted_time = time.ctime(modification_time)
print(formatted_time)

os.rmdir('CS')