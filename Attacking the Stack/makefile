CC=gcc
OBJ=flawed-program.o

CC_FLAGS=-O0 -no-pie -m32 -g -z execstack -fno-stack-protector -fno-builtin

%.o: %.c
	$(CC) -c -o $@ $< $(CC_FLAGS)

main: $(OBJ)
	$(CC) -o flawed-program flawed-program.o $(CC_FLAGS) $(ALT_CC_FLAGS)


clean:
	rm *.o flawed-program
	rm -rf a.out core

