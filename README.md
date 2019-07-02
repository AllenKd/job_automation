# Job Automation

A CLI to perform frequently task.

## Video Rearrange

Given a folder path, the folder should contains many sub-folder,
each sub-folder contains not only a video file but also many useless files,
the purpose of the rearranger is to move all of the video files from sub-folder
to the given folder and finally remove all useless files.

### Example

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