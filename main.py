import lexico

filename = 'input.txt'


def main():
	statements = open(filename).read()
	# print (statements)
	for token in lexico.tokenize(statements):
		print(token)

if __name__ == "__main__":
    main()

