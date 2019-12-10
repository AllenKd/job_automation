import os

import click

from util.util import Util
from video_rearranger.video_rearranger import VideoRearranger


@click.group()
def cli():
    pass


@click.command('video_rearrange', help='Move out the largest file from each sub-folder on given folder.')
@click.option('--path', '-p',
              default=os.environ['VIDEO_PATH'] if 'VIDEO_PATH' in os.environ else
              Util().get_config()['video_rearranger']['target_path'],
              help='Specify video folder path', show_default=True)
def video_rearrange(path):
    VideoRearranger(path).start()


if __name__ == '__main__':
    cli.add_command(video_rearrange)
    cli()
