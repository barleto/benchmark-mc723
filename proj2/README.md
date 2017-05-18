###### **MC723A**, *1s2017*, IC - UNICAMP
# Projeto 2
### Grupo 14
- Ricardo Zaideman Charf 	- **151238**
- Vitor Marge Eichenberger 	- **149053**
- Guilherme Zanelato		- **119494**

## TODO:
Esta seção serve somente para o grupo se orientar e **deverá ser apagada** antes da submissão final do projeto.

- [ ] Escolher configurações das simulações
- [x] Atualizar arquivos das simulações
	- [x] Arquivos de trace
	- [x] Arquivo do mips **.cpp**
- [ ] Compilar tudo
- [ ] Rodar testes
- [ ] Redigir relatório

## Roteiro *(resumido)*
- Será utilizado o software Dinero IV para o teste de software em várias configurações de cache distintas.
- A implementação do Simulador MIPS em archC, também será modificada para ser possível contabilziar hazard em diferentes implementaçes (Tamanho do pipeline: 5, 7 e 13 estágios, processador escalar VS superescalar, etc)
- Sero testados:
  - Tamanho do pipeline: 5, 7 e 13 estágios
  - Processador escalar vs superescalar
  - Hazard de dados e controle
  - Branch predictor
  - Cache (Sendo essa testada a partir do Dinero IV)

## **Relatório**

### Introdução

### Ferramentas
- DineroIV
- ArchC
- Simulador de MIPS (em ArchC)

### Metodologia
Primeiramente foram baixadas, instaladas e configuradas todas as ferramentas necessárias ao projeto.

Em seguida foi feita uma revisão sobre processadores, pipelines e suas características, focando em relembrar os conceitos para garantir coerência e validade ao projeto, seus dados e resultados.

Adaptação do código fonte do mips (do simulador) que não possui muitas funcionalidades desejadas para as análises:
- Pipeline, com diferentes tamanhos
- Branch Predictor
- Hazards (de controle e de dados)
- Pipeline Superescalar

Além é claro de todas as implementações necessárias para gerarem estatísticas e registros dos eventos a serem analisados.

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

Também foi feito um script em *Python* para formatar e gerar dados a partir da saída do *simulador MIPS* e do *DineroIV*. Este é também capaz de mudar algumas das configurações.

Por fim tudo isto foi compilado e executado, gerando os dados que - foram melhor organizados numa tabela e - proporcionaram a análise que se encontra adiante.


### Resultados
Dados e tabelas aqui...

### Análise
Fazer análise dos resultados...

### Conclusão
Concluir...
