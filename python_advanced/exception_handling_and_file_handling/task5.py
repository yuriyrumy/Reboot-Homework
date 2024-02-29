# Реалізуйте програму, яка копіює вміст одного файлу в інший.

file_name1 = 'example_file.txt'
file_name2 = 'example_file3.txt'

read_file1 = open(file_name1, 'r', encoding='utf-8')
contents_file1 = read_file1.readlines()
read_file1.close()

copy_file = open(file_name2, 'w', encoding='utf-8')
copy_file.write(''.join(contents_file1))
copy_file.close()
