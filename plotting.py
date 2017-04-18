import matplotlib.pyplot as plt
import textwrap


def plot_bar_group_count(
        data, field, title, title_pad=1.05, label_pad=15, wrap_chars=10
):

    sizes = data.groupby(field).size()

    axes = sizes.plot.barh()
    axes.set_title(title, y=title_pad)
    axes.set_xlabel("Frequency", labelpad=label_pad)
    axes.set_ylabel(field, labelpad=label_pad)

    labels = ['\n'.join(textwrap.wrap(str(label), wrap_chars, break_long_words=False)) for label in sizes.keys()]
    axes.set_yticklabels(labels)

    return axes


def plot_pie_group_count(
        data, field, title, percent_format="%1.1f%%", title_pad=1.1
):

    sizes = data.groupby(field).size()

    axes = sizes.plot.pie(autopct=percent_format)
    axes.set_title(title, y=title_pad)
    axes.set_ylabel('')
    axes.axis("equal")

    return axes
