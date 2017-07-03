# Exercício 3

#### Nome: Ricardo Zaideman Charf
#### RA: 151238

### Hello World

Para me familiarizar com o simulador, escrevi o pequeno arquivo em c, `hello.c`:

```c
#include<stdio.h>

int main(){
  printf("Hello MC723\n");
  return 0;
}
```
Como parte da pré-atividade, adicionei um contador de instruções ADD,ADDI e ADDU, no arquivo `mips_isa.cpp`:

```c++
(...)
int addCounter = 0;
(...)
void ac_behavior( addi )
{
(...)
  addCounter++;
};
(...)
void ac_behavior( addu )
{
(...)
  addCounter++;
};
(...)
void ac_behavior( add )
{
(...)
  addCounter++;
};
(...)
```

E foi adiconada alinha a seguir, na função `void ac_behavior(end)`, para printar a contagem total de intruções ADD:

``` c++
printf("[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas %d vez(es).\n", addCounter);
```
