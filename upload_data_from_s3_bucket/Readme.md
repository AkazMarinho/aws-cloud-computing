
## Parte 01

### Credenciais
- Para realizar o acesso ao AWS S3, é necessário utilizar credenciais, nesse caso sendo utilizado o AWS Single Sign-On (SSO). Para manter a segurança dos dados de credenciais, utilizo neste projeto variáveis de ambiente (.env).

### Função de Criar Bucket
- A primeira função é responsável por criar um bucket e retornar uma resposta de sucesso. Caso as credenciais não existam ou estejam incorretas, o bucket já exista, o nome seja inválido ou aconteça outro problema, será retornada uma exceção.

### Função de Envio de Dados
- Responsável por enviar arquivos para o bucket S3, a função precisa de três parâmetros para que o carregamento seja executado com sucesso: o caminho local do arquivo, o nome do bucket e o nome do arquivo no destino. Neste último, podem ser adicionados separadores "/" para definir diretórios.

### Variáveis de Acesso
- Para armazenar as credenciais em variáveis, utiliza-se a biblioteca dotenv, que permite resgatar os valores do arquivo .env.

### Serviço de Acesso 
- Para que a conexão com a AWS seja realizada de forma correta, é utilizada a biblioteca Boto3, onde as credenciais serão enviadas.

Os dados utilizados estão disponibilizados na plataforma Kaggle, na URL: https://www.kaggle.com/datasets/ahmedabbas757/dataset

A documentação da biblioteca Boto3 pode ser encontrada em: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

O código pode ser encontrado em meu repositório do GitHub: https://github.com/AkazMarinho/aws-cloud-computing

## Parte 02

Continuando com o aprendizado sobre o uso da AWS, hoje demonstro como criar buckets e realizar o upload de arquivos para a AWS através de um container Docker criado a partir de um arquivo Docker Compose.

## Alteração
Inicialmente, fiz uma alteração no arquivo Python relacionada ao nome do bucket. 

## Docker compose
Em seguida, criei um arquivo Docker Compose onde defini a versão do Python a ser utilizada, o diretório de trabalho do Docker, o volume para os arquivos e os comandos para instalação das bibliotecas necessárias e execução do arquivo Python.

Após isso, utilizei o comando docker-compose up para criar o container e executar o arquivo Python. Isso resultou na criação do bucket e no upload do arquivo CSV.

Imagem 01: À esquerda, o script Python com importações de bibliotecas e parte da função de criação de bucket. À direita, o script Docker Compose com as configurações necessárias para gerar o container e executar o script Python. Abaixo, a execução do Docker Compose após o comando docker-compose up.

Imagem 02: Log mostrando a criação bem-sucedida do container Docker e a execução concluída com sucesso do script.

Imagem 03: Imagem mostrando o bucket criado e o arquivo dentro do ambiente da AWS.

Este processo demonstra como utilizar Docker para facilitar o trabalho com AWS, permitindo uma abordagem mais controlada e portátil para o desenvolvimento e execução de scripts na nuvem.

O código pode ser encontrado em meu repositório do GitHub: https://github.com/AkazMarinho/aws-cloud-computing

Observação: Para que o script seja executado com sucesso, é necessário criar um arquivo .env e declarar suas credenciais corretamente.

A documentação foi corrigida e adaptada por ChatGPT.
