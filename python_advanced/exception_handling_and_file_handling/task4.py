# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст, виводячи рядки, які є у першому файлі,
# але відсутні у другому.

file_name1 = 'example_file.txt'
file_name2 = 'example_file2.txt'

read_file1 = open(file_name1, 'r', encoding='utf-8')
contents_file1 = [word.strip('\n') for word in read_file1.readlines()]
read_file1.close()

read_file2 = open(file_name2, 'r', encoding='utf-8')
contents_file2 = [word.strip('\n') for word in read_file2.readlines()]
read_file2.close()

for line in contents_file1:
    if line not in contents_file2:
        print(line)
