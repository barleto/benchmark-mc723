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

Com isso, obtivemos a saída:
```
SystemC 2.3.1-Accellera --- Feb 16 2017 14:37:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: hello.mips

ArchC: -------------------- Starting Simulation --------------------

Hello MC723

ArchC: -------------------- Simulation Finished --------------------
[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas 475 vez(es).

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.00 user, 0.00 system, 0.00 real
    Number of instructions executed: 2726
    Simulation speed: (too fast to be precise)

```

### Contagem de instruções

Para contar as instruções, um contador novo foi criado com nome de `instructionCounter`.
Esse contador deve ser incrmentado toda vez que uma instrução executar. Para isso, modifiquei a função `void ac_behavior( instruction )`, que executa toda vez que uma instrução executa, adicionando uma linha de código:

```c++
void ac_behavior( instruction )
{
(...)
  instructionCounter++;
};
```
Com isso, conseguimos contar o número de instruções executadas.

Precisaremos contar também o número de ciclos. para isso, foi criado um outro contador, que chamei de `cycleCounter`. O cycleCounter é incrementado nas funções que executam as intruções do simulador, seguindo a seguinte tabela:

| Categoria de instrução | Ação com cycleCounter |
|------------------------|-----------------------|
| Acesso à memória       | cycleCounter+=10;     |
| Controle (branch/jump) | cycleCounter+=3;      |
| Outras                 | cycleCounter++;       |

O arquivo final `mips_isa.cpp`, com todos os contadores implementados, se encontra [aqui](mips-2.4.0/mips_isa.cpp)

Para finalizar, foram adicionados linhas de output, com as estatísticas necessárias para o exercício:

```c++
void ac_behavior(end)
{
  dbg_printf("@@@ end behavior @@@\n");
  printf("[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas %d vez(es).\n", addCounter);
  printf("[EXERCICIO 3] Ciclos: %.0f\n", cycleCounter);
  printf("[EXERCICIO 3] Instrucoes: %d\n", instructionCounter);
  printf("[EXERCICIO 3] CPI: %.1f\n", cycleCounter/instructionCounter);
}
```

## Avaliação de ciclos e CPI

Com o simulador compilado, é hora de fazer os benchmarks.

### Benchmark 1: Susan Corners

Executando o algoritmo 3 vezes, um para cada entrada diferente, temos o seguinte output:
```
SystemC 2.3.1-Accellera --- Feb 16 2017 14:37:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: susan

ArchC: -------------------- Starting Simulation --------------------

Can't output imageoutput_small.smoothing.pgm.

ArchC: -------------------- Simulation Finished --------------------
[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas 8367053 vez(es).
[EXERCICIO 3] Ciclos: 72218800
[EXERCICIO 3] Instrucoes: 31597495
[EXERCICIO 3] CPI: 2.3

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.62 user, 0.00 system, 0.63 real
    Number of instructions executed: 31597531
    Simulation speed: 50963.76 K instr/s


        SystemC 2.3.1-Accellera --- Feb 16 2017 14:37:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: susan

ArchC: -------------------- Starting Simulation --------------------

Can't output imageoutput_small.edges.pgm.

ArchC: -------------------- Simulation Finished --------------------
[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas 1518319 vez(es).
[EXERCICIO 3] Ciclos: 33688056
[EXERCICIO 3] Instrucoes: 8071711
[EXERCICIO 3] CPI: 4.2

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.16 user, 0.00 system, 0.17 real
    Number of instructions executed: 8071747
    Simulation speed: 50448.42 K instr/s


        SystemC 2.3.1-Accellera --- Feb 16 2017 14:37:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: susan

ArchC: -------------------- Starting Simulation --------------------

Can't output imageoutput_small.corners.pgm.

ArchC: -------------------- Simulation Finished --------------------
[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas 689699 vez(es).
[EXERCICIO 3] Ciclos: 12218663
[EXERCICIO 3] Instrucoes: 3200586
[EXERCICIO 3] CPI: 3.8

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.07 user, 0.00 system, 0.07 real
    Number of instructions executed: 3200624
    Simulation speed: 45723.20 K instr/s

```
O melhor(maior) CPI foi 4.2, o CPI da segunda execução, mesmo essa execução tendo o maior número de instruções em relação à terceira execução.
É possível notar que o CPI e o número de ciclos muda, dependendo da entrada, como era de se esperar.

### Benchmark 2: SHA com input pequeno

Executando SHA, obtive a seguinte saída:
```
SystemC 2.3.1-Accellera --- Feb 16 2017 14:37:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: sha

ArchC: -------------------- Starting Simulation --------------------


ArchC: -------------------- Simulation Finished --------------------
[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas 4980324 vez(es).
[EXERCICIO 3] Ciclos: 33398936
[EXERCICIO 3] Instrucoes: 13175638
[EXERCICIO 3] CPI: 2.5

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.25 user, 0.00 system, 0.26 real
    Number of instructions executed: 13175979
    Simulation speed: 52703.92 K instr/s
```
Esse CPI é o mais baixo que obtive até o momento.

### Benchmark 3: SHA com input grande

Rodando SHA com input grande, obtive:
```
SystemC 2.3.1-Accellera --- Feb 16 2017 14:37:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: sha

ArchC: -------------------- Starting Simulation --------------------


ArchC: -------------------- Simulation Finished --------------------
[EXERCICIO 3] A instrução ADD, ADDI e ADDU foram executadas 51842908 vez(es).
[EXERCICIO 3] Ciclos: 268435456
[EXERCICIO 3] Instrucoes: 137085583
[EXERCICIO 3] CPI: 2.0

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 2.73 user, 0.00 system, 2.75 real
    Number of instructions executed: 137088791
    Simulation speed: 50215.67 K instr/s
```
Em comparação com o SHA de input pequeno, o CPI com input grande piorou(diminuiu). Vale notar tmabém que o número de instruções e ciclos aumentou em relação ao teste com SHA de input pequeno, como era esperado.

## Conclusão
Dentre todos os testes, o algoritmo que obteve maior CPI foi o algoritmo de **susan corners**. Apesar disso, não é possível afirmar que esse algoritmo tem o melhor desempenho em todos os casos, já que seu CPI muda considerávelmente dependendo da entrada. E esse comportamento se repete para o outro algoritmo testado o **SHA**, quando observado o CPI para entradas grandes e pequenas.
