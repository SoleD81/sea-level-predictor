import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(12, 6))

    x = df['Year']
    x1 = range(1880, 2051, 1)
    x2 =  range(2000, 2051, 1)
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y, color = 'steelblue')

    # Create first line of best fit
    fitl_1880_2012 = linregress(x, y)
    ### Cálculo de la pendiente y la intercepción para que encaje lo mejor posible con los datos representados en el Scatter
    y_predict_1 = fitl_1880_2012.intercept + fitl_1880_2012.slope * x1
    plt.plot(x1, y_predict_1, color='green')

    # Create second line of best fit
    fit2_2000_2050 = linregress(df.query('Year >= 2000')['Year'], 
                                df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    y_predict_2 = fit2_2000_2050.intercept + fit2_2000_2050.slope * x2
    plt.plot(x2, y_predict_2, color='orange')

    # Add labels and title
    axes.set(xlabel = 'Year', ylabel = 'Sea Level (inches)')
    axes.set_title('Rise in Sea Level')


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()