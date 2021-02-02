import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from base64 import b64encode
import io
from math import log
from scipy.stats import chisquare


def benford_correlation(digit):
    return log(1 + 1 / digit) / log(10)


BENFORD_CURVE = pd.Series({digit: benford_correlation(
    digit) for digit in range(1, 10)})


def get_benford_column(file_body, target_col_header=None):
    def extract_first_digit(number):
        string = str(number)
        first_char = string[0]
        first_digit = int(first_char)

        return first_digit

    # extract leading digit from target column, drop 0 values
    dataset = pd.read_csv(io.BytesIO(file_body), sep='\t')
    target_col = dataset['7_2009']
    target_col = target_col.rename('actual_freq')
    target_col = target_col.transform(extract_first_digit, axis=0)
    target_col = target_col[(target_col.T != 0)]

    # perform chi-square test, CL95 target
    actual_freq = target_col.value_counts()
    observation_count = actual_freq.sum()
    expected_freq = pd.Series(
        [int(round(fraction * observation_count, 0)) for fraction in BENFORD_CURVE])
    print(expected_freq)

    # convert counts to percentage
    benford_df = actual_freq.to_frame().reset_index()
    benford_df['expected_freq'] = expected_freq
    benford_df = benford_df.rename(columns={'index': 'digit'})
    print(benford_df)
    return benford_df


def get_p_value(actual_freq, observed_freq):
    (_, p_value) = chisquare(actual_freq, observed_freq)
    return p_value


def get_benford_plot_src_str(benford_df):
    # Calculate p_value for plot
    print(benford_df)
    p_val = round(get_p_value(
        benford_df['actual_freq'], benford_df['expected_freq']), 4)
    print(p_val)
    # Create combo chart
    fig, ax = plt.subplots(figsize=(10, 6))
    # bar plot from user data
    sns.barplot(x='digit', y='actual_freq', data=benford_df)
    # line plot from Benford's Law
    sns.lineplot(x=benford_df.index, y='expected_freq', data=benford_df,
                 color="black", label="Benford's Law Distribution", linestyle="-")

    # annotate plot with labels
    plt.title("Benford's Law")
    plt.xlabel("Leading Digit")
    plt.ylabel("Frequency")
    plt.gcf().text(0.10, 0.90, f'p = {p_val}', fontsize=14)

    # convert to base64 encoded PNG, for use in <img> src template
    stream = io.BytesIO()
    plot = ax.get_figure()
    plot.savefig(stream, format="png")
    stream.seek(0)
    plot = b64encode(stream.read())
    plot_src = 'data:image/png;base64,' + plot.decode('utf-8')

    return plot_src
