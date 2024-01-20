![296661514-f2c1e5d8-90fe-448d-b427-4630d6a2db37](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/48d37d0a-fa19-4651-a288-ed178e316eb3)

# Inteligência Artificial

# Simulated Annealing for Local Search

# Visão Geral

Este repositório documenta a implementação do algoritmo Simulated Annealing para busca local no campo da Inteligência Artificial. O Simulated Annealing é um algoritmo de otimização conhecido por sua eficiência na exploração de espaços de solução complexos. O README fornece insights sobre os conceitos básicos, desenvolvimento do algoritmo, exemplos práticos e aplicações no mundo real.

## Contributors

- Alano Baptista 
- Luquenia Galiano 

## Conceitos Básicos

### Algoritmo de Otimização

Os algoritmos de otimização desempenham um papel crucial na resolução de uma variedade de problemas complexos em diferentes domínios. Esses algoritmos visam encontrar a melhor solução possível para um problema específico, explorando e ajustando um conjunto de parâmetros ao longo do tempo.

Em comparação com alguns algoritmos de busca determinísticos, como o A*, que buscam encontrar a solução mais otimizada por meio de uma abordagem heurística, o Simulated Annealing destaca-se devido à sua capacidade de lidar com espaços de busca mais complexos. A complexidade computacional do Simulated Annealing permite uma exploração mais eficiente e abrangente do espaço de solução, especialmente em situações em que a topologia do espaço é desconhecida ou mal definida.

### Escolha de Estados Aleatórios

Um aspeto fundamental dos algoritmos de otimização é a capacidade de explorar o espaço de busca de maneira eficiente. A escolha de estados aleatórios é uma estratégia que visa evitar ficar preso em ótimos locais, permitindo que o algoritmo explore regiões mais amplas do espaço de solução. Isso proporciona uma maior probabilidade de descobrir soluções mais ótimas globalmente.

![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/3c1e0c64-74ea-4162-bdc3-b2f4c1397463)

### Aceitação com Probabilidade

Ao explorar o Simulated Annealing, um dos conceitos fundamentais é a Aceitação com Probabilidade. Este mecanismo permite que o algoritmo aceite soluções subótimas com uma certa probabilidade, evitando ficar preso em ótimos locais. A fórmula utilizada para calcular a probabilidade de aceitação é:

![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/28bbcc6d-43a2-4b76-a8d6-2a9390c01aa6)

Essa fórmula reflete a probabilidade de aceitar uma solução pior com base na diferença de custo e na temperatura do sistema. À medida que a temperatura diminui, a probabilidade de aceitar soluções subótimas também diminui, refletindo o processo de resfriamento no algoritmo.

## O que é Annealing?

### Definição

Annealing é um termo derivado do processo metalúrgico de recozimento, no qual um metal é aquecido a altas temperaturas e, em seguida, resfriado lentamente para reduzir a dureza e eliminar defeitos. Este processo visa atingir um estado mais equilibrado e estável.

### Procurando Soluções na Natureza

O conceito de Simulated Annealing encontra inspiração na busca de soluções na natureza. Três pesquisadores da IBM, inspirados pelo recozimento de metais, desenvolveram uma analogia para encontrar soluções otimizadas em espaços de busca complexos.

### Recozimento de Metais como Inspiração

O Simulated Annealing é inspirado no recozimento de metais, onde durante o aquecimento, os átomos ganham energia e movem-se mais livremente. Ao resfriar lentamente, têm a oportunidade de se reorganizar em uma estrutura mais estável e de menor energia. Analogamente ao recozimento de metais, a "temperatura" no Simulated Annealing controla a probabilidade de aceitar soluções subótimas. À medida que a temperatura diminui, o algoritmo torna-se mais seletivo, refletindo o processo de resfriamento no recozimento metalúrgico. Essa adaptação permite ao algoritmo focar em soluções de menor energia à medida que avança, assim como o recozimento metalúrgico busca um estado mais estável e equilibrado durante o resfriamento.

## Temperatura no Contexto do Simulated Annealing

### Compreendendo as Fases Térmicas

O Simulated Annealing incorpora um conceito crucial de temperatura, desempenhando um papel fundamental na exploração e aceitação de soluções. A temperatura no algoritmo é dinamicamente ajustada ao longo do processo, passando por diferentes fases térmicas.

![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/e08dbd20-6977-4f86-a3f5-6e83033a5293)

#### Alta Temperatura - Fase Quente

Durante a fase quente, a temperatura é alta, permitindo uma exploração mais ampla do espaço de solução. Nessa fase, o algoritmo é mais propenso a aceitar soluções subótimas, incentivando uma busca mais exploratória e movimentos aleatórios pelo espaço de solução.

#### Decaimento Gradual da Temperatura

Ao longo do tempo, a temperatura no Simulated Annealing decai gradualmente. Esse decaimento é controlado para permitir uma transição suave entre as fases quente e fria. O decaimento gradual é crucial para equilibrar a exploração inicial com uma busca mais intensiva por soluções ótimas.

#### Baixa Temperatura - Fase Fria

Na fase fria, a temperatura atinge níveis mais baixos. O algoritmo torna-se mais seletivo, sendo menos propenso a aceitar soluções subótimas. Isso possibilita uma busca mais intensiva em torno de soluções promissoras, visando convergir para uma solução ótima.

### Consideração final

Ao ajustar dinamicamente a temperatura ao longo do processo, o Simulated Annealing equilibra a exploração e a exploração intensiva, adaptando-se à complexidade do espaço de solução e melhorando a eficiência na busca por soluções otimizadas.

## Salesman Problem

### Introdução

O Problema do Caixeiro Viajante é um desafio clássico em otimização, no qual o objetivo é encontrar o caminho mais curto que visita um conjunto de cidades e retorna ao ponto de origem. Este problema tem implicações práticas em diversas áreas, como logística, planeamento de rotas e circuitos integrados.

### Na Natureza

Na natureza, observamos que muitos animais possuem uma notável habilidade em mapear soluções eficientes para problemas semelhantes. As abelhas, ao polinizar flores, e as formigas, ao buscar comida, são exemplos de como a natureza encontrou soluções eficazes para problemas de otimização espacial.

Apesar das habilidades notáveis dos animais na busca por soluções eficientes, muitas vezes, essas soluções não são as ótimas. Mesmo com estratégias adaptativas e eficazes, a natureza enfrenta limitações na busca pela solução de menor custo em espaços de solução complexos.


## Formigas
![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/2a968d3e-f9c9-43f4-afb0-18d4a8e6d555)

## Amoeba
![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/c049b626-ac85-4124-a7bf-def147268ef3)

Uma imagem radiográfica que destaca o padrão coberto pela ameba, onde o organismo é representado em cinza, enquanto os pontos quimiotáticos são ordenados alfabeticamente e circulados em verde.

![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/6c7e3cf2-2666-49a8-beab-8449e4cc2de5)

## Pombos
![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/cdf713e1-4d3a-4f82-a40e-4e22a4be6794)

Diagrama resumido dos movimentos de pombos em direção à comida de acordo com as várias disposições. Se preferir, pode imaginar que é um esquema de jogo compreensível apenas para especialistas em zoologia, evidentemente mais elaborado do que o clássico 3-4-3.

Outra imagem microscópica do organismo alcançando vários pontos quimiotáticos.

### Limitações na Busca da Solução Ótima

Apesar dos avanços significativos em algoritmos de otimização, incluindo o Simulated Annealing, a resolução do Problema do Caixeiro Viajante ainda apresenta desafios substanciais. Algumas das principais limitações incluem:

- **Espaço de Busca Exponencial:** O número de possíveis combinações de rotas cresce exponencialmente com o aumento do número de cidades, tornando a busca pela solução ótima computacionalmente intensiva.
- **Presença de Ótimos Locais:** O espaço de solução muitas vezes contém ótimos locais que podem atrair o algoritmo, resultando em soluções subótimas se a busca for interrompida prematuramente.
- **Complexidade Computacional:** Algoritmos de otimização, incluindo o Simulated Annealing, podem encontrar dificuldades em lidar com a complexidade computacional associada à busca pela solução ótima em grandes conjuntos de dados.
- **Sensibilidade a Parâmetros:** Alguns algoritmos são sensíveis à escolha de parâmetros, e encontrar uma configuração ideal pode ser desafiador.

## Desenvolvimento de Algoritmo: Simulated Annealing para Roteirização Eficiente

### Considerações

Antes de explorar os exemplos, é importante esclarecer que as distâncias apresentadas nas soluções são fictícias e foram atribuídas com base nas posições relativas de 17 pontos que simulam a localização das cidades introduzidas na análise. Essa abordagem foi adotada para ilustrar o funcionamento do algoritmo em um contexto visual, sem refletir necessariamente a escala ou magnitude real das distâncias no mundo físico. Esta escolha visa destacar a adaptabilidade do algoritmo em resolver o Problema do Caixeiro Viajante, independentemente das magnitudes específicas das distâncias entre as cidades simuladas.

#### Primeiro Exemplo - 500 Iterações

Na primeira execução do algoritmo, após 500 iterações, foi alcançada a solução ótima para o Problema do Caixeiro Viajante. Esta rápida convergência destaca a eficiência do algoritmo ao encontrar a solução de melhor qualidade em um curto espaço de tempo.

Distância da Melhor Rota: 77.74779907190627

![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/5497b709-e182-49f7-a32b-b0fec2716c02)


#### Segundo Exemplo - 1.000.000 de Iterações

No segundo exemplo, mesmo após realizar um milhão de iterações e variar a temperatura e o cooling rate, o algoritmo não alcançou a solução ótima. No entanto, é notável que o algoritmo encontrou uma segunda solução próxima à ótima.

Distância da Melhor Rota: 78.88802579825476

![image](https://github.com/alanocb/Simulated-Annealing-Algoritmh/assets/99679262/5dd484ef-afcd-4f12-9432-4470fd6257da)


### Conclusão no desenvolvimento do algoritmo

Ao explorar os exemplos práticos do Simulated Annealing na resolução do Problema do Caixeiro Viajante, observamos que o algoritmo pode, por vezes, ficar preso em ótimos locais, especialmente em espaços de solução complexos. Isso significa que, embora seja eficaz na busca de soluções de alta qualidade, não há garantia de sempre atingir o ótimo global. É importante considerar a sensibilidade do algoritmo a parâmetros específicos e explorar estratégias adicionais, como reinicializações ou variações nos parâmetros, para mitigar o risco de ficar preso em ótimos locais.

## Aplicações Práticas

### Design de Redes de Telecomunicações

O Simulated Annealing é aplicado no design de redes de telecomunicações para otimizar a disposição de torres, roteadores e outros elementos. Ele ajuda a encontrar configurações eficientes que minimizam a interferência e maximizam a cobertura, contribuindo para o desempenho global da rede.

### Roteamento de Veículos

Na logística, o Simulated Annealing é empregado no roteamento de veículos, buscando as rotas mais eficientes para entrega ou coleta. Isso resulta em economia de tempo, combustível e recursos, melhorando a eficiência operacional.

### Problemas de Localização de Instalações

Ao lidar com a localização estratégica de instalações, como armazéns, fábricas ou centros de distribuição, o Simulated Annealing ajuda a determinar as posições ideais para otimizar o acesso, minimizar custos de transporte e atender à demanda regional de forma eficiente.

### Otimização de Horários de Linhas Aéreas

No setor de aviação, o Simulated Annealing é aplicado para otimizar os horários de voos, levando em consideração fatores como tempo de voo, conexões, demanda de passageiros e custos operacionais. Isso contribui para a eficiência global das operações aéreas.

## Vantagens e Desvantagens do Simulated Annealing

### Vantagens

- **Adaptação a Espaços de Solução Complexos:** O Simulated Annealing é eficaz em explorar espaços de solução complexos, onde a busca tradicional pode ser desafiadora.
- **Abordagem Heurística Versátil:** Pode ser aplicado a uma variedade de problemas de otimização, tornando-se uma ferramenta versátil em diversas áreas.
- **Exploração e Explotação Balanceadas:** Ajustando a temperatura, o algoritmo consegue equilibrar a exploração inicial com a exploração intensiva, melhorando a busca por soluções ótimas.

### Desvantagens

- **Sensibilidade a Parâmetros:** O desempenho do Simulated Annealing pode ser sensível à escolha de parâmetros, exigindo ajustes cuidadosos para obter resultados ideais.
- **Não Garante a Solução Ótima:** Não há garantia de encontrar a solução globalmente ótima, pois o algoritmo pode ficar preso em ótimos locais.
- **Complexidade Computacional:** Em problemas com espaços de solução muito grandes, a complexidade computacional pode ser um desafio, impactando o tempo de execução.

### Conclusão

O Simulated Annealing destaca-se como uma ferramenta robusta para a resolução de problemas de otimização em diversos contextos. Sua habilidade de realizar uma exploração abrangente e se adaptar a mudanças ambientais o posiciona como uma abordagem valiosa, especialmente em cenários complexos e dinâmicos. Uma implementação cuidadosa e estratégica permite que o Simulated Annealing forneça soluções eficazes, consolidando-se como uma ferramenta versátil e eficiente para enfrentar desafios práticos.

### Bibliografia

- [SciShow - Simulated Annealing: The Math of Cooling Systems](https://www.youtube.com/watch?v=I_0GBWCKft8&ab_channel=SciShow)
- [Reducible - Simulated Annealing: A Math Science](https://www.youtube.com/watch?v=GiDsjIBOVoA&t=1387s&ab_channel=Reducible)
- [ChallengingLuck - Simulated Annealing: Explained and Implemented](https://www.youtube.com/watch?v=FyyVbuLZav8&ab_channel=ChallengingLuck)
- [Pesci di Ippaso - Travelling Salesmen vs Pigeons (Part 2)](https://pescidiippaso.medium.com/travelling-salesmen-vs-pigeons-part-2-1156d5e4d9e)
- [OpenAI Chat](https://chat.openai.com/)

