#! /usr/bin/env python3

"""
a script for regressing and plotting two variables stored in columns of tabular data file
"""

import os
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def compose_plot_file_name(x_label, y_label, category_label = None):
    """
    Creates a name for a plot file based on the labels for the X, Y, and
    categorical variables.
    Parameters
    ----------
    x_label : str 
        The label for the X variable
    y_label : str 
        The label for the Y variable
    category_label : str 
        The label for the categorical variable. 
    Returns
    -------
    str
        The file name.
    """
    category_str = ""
    if category_label:
        category_str = "-by-{0}".format(category_label)
    plot_path = "{0}-v-{1}{2}.pdf".format(x_label, y_label,
            category_str)
    return plot_path
