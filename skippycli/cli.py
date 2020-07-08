import logging
import click

from skippycli.commands.deploy import deploy_openfaas


@click.group()
@click.option('--debug/--no-debug', default=False)
def skippy(debug):
    if debug:
        click.echo('Debug mode is %s' % ('on' if debug else 'off'))
        logging.basicConfig(level=logging.DEBUG)


@skippy.command()
@click.argument('args', nargs=-1)
@click.option('--config', default='skippy.yml')
def deploy(args, config):
    logging.debug('reading skippy.yml')
    logging.debug('arguments %s' % " ".join(args))
    deploy_openfaas(args[0], config)


def main(*args, **kwargs):
    skippy(*args, **kwargs)


if __name__ == '__main__':
    main()
