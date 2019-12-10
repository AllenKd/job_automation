import os
import shutil

from hurry.filesize import size

from config.logger import get_logger
from util.util import Util


class VideoRearranger(object):
    def __init__(self, path):
        self.logger = get_logger(self.__class__.__name__)
        self.config = Util().get_config()
        self.video_folder_path = path
        self.ignore_folder = []
        self.logger.info('video rearranger initialized, video path: {}'.format(self.video_folder_path))

    def start(self):
        self.logger.info('start rearrange')
        for folder_name in os.listdir(self.video_folder_path):
            if not os.path.isdir('{}/{}'.format(self.video_folder_path, folder_name)):
                self.logger.debug('{} is not folder, skip'.format(folder_name))
                continue

            largest_file = self.get_largest_file(folder_name)

            if not self.is_allowed_extension(largest_file):
                self.logger.warn('{} not in expected file extension, add to ignore folder')
                self.ignore_folder.append(largest_file)
                continue

            self.move_out(self.get_largest_file(folder_name))

        self.clean_folder()
        self.logger.info('finished video rearrange, ignore folder: {}'.format(self.ignore_folder))

    def get_largest_file(self, folder_name):
        self.logger.info('start get largest file')
        folder_path = '{}/{}'.format(self.video_folder_path, folder_name)
        largest_file = ""
        largest_size = 0
        for afile in os.listdir(folder_path):
            file_abs_path = '{}/{}'.format(folder_path, afile)
            if largest_size < os.path.getsize(file_abs_path):
                largest_file = file_abs_path
                largest_size = os.path.getsize(file_abs_path)
        self.logger.info('largest file: {}, size: {}'.format(os.path.basename(largest_file), size(largest_size)))
        return largest_file

    def is_allowed_extension(self, file_abs_path):
        return os.path.splitext(file_abs_path)[-1] in self.config['video_rearranger']['expected_extension']

    def move_out(self, file_path):
        self.logger.info('start move file out: {}'.format(file_path))
        os.rename(file_path, '{}/{}'.format(self.video_folder_path, os.path.basename(file_path)))

    def clean_folder(self):
        self.logger.info('start clean folder')
        for folder_name in os.listdir(self.video_folder_path):
            if os.path.isdir(
                    '{}/{}'.format(self.video_folder_path, folder_name)) and folder_name not in self.ignore_folder:
                self.logger.debug('remove folder: {}'.format(folder_name))
                shutil.rmtree('{}/{}'.format(self.video_folder_path, folder_name))
