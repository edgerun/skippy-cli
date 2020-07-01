import logging

import click


@click.group()
@click.option('--debug/--no-debug', default=False)
def skippy(debug):
    if debug:
        click.echo('Debug mode is %s' % ('on' if debug else 'off'))
        logging.basicConfig(level=logging.DEBUG)


@skippy.command()
def build():
    print('creating skippy.yaml')


def main(*args, **kwargs):
    skippy(*args, **kwargs)


if __name__ == '__main__':
    main()
