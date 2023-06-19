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

def file_entire_data_split_at_new_line():
	file = open('test.py', 'r')
	lines = file.readlines()
	for line in lines:
		print line,
	file.close()

def file_read_line_by_line():
	file=open('test.py','r')
	print "\nRead file line by line\n"
	while True:
		line=file.readline()
		if line == '':
			break  
		print line,  	
func()
stdio()
run_cmd()
file_read()
file_entire_data_split_at_new_line()
file_read_line_by_line()
