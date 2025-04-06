import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv("data/SaaS-Sales.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

# Donut Chart
industry_profit = df.groupby("Industry")["Profit"].sum().sort_values()
fig1, ax1 = plt.subplots()
ax1.pie(industry_profit, labels=industry_profit.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
plt.title("Profit Distribution by Industry")
plt.savefig("images/donut_chart.png")

# Line Chart
line_data = df.groupby(["YearMonth", "Industry"])["Profit"].sum().reset_index()
pivot = line_data.pivot(index="YearMonth", columns="Industry", values="Profit").fillna(0)
pivot.plot(figsize=(10, 5))
plt.title("Monthly Profit Trend by Industry")
plt.savefig("images/line_chart.png")

# Scatter Plot
scatter_data = df.groupby(["Country", "Industry"]).agg({"Profit": "sum", "Industry": "count"}).rename(columns={"Industry": "Industry Count"}).reset_index()
fig2, ax2 = plt.subplots()
sns.scatterplot(data=scatter_data, x="Industry Count", y="Profit", hue="Country", ax=ax2)
plt.title("Profit vs Industry Count by Country")
plt.savefig("images/scatter_plot.png")

# Choropleth Map
country_profit = df.groupby("Country")["Profit"].sum().reset_index()
fig3 = px.choropleth(country_profit, locations="Country", locationmode="country names", color="Profit", color_continuous_scale="Blues")
fig3.write_image("images/choropleth_map.png")
