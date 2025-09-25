#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE 5



void smash(char* arg) {
	char buffer[BUF_SIZE];
	strcpy(buffer, arg);
}

int main(int argc, char* argv[]) {
	char* arg = argv[1];
	smash(arg);
	return 0;
}

void uncalled() {

	//string initialisation
    char Mystr[] = "sekkrit stuff!";
    
    puts(Mystr); //writing the string to stdout
    

}

