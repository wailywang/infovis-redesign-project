
from data_loader import load_and_clean_data
from plots import plot_all
import matplotlib.pyplot as plt

csv_path = "fe273d7c-9adf-46e7-9aab-24dfad3d7967.csv"
df = load_and_clean_data(csv_path)

correlation = df.corr()['Potability'].drop('Potability').sort_values()
mean_features = df.groupby('Potability').mean().T

fig = plot_all(df, correlation, mean_features)
fig.savefig("water_quality_dashboard_modular.png", facecolor='#1F1F1F')
