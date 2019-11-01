#!/bin/bash/env python3
import readline
import sys

def red(skk): print("\033[91m {}\033[00m" .format(skk)) #red for negatives
def green(skk): print("\033[92m {}\033[00m" .format(skk)) #green for positives

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def multi(a, b):
	return a * b

def divide(a, b):
	return a / b

def mod(a, b):
	return a % b

#hashtable
operators = {
	'+': add,
	'-': sub,
	'*': multi,
	'/': divide,
	'%': mod
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		'''
		if token == '+':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
			print((lambda: green(result), lambda: red(result)) [result < 0] ())
		elif token == '-':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 - arg2
			stack.append(result)
			print((lambda: green(result), lambda: red(result)) [result < 0] ())
		elif token == '*':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 * arg2
			stack.append(result)
			print((lambda: green(result), lambda: red(result)) [result < 0] ())
		elif token == '/':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 / arg2
			stack.append(result)
			print((lambda: green(result), lambda: red(result)) [result < 0] ())
		elif token == '%':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 % arg2
			stack.append(result)
			print((lambda: green(result), lambda: red(result)) [result < 0] ())
		else:
			stack.append(int(token))
		#print(stack)
		'''
	if len(stack) != 1:
		raise TypeError
	return stack.pop()

def main():
	try:
		while True:
			calculate(input("\033[1;36;40m INPUT: "))
	except ValueError:
		print("Input two integers then an operation")
		sys.exit()
	except EOFError:
		print("You terminated the program")
		sys.exit()
	except TypeError:
		print("Malformed input: input two integers then an operation")
		sys.exit()
	except:
		print("An error occured...")
		sys.exit()
	return

if __name__ == '__main__':
	main()
