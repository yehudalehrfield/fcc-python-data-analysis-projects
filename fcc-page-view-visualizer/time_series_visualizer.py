import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
filterTop = (df['value'] <= df['value'].quantile(.975))
filterBottom = df['value'] >= df['value'].quantile(.025)
# df_filtered = df[filterTop & filterBottom]
df = df[filterTop & filterBottom]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(14, 6))
  # ax.plot(df_filtered, linestyle='solid', markersize=0)
  ax.plot(df, linestyle='solid', markersize=0)
  plt.ylabel('Page Views')
  plt.xlabel('Date')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  # Maybe we should copy df instead of df_filtered
  # df_bar = df_filtered.copy()
  df_bar = df.copy()
  df_bar['month'] = df_bar.index.month
  df_bar['year'] = df_bar.index.year
  df_bar = df_bar.groupby(['year', 'month']).mean()
  df_bar = df_bar.reset_index(drop=False)
  df_bar['month_name'] = pd.to_datetime(df_bar['month'],
                                        format='%m').dt.month_name()

  # Draw bar plot
  month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
  ]
  fig = sns.catplot(data=df_bar,
                    kind='bar',
                    x='year',
                    y='value',
                    hue='month_name',
                    palette='Spectral',
                    hue_order=month_order)
  fig.set(xlabel='Years', ylabel='Average Page Views')
  plt.legend(title='Months') # fcc doesn't read the other legend and will give an error without this
  legend = fig._legend
  legend.set_title('Months')

  # Save image and return fig (don't change this part)
  fig = fig.fig # this bypasses fcc AttributeErrors
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, ax = plt.subplots(1,2, figsize=(15,5))
  month_order = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  
  year_box_plot = sns.boxplot(
    data=df_box,
    x='year',
    y='value',
    fliersize=1.5,
    flierprops=dict(marker='o'),
    saturation=.85,
    linewidth=.5,
    ax = ax[0]
  ).set(
      xlabel='Year',
      ylabel='Page Views',
      title='Year-wise Box Plot (Trend)'
  )
  month_box_plot = sns.boxplot(
      data=df_box,
      x='month',
      y='value',
      fliersize=1.5,
      flierprops=dict(marker='o'),
      saturation=.85,
      linewidth=.5,
      order=month_order,
      ax = ax[1]
  ).set(
      xlabel='Month',
      ylabel='Page Views',
      title='Month-wise Box Plot (Seasonality)'
  )

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
