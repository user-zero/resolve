from sys import argv 
import socket 
from time import time

script, filename = argv

resolved_hosts = {}
with open(filename) as f:
	for line in f:
	
		try:
			host_info = socket.gethostbyname(line)
			resolved_hosts[line] = host_info
		except socket.gaierror, err:
			resolved_hosts[line] = None
		return resolved_hosts
	
if __name__ == "__main__":
    host_format = "www.domain%d.com"
    number_of_hosts = 1000

    hosts = [host_format % i for i in range(number_of_hosts)]

    start = time()
    resolved_hosts = resolve_slow(hosts)
    end = time()

print "It took %.2f seconds to resolve %d hosts." % (end-start, number_of_hosts)
"""
		print "%r,%r" %(line, socket.gethostbyaddr(line))
		if 'str' in line:
			break
"""