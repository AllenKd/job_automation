# Job Automation

A CLI to perform frequently task.

## Video Rearrange

Given a folder path, the folder should contains many sub-folder,
each sub-folder contains not only a video file but also many useless files,
the purpose of the rearranger is to move all of the video files from sub-folder
to the given folder and finally all useless files.

### Description

Before rearrange
```
├── video_1
├── video_folder_a
│   ├── foo_a1
│   ├── foo_a2
│   └── video_a
└── video_folder_b
    ├── foo_b1
    ├── foo_b2
    ├── foo_b3
    └── video_b
```

After rearrange

```
├── video_1
├── video_a
└── video_b
```

### Usage

```bash
$ python3 main.py video_rearrange --help
Usage: main.py video_rearrange [OPTIONS]

  Move out the largest file from each sub-folder on given folder.

Options:
  -p, --path TEXT  Specify video folder path  [default:
                   /home/allen/DataDisk/Video]
  --help           Show this message and exit.

```

## Docker Image

```
$ docker pull allensyk/job_automation
```
| Environment Variable | Description |
| :--- | :--- |
| TARGET_PATH | Target path in the container which bind with host target folder. |