import threading
import time

import yaml

from config.logger import get_logger
from video_rearranger.video_rearranger import VideoRearranger


class Scheduler(object):
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        with open('config/configuration.yaml') as config:
            self.config = yaml.load(config, Loader=yaml.FullLoader)

    def start(self):
        threading.Thread(target=self.video_rearrange_worker).start()

    def video_rearrange_worker(self):
        self.logger.info('start video rearrange worker')
        while True:
            if self.config['app_switch']['video_rearrange']:
                VideoRearranger().start()
            else:
                self.logger.info('video rearrange disabled')
            time.sleep(self.config['video_rearranger']['schedule_period'])
            self.reload_config()

    def reload_config(self):
        self.logger.info('reload config')
        with open('config/configuration.yaml') as config:
            self.config = yaml.load(config, Loader=yaml.FullLoader)


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.start()
