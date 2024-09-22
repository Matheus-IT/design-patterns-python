from time import sleep
from abc import ABC, abstractmethod


class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self): pass

    @abstractmethod
    def get_video_info(self, id: int): pass

    @abstractmethod
    def download_video(self, id: int): pass

download_repository = []

def download_exists(id: int):
    return id in download_repository


class ThirdPartyYoutubeManipulator(ThirdPartyYoutubeLib):
    def list_videos(self):
        sleep(2)
        print('sending request to list videos')

    def get_video_info(self, id):
        sleep(1)
        print('sending request to get video info')

    def download_video(self, id):
        sleep(3)
        print('sending request to download video')
        download_repository.append(id)


class CachedThirdPartyYoutubeManipulator(ThirdPartyYoutubeLib):
    __service: ThirdPartyYoutubeLib
    __list_cache = None
    __video_cache = None
    need_reset = False

    def __init__(self, service: ThirdPartyYoutubeLib):
        self.__service = service

    def list_videos(self):
        if self.__list_cache == None or self.need_reset:
            self.__list_cache = self.__service.list_videos()
        return self.__list_cache

    def get_video_info(self, id):
        if self.__video_cache == None or self.need_reset:
            self.__video_cache = self.__service.get_video_info(id)
        return self.__video_cache

    def download_video(self, id):
        if not download_exists(id) or self.need_reset:
            self.__service.download_video(id)


class YoutubeManager:
    _service: ThirdPartyYoutubeLib

    def __init__(self, service: ThirdPartyYoutubeLib):
        self._service = service

    def render_video_page(self, id):
        info = self._service.get_video_info(id)
        print('Rendering video page...')

    def render_list_panel(self):
        list = self._service.list_videos()
        print('Rendering list of video thumbnails')

    def react_on_user_input(self):
        self.render_list_panel()


if __name__ == '__main__':
    youtube_service = ThirdPartyYoutubeManipulator()
    youtube_proxy = CachedThirdPartyYoutubeManipulator(youtube_service)
    manager = YoutubeManager(youtube_proxy)
    manager.react_on_user_input()
