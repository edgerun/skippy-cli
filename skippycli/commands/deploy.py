from typing import Set
import logging
import yaml
import subprocess
import re

# TODO remove
_config_file = '../tests/skippy.yml'
_skippy_prefix = 'io.skippy.'
_consume_label = 'data.consume'
_produce_label = 'data.produce'
_capability_label = 'policy.capability'
_faas_cli_deploy = 'faas-cli deploy -f '


def parse_yaml(config_file: str = None):
    if not config_file:
        config_file = _config_file
    with open(config_file) as f:
        return yaml.safe_load(f)


def read_skippy_labels(config_file: str = None) -> Set[str]:
    config = parse_yaml(config_file)
    skippy_labels = set()
    skippy_labels.add(extract_label(_consume_label, config))
    skippy_labels.add(extract_label(_produce_label, config))
    skippy_labels.add(extract_label(_capability_label, config))
    logging.info('Skippy labels %s' % skippy_labels)
    return skippy_labels


def extract_label(label_suffix: str, data) -> Set[str]:
    label_arr = label_suffix.split('.')
    value = data[label_arr[0]][label_arr[1]]
    labels= set()
    if isinstance(value, list):
        # label_value = "[{}]".format(','.join(value))
        for v in value:
            print()

    else:
        label_value = value
    return "{}{}={}".format(_skippy_prefix, label_suffix, label_value)


def deploy_openfaas(deploy_cmd: str, config_file: str = None) -> None:
    skippy_config_path = build_skippy_config_path(deploy_cmd, config_file)
    labels = read_skippy_labels(skippy_config_path)
    cmd = _faas_cli_deploy + deploy_cmd + ' --label ' + ' --label '.join(labels)
    logging.debug('cmd %s' % cmd)
    subprocess.run(cmd, shell=True, check=True)


def build_skippy_config_path(deploy_cmd: str, config_file: str) -> str:
    deploy_cmd = deploy_cmd.replace('.yml', '')
    skippy_config_dir = re.sub('[^0-9a-zA-Z-]', '', deploy_cmd)
    skippy_config_path = skippy_config_dir + '/' + config_file
    logging.debug('Skippy config path %s' % skippy_config_path)
    return skippy_config_path
