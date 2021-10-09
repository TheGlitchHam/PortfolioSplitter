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

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = PortfolioSplitter()

@cli.command()
@click.pass_obj
def next_invest(ctx):
    """
    This shows the user the next etf to invest into 
    """
    ctx.print_next_invest()

@cli.command()
@click.argument("symbol", required=True)
@click.option("--amount",  default=1, help='Number of positions to be bought.')
@click.pass_obj
def invest(ctx, symbol, amount):
    """This command can be used to direktly invest into a postion
        Takes a symbol
    """
    ctx.invest(symbol, amount)
    click.echo(f"Bought {amount} x {symbol}")


@cli.command()
@click.pass_obj
def symbols(ctx):
    ctx.print_symbol_names()

@cli.command()
@click.pass_obj
def current_values(ctx):
    """This command prints out all positions in portfolio"""
    click.echo(ctx.get_current_values())
    
if __name__ == "__main__":
    cli()