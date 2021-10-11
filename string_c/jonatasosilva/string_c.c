#include <stdio.h>

void mostra_palavra(char *s, int i, int f)
{
    if (i == f) return;

    printf("%c",*(s+i));
    mostra_palavra(s, ++i, f);
}

int main(void)
{
    char *s = "gustavo";
    char *p = &s[0];
    mostra_palavra(p, 0, 7);
}