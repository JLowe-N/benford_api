import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from base64 import b64encode
import io

def get_benford_column(file_body, target_col_header=None):
    def extract_first_digit(number):
        string = str(number)
        first_char = string[0]
        first_digit = int(first_char)

        return first_digit

    dataset = pd.read_csv(io.BytesIO(file_body), sep='\t')
    target_col = dataset['7_2009']
    target_col = target_col.transform(extract_first_digit, axis=0)
    target_col = target_col[(target_col.T != 0)]
    target_col = target_col.value_counts(normalize=True)
    return target_col


def get_benford_plot_src_str(benford_col):
    ax = sns.barplot(
        x=benford_col.index, y=benford_col)
    stream = io.BytesIO()
    plot = ax.get_figure()
    plot.savefig(stream, format="png")
    stream.seek(0)
    plot = b64encode(stream.read())
    plot_src = 'data:image/png;base64,' + plot.decode('utf-8')
    return plot_src
