number_1=int(input('enter any number you want its multiplication table \n'))
limit_1=int(input('enter the number you want the mutiplication table to end\n'))
print(f'THE MULTIPLICATION TABLE OF  {number_1} FROM 0 TO {limit_1}\n')
for i in range(0,limit_1+1):
           result_1= number_1 * i
           print(f' {number_1} * {i} = {result_1}\n')

number_2=int(input('please enter any number you want its division table \n'))
limit_2=int(input('please enter the number you want the division table to end\n'))             
print(f'THE DIVISION TABLE OF {number_2} FROM 1 TO {limit_2}\n')
for i in range(1,limit_2+1):
    result_2= i /number_2
    print(f' {i} / {number_2} = {result_2}\n')
