#include <stdio.h>
#include <stdlib.h>

void main()
{
    char* shell = getenv("MYSHELL");
    char* argv_0 = getenv("MY_ARGV_0");
    char* argv_1 = getenv("MY_ARGV_1");

    if (shell)
    {
        printf("%x\n", (unsigned int)shell);
    }
}