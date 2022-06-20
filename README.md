# EgoAction
EgoAction is a multi-scene cross-site dataset for first-person video action recognition research through domain adaptation methods. The dataset contains 5 domains including 6716 action clips. All clips are selected from ADL, GTEA and Kitchen datasets.

## Usage

### Step 1. Video Downloading
The full dataset can be downloaded by running

```python
git clone https://github.com/XianyuanLiu/EgoAction
cd EgoAction
python download_videos.py
```

You can also download videos from the source websites, e.g. [ADL](https://www.csee.umbc.edu/~hpirsiav/papers/ADLdataset/), [GTEA](https://cbs.ic.gatech.edu/fpv/), and [Kitchen](http://kitchen.cs.cmu.edu/main.php).

### Step 2. Frame Extraction
We use [Denseflow](https://github.com/open-mmlab/denseflow) to extract RGB and optical flow frames from videos. You can follow the source instructions to install Denseflow.

### Step 3. Annotations
We provide pickle files for the whole annotations in the dataset for ease of use. These files require python 3.5+ and pandas 1.0.0+ to read.
You can read the annotations by running
```
>>> import pandas as pd
>>> data = pd.read_pickle('gtea.pkl')
```

## Structure
### 1. Data
We use the same structure as follows to store ADL, GTEA and Kitchen in our dataset. `annotations` stores the annotations of each clip. `frames_rgb_flow`stores extracted RGB and optical flow frames. `videos` stores the source video.
Take ADL for example:
```
├─ADL
│  ├─annotations
│  │  └─labels_train_test
│  ├─frames_rgb_flow
│  │  ├─flow
│  │  │  ├─video_name
│  │  │  └─video_name
│  │  └─rgb
│  │     ├─video_name
│  │     └─video_name
│  └─videos
├─GTEA
└─KITCHEN

```

### 2. Annotation File
We create new annotations for all datasets in the following format. We also split the dataset into training and testing sets by the ratio of 8:2 and provide training and testing annotation files individually.
```
[
    "video_name":
    "start_frame":
    "end_frame":
    "action_label":
    "verb_label":
    "class_number":
]
```

## License
You may use the codes and files for research only, including sharing and modifying the material. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
