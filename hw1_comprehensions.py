#HOMEWORK 1
#COUNT PALINDROMES 


# COUNT PALINDROME WITH ONE STATEMENT CODE

print("Count palindromes using one statement ",
	len(list(
		filter(lambda x: x[::-1] in x,
			(set(open("english").read().split('\n')))
		)
	))
)

#COUNT PALINDROMES WITH MORE READABLE METHOD

def converted_to_array_file(file_name):

	array=set(open(file_name).read().split('\n'))
	return (array)

def reverse_fun(n):
	return n[::-1]


print("Count palindromes using more readable method",
	len(list(filter(lambda x: reverse_fun(x) in x, converted_to_array_file("english"))))
)
