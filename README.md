# UNZIP
## O que faz? Para que serve?
Esse benchmark analisa o desempenho da máquina ao executar um unzip de um arquivo zipado.
Vamos usar unzip, programa de linha de comando nativo do linux e macOS.
## Por que é bom para medir desempenho?
Fazer o unzip de um arquivo grande é intenso para o processador. Com isso mediremos a capacidade do processador.
## O que baixar
Baixe esse repositório. Nele está contido todo o código necessário e o arquivo zipado.
## Como compilar/instalar
Não é necessário compilar nem instalar. O script que vai rodar é em Python. Consideramos que os computadores que rodarem o benchmark terão python instalado pois python vem nos linux instalado por padrão.
## Como executar
Execute o script python na pasta raíz do repositório. O arquivo a ser descompactado é um zip dentro da pasta `/zips`. Caso queiram trocar o arquivo por outro zip lembre-se que o arquivo deve manter o mesmo nome que o arquivo original da pasta.

**Importante:** Para o benchmark funcionar, o teste nos computadores deve ser feito com o mesmo arquivo `.zip`.
## Como medir o desempenho
Como o unzip será feito em máquinas diferentes sempre com o mesmo arquivo, então, uma máquina com tempo melhor indica um desempenho melhor.
## Como apresentar o desempenho
O desempenho é o resultado da média de tempo de 10 tentativas de unzip do mesmo arquivo. O desvio padrão e o erro padrão serão mostrados. O Erro Padrão dessa medida deve ser assumido como erro.
## Medições base (uma máquina)
Saída da máquina base:
```
Time of each unzip(s)
1.04522204399
0.915126085281
0.894931077957
0.885153055191
0.893769025803
0.929057121277
0.88160610199
0.907269001007
0.944057941437
0.868448972702
#############RESULTS###############

Final results:
mean : 0.916464042664s
standart Deviation : 0.0506234508379s
standart error: 0.0160085407665s
```
