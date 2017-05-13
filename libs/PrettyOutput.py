import sys, console

def output_good(line):
	console.set_color(0,1,0)
	sys.stdout.write("[+] ")
	console.set_color()
	sys.stdout.write(line+"\n")

def output_indifferent(line):
	console.set_color(1,1,0)
	sys.stdout.write("[*] ")
	console.set_color()
	sys.stdout.write(line+"\n")

def output_error(line):
	console.set_color(1,0,0)
	sys.stdout.write("[-] !!! ")
	console.set_color()
	sys.stdout.write(line)
	console.set_color(1,0,0)
	sys.stdout.write(" !!!\n")
	console.set_color()

def output_bad(line):
	console.set_color(1,0,0)
	sys.stdout.write("[-] ")
	console.set_color()
	sys.stdout.write(line+"\n")

def output_info(line):
	console.set_color(1,1,1)
	sys.stdout.write("[+] ")
	console.set_color()
	sys.stdout.write(line+"\n")
