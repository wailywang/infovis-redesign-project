
import seaborn as sns
import matplotlib.pyplot as plt
from config import colors_blue, colors_green, DARK_BG, TEXT_COLOR

def fancy_layout(ax):
    ax.set_facecolor(DARK_BG)
    ax.tick_params(colors=TEXT_COLOR)

def plot_all(df, correlation, mean_features):
    fig, axs = plt.subplots(3, 3, figsize=(24, 18), facecolor=DARK_BG)
    fig.subplots_adjust(hspace=0.4, wspace=0.3)

    for ax in axs.flat:
        fancy_layout(ax)

    sns.histplot(df, x='ph', hue='Potability', bins=30, kde=True,
                 palette={0: colors_green[0], 1: colors_green[3]}, ax=axs[0, 0])
    axs[0, 0].set_title("pH Distribution", color=TEXT_COLOR)

    axs[0, 1].barh(correlation.index, correlation.values, color=colors_blue[3])
    axs[0, 1].set_title("Correlation with Potability", color=TEXT_COLOR)

    counts = df['Potability'].value_counts()
    axs[0, 2].pie(counts, labels=['Not Potable', 'Potable'], autopct='%1.1f%%',
                  startangle=90, colors=[colors_green[0], colors_green[3]],
                  textprops={'color': TEXT_COLOR})
    axs[0, 2].set_title("Potability Distribution", color=TEXT_COLOR)

    sns.scatterplot(data=df, x='Conductivity', y='Hardness', hue='Potability',
                    palette={0: colors_green[0], 1: colors_green[3]}, ax=axs[1, 0])
    axs[1, 0].set_title("Conductivity vs Hardness", color=TEXT_COLOR)

    sns.boxplot(data=df, x='Potability', y='Solids', palette=[colors_green[0], colors_green[3]], ax=axs[1, 1])
    axs[1, 1].set_title("Solids by Potability", color=TEXT_COLOR)
    axs[1, 1].set_xticklabels(['Not Potable', 'Potable'], color=TEXT_COLOR)

    sns.violinplot(data=df, x='Potability', y='Organic_carbon', palette=[colors_green[0], colors_green[3]], ax=axs[1, 2])
    axs[1, 2].set_title("Organic Carbon by Potability", color=TEXT_COLOR)
    axs[1, 2].set_xticklabels(['Not Potable', 'Potable'], color=TEXT_COLOR)

    sns.kdeplot(data=df, x='Chloramines', hue='Potability', fill=False,
                palette={0: colors_green[0], 1: colors_green[3]}, ax=axs[2, 0])
    axs[2, 0].set_title("Chloramines Density (Line)", color=TEXT_COLOR)

    sns.heatmap(df.corr(), ax=axs[2, 1], cmap=sns.color_palette(colors_blue, as_cmap=True),
                annot=True, fmt=".2f", linewidths=0.5, cbar=False)
    axs[2, 1].set_title("Correlation Matrix", color=TEXT_COLOR)

    mean_features.plot(kind='bar', ax=axs[2, 2], color=[colors_green[0], colors_green[3]])
    axs[2, 2].set_title("Mean Feature Values by Potability", color=TEXT_COLOR)
    axs[2, 2].legend(['Not Potable', 'Potable'], facecolor=DARK_BG, labelcolor=TEXT_COLOR)

    return fig
