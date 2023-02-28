import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = sea_df['Year']
    y = sea_df['CSIRO Adjusted Sea Level']

    plt.figure(1, figsize = (12, 8))
    ax = plt.subplot()
    ax.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    first_line_x = range(x.min(), 2051)
    first_line_y = slope * first_line_x + intercept

    plt.plot(first_line_x, first_line_y, label = 'First Line of Best Fit: $%.2fx %.2f$, $R^2=%.2f$' % (slope, intercept, r_value ** 2))
    # Create second line of best fit
    x_cleaned = sea_df[sea_df.Year >= 2000]['Year']
    y_cleaned = sea_df[sea_df.Year >= 2000]["CSIRO Adjusted Sea Level"]

    cleaned_slope, cleaned_intercept, cleaned_r_value, cleaned_p_value, cleaned_std_err = linregress(x_cleaned, y_cleaned)

    second_line_x = range(x_cleaned.min(), 2051)
    second_line_y = cleaned_slope * second_line_x + cleaned_intercept

    plt.plot(second_line_x, second_line_y, label = 'Second Line of Best Fit: $%.2fx %.2f$, $R^2=%.2f$' % (cleaned_slope, cleaned_intercept, cleaned_r_value ** 2))
    # Add labels and title
    plt.legend(loc = 'best')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()