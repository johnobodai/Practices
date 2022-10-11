#include <stdio.h>

int main()
{
    int ch;

    printf("Please type in one charater:\n");
    ch = getc( stdin );
    printf("The character you just entered is: %c\n",ch);
    return 0;
}
