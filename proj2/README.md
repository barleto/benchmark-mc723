# Projeto 2
### Grupo 14
- Ricardo Z Charf 151238
- Vitor Marge Eichenberger 149053
- Guilherme **PREENCHER DADOS DO GUILHEREME AQUI!!**

## TODO:
Esta seção serve somente para o grupo se orientar e **deverá ser apagada** antes da submissão final do projeto.

- [ ] Escolher configurações das simulações
- [ ] Atualizar arquivos das simulações
	- [ ] Arquivos de trace
	- [ ] Arquivo do mips **.cpp**
- [ ] Compilar tudo
- [ ] Rodar testes
- [ ] Redigir relatório

## Roteiro

### Metodologia

- Será utilizado o software Dinero IV para o teste de software em várias configurações de cache distintas.
- A implementação do Simulador MIPS em archC, também será modificada para ser possível contabilziar hazard em diferentes implementaçes (Tamanho do pipeline: 5, 7 e 13 estágios, processador escalar VS superescalar, etc)
- Sero testados:
  - Tamanho do pipeline: 5, 7 e 13 estágios
  - Processador escalar vs superescalar
  - Hazard de dados e controle
  - Branch predictor
  - Cache (Sendo essa testada a partir do Dinero IV)



# Roteiro do Guilherme - **ATUALIZAR!!**

## Roteiro

Nesse projeto iremos análisar o a diferença causada no desempenho de um processador dadas diversas configurações.
Usaremos os seguintes programas disponibilizados na box do Vagrant para a execução do Benchmark.
* jpeg
* dijkstra
* FFT


## Desenvolvimento

### 1 etapa - Pipeline

Iremos estudar diversas características da arquitetura de um processador, iremos começar análisando o impacto causado pelo tamanho do pipeline. Executaremos nosso benchmark primeiramente considerando a execução sem pipeline e depois com tamanhos 5, 7 e 13 fazendo alterações no simulador para captarmos a diferença na quantidade de cliclos total.


### 2 etapa - Escalar x Superescalar

Para análisar a concorrência entre intruções para múltiplos pipelines, podemos percorrer a sequência de instruções e verificar as dependências entre elas, já que podem ser executadas no mesmo estágio do pipeline.
Definimos então um pipeline de tamanho 5, e analisamos as instruções duas a duas, verificando pontos em que potencialmente haveria conflitos com a concorrência. Nesse caso, é contabilizado o atraso gerado pelo problema em questão.


### 3 etapa - Hazard de dados e controle

Nessa etapa, com um tamanho de pipeline fixado, também iremos realizar alterações no simulador para mantermos um histórico das instruções executadas e determinar quando um hazard acontece e considerar a quantidade de ciclos necessários para a resolução do Hazard na contagem de ciclos total para a execução.
Hazards que podem ser resolvidos com forward não irão impactar a contagem de ciclos. Para hazard de dados vamos considerar hazards do tipo RAW, WAW e WAR e para hazard de controle vamos análisar o atraso em número de ciclos causados pelo branch.


### 4 etapa - Branch prediction

Vamos utilizar as seguintes técnicas de branch predictor:
O desvio sempre acontece.
O desvio nunca acontece.
Além disso, adotaremos o uso do caso sem nenhum tratamento de branch predictor.
Para a análise, podemos percorrer as instruções geradas para o programa e, caso ocorra uma instrução de salto, verificamos se o caso se encaixa ou não na previsão do método em questão. Para cada verificação, incrementamos o número de ciclos necessários, caso haja algum tipo de atraso.


### 5 etapa - Cache

Iremos tentar utilizar o software Dinero como biblioteca (ainda não tivemos contato com o software no modo de biblioteca) e incluir sua chamada no código do simulador quando operamos com a memória. Iremos passar o endereço de memória e descobrir onde esse dado esta alocado e obeter o tempo em ciclos necessários para acessar esse dado para cada configuração de cache.
Iremos escolher 4 configurações diferentes de cache baseado nos resultados do exercício 2;

**Configurações**
* Sem Pipeline
* Com pipeline de 5,7 e 13 estágios
* Superescalar de 5 estágios
* Pipeline de 5 estágios com duas implementações diferentes de branch predictor
* Pipeline de 5 estágios com melhor resultado do branch predictor e melhor configuração de memória

Vamos determinar a melhor configuração para cada programa executado, e executar todos os programas com cada configuração.
