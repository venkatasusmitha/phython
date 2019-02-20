def do_stuff(input):
	s, op, m = [s for s in input.split(" ")]
	if op == '/':
		print(int(s) / int(m))
	else:
		print(int(s) % int(m))
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
