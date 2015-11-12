import csv
import collections
import re
rules = [
		(1,'$accept'),
		(2, 'p'),
		(7, 's'),
		(6, 's'),
		(6, 's'),
		(5, 's'),
		(9, 's'),
		(6, 's'),
		(2, 'ss'),
		(1, 'ss'),
		(3, 'tit')
]
Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

with open('parsing-table.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	reader = (list(reader))

def analyze(tokens):
	stack = []
	estate = 0
	stack.append(("$end", estate))
	
	for t in tokens:
		
		print(estate, ':', t.typ)
		if reader[estate][t.typ] != '':
			#leemos la accion que nos indica el estado + token leido
			action = reader[estate][t.typ]
			while 'r' in action:
				#rule number: regla de reduccion
				rule_number = int(re.findall('\d+', action)[0]) 
				#rule
				rule = rules[rule_number]
				print("rule ", rule_number, ":", rule)
				#ejecutar reduccion
				stack = stack[:-rule[0]]
				#estado cabeza de la pila (estado despues de reducir)
				estate = stack[-1][1]
				#next state en la tabla segun el estado de la cabeza de la pila
				next_state = int(reader[estate][rule[1]])
				#desplazar el nuevo simbolo
				stack.append((rule[1], next_state))
				#ir al siguiente estado
				print("now: ", stack)
				estate = next_state
				#leer action
				action = reader[estate][t.typ]

			if 's' in action:
				estate = int(re.findall('\d+', action)[0])
				stack.append((t.typ,estate))

		else:
			print("Bad program in line ", t.line, " on value ", t.value)
			return False

	while len(stack):

		#token de movilizacion por que lleamos al final
		t = Token('$end', '$end', 99, 99)			
		#mostramos movimiento entre estados
		print(estate, ':', t.typ)
		#leemos la accion
		action = reader[estate][t.typ]
		#vemos si estamos en un programa aceptado
		if (action == 'a'):
			print("Felicidades su programa ha sido aceptado!")
			return True
		#regla
		rule_number = int(re.findall('\d+', action)[0])
		#ubicamos regla
		rule = rules[rule_number]	
		#reducimos
		stack = stack[:-rule[0]]
		#estado en que estamos despues de reducir
		estate = stack[-1][1]
		#next state
		next_state = int(reader[estate][rule[1]])
		#igualamos
		estate = next_state
		#desplazamos
		stack.append((rule[1],estate))
		print(stack)


