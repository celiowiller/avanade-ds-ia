# 0. importar recursos necessarios 
import numpy as np
import pandas as pd


from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans

# 1. criar um dataset sintetico
X_raw, y_raw = make_classification(
    n_samples=1000, n_features=4, n_informative=3, n_redundant=1, random_state=42
)

# 2. definir o df
df = pd.DataFrame(
    X_raw,
    columns = ['feat_num_1', 'feat_num_2', 'feat_num_3', 'feat_num_4' ],
)

# 3. adicionar uma nova coluna do tipo categorical
df['categoria'] = np.random.choice(['Baixo', 'Medio', 'Alto'], size = 1000)

# 4. fluxo de pré-processamento (Feature Engineering)
num_cols = ['feat_num_1', 'feat_num_2', 'feat_num_3', 'feat_num_4']
cat_cols = ['categoria']

# definir o objeto gerado a partir da instancia da classe ColumnTransformer
preprocessor = ColumnTransformer(
    transformers = [
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(drop='first'), cat_cols)
    ]
)

# 5. Pipeline completo de Classifição - Random Forest

pipeline_rf = Pipeline(steps = [
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ]
)

# atribuição multipla das vars para o treino do modelo
X_train, X_test, y_train, y_test = train_test_split(df, y_raw, test_size = 0.2, random_state=42)

# 6. Treino e predição do modelo ML
pipeline_rf.fit(X_train, y_train)
Y_pred_rf = pipeline_rf.predict(X_test)
print('Pipeline de classificação treinado e testado com sucesso!')

# 7. Treinamento em clustering - não supervisionado
X_cluster, _ = make_blobs(n_samples = 500, centers = 3, n_features=2, random_state=42)

kmeans = KMeans(n_clusters = 3, random_state=42, n_init = 10)

cluster_labels = kmeans.fit_predict(X_cluster)

print(f'Centroides dos Clusters Encontrados:\n{kmeans.cluster_centers_}')