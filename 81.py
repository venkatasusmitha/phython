def do_stuff(input):
	s,m = [int(z) for z in input.split(" ")]
	print(m-s)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
