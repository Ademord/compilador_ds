import lexico
import sintactico
filename = 'input.txt'


def main():
	statements = open(filename).read()
	tokens = list(lexico.tokenize(statements))
	
	if tokens[-1].typ != 'NEWLINE':
		statements+='\n'
		tokens = list(lexico.tokenize(statements))
	'''
	for token in tokens:
		print(token)
	return
	'''
	sintactico.analyze(tokens)


if __name__ == "__main__":
    main()

