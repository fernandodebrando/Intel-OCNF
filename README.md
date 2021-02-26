# Intel-OCNF - Intelligent Orchestration of Containerized Network Functions for Anomaly Mitigation
Algoritmos utilizados para dissertação apresentada  como  requisito  parcial para a obtenção do grau de Mestre em Ciência da Computação
###### Abaixo mais informações sobre como usar os algoritmos de implementação da orquestração inteligente de funções de rede em containeres para mitigação de anomalias

Para execução dos experimentos, é utilizadado o dataset [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html), os arquivos do conjunto de dados devem estar na pasta "CSVs" na raiz deste projeto.

Para que as seguintes etapas funcionem, primeiro é feito um pré-processamento e agrupamento do dataset ([preprocessing.ipynb](./preprocessing.py)), resultando em um únivo CSV denominado "all_data.csv".

Os algoritmos estão seprados em 4 etapas de execução, que são:
1. [Coleta de estatísticas](#coleta-de-estatísticas)
2. [Separação por tipo de Ataque](#Separação-por-tipo-de-Ataque)
3. [Seleção de Características](#Seleção-de-Características)
4. [Categorização do tráfego (implementação de aprendizado de máquina)](#Categorização-do-tráfego-(implementação-de-aprendizado-de-máquina))


Para cada etapa contém um ou mais arquivos Python. Para executar os algoritmos, as etapas devem ser executadas em sequência. Porque a saída de um algoritmo é o pré-requisito para a execução do próximo. Cada etapa é descrita em detalhes abaixo.

## Coleta de estatísticas
Esta etapa consiste em um único algoritmo ([statistics.ipynb] (./statistics.ipynb)). Este script analisa o arquivo "all_data.csv" e imprime as estatísticas de registros de ataque e benigno. Não é um pré-requisito para nenhuma outra etapa. Ele apenas fornece informações.
