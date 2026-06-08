import pandas as pd

colunas = [
    'Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigreeFunction',
    'Age',
    'Outcome'
]

df = pd.read_csv(
    'dataset/diabetes.csv',
    names=colunas
)

print("Primeiras 5 linhas:")
print(df.head())

print("\nInformações:")
print(df.info())

print("\nEstatísticas:")
print(df.describe())

print("\nQuantidade de pacientes com diabetes:")
print(df['Outcome'].value_counts())