# 1)

def unique_in_order(sequence):
    first_world = ''#A
    unique_world = []
    for i in sequence: #B
        if i != first_world: # B != A
            unique_world.append(i)
            first_world = i
        else:
            continue
    return unique_world
print(unique_in_order('AAAkflewlfBSSSBAA'))
# from functools import total_ordering


# 2)

# def find_outlier(integers):
#     total = 0
#     num1 = 0
#     num2 = 0
#     for i in integers:
#         if i % 2 == 0:
#             num1 += 1
#         else:
#             num2 += 1
#     for n in integers:
#         if num1 < num2:
#             for j in integers:
#                 if j % 2 == 0:
#                     total = j
#         else:
#             for o in integers:
#                 if o % 2 != 0:
#                     total = o
#     return total
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

# 3)
# def is_isogram(string):
#     word = ''
#     for i in string:
#         if i == word:
#             return True
#         else:
#             word = i
#             continue
#     return False
# print(is_isogram('AAajnswe'))

# 4)

# def find_it(seq):
#     total = []
#     for i in seq:
#         if i in total:
#             total.remove(i)
#         else:
#             total.append(i)
#     return total
# print(find_it(([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])))

# # 5)
# def high(x):
#     total = 0
#     alphabit = ['a','b','c','d','e','h','i'
#                 ,'j','k','l','m','n','o','p',
#                 'q','r','s','t','u','v','w','x','y','z']
#     for i in x:
#         if i in alphabit:
#             index = alphabit.index(i)
#             total += index+1
#     return total
# print(high('taxi'))




# 6)
#
# def is_prime(num):
#     total = 0
#     if  num > 1:
#         for i in range(1,11):
#             if num % i== 0:
#                 total+=1
#             else:
#                 continue
#         if total >2:
#             return False
#         else:
#             return True
#     else:
#         return False
# print(is_prime(33535681))



# print(33535681 / 7 )
# '''
# soz jaz: ата
# polindroma
#
# soz jaz: мадам
# polindroma
#
# soz jaz: адахан
# polindroma emes
#
# '''

#
# name = input('soz jaz: ')
# if name == name[::-1]:
#     print('polinrdoma')
# else:
#     print('polindroma emes')