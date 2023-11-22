# docker-multi-stage-ml

Projeto para criar um pipeline de machine learning.

- Passo 1
    Treinar o modelo com os dados na pasta data
- Passo 2
    Criar uma imagem docker com o modelo, utilizando multi-steps
- Passo 3
    Servir o modelo para ser utilizado



# Build Imagem

Como Buildar sua imagem para teste local

docker build -t dev-model .
docker run -p 8000:8000 dev-model

Acessar o localhost:8000/doc para testar com o swaguer