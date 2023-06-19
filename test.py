import subprocess

def func():
 	 print("Hello from a function")

def stdio():
	value = raw_input("Please enter a string:")
	
	try:
		choice = int(value)
	except:
		print "Enter numbers only"

def run_cmd():
	command = 'sudo -u postgres psql -qAtc "select datname from pg_database;" 2> /dev/null'
	output = subprocess.check_output(command, shell=True)
	output = output.strip()
	print(output)

def file_read():
	file = open('test.py', 'r')
	content = file.read()
	print(content)
	file.close()

def file_read_line_by_line():
	file = open('test.py', 'r')
	lines = file.readlines()
	for line in lines:
		print line,
	file.close()

def file_read_in_chunks():
	print "\nFile read in chunks:-"
	file = open('test.py', 'r') 
	while True: # from   w  w w  .j av a  2  s  .c o  m
   		chunk = file.read(512)       # Read byte chunks: up to 10 bytes 
   		print "chunk: ", chunk
   		if not chunk: 
   			break 
    	print chunk, 
    	
func()
stdio()
run_cmd()
file_read()
file_read_line_by_line()
file_read_in_chunks()
