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

## 6.0. Modelagem dos dados

## 7.0. Algoritmos de Machine Learning

## 8.0. Avaliação do Algoritmo

## 9.0. Modelo em produção
