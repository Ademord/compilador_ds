import csv
import collections
import re
import drawings


rules = [
		(1,'$accept', ''),
		(2, 'p', 'render'),
		(7, 's', 'note'),
		(6, 's', 'message'),
		(6, 's', 'extended-loop'),
		(5, 's', 'simple-loop'),
		(9, 's', 'extended-alt'),
		(6, 's', 'simple-alt'),
		(2, 'ss', ''),
		(1, 'ss', ''),
		(3, 'tit', 'title')
]
Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])
comments = False
with open('parsing-table.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	reader = (list(reader))

def analyze(tokens):
	stack = []
	estate = 0
	stack.append(("$end", estate))
	last = True
	for t in tokens:
		
		if(comments): print(estate, ':', t.typ)
		if reader[estate][t.typ] != '':
			#leemos la accion que nos indica el estado + token leido
			action = reader[estate][t.typ]
			while 'r' in action:
				#rule number: regla de reduccion
				rule_number = int(re.findall('\d+', action)[0]) 
				#rule
				rule = rules[rule_number]

				if(comments): print("before: ", stack)
				if(comments): print("rule ", rule_number, ":", rule)
				#ejecutar reduccion
				stack = stack[:-rule[0]]
				#semantic
				func = rule[2]
				drawings.dispatcher[func]()

				#estado cabeza de la pila (estado despues de reducir)
				estate = stack[-1][1]
				#next state en la tabla segun el estado de la cabeza de la pila
				next_state = int(reader[estate][rule[1]])
				#desplazar el nuevo simbolo
				stack.append((rule[1], next_state))
				#ir al siguiente estado
				if(comments): print("now: ", stack)
				estate = next_state
				#leer action
				action = reader[estate][t.typ]

			if 's' in action:
				estate = int(re.findall('\d+', action)[0])
				stack.append((t.typ,estate, t.value))

		else:
			print("Bad program in line ", t.line, " on value ", t.value)
			return False

	while len(stack):

		#token de movilizacion por que lleamos al final
		t = Token('$end', '$end', 99, 99)			
		#mostramos movimiento entre estados
		if(comments): print(estate, ':', t.typ)
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
		#semantic 
		func = rule[2]
		drawings.dispatcher[func]()
		if (last): 
			last = False
			#ejecutar dibujo

		#estado en que estamos despues de reducir
		estate = stack[-1][1]
		#next state
		next_state = int(reader[estate][rule[1]])
		#igualamos
		estate = next_state
		#desplazamos
		stack.append((rule[1],estate))
		if(comments): print(stack)


