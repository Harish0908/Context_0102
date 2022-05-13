N = int(input('number of elements: '))
user_input = list(map(int, input('enter the elements:').split(',')))
output1 =[]
output2 =[]
if N == len(user_input):
        for number in user_input:
            if (number >= 0):
                output1.append(number)
            else:
                output2.append(number)
        result = output1 + output2
        print(result)
else:
        print("Length of array and the number of elements doesn't match!")
