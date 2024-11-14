import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level Data')

    # Create first line of best fit for entire dataset
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = intercept_all + slope_all * x_all
    plt.plot(x_all, y_all, 'r', label='Best fit line (1880-2050)')

    # Create second line of best fit for data from year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = pd.Series(range(2000, 2051))
    y_2000 = intercept_2000 + slope_2000 * x_2000
    plt.plot(x_2000, y_2000, 'green', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
