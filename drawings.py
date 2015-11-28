
def render():
	print("syncing drawing with browser")
def note():
	print("draw a note!")
def message():
	print("draw a message!")
def extended_loop():
	print("draw an extended_loop!")
def simple_loop():
	print("draw a simple_loop!")
def extended_alt():
	print("draw an extended_alt!")
def simple_alt():
	print("draw a simple_alt!")
def title():
	print("draw a title!")
def default():
	return

dispatcher = {	
				'render': render, 
				'note': note,
				'message': message,
				'extended-loop': extended_loop,
				'simple-loop': simple_loop,
				'extended-alt': extended_alt,
				'simple-alt': simple_alt,
				'title': title,
				'': default
			}