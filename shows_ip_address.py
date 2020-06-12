# find ip addresss of machine
from socket import gethostbyname
from socket import gethostname

ipaddress = gethostbyname('')
print(ipaddress)

ipaddress = gethostbyname('www.google.co.in')
print(ipaddress)

hostname = gethostname()
ipaddress = gethostbyname(hostname)
print(ipaddress)