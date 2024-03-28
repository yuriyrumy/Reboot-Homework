# Напишіть рекурсивну функцію, буде конвертувати десяткове число у двійкове.

def recursive_dec_to_bin_converter(number: int) -> int:
    if number <= 1:
        return number

    return int(str(recursive_dec_to_bin_converter(number // 2)) + str(number % 2))


result = recursive_dec_to_bin_converter(12)   # 1100
print(result)
