
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