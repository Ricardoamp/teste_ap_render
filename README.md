 <h1 align="center"> Calculando a propensão de compras de clientes </h1>
 
O principal objetivo desse projeto é direcionar os esforços de vendas da empresa para os clientes mais propensos a comprar um seguro, eliminando chamadas desnecessárias e melhorando a lucratividade geral. Para alcançar esse objetivo, o modelo foi treinado com dados coletados de clientes existentes que já possuem seguro de saúde, o que proporciona insights valiosos sobre o comportamento dos consumidores.

A metodologia adotada envolveu a utilização de diversos algoritmos, com o intuito de encontrar o equilíbrio ideal entre eficiência e tamanho do modelo. Após uma análise minuciosa, o algoritmo escolhido foi a regressão logística, devido à sua capacidade de oferecer resultados precisos, além de ser computacionalmente viável para a aplicação em larga escala.

Como resultado, foi desenvolvido um documento do Google Sheets que está vinculado ao modelo de aprendizado de máquina atualmente em produção. Esse documento oferece uma lista de clientes que provavelmente estão mais propensos a adquirir um seguro de carro, com base nas previsões feitas pelo modelo. Com essa informação em mãos, a equipe de vendas pode direcionar seus esforços de forma mais eficiente, aumentando as chances de sucesso e reduzindo os custos associados a chamadas desnecessárias.

Em suma, o projeto de propensão de compras de clientes é uma iniciativa inovadora que demonstra o poder do machine learning na área de vendas. Ao utilizar algoritmos inteligentes, como a regressão logística, e aproveitar dados valiosos dos clientes existentes, a empresa pode otimizar suas estratégias de vendas, maximizar a lucratividade e fornecer um serviço mais personalizado aos seus clientes em potencial.

## 1.0. Questão de negócio
O projeto é para uma empresa de seguros que forneceu seguro de saúde aos seus clientes e agora precisa de ajuda para construir um modelo que preveja se os segurados (clientes) do ano passado também terão interesse no seguro de veículos oferecido pela empresa.

Construir um modelo para prever se um cliente teria interesse no seguro de veículos é extremamente útil para a empresa, pois ela pode planejar sua estratégia de comunicação de acordo para alcançar esses clientes e otimizar seu modelo de negócios e receita.

## 2.0. Entendimento do Negócio
Uma apólice de seguro é um acordo pelo qual uma empresa se compromete a fornecer uma garantia de compensação por perda, dano, doença ou morte especificados, em troca do pagamento de um prêmio especificado. Um prêmio é uma quantia de dinheiro que o cliente precisa pagar regularmente a uma empresa de seguros por essa garantia.

Por exemplo, você pode pagar um prêmio de 5000 por ano por uma cobertura de seguro de saúde de 200.000, para que, se você fique doente e precise ser hospitalizado naquele ano, a empresa provedora de seguro arcará com os custos de hospitalização até 200.000. Para a empresa pode arcar com um custo de hospitalização tão alto quando cobra um prêmio de apenas 5000, é aí que entra o conceito de probabilidades. Por exemplo, assim como você, pode haver 100 clientes que pagariam um prêmio de 5000 todos os anos, mas apenas alguns deles (digamos 2-3) seriam hospitalizados naquele ano, e não todos. Dessa forma, todos compartilham o risco uns dos outros.

Assim como o seguro médico, existe o seguro de veículos, no qual o cliente precisa pagar um prêmio de determinado valor para a empresa provedora de seguro para que, em caso de acidente infeliz com o veículo, a empresa provedora de seguro forneça uma compensação (chamada de "valor segurado") ao cliente.

## 3.0. Coleta de dados
Foi realizado o download dos conjuntos de dados no formato csv por meio da plataforma kaggle.
[Kaggle dados Health Insurance Cross Sell](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction?select=train.csv)

Colunas | descrição
------- | ---------
Id | ID exclusivo para o cliente
Gênero | Sexo do cliente
Idade | Idade do cliente
Driving_License | 0 : O cliente não tem Licença de carro, 1 : O cliente já tem Licença de carro
Region_Code | Código exclusivo para a região do cliente
Previously_Insured | 1 : Cliente já tem Seguro de Veículo, 0 : Cliente não tem Seguro de Veículo
Vehicle_Age | Idade do Veículo
Vehicle_Damage | 1 : Cliente teve seu veículo danificado no passado. 0 : O cliente não teve seu veículo danificado no passado.
Annual_Premium | O valor que o cliente precisa pagar como prêmio no ano
Policy_Sales_Channel | Código anonimizado para o canal de contato com o cliente ou seja. Agentes diferentes, por correio, por telefone, pessoalmente, etc.
Vintage | Número de Dias, o Cliente foi associado à empresa
Response | 1 : O cliente está interessado, 0 : O cliente não está interessado

## 4.0. Limpeza dos dados
Para esse dataset específico, não foi necessário uma limpeza ou tratamento de valores vazios.

## 5.0. Exploração dos dados
Na etapa de exploração dos dados, o objetivo principal é obter um entendimento mais profundo do negócio por meio da análise dos dados disponíveis. Essa etapa envolve identificar padrões, relacionamentos e insights relevantes que possam ajudar a compreender melhor o comportamento dos dados e a tomar decisões embasadas. A seguir, são apresentadas algumas etapas comuns durante a exploração dos dados:

### 5.1 Análise Descritiva
Uma análise descritiva das variáveis disponíveis, como a média, mediana, desvio padrão, valores mínimos e máximos. Essa análise fornece uma visão geral do intervalo de valores, identificando possíveis discrepâncias ou anomalias nos dados.

attributes |	min |	max	| range	| mean	| median	| std	| skew	| kurtosis
---------- | --- | --- | ----- | ---- | ------ | --- | ---- | --------
Age	| 20.0	| 85.0	| -65.0	| 38.835582 |	36.0 |	15.509496 |	0.670000 |	-0.570016
Driving_License |	0.0 |	1.0 |	-1.0 |	0.997829 |	1.0 |	0.046547 |	-21.390677 |	455.564047
Region_Code |	0.0 |	52.0 |	-52.0 |	26.413340 |	28.0 |	13.217997 |	-0.117479 |	-0.863585
Previously_Insured |	0.0 |	1.0 |	-1.0 |	0.458373 |	0.0 |	0.498264 |	0.167088 |	-1.972094
Annual_Premium |	2630.0 |	540165.0 |	-537535.0 |	30571.851319 |	31675.0 |	17254.215590 |	1.853769 |	36.695689
Policy_Sales_Channel |	1.0 |	163.0 |	-162.0 |	111.966591 |	131.0 |	54.229980 |	-0.897379 |	-0.976093
Vintage |	10.0 |	299.0 |	-289.0 |	154.272609 |	154.0 |	83.642252 |	0.004656 |	-1.199888


### 5.2. Visualização dos dados 
Utilizando gráficos e visualizações, é possível explorar as relações entre as variáveis e identificar tendências ou padrões. Histogramas, gráficos de dispersão, gráficos de linhas e box plots são algumas das ferramentas comumente utilizadas para essa análise visual.



## 6.0. Modelagem dos dados
Na etapa de modelagem dos dados, o objetivo é preparar os dados de forma adequada para que os algoritmos de machine learning possam ser aplicados. Essa etapa envolve uma série de processos, como codificação de variáveis categóricas em variáveis numéricas, transformações de dados e separação dos dados em conjuntos de treinamento e teste.

## 7.0. Algoritmo de Machine Learning (Random Forest)

O algoritmo Random Forest é uma escolha interessante para projetos "Learn to Rank" devido à sua capacidade de lidar com tarefas de classificação e seu desempenho robusto em conjunto com a natureza do aprendizado de ranking.

Ao utilizar o Random Forest para projetos "Learn to Rank", o objetivo é criar um modelo que possa classificar e ordenar uma lista de itens de acordo com sua relevância para um determinado critério.

## 8.0. Avaliação do Algoritmo
Após o treinamento, desenvolvi um modelo capaz de identificar a quantidade de pessoas interessadas em adquirir o seguro e classificá-las por ordem de prioridade, conforme ilustrado na imagem abaixo:

Através das previsões feitas pelo modelo, consigo identificar todas as pessoas que demonstraram interesse no seguro. Ao organizá-las em uma ordem específica, percebi que seria necessário entrar em contato com um pouco mais da metade da minha base de clientes para alcançar todos os possíveis interessados em efetuar a compra.

Essa abordagem me permite otimizar os esforços de vendas, concentrando-me nos clientes com maior probabilidade de conversão, maximizando o retorno sobre os investimentos e garantindo que a equipe de vendas entre em contato com aqueles mais propensos a adquirir o seguro.

Com essa estratégia, tenho como objetivo alcançar uma eficiência maior nas ações de vendas, direcionando recursos e tempo de forma mais eficaz, o que contribui para a melhoria da lucratividade e do desempenho geral da empresa.

## 9.0. Modelo em produção
Para esse projeto específico, meu objetivo era disponibilizar meu modelo em uma API online, e por meio de uma planilha do Google Sheets, permitir que, ao clicar em um botão, as informações com as colunas adequadas fossem usadas para fazer previsões e criar um ranking dos clientes mais propensos a adquirir o seguro.

Essa abordagem visava fornecer uma solução prática e acessível, permitindo que a equipe de vendas utilizasse facilmente a planilha para identificar os clientes com maior probabilidade de compra. Ao clicar no botão, o modelo seria acionado, processando as informações relevantes e fornecendo uma lista ordenada dos potenciais compradores.

Com essa implementação, eu buscava aumentar a eficiência das operações de vendas, permitindo uma abordagem mais direcionada e personalizada para entrar em contato com os clientes em potencial. Dessa forma, seria possível otimizar os recursos da equipe de vendas, concentrando esforços naqueles com maior probabilidade de conversão, o que poderia resultar em melhores resultados e maior lucratividade para a empresa.
 
