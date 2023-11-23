import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load

df = pd.read_csv("./data/heart.csv")


# Divisão dos dados em features (X) e target (y)
X = df.drop('target', axis=1)
y = df['target']

# Codificação das variáveis categóricas (exemplo com One-Hot Encoding)
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

# Divisão em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Inicialização e treinamento do modelo (Random Forest neste exemplo)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predições
predictions = model.predict(X_test)

# Avaliação do modelo
accuracy = accuracy_score(y_test, predictions)
print(f"Acurácia do modelo: {accuracy}")

# Salvar o modelo treinado
# dump(model, f'./model/acc={accuracy:.4f}/modelo_treinado.joblib')
dump(model, f'./model/modelo_treinado.joblib',protocol=4)  # protocol=4 é a versão mais recente do joblib
dump(encoder, './model/encoder.joblib')
