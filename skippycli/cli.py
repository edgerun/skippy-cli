import logging

import click


@click.group()
@click.option('--debug/--no-debug', default=False)
def symmetry(debug):
    if debug:
        click.echo('Debug mode is %s' % ('on' if debug else 'off'))
        logging.basicConfig(level=logging.DEBUG)


@symmetry.command()
def build():
    print('creating skippy.yaml')


def main(*args, **kwargs):
    symmetry(*args, **kwargs)


if __name__ == '__main__':
    main()
