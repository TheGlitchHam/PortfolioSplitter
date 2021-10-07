import click
from portfoliosplitter import PortfolioSplitter
"""
    Small program to calulate current portfolio split /
    and give advice on where to invest next

    Will also save data and transactions

"""


import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


finance = PortfolioSplitter()
finance.print_next_invest()
finance.invest("EXSA.DE", 100)

@click.group()
def cli():
    pass

if __name__ == "__main__":
    cli()