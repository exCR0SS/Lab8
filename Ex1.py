# Считываем первую строку и записываем ее в результирующий файл
with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
    line1 = f_in.readline()
    f_out.write(line1)
    line2 = f_in.readline()
    words = line2.split()

# Записываем вторую строку в результирующий файл, пропуская отрицательные числа
for word in words:
    try:
        num = float(word)
        if num > 0:
            f_out.write(word + ' ')
    except ValueError:
        f_out.write(word + ' ')
        f_out.write('\n')
    # Считываем оставшиеся числа и записываем в результирующий файл
    numbers = f_in.readline()
    f_out.write(numbers)