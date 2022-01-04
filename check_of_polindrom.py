input_string = 'sos'

def is_polindrom(input_text:str):
	if input_text is not None:
		format_string = input_text.strip().lower()
		if format_string.isdigit():
			print('Text have a digit')
		else:
			if format_string == format_string[::-1]:
				print('The text is polindrom')
			else:
				print('The text is not polindrome')
	else:
		print('Text is empty')

print(is_polindrom(input_string))