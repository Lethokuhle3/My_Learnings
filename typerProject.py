import typer

def main(a: string ,b: int):
    typer.echo(f"welcome to typer")
    typer.echo(f"The value of <a> is {a} and the value of <b> is {b}")


if __name__== '__main__':
    typer.run(main)

