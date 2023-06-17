with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
# Считываем все строки из исходного файла
    lines = f_in.readlines()
# Ищем слова, начинающиеся с согласных букв, в каждой строке и записываем их в результирующий файл
for n, line in enumerate(lines):
# Разделяем строку на слова, используя пробел в качестве разделителя
    words = line.split()
# Ищем слова, начинающиеся с согласных букв, и записываем их в результирующий файл
    for word in words:
# Получаем первую букву слова, используя метод lower() для приведения буквы к нижнему регистру
        first_letter = word[0].lower()
        if first_letter not in 'aeiouy' and word.isalpha():
            f_out.write('Строка {} : {}\n'.format(n + 1, word))
