# Fundamentos de Redes Neurais para Visão Computacional

## O que é uma Rede Neural?

Uma rede neural é um modelo computacional inspirado no funcionamento do cérebro humano. Ela é composta por unidades chamadas neurônios artificiais, organizados em camadas, que recebem dados de entrada, realizam cálculos matemáticos e produzem uma saída.

O objetivo de uma rede neural é aprender padrões presentes nos dados. Em vez de programar explicitamente regras para identificar um objeto, por exemplo, a rede aprende essas características observando milhares de exemplos.

Na visão computacional, uma rede neural pode aprender a identificar pessoas, veículos, animais ou qualquer outro objeto presente em imagens e vídeos.

Exemplo:
Ao fornecer milhares de imagens contendo pessoas e informar à rede quais imagens realmente possuem pessoas, ela aprende automaticamente características como formato do corpo, membros e outras informações visuais relevantes.

## O que é Treinamento?

Treinamento é o processo pelo qual uma rede neural aprende a realizar uma tarefa.

Durante o treinamento, são fornecidos:
Dados de entrada (imagens);
Respostas esperadas (rótulos ou anotações).

A rede realiza previsões e compara seus resultados com as respostas corretas. Com base nos erros encontrados, seus parâmetros internos são ajustados para melhorar futuras previsões.

Esse processo é repetido milhares ou milhões de vezes até que a rede consiga produzir resultados satisfatórios.

Exemplo:
Em um dataset de detecção de pessoas:
Entrada: imagem contendo pessoas;
Saída esperada: localização exata das pessoas na imagem.

A rede tenta localizar as pessoas e ajusta seus parâmetros sempre que comete erros.

## O que é Inferência?

Inferência é a utilização de uma rede neural já treinada para realizar previsões em novos dados.

Diferentemente do treinamento, durante a inferência a rede não aprende nem modifica seus parâmetros. Ela apenas aplica o conhecimento adquirido anteriormente.

Exemplo:
Uma YOLO treinada para detectar pessoas recebe uma imagem nova:
Entrada: fotografia capturada por uma câmera;
Saída: caixas delimitadoras indicando onde as pessoas estão localizadas.

Esse processo geralmente é rápido e ocorre em tempo real em aplicações industriais, sistemas de segurança e veículos autônomos.

## O que são Épocas (Epochs)?

Uma época representa uma passagem completa por todo o conjunto de treinamento.

Se um dataset possui 1.000 imagens:

1 época significa que a rede analisou as 1.000 imagens uma vez;
10 épocas significam que analisou as mesmas imagens dez vezes.

O uso de múltiplas épocas permite que a rede refine gradualmente seu conhecimento sobre os dados.

Exemplo:
Dataset: 1000 imagens

Epoch 1 → Primeira passagem
Epoch 2 → Segunda passagem
Epoch 3 → Terceira passagem

Durante as primeiras épocas, os erros costumam ser elevados. Com o tempo, a rede tende a melhorar seu desempenho.

## O que é Função de Perda (Loss)?

A função de perda, ou loss, é uma métrica que indica o quão errada está a previsão da rede neural.

Ela mede a diferença entre:

Resultado previsto pela rede;
Resultado esperado.

Quanto menor o valor da loss, melhor o desempenho do modelo.

Durante o treinamento, a rede busca continuamente minimizar essa perda.

Exemplo:
Suponha que a posição correta de uma pessoa esteja em determinada região da imagem.
Se a rede desenhar a caixa de detecção em uma posição incorreta, a loss será alta.
À medida que aprende a localizar corretamente os objetos, a loss diminui.

## O que é Overfitting?

Overfitting ocorre quando a rede neural memoriza excessivamente os dados de treinamento em vez de aprender padrões gerais.

Nesse caso, ela apresenta ótimo desempenho nos dados utilizados durante o treinamento, mas falha ao analisar imagens novas.

É um dos problemas mais comuns em Machine Learning.

Exemplo:
Imagine treinar uma rede apenas com imagens de pessoas usando roupas vermelhas.
A rede pode aprender incorretamente que a presença da cor vermelha é uma característica importante para identificar pessoas.
Quando encontrar pessoas usando roupas de outras cores, seu desempenho poderá cair significativamente.

Sinais de Overfitting:
Excelente desempenho no treinamento;
Baixo desempenho em validação;
Perda de generalização.

## O que são CNNs (Convolutional Neural Networks)?

CNN significa Convolutional Neural Network (Rede Neural Convolucional).

Esse tipo de rede foi desenvolvido especificamente para trabalhar com imagens.

Enquanto uma rede neural tradicional analisa dados de forma mais genérica, uma CNN consegue identificar características visuais importantes como:

Bordas;
Texturas;
Formas;
Objetos completos.

Ela realiza isso utilizando operações chamadas convoluções.

Funcionamento simplificado

A CNN aprende em diferentes níveis:

Imagem
   ↓
Bordas
   ↓
Formas simples
   ↓
Partes de objetos
   ↓
Objeto completo

Por exemplo:

Bordas → Olhos → Rosto → Pessoa

ou

Bordas → Rodas → Carro → Veículo

## Relação com o YOLO

A YOLO (You Only Look Once) é um modelo de detecção de objetos baseado em redes neurais convolucionais.

Quando treinamos uma YOLO:

A CNN extrai características da imagem;
O modelo identifica objetos presentes;
O modelo localiza esses objetos através de caixas delimitadoras (bounding boxes);
O modelo informa a classe detectada (pessoa, carga, veículo, etc.).

Em aplicações industriais, como monitoramento de guindastes, a YOLO pode ser utilizada para detectar pessoas e cargas em tempo real, fornecendo informações para sistemas de segurança, automação e Digital Twins.