###### **MC723A**, *1s2017*, IC - UNICAMP
# Projeto 2
### Grupo 14
- Ricardo Zaideman Charf 	- **151238**
- Vitor Marge Eichenberger 	- **149053**
- Guilherme Zanelato		- **119494**

Link para apresentação: [Clique Aqui](https://docs.google.com/presentation/d/1_Q6eZMrHkgLgolFS9ZSB9k_CY57Flvg8wzlQ7WicGgw/edit?usp=sharing)

## Roteiro *(resumido)*
- Será utilizado o software Dinero IV para o teste de software em várias configurações de cache distintas.
- A implementação do Simulador MIPS em archC, também será modificada para ser possível contabilziar hazard em diferentes implementaçes (Tamanho do pipeline: 5 e 9 estágios, processador escalar VS superescalar, etc)
- Sero testados:
  - Tamanho do pipeline: 5 e 9 estágios
  - Processador escalar vs superescalar
  - Hazard de dados e controle
  - Branch predictor
  - Cache (Sendo essa testada a partir do Dinero IV)

##### Pipelines usados como referência

![pipelines](https://www.ecse.rpi.edu/frisc/finalreports/spring95/Image7.gif)

## **Relatório**

### Ferramentas
- DineroIV
- ArchC
- Simulador de MIPS (em ArchC)

### Metodologia
##### Início e Parte Teórica
Primeiramente foram baixadas, instaladas e configuradas todas as ferramentas necessárias ao projeto.

Em seguida foi feita uma revisão sobre processadores, pipelines e suas características, focando em relembrar os conceitos para garantir coerência e validade ao projeto, seus dados e resultados. Dentre muitos pontos que vimos nesta etapa, consideramos importante destacar algumas informações sobre **_Hazards_**

##### Observações sobre **_Hazards_**
Tipos de hazards e suas ocorrências:
* <b>RAW</b> - ocorre independente do processador ser escalar ou superescalar
* <b>WAR</b> - não ocorre em nenhum caso estudado
* <b>WAW</b> - ocorre apenas quando há concorrência, ou seja, somente nos processadores superescalares

fonte: <a href="https://en.wikipedia.org/wiki/Hazard_(computer_architecture)">Wikipédia - seção sobre hazards</a>

##### Parte Prática
Adaptação do código fonte do mips (do simulador) que não possui muitas funcionalidades desejadas para as análises:
- Pipeline, com diferentes tamanhos
- Branch Predictor
- Hazards (de controle e de dados)
- Pipeline Superescalar

Além é claro de todas as implementações necessárias para gerarem estatísticas e registros dos eventos a serem analisados.

Este código se encontra na pasta raiz deste projeto: **mips_isa.cpp** para visualização mais fácil. Há outra cópia do código que é usado pelo simulador na pasta do simulador: mips-2.4.0

As configurações foram feitas por código (através da biblioteca em **C** *configMIPS.h*) com a parte mais interna, relacionada majoritáriamente ao pipeline, e pelo DineroIV (através de seus parâmetros de execução) relativa à memória/cache. Dispondo-se assim das seguintes configurações:
* configMIPS.h
	- Nome do *trace* a ser executado
	- Gerar *traces* ou não
	- Uso de *fowarding* ou não
	- Se *superescalar* ou não
	- *Branch Predictor* ativo ou não
	- Tamanho do *pipeline*
* DineroIV
	- Quantidade de *traces* a executar
	- Tamanho das caches, seus blocos e associatividade

Também foi feito um script em *Python* para formatar e gerar dados a partir da saída do *simulador MIPS* e do *DineroIV*. Este script é também capaz de mudar algumas das configurações.

Por fim tudo isto foi compilado e executado, gerando os dados que - foram melhor organizados numa tabela e - proporcionaram a análise que se encontra adiante.

### Configurações
Os atributos usados para montar as configurações de arquitetura foram:
* <b>Pipeline</b>
	- *Tamanho*: **5** e **9**
	- *Fowarding*: **com** e **sem**
	- *Concorrência*: **escalar** e **superescalar**
	- *Branch Predictor*: **Always not taken** e **1 bit**
* <b>Cache</b>
	- Quantidade de *traces* a executar: fixo em 20
	- Veja a tabela a seguir

##### Cache
As configurações de cache avaliadas serão as mostradas na tabela abaixo.

| Configuração | L1usize| L1block | Associatividade L1 | L2usize | L2block | Associatividade L2 |
|:------------:|:------:|:-------:|:------------------:|:------:|:-------:|:------------------:|
|    Cache 1   |   32   |    64   |          2         |   256  |   1024  |          2         |
|    Cache 2   |   128  |   128   |          2         |  1024  |   2048  |          4         |

Por fim usaremos as seguintes configurações:
#### Configurações Usadas

| Configuração |     Tipo     | Fowarding | Branch Predictor |
|:------------:|:------------:|:---------:|:----------------:|
|**5 estágios**|              |           |                  |
|      C5a     |    Escalar   |    NÃO    | Always not taken |
|      C5b     |    Escalar   |    SIM    |       1 bit      |
|      C5c     | Superescalar |    SIM    |       1 bit      |
|**9 estágios**|              |           |                  |
|      C9a     |    Escalar   |    NÃO    | Always not taken |
|      C9b     |    Escalar   |    SIM    |       1 bit      |
|      C9c     | Superescalar |    SIM    |       1 bit      |

**OBS:** Todas as configurações acima serão testadas com todas as configurções de cache.
Ex: C5a será rodada para cada um das 2 configurações de cache, resultando nas configurações C5a1 e C5a2 respecivamente.

### Resultados

| Config         | C5a1     |          | C5a2     |          | C5b1     |          | C5b2     |          | C5c1     |          | C5c2     |          | C9a1     |          | C9a2     |          | C9b1     |          | C9b2     |          | C9c1     |          | C9c2     |          |
|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Programa       | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    | bitcount | qsort    |
| L1 Miss        | 612      | 49069    | 320      | 22874    | 612      | 49069    | 320      | 22874    | 612      | 49069    | 320      | 22874    | 612      | 49069    | 320      | 22874    | 612      | 49069    | 320      | 22874    | 612      | 49069    | 320      | 22874    |
| L2 Miss        | 117      | 2768     | 81       | 353      | 117      | 2768     | 81       | 353      | 117      | 2768     | 81       | 353      | 117      | 2768     | 81       | 353      | 117      | 2768     | 81       | 353      | 117      | 2768     | 81       | 353      |
| Branch Stalls  | 171651   | 3012852  | 171651   | 3012852  | 205722   | 1131408  | 205722   | 1131408  | 205722   | 1131408  | 205722   | 1131408  | 286085   | 5021420  | 286085   | 5021420  | 342870   | 1885680  | 342870   | 1885680  | 342870   | 1885680  | 342870   | 1885680  |
| Branch Hazards | 57217    | 1004284  | 57217    | 1004284  | 68574    | 377136   | 68574    | 377136   | 68574    | 377136   | 68574    | 377136   | 95361    | 1673806  | 95361    | 1673806  | 114290   | 628560   | 114290   | 628560   | 114290   | 628560   | 114290   | 628560   |
| Data Stalls    | 217098   | 10467700 | 217098   | 10467700 | 0        | 0        | 0        | 0        | 15874    | 372125   | 15874    | 372125   | 740555   | 26285599 | 740555   | 26285599 | 0        | 0        | 0        | 0        | 15874    | 372125   | 15874    | 372125   |
| Data Hazards   | 147324   | 7325664  | 147324   | 7325664  | 0        | 0        | 0        | 0        | 15874    | 372125   | 15874    | 372125   | 299766   | 8097094  | 299766   | 8097094  | 0        | 0        | 0        | 0        | 15874    | 372125   | 15874    | 372125   |
| Ciclos         | 920006   | 33068732 | 920006   | 33068732 | 736979   | 20719588 | 736979   | 20719588 | 487224   | 11297623 | 487224   | 11297623 | 1443463  | 48886631 | 1443463  | 48886631 | 736979   | 20719588 | 736979   | 20719588 | 555798   | 11674759 | 555798   | 11674759 |
| Instruções     | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 | 531257   | 19588180 |
| CPI            | 1.73     | 1.69     | 1.73     | 1.69     | 1.39     | 1.06     | 1.39     | 1.06     | 0.92     | 0.58     | 0.92     | 0.58     | 2.72     | 2.50     | 2.72     | 2.50     | 1.39     | 1.06     | 1.39     | 1.06     | 1.05     | 0.60     | 1.05     | 0.60     |
| tempo aprox | 996326 | 35220222 | 971806 | 33509272 | 813299 | 22871078 | 788779 | 21160128 | 563544 | 13449113 | 539024 | 11738163 | 1519783 | 51038121 | 1495263 | 49327171 | 813299 | 22871078 | 788779 | 21160128 | 632118 | 13826249 | 607598 | 12115299 |

Medidas obtidas indiretamente:
- `CPI = Ciclos / Instruções`
- `tempo aprox = ciclos + (L1Miss x 10) + (L2Miss x 600)`

A seguir algumas tabelas com os resultados apenas dos melhores e piores para cada programa.

##### Ordenado por tempo de execução aproximado

| Config      | C5c2     | C9a1     | C5c2     | C9a1     |
|-------------|----------|----------|----------|----------|
| Programa    | bitcount | bitcount | qsort    | qsort    |
| tempo aprox | 539024   | 1519783  | 11738163 | 51038121 |

##### Ordenado por Programa e Branch Stalls

| Config        | C5a2     | C9b1     | C5c2    | C9a1    |
|---------------|----------|----------|---------|---------|
| Programa      | bitcount | bitcount | qsort   | qsort   |
| Branch Stalls | 171651   | 342870   | 1131408 | 5021420 |

##### Ordenado por CPI

| Config   | C5c2     | C9a1     | C5c2  | C9a1  |
|----------|----------|----------|-------|-------|
| Programa | bitcount | bitcount | qsort | qsort |
| CPI      | 0.92     | 2.72     | 0.58  | 2.50  |

### Análise e Conclusões
A partir dos dados obtidos acima fizemos as seguintes conclusões:
- A arquitetura do processador não influi na taxa de acerto a memória
- Analisando em ordem crescente por tempo aproximado de execução vemos que
	- configu de proc > pipeline size > cache setting
	- A ordem de influencia dos atributos é: Configurações do Processador, Tamanho do Pipeline e por fim as configurações da cache (menos importante)
	- A melhor configuração por nós analisada foi
		- Superescalar
		- Com fowarding
		- Com Branch Predictor
		- 5 estágios
		- Configuração de Cache 2 (veja tabela de caches)
	- A pior configuração por nós analisada foi
		- Escalar
		- Sem fowarding
		- Sem Branch Predictor
		- 9 estágios
		- Configuração de Cache 1 (veja tabela de caches)
- Notamos que as configurações de cache continuam tendo mesmo impacto que nos exercícios anteriores (maior memoria, bloco e associatividade trazem melhores resultados), porém não são tão influentes quanto a configuração do processador, pelo menos nos casos analisados.
- O tamanho do pipeline parece ser prejudicial, no sentido em que ao aumentá-lo pioramos o tempo de execução, já que quando um stall acontece temos mais ciclos perdidos devido à maior quantidade de estágios.
- Quanto ao Branch Predictor notamos que seu impacto é variável, nem sempre ele beneficiou: no qsort seu uso melhorava o desempenho, porém no bitcount ele piorava
- Fowarding é algo com um impacto positivo notável
- Superescalar melhora o CPI, ou seja, reduz o número de ciclos por instrução
