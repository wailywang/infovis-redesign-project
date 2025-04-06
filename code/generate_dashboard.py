import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import pandas as pd
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Set the style
sns.set(style="whitegrid")

# Load real data
df = pd.read_csv("data/SaaS-Sales.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

# Helper: aggregate monthly profit by industry
def get_line_data():
    return df.groupby(['YearMonth', 'Industry'])['Profit'].sum().reset_index()

# Helper: aggregate total profit by industry
def get_donut_data():
    return df.groupby('Industry')['Profit'].sum().reset_index()

# Helper: extract profit by industry and country
def get_scatter_data():
    return df[['Country', 'Industry', 'Profit']].dropna()

# Helper: generate world map with country-level profit
def get_choropleth_data():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    country_profit = df.groupby('Country')['Profit'].sum().reset_index()
    merged = world.merge(country_profit, how='left', left_on='name', right_on='Country')
    return merged

def plot_dashboard():
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))

    # Donut Chart
    donut_data = get_donut_data()
    wedges, texts, autotexts = axs[0, 0].pie(
        donut_data['Profit'],
        labels=donut_data['Industry'],
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("YlOrRd", len(donut_data))
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    axs[0, 0].add_artist(centre_circle)
    axs[0, 0].axis('equal')
    axs[0, 0].set_title('Industry Profit Breakdown')

    # Line Chart
    line_data = get_line_data()
    sns.lineplot(
        data=line_data,
        x='YearMonth', y='Profit', hue='Industry',
        palette='YlOrRd', ax=axs[0, 1]
    )
    axs[0, 1].set_title('Monthly Profit Trends')
    axs[0, 1].tick_params(axis='x', rotation=45)

    # Scatter Plot
    scatter_data = get_scatter_data()
    sns.scatterplot(
        data=scatter_data,
        x='Industry', y='Profit', hue='Country',
        palette='YlOrRd', ax=axs[1, 0]
    )
    axs[1, 0].set_title('Profit by Industry and Country')

    # Choropleth Map
    choropleth_data = get_choropleth_data()
    divider = make_axes_locatable(axs[1, 1])
    cax = divider.append_axes("right", size="5%", pad=0.1)
    choropleth_data.plot(
        column='Profit', cmap='YlOrRd', linewidth=0.8,
        ax=axs[1, 1], edgecolor='0.8', legend=True, cax=cax,
        missing_kwds={"color": "lightgrey"}
    )
    axs[1, 1].set_title('Global Profit Distribution')
    axs[1, 1].axis('off')

    fig.suptitle('Figure 3. Redesigned Multiview Dashboard for Profit Analysis', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fancy_dashboard.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_dashboard()
