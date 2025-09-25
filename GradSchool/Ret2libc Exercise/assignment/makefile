CC=gcc
OBJ=flawed-program.o getenv.o

CC_FLAGS=-no-pie -m32 -g -z execstack -fno-stack-protector

%.o: %.c
	$(CC) -c -o $@ $< $(CC_FLAGS)

main: $(OBJ)
	$(CC) -m32 -shared -o libgadgets.so -fPIC gadgets.c
	$(CC) -o getenv getenv.o $(CC_FLAGS)
	$(CC) -o flawed-program flawed-program.o $(CC_FLAGS) $(ALT_CC_FLAGS)

clean:
	rm *.o flawed-program getenv *.so
	rm -rf a.out core