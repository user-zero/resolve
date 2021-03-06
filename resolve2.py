#!/usr/bin/python

from sys import argv 
import socket
from time import time

script, filename = argv

unresolved_hosts = {}
counter = 0
with open(filename) as f:
	for line in f:
	unresolved_hosts
	

def resolve_slow(hosts):
    """
    Given a list of hosts, resolves them and returns a dictionary
    containing {'host': 'ip'}.
    If resolution for a host failed, 'ip' is None.
    """
    resolved_hosts = {}
    for host in hosts:
        try:
            host_info = socket.gethostbyname(host)
            resolved_hosts[host] = host_info
        except socket.gaierror, err:
            resolved_hosts[host] = None
    return resolved_hosts

if __name__ == "__main__":
    host_format = "www.domain%d.com"
    number_of_hosts = 1000

    hosts = [host_format % i for i in range(number_of_hosts)]

    start = time()
    resolved_hosts = resolve_slow(hosts)
    end = time()

    print "It took %.2f seconds to resolve %d hosts." % (end-start, number_of_hosts)