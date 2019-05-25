import datetime
import logging
import os

import yaml

init = False


def get_logger(player_id):
    global init
    if not init:
        if not os.path.exists('log'):
            os.mkdir('log')
        with open('config/configuration.yaml', 'r') as config:
            level = logging.getLevelName(yaml.load(config, Loader=yaml.FullLoader)['logging']['level'])
            logging.basicConfig(level=level,
                                format='%(asctime)s %(filename)s %(lineno)d %(name)s: %(levelname)s %(message)s',
                                datefmt='%y-%m-%d %H:%M:%S',
                                filename='log/{:%Y-%m-%d}.log'.format(datetime.datetime.now()))

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(filename)s %(lineno)d %(name)s: %(levelname)s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        init = True

    logger = logging.getLogger(player_id)

    return logger
