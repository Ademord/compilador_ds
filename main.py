import lexico
import sintactico
filename = 'input.txt'


def main():
	statements = open(filename).read()
	tokens = list(lexico.tokenize(statements))
	sintactico.analyze(tokens)


if __name__ == "__main__":
    main()

