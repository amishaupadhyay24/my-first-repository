import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (1880–2050)
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = np.arange(df["Year"].min(), 2051)
    y = result.slope * x + result.intercept
    ax.plot(x, y, color="red")

    # Second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = np.arange(2000, 2051)
    y_recent = result_recent.slope * x_recent + result_recent.intercept
    ax.plot(x_recent, y_recent, color="green")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return figure
    fig.savefig("sea_level_plot.png")
    return fig