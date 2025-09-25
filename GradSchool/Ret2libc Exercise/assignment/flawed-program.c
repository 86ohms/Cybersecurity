#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <sys/stat.h>

#define BUF_SIZE 5

void smash(char* arg) {
	char buffer[BUF_SIZE];
	strcpy(buffer, arg);
}

void load(void) {
	struct stat st;
	stat("./libgadgets.so", &st);
	int fd = open("./libgadgets.so", 0, 00);
	mmap((void*) 0x30000000, st.st_size, PROT_READ, 17, fd, 0);
}

int main(int argc, char* argv[]) {
	char* arg = argv[1];
	load();
	smash(arg);
	return 0;
}

