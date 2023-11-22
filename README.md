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

Acessar o [http://localhost:8000/docs](http://localhost:8000/docs) para testar com o swaguer

um swagger para testar

{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}

curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}'