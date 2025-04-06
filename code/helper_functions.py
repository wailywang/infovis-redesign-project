# Optional
import pandas as pd

def format_currency(x):
    """Format a number as currency string."""
    return "${:,.2f}".format(x)

def standardize_dates(df, column_name):
    """Convert a column to datetime and add YearMonth column."""
    df[column_name] = pd.to_datetime(df[column_name])
    df["YearMonth"] = df[column_name].dt.to_period("M").astype(str)
    return df

def get_profit_summary(df):
    """Prints summary stats for Profit column."""
    print("Profit Summary:")
    print(df["Profit"].describe())
    print(f"Total Profit: {df['Profit'].sum():,.2f}")
    print(f"Total Orders: {df['Order ID'].nunique()}")

def apply_color_palette(palette_name="Blues"):
    """Returns color map for visual consistency."""
    import matplotlib.cm as cm
    return cm.get_cmap(palette_name)
