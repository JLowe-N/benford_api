import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from base64 import b64encode
import io
from math import log


def benford_correlation(digit):
    return round(log(1 + 1 / digit) / log(10), 2)

BENFORD_CURVE = pd.Series({digit: benford_correlation(
    digit) for digit in range(1, 10)})

def get_benford_column(file_body, target_col_header=None):
    def extract_first_digit(number):
        string = str(number)
        first_char = string[0]
        first_digit = int(first_char)

        return first_digit

    dataset = pd.read_csv(io.BytesIO(file_body), sep='\t')
    target_col = dataset['7_2009']
    target_col = target_col.rename('user_data')
    target_col = target_col.transform(extract_first_digit, axis=0)
    target_col = target_col[(target_col.T != 0)]
    target_col = target_col.value_counts(normalize=True)
    benford_df = target_col.to_frame()
    benford_df['correlation'] = BENFORD_CURVE
    benford_df = benford_df.reset_index()
    return benford_df


def get_benford_plot_src_str(benford_df):
    # Create combo chart
    fig, ax = plt.subplots(figsize=(10, 6))
    # bar plot from user data
    sns.barplot(x=benford_df.index, y='user_data', data=benford_df)
    # line plot from Benford's Law
    sns.lineplot(x=benford_df.index, y='correlation', data=benford_df)
    stream = io.BytesIO()
    plot = ax.get_figure()
    plot.savefig(stream, format="png")
    stream.seek(0)
    plot = b64encode(stream.read())
    plot_src = 'data:image/png;base64,' + plot.decode('utf-8')
    return plot_src
