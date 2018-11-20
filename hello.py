def hello():
	i = 10
	print("Hello world: ", i)
	
def print_file(file_name):
	f = open(file_name, "r")
	lines = f.readlines()
	for line in lines:
		print(line)
	f.close()

def write_file(file_name):
	print("into file")
	f = open(file_name, "w+")
	f.write("hello")
	f.write("\tworld\n")
	f.write("new line")
	f.close()
	
if __name__ == '__main__':
	import sys
	hello()
	print("===========file content is====================")
	print_file(sys.argv[1])
	write_file(sys.argv[2])