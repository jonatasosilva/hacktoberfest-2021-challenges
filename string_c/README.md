# hacktoberfest-challenges-2021
--

Nesse execício, vamos retomar ou para quem não conhece aprender um pouquinho do C.
C é uma linguagem muito fascinante, que pode mexer direto na memória do seu computador

Nesse execício, iremos trabalhar direto com uma string, por exemplo:

```c
  #include <stdio.h>
  void mostra_palavra(char *s, int i, int f){
  }

  int main(void){
      char *s = "gustavo";
      char *p  = &s[0];
      mostra_palavra(p, 0, 7);
  }
```

No primeiro parâmetro, passamos o ponteiro que aponta para a primeira posição do string.
No segundo parâmetro passamos o primeiro índice e no terceiro parâmetro passamos onde acaba.

Sua missão é terminar de implementar esse código de forma recursiva, boa codificação, e qualquer duvida pode entrar em contato comingo. Pelo github mesmo!



Aqui abaixo tem uma dica de como poderia ser deito usando for

```c
  #include <stdio.h>

  int main(void){
      char *s = "gustavo";
      char *p  = &s[0];


      for(int i=0; i<7; i++){
          printf("%c",*(p+i));
      }
  }
```

Vamos exercitar essa recurção pessoal. :)