numbers = input("Введите числа через пробел:")

List_of_strings=numbers.split()
List_of_numbers=list(map(float,List_of_strings))
List_of_numbers[0],List_of_numbers[-1]=List_of_numbers[-1],List_of_numbers[0]
print(List_of_numbers)
List_of_numbers.append(sum(List_of_numbers[:]))
print(List_of_numbers)