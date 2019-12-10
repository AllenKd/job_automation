import os

import yaml

from config.logger import get_logger


class Util(object):
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        with open('config/configuration.yml') as config:
            self.config = yaml.load(config, Loader=yaml.FullLoader)

    def load_environment_variable(self):
        self.logger.info('start load environment variables and overwrite config file')
        with open('config/configuration.yml') as config:
            config = yaml.load(config, Loader=yaml.FullLoader)

            if os.environ.get('TARGET_PATH'):
                self.logger.debug(
                    'overwrite target path from {} to {}'.format(config['video_rearranger']['target_path'],
                                                                 os.environ.get('TARGET_PATH')))
                config['video_rearranger']['target_path'] = os.environ.get('TARGET_PATH')

        # overwrite config by environment variable
        with open('config/configuration.yml', 'w') as new_config:
            yaml.dump(config, new_config)

        self.logger.debug('finish update config file')
        return

    def get_config(self):
        self.logger.info('getting config')
        return self.config
