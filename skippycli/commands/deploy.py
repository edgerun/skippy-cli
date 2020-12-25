from typing import Set
import logging
import yaml
import subprocess
import re

# TODO remove
_skippy_prefix = 'skippy.io.'
_consume_label = 'data.consume'
_produce_label = 'data.produce'
_capability_label = 'policy.capability'
_faas_cli_deploy = 'faas-cli deploy -f '


def parse_yaml(config_file: str = None):
    with open(config_file) as f:
        return yaml.safe_load(f)


def read_skippy_labels(config_file: str = None):
    config = parse_yaml(config_file)
    skippy_labels = list()
    skippy_labels.extend(extract_label(_consume_label, config))
    skippy_labels.extend(extract_label(_produce_label, config))
    skippy_labels.extend(extract_label(_capability_label, config))
    logging.info('Skippy labels %s' % skippy_labels)
    return skippy_labels


def extract_label(label_suffix: str, data):
    label_arr = label_suffix.split('.')
    value = data[label_arr[0]][label_arr[1]]
    labels = list()
    if isinstance(value, list):
        # label_value = "[{}]".format(','.join(value))
        for v in value:
            labels.append("{}{}.{}={}".format(_skippy_prefix, label_suffix, value.index(v), v))
    else:
        label_value = value
        labels.append("{}{}={}".format(_skippy_prefix, label_suffix, label_value))
    logging.debug('labels %s' % labels)
    return labels


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
