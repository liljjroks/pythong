def math_func(a, b, func):
	if (func == 'add'):
		return a + b
	elif (func == 'sub'):
		return a - b
	elif (func == 'mul'):
		return a * b
	elif (func == 'div'):
		return a / b
	else:
		print('Fuck you cunt')
x  = int(input('Enter the first number: '))
op = str(input('Operation? (add/sub/mul/div)'))
y  = int(input('Enter the second number: '))
print(math_func(x, y, op))
