numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)



def sum(num1, num2, num3):
    return(num1 + num2 + num3)


print(sum(1, 2, 3))



sum = lambda num1, num2, num3: (num1 + num2 + num3)


print(sum(1, 2, 3))



name_list = ['Jessica', 'Paul', 'George', 'Henry', 'Adam']

for name in name_list:
    if name == 'Henry':
        print('Match')
    else:
        print('Not a match')
