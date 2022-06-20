import os
import shutil
import zipfile

import requests


os.mkdir("data") if not os.path.exists("data") else None


# Download GTEA videos
def download_gtea():
    url = "https://www.dropbox.com/s/xzdw0mloohtxjn5/gtea_videos.zip?dl=1"
    res = requests.get(url, stream=True)
    with open("data/gtea_videos.zip", "wb") as f:
        for chunk in res.iter_content(chunk_size=10240):
            f.write(chunk)
    print("Downloaded GTEA videos")

    file = zipfile.ZipFile("data/gtea_videos.zip", "r")
    for f in file.namelist():
        file.extract(f, "data/gtea_videos")
    file.close()
    os.remove("data/gtea_videos.zip")
    print("Extracted GTEA videos")


# Download ADL videos
def download_adl():
    os.mkdir("data/adl_videos") if not os.path.exists("data/adl_videos") else None
    url_list = ["http://jasmine.csail.mit.edu/ADLdataset/ADL_videos/P_04.MP4",
                "http://jasmine.csail.mit.edu/ADLdataset/ADL_videos/P_05.MP4",
                "http://jasmine.csail.mit.edu/ADLdataset/ADL_videos/P_06.MP4",
                "http://jasmine.csail.mit.edu/ADLdataset/ADL_videos/P_09.MP4",
                "http://jasmine.csail.mit.edu/ADLdataset/ADL_videos/P_11.MP4",
                ]
    for url in url_list:
        res = requests.get(url, stream=True)
        with open("data/adl_videos/{}".format(url[-8:]), "wb") as f:
            for chunk in res.iter_content(chunk_size=10240):
                f.write(chunk)
        print("Downloaded ADL videos: {}".format(url[-8:]))
    print("Downloaded ADL videos")


# Download KITCHEN videos
def download_kitchen():
    os.mkdir("data/kitchen_videos") if not os.path.exists("data/kitchen_videos") else None
    url_list = ["http://kitchen.cs.cmu.edu/Main/S07_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S09_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S12_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S13_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S14_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S16_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S17_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S18_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S19_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S20_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S22_Brownie_Video.zip",
                "http://kitchen.cs.cmu.edu/Main/S24_Brownie_Video.zip",
                ]
    for url in url_list:
        res = requests.get(url, stream=True)
        with open("data/kitchen_videos/{}".format(url[-21:]), "wb") as f:
            for chunk in res.iter_content(chunk_size=10240):
                f.write(chunk)

        file = zipfile.ZipFile("data/kitchen_videos/{}".format(url[-21:]), "r")
        for f in file.namelist():
            file.extract(f, "data/kitchen_videos/{}".format(url[-21:-3]))
        file.close()
        print("Downloaded KITCHEN videos: {}".format(url[-21:-3]))

        video_list = os.listdir("data/kitchen_videos/{}".format(url[-21:-3]))
        for video in video_list:
            if "7150991" in video and "avi" in video:
                shutil.move("data/kitchen_videos/{}/{}".format(url[-21:-3], video), "data/kitchen_videos")
            else:
                os.remove("data/kitchen_videos/{}/{}".format(url[-21:-3], video))
        os.remove("data/kitchen_videos/{}".format(url[-21:]))
        os.rmdir("data/kitchen_videos/{}".format(url[-21:-3]))
    print("Downloaded KITCHEN videos")


if __name__ == "__main__":
    # download_gtea()
    download_kitchen()
    # download_adl()
