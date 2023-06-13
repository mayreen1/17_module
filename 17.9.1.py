list = [int(x) for x in input("Введите числа от 1 до 100 в любом порядке, через пробел: ").split()]

def merge_sort(list):  # "разделяй"
    if len(list) < 2:  # если кусок массива равен 2,
        return list[:]  # выход из рекурсии
    else:
        middle = len(list) // 2  # ищем середину
        left = merge_sort(list[:middle])  # рекурсивно делим левую часть
        right = merge_sort(list[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(list))


def binary_search(list, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if list[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < list[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(list, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(list, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 100: "))
        if element < 0 or element > 100:
            raise Exception
        break
    except ValueError:
        print("Введите число")
    except Exception:
        print("Неверный диапазон чисел")


print(binary_search(list, element, 0,  len(list)))