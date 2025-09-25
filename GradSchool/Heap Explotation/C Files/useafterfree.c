#include <stdlib.h>

int main(int argc, char** argv) 
{
    char *a = malloc(300);
    char *b = malloc(250);

    free(a);

    char *c = malloc(300);
}