#!/bin/bash/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		if token == '+':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 - arg2
			stack.append(result)
		elif token == '*':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 * arg2
			stack.append(result)
		elif token == '/':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 / arg2
			stack.append(result)
		else:
			stack.append(int(token))
		#print(stack)
	if len(stack) != 1:
		raise TypeError('Malformed input: ' + arg)
	return stack.pop()

def main():
	while True:
		calculate(input('rpn calc> '))
	return

if __name__ == '__main__':
	main()
