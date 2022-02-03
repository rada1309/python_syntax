# логически операции


from ast import operator


x = '3'
y = '4'



# x = 3.14
# y = 3.14
# оператор равенсвта
res = x == y


# оператор неравенсвта
res = x != y

# оператор меньше
res =x < y 

# оператор болььше
res =x > y 

# оператор меньше или равно
res =x <= y

 # оператор больше или равно
res =x >= y

# логические операторы (вентили)
var_1 = False
Var_2 = True

# оператор НЕ
res = not var_1

# оператор И (если хоть один элемнет false то всегда false dsqltn)
res = var_1 and Var_2

# орператор ИЛИ (если оба False ,  то будет False)
res =  var_1 or Var_2

#пример комбинации лог операций  и операвторов сравнения
a = 5
b = 3
c = 3
res = ((a > b) and b != c) or (a == c)

# print(res)

# условные операторы
a = -2

# оператор IF - если
# if a != 0:
#    print("равно нулю")

# if not a == 0:
#     print("неравно нулю")

# оператор ELSE иначе
# if a >= 0:
#     print('больше либо ровно нулю') 
# else:
#     print('меньше нуля') 
# оператор elif сокращение else if
char = 'o'
if char =='A':
    res = "literal A"
elif char == 'a':
    res =  "literal a"
elif char =='B':
    res = "literal B"
else:
    res = "other literals"
# print(res)
# калькулятор консольный- пример
num_1 = int(input("введите первое число: "))
num_2 = int(input("введите второе число: "))

operator = input("Введите символ операции: ")

if operator == '+':
    res = num_1 + num_2

elif operator == '-':
    res = num_1 - num_2 
elif operator == '*':
    res = num_1 * num_2
elif operator == '/':
    res = num_1 / num_2
else:
    res = "символ не распознан"
print(f"результат:{res}")