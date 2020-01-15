import sys
from config_parser import parse_config


def main():
    args = sys.argv
    if 1 >= len(args):
        config_path = False
    else:
        config_path = args[1]

    instances, configs = parse_config(config_path)
    for i in instances:
        print(i.instance_name)


if __name__ == '__main__':
    main()
