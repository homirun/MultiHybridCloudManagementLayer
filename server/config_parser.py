import yaml
import pymysql
import json


def parse_config(file_path) -> object:
    """
    return instances object and configs object
    :param file_path: configfile path
    :return: instances object, configs object
    """
    if file_path is False:
        configs = _load_file(input('file path => '))
    else:
        configs = _load_file(file_path)

    instances = _parse_instances(configs)
    configs = _parse_configs(configs)
    connection = _db_init()
    _insert_target_instances(connection, instances)
    return instances, configs


def _load_file(file_path: str) -> dict:
    """
    load yaml file
    :param file_path: configfile path
    :return: config
    """
    with open(file_path) as f:
        # example_path: ../docs/example.yaml
        configs = yaml.safe_load(f)
    return configs


def _parse_instances(configs: dict) -> object:
    """
    config parse
    :param configs: config dict
    :return: instances
    """
    instances = []
    for key, value in configs['instances'].items():
        instances.append(Instance(key, instance_type=value['instance-type'], account=value['account']))

    # print(instances)
    return instances


def _parse_configs(configs: dict) -> object:
    config_contents = []
    for key in configs.keys():
        config_contents.append(ConfigContent(key, configs[key]))
    # print(config_contents)
    return config_contents


def _db_init():
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3307,
                                 user='root',
                                 password='hogehoge',
                                 db='mhcml_process',
                                 charset='utf8')
    return connection


def _insert_target_instances(connection: pymysql.connect, instances: dict):
    try:
        with connection as cursor:
            query = \
                "INSERT INTO target_instances (`type`, `authenticate`) values(%s, %s)"
            for instance in instances:
                r = cursor.execute(query, (instance.instance_type, json.dumps(instance.account)))

    except Exception as e:
        print(e)


def _insert_process(connection: pymysql.connect):
    try:
        with connection as cursor:
            query = "INSERT INTO processes (`type`, `action`, `target_instance_id`, finished) values(%s, %s, %d, %s)"
            r = cursor.execute(query, ())
    except Exception as e:
        print(e)


class Instance:
    def __init__(self, instance_name: str, instance_type: str, account: dict) -> None:
        super().__init__()
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.account = account


class ConfigContent:
    def __init__(self, config_name: str, config_dict: dict) -> None:
        super().__init__()
        self.config_name = config_name
        self.config_dict = config_dict


if __name__ == '__main__':
    parse_config(input('file path => '))
