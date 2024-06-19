
fileread= 'demo.txt'

file = open(fileread, 'r')

file_content = file.read()
print("Content of the file:\n", file_content)

file.close()
