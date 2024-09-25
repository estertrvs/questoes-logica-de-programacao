# Questões de lógica de programação

## Questões

### Questão 1

**Descrição**: Observe o trecho de código abaixo: 
```
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável SOMA?

**Solução**: Para resolver essa questão, foi utilizado um laço `while` que realiza a soma incremental de valores de 1 a 13. Valor da variável soma: 91

### Questão 2

**Descrição**: Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

**Solução**: O programa inicializa a sequência de Fibonacci com as variáveis a e b (0 e 1, respectivamente). Em seguida, atualizamos as variáveis para os próximos números da sequência, onde a recebe o valor de b, e b recebe a soma dos valores anteriores de a e b. A cada iteração, verificamos se o valor atual de a é igual ao número que estamos tentando verificar.

### Questão 3

**Descrição**: Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a - Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b - Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

**Solução**: Adicionei um json de exemplo para testar o código com os seguintes valores: [1000, 2000, 0, 3000, 4000, 0, 5000, 6000, 0, 7000] o retorno do código foi: 
Menor faturamento: 1000
Maior faturamento: 7000
Dias com faturamento acima da média: 3

### Questão 4

**Descrição**: Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

**Solução**: Foi feito um laço para iterar cada estado e seu faturamento e com isso calcular o percentual.  Resultado do código:
SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
Outros: 10.98%

### Questão 5

**Descrição**: Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a - Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b - Evite usar funções prontas, como, por exemplo, reverse; 

**Solução**: O programa reverte a string usando um for que percorre a string de trás para a frente e armazena em uma variável auxiliar. Depois do for basta retornar a variável.







