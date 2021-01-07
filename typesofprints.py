num1=10
num2=20
sum1=num1+num2
print('format specfication')
print('addition of %d and %d is %d'%(num1,num2,sum1))

print()

print('f format')
print(f'addition of {num1} and {num2} is {sum1}')

print()

print('. format')
print('addition of {0} and {1} is {2}'.format(num1,num2,sum1))

print()

print('str functions')
print('addition of '+ str(num1)+' and ' +str(num2)+' is '+str(sum1))

print()

print('standard format')
print('addition of',num1,'and',num2,'is',sum1)
