# Intel-OCNF - Intelligent Orchestration of Containerized Network Functions for Anomaly Mitigation
Algoritmos utilizados para dissertação apresentada  como  requisito  parcial para a obtenção do grau de Mestre em Ciência da Computação
###### Abaixo mais informações sobre como usar os algoritmos de implementação da orquestração inteligente de funções de rede em containeres para mitigação de anomalias

Para execução dos experimentos, é utilizadado o dataset [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html), os arquivos do conjunto de dados devem estar na pasta "CSVs" na raiz deste projeto.

Para que as seguintes etapas funcionem, primeiro é feito um pré-processamento e agrupamento do dataset ([preprocessing](./preprocessing.ipynb)), resultando em um únivo CSV denominado "all_data.csv".

Os algoritmos estão seprados em 4 etapas de execução, que são:
1. [Coleta de estatísticas](#coleta-de-estatísticas)
2. [Separação por tipo de Ataque](#Separação-por-tipo-de-Ataque)
3. [Seleção de Características](#Seleção-de-Características)
4. [Categorização do tráfego (implementação de aprendizado de máquina)](#Categorização-do-tráfego-(implementação-de-aprendizado-de-máquina))


Para cada etapa contém um ou mais arquivos Python. Para executar os algoritmos, as etapas devem ser executadas em sequência. Porque a saída de um algoritmo é o pré-requisito para a execução do próximo. Cada etapa é descrita em detalhes abaixo.

## Coleta de estatísticas
Esta etapa consiste em um único algoritmo ([statistics](./statistics.ipynb)). Este script analisa o arquivo "all_data.csv" e imprime as estatísticas de registros de ataque e benigno. Não é um pré-requisito para nenhuma outra etapa. Ele apenas fornece informações.

## Separação por tipo de Ataque
Esta etapa consiste em um único algoritmo ([attack_type](./attack_type.ipynb)). Este script usa o arquivo "all_data.csv" para criar arquivos de ataque e então os salva no diretório "./attacks/". O conjunto de dados contém 12 tipos de ataque no total. Portanto, 12 arquivos CSV são criados para esses ataques. Em cada arquivo contêm 30% de ataque e 70% de registro benigno. Esta etapa é pré-requisito para as seguintes etapas.

## Seleção de Características
Esta etapa realiza a seleção de características de duas formas, determinando as características mais importantes para cada tipo de ataque e para todos os tipos de ataque.

### Seleção de Características de Acordo com os Tipos de Ataque

O script [feature_selection_for_attack_types](./feature_selection_for_attack_types.ipynb) usa arquivos dos ataques localizados no diretório "attacks". O objetivo deste algoritmo é determinar quais características são importantes para cada ataque. Para tanto, é utilizado o algoritmo Random Forest Regressor para calcular os pesos de importância.

### Seleção de Características entre Fluxo de Ataque e Benigno
O script [feature_selection_for_all_attack](./feature_selection_for_all_attack.ipynb) 
 aplica a seleção de características para todos os tipos de ataque. Assim, ele cria os pesos de importância de característica que são válidos para todo o conjunto de dados. Ele usa o arquivo "all_data.csv" e o algoritmo Random Forest Regressor. 

## Categorização do Tráfego (implementação de aprendizado de máquina)
Esta etapa aplica os algoritmos de aprendizado de máquina ao conjuto de dados.

### Categorização do Tráfego de Acordo com os Tipos de Ataque
O algoritmo [traffic_categorizer_for_attack_types](./traffic_categorizer_for_attack_types.ipynb) usa arquivos dos ataques localizados no diretório "attacks".
As características usadas ​​são as 4 com maior peso para cada tipo de ataque, produzidos pelo algoritmo feature_selection_for_attack_types. O script traffic_categorizer_for_attack_types aplica 4 algoritmos de aprendizado de máquina para cada tipo de ataque e imprime os resultados dessas operações na tela e no arquivo "./attacks/results_traffic_categorizer_for_attack_types.csv". Ele também cria gráficos dos resultados e os imprime na tela e na pasta "./attacks/result_graph_traffic_categorizer_for_attack_types/".

### Categorização do Tráfego de Acordo com os Tipos de Ataque (com 18 características)
O algoritmo [traffic_categorizer_with_18_feature](./traffic_categorizer_with_18_feature.ipynb) usa o arquivo  "all_dada.csv" com todos os ataques.  O conjunto de características a ser usado consiste em combinar as 4 características com o maior peso de importância alcançado para cada ataque em "traffic_categorizer_for_attack_types". Assim, 4 características são obtidas de cada um dos 12 tipos de ataque, resultando em um conjunto de características composto por 48 atributos. Depois que as repetições são removidas, o número de características é 18.

Este script aplica 4 algoritmos de aprendizado de máquina ao arquivo "all_data.csv" e imprime os resultados dessas operações na tela e no arquivo "./attacks/results_traffic_categorizer_with_18_feature.csv". Ele também cria gráficos dos resultados e os imprime na tela e na pasta "./attacks/result_graph_traffic_categorizer_with_18_feature/".

### Categorização do Tráfego de Acordo com os Tipos de Ataque (com 7 características)
O algoritmo [traffic_categorizer_with_7_feature](./traffic_categorizer_with_7_feature.ipynb) usa o arquivo  "all_dada.csv" com todos os ataques.  As características usadas ​​são as 7 características com maior peso, produzidos pelo script feature_selection_for_all_attack.
Este script aplica 4 algoritmos de aprendizado de máquina ao arquivo "all_data.csv" e imprime os resultados dessas operações na tela e no arquivo "./attacks/results_traffic_categorizer_with_7_feature.csv". Ele também cria gráficos dos resultados e os imprime na tela e na pasta "./attacks/result_graph_traffic_categorizer_with_7_feature/".

