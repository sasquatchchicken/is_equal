#!/usr/bin/env python3

numbers = input('enter your first number \n')
numbers1= input('now enter a second number \n')

def is_equal_to(c, e):
	sum_of_digits = 0
	for digit in str(numbers): #use str() to convert number to a string. 
		sum_of_digits += int(digit) #use int() to convert the string to an integer
	print(sum_of_digits)

	sum_of_digits1 = 0
	for digit in str(numbers1): #use str() to convert number to a string. 
		sum_of_digits1 += int(digit) #use int() to convert the string to an integer
	print(sum_of_digits1)
	if sum_of_digits == sum_of_digits1:
		return True
	if sum_of_digits != sum_of_digits1:
		return False
	return True
print(is_equal_to(numbers, numbers1))
