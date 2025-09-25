#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SIZE 32

typedef void (*func_ptr)();

typedef struct {
    func_ptr function;
} pointer_t;

void print_smiley_face()
{
    printf("I win :-)\n");
}

void print_frowny_face()
{
    printf("I lose :-(\n");
}

int main(int argc, char** argv)
{
    
    char *a = malloc(BUFFER_SIZE);

    pointer_t *b = malloc(sizeof(pointer_t));

    b->function = print_frowny_face;

    strcpy(a, argv[1]);

    b->function();

    free(b);
    free(a);

    return 0;
}