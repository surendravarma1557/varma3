# varma3
n = raw_input()
if(n >= 'a'and n <= 'z') or (n >= 'A' and n <= 'Z'):
	if n in['a','e','i','o','u','A','E','I','O','U']:
		print('Vowel')
	else:
		print('Consonant')
else:
	print('Invalid')
