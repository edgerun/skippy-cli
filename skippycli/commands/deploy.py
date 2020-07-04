from typing import Set
import logging
import yaml

_config_file = '../tests/skippy.yml'
_skippy_prefix = 'io.skippy.'
_consume_label = 'data.consume'
_produce_label = 'data.produce'
_capability_label = 'policy.capability'


def parse_yaml(config_file: str = None):
    if not config_file:
        config_file = _config_file
    with open(config_file) as f:
        return yaml.safe_load(f)


def extract_skippy_labels(config_file: str = None) -> Set[str]:
    config = parse_yaml(config_file)
    skippy_labels = set()
    skippy_labels.add(extract_label(_consume_label, config))
    skippy_labels.add(extract_label(_produce_label, config))
    skippy_labels.add(extract_label(_capability_label, config))
    logging.info('Skippy labels %s' % skippy_labels)
    return skippy_labels


def extract_label(label_suffix: str, data) -> str:
    label_arr = label_suffix.split('.')
    value = data[label_arr[0]][label_arr[1]]
    if isinstance(value, list):
        label_value = "[{}]".format(','.join(value))
    else:
        label_value = value
    return "{}{}:{}".format(_skippy_prefix, label_suffix, label_value)


def deploy_openfaas(deploy_cmd: str, config_file: str = None) -> None:
    labels=extract_skippy_labels(config_file)
