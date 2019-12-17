import yaml


def parse_config():
    file_path = input('file path => ')
    configs = load_file(file_path)
    parse_instances(configs)
    parse_configs(configs)


def load_file(file_path: str) -> dict:
    """
    load yaml file
    :param file_path: configfile path
    :return: config
    """
    with open(file_path) as f:
        # example_path: ../docs/example.yaml
        configs = yaml.safe_load(f)
    return configs


def parse_instances(configs: dict) -> object:
    instances = []
    for key, value in configs['instances'].items():
        instances = Instance(key, instance_type=value['instance-type'], account=value['account'])

    return instances


def parse_configs(configs: dict) -> object:
    config_contents = []
    for key in configs.keys():
        config_contents = ConfigContent(key, configs[key])

    return config_contents


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
    parse_config()
