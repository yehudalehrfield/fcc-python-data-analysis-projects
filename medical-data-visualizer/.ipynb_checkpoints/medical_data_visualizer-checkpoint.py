import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight']/((df['height']/100)**(2))) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(data=df_cat.value_counts(), columns=[
                          "total"]).sort_index().reset_index()

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, col='cardio', kind='bar',
                x='variable', y='total', hue='value')

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, col='cardio', kind='bar',
                      x='variable', y='total', hue='value').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    filterBloodPres = (df['ap_lo'] <= df['ap_hi'])
    filterHeight = (df['height'] >= df['height'].quantile(.025)) & (
        df['height'] <= df['height'].quantile(.975))
    filterWeight = (df['weight'] <= df['weight'].quantile(.975)) & (
        df['weight'] >= df['weight'].quantile(.025))
    df_heat = df[filterBloodPres & filterHeight & filterWeight]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr).astype('bool')

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr,
                mask=mask,
                cmap='crest',
                linewidths=.5,
                annot=True,
                fmt='.1f',
                annot_kws={
                    'fontsize': 8,
                    'fontweight': 'bold'
                })

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
