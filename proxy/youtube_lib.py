from time import sleep
from abc import ABC, abstractmethod

class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self): pass

    @abstractmethod
    def get_video_info(self): pass

    @abstractmethod
    def download_video(self): pass


class ThirdPartyYoutube(ThirdPartyYoutubeLib):
    def list_videos(self):
        sleep(2)
        print('sending request to list videos')

    def get_video_info(self):
        sleep(1)
        print('sending request to get video info')

    def download_video(self):
        sleep(3)
        print('sending request to download video')
