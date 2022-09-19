# EgoAction Dataset
EgoAction Dataset is a multi-scene cross-site dataset for 
first-person video action recognition research through 
domain adaptation methods. 
The dataset contains ADL-7 and GTEA_KITCHEN-6 with 5 domains including 6716 action clips. 
All clips are selected from ADL, GTEA and Kitchen datasets.

The table below compares the settings of our dataset to other related first-person datasets.
G_K-6 refers to GTEA_KITCHEN-6.

|              | First-person | Multi-domain | Multi-scene | Cross-site |
|:------------:|:------------:|:------------:|:-----------:|:----------:|
|   ADL [1]    |   &check;   |   &cross;    |   &cross;   |  &cross;   |
|   GTEA [2]   |   &check;   |   &cross;    |   &cross;   |  &cross;   |
| KITCHEN [3]  |   &check;   |   &cross;    |   &cross;   |  &cross;   |
| EPIC-97 [4]  |   &check;   |   &check;    |   &cross;   |  &cross;   |
|  EPIC-8 [5]  |   &check;   |   &check;    |   &cross;   |  &cross;   |
| ADL-7 (ours) |   &check;   |   &check;    |   &check;   |  &cross;   |
| G_K-6 (ours) |   &check;   |   &check;    |   &cross;   |  &check;   |

## Usage

### Step 1. Video Downloading
The full dataset can be downloaded by running

```
git clone https://github.com/XianyuanLiu/EgoAction
cd EgoAction
python download_videos.py
```

You can also download videos directly from the source websites if the code fails to run, i.e. [ADL](https://www.csee.umbc.edu/~hpirsiav/papers/ADLdataset/), [GTEA](https://cbs.ic.gatech.edu/fpv/), and [Kitchen](http://kitchen.cs.cmu.edu/main.php).

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

## Acknowledgement

This implementation is based on early works [1], [2], [3], [4] and [5]. We thank the authors for sharing their datasets.

## Reference

```
[1] H. Pirsiavash and D. Ramanan, “Detecting activities of daily living in first-person camera views,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2012.

[2] A. Fathi, X. Ren, and J. M. Rehg, “Learning to recognize objects in egocentric activities,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.

[3] F. de la Torre, J. K. Hodgins, J. Montano, and S. Valcarcel, “Detailed human data acquisition of kitchen activities: the CMU-multimodal activity database (CMU-MMAC),” in Proceedings of the ACM SIGCHI Conference on Human Factors in Computing Systems (CHI) Workshop, 2009.

[4] D. Damen, H. Doughty, G. M. Farinella, A. Furnari, E. Kazakos, J. Ma, D. Moltisanti, J. Munro, T. Perrett, W. Price et al., “Rescaling egocentric vision: Collection, pipeline and challenges for EPIC-KITCHENS-100,” International Journal of Computer Vision (IJCV), 2022.

[5] J. Munro and D. Damen, “Multi-modal domain adaptation for fine-grained action recognition,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2020.
```
