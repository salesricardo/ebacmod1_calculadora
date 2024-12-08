# EBAC - PRÁTICA MÓDULO 1

**Aluno:** Ricardo Dias de Sales (salesdiasrds@gmail.com)
**Professor:** Rodrigo Rebouças
**Curso:** Curso EBAC, Analista de Dados
**Criação:** 29/11/2024
**Última revisão:** 30/11/2024


## Descrição

Este repositório foi criado para a concretização da prática do módulo 1 do curso Analista de Dados, EBAC. Aqui é possível encontrar tanto o código fonte do exercício, como também outras respectivas informações.

Neste projeto nós temos um simples programa de calculadora escrito em Python, o qual oferece algumas operações básicas da matemática para serem utilizadas pelo usuário. 

O processo de escolha da operação é feito por números, onde o usuário escolhe um número para uma respectiva operação, e depois deverá apenas digitas os números da operação em si para obter o resultado.

## Instalação

Dois processos precisam ser feitos para que este projeto possa ser instalado adequadamente. São eles:

 1. Fork
 2. Clone

Faça um Fork desse projeto clicando na opção Fork mais acima. Isso criará um novo repositório cópia deste em sua conta GitHub. 

Logo em seguida, uilize o Git em sua máquina para criar um repositório local da cópia criada do repositório feito o Fork. Para isso, abra o Terminal Linux e digite:

```bash
# Baixa o repositório remoto para criar um repositório local.
git clone <URL do seu repositório cópia>
```
Se estiver usando o Windows tome proveito do WSL para acessar o Git. Basta que faça:

```bash
# Ativa o WSL para entrar no ambiente Linux isntalado.
wsl

# Baixa o repositório remoto para criar um repositório local.
git clone <URL do seu repositório cópia>
```
É importante lembrar que os arquivos do repositório remoto serão baixados para a sua máquina. Então esteja num diretório onde sinta-se confortável para fazer esse processo.

Dois arquivos importantes serão baixados, são eles:

 - calculadora.sh: Contém o código script shell para dar início ao aplicativo de calculadora desenvolvido.
 - calculadora.py: Contém o código fonte Python do programa de calculadora.

## Execução

A execução do programa de calculadora se dá pelo uso do script shell existente no arquivo:

	calculadora.sh

Tanto o arquivo Python como o script precisam estar no mesmo local. Para executar o script basta usar o interpretador shell de sua distribuição Linux. No Ubuntu, por exemplo, é possível usar o Bash:

```bash
# Executa script shell para chamar programa de calculadora.
bash calculadora.sh
```

Certifique-se apenas de estar com os dois arquivos no mesmo local, e com o Terminal na pasta onde eles foram baixados.

A mesma execução pode ser feita no Windows, onde nesse caso é preciso fazer o uso do WSL (Windwos Subsystem for Linux). Ao abrir o prompt de comando do Windows, digite o seguinte:

```bash
# Ativa o WSL para entrar no ambiente Linux isntalado.
wsl

# Executa script shell para chamar programa de calculadora.
bash calculadora.sh
```

O script fará atribuições de acesso ao arquivo Python (744), e depois irá verificar se o pacote Python está instalado, baixando-o caso não esteja. Isso garante que o programa da calculadora seja executado sem erros, o que deixaria o usuário sem saber o que fazer.

É claro que o programa Python pode ser executado apenas com o arquivo do código fonte, mas o script garante uma boa execução, novamente, evitando erros.


## FAQ - Perguntas Frequentes

1 - Posso contribuir para este projeto?

Este projeto foi pensado para servir apenas com o propósito de conclusão das atividades práticas do curso Analista de Dados, da EBAC. Não haveria de fazer sentido atualizar ele sem necessidade, pois o mesmo não representa um caso real, mas apenas um exercício de estudo e preparação. Assim sendo, ele encontra-se limitado ao escopo do módulo e da atividade requisitada em si.

2 - O código visivelmente poderia ser melhorado. Não poderia fazer isso?

A citar um exemplo claro, seria fazer o uso do tratamento de exceções, por exemplo, uma vez que a calculadora acaba que se limitando a trabalhar apenas com números positivos. Contudo, embora essa seja uma possível melhoria para o programa, é importante lembrar de manter-me dentro apenas do conteúdo que foi visto, sem atropelar o material que deve ser passado e estudado. Eventualmente, nada me impede de fazer uma versão melhor do programa num momento futuro e, provavelmente, isso estará em outro repositório, preservando este como uma atividade feita.

## Licença

Este programa é distribuído sob a licença [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Suporte

Quaisquer dúvidas, problemas ou ideias, por favor, não deixe de retornar o contato comigo pelo e-mail salesdiasrds@gmail.com
