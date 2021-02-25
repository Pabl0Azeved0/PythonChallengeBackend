#Python Challenge

Uma app simples para cumprir um desafio em python backend quais foram dadas 
4 questões e solucionadas obrigatoriamente no backend, nesta solução fiz uma
interface gráfica para o usuário ter uma visualização do que acontece, não foi 
feito pensando em ter uma rota, expor ela e responder com um output, portanto 
será necessário seguir este tutorial para conseguir visualizar e avaliar as 
questões.

####Links úteis:
* **[Documentação oficial do Docker](https://docs.docker.com/get-docker/)**
* **[Site oficial do Python](https://python.org.br/)**

Tendo Docker instalado em sua máquina e python na versão 3.7+, será possível 
rodar esta aplicação, para isto criei um Makefile tendo em vista facilitar o 
processo, apenas digite 'make' no seu terminal e leia as instruções, temos o 
'make build' qual executa o seguinte comando no seu terminal:

```
docker build -t flask-app:latest .
```

E também o comando 'make run' qual executa o seguinte comando no terminal:
```
docker run -p 8000:8000 flask-app
```

Basicamente o 'make build' contém o comando de criação do container e o comando
'make run' contém o comando de executar este container e colocar-lo para rodar 
na porta 8000 (pode modificar se necessário).

Tendo dito isto a interface é bem amigável e intuitiva, as questões estão lá e 
os campos para inserir e testar também, vamos lá, execute a aplicação!