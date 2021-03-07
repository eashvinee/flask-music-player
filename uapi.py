#Youtube Search APi
from youtube_search import YoutubeSearch

class UAPI:
    def search(term):
        results = YoutubeSearch(term, max_results=20).to_dict()
       
        return results

"""
[
    {
        "channel": "Santosh Yadav Madhur",
        "duration": "7:33",
        "id": "zsWFnTAjois",
        "long_desc": "Santosh yadav madhur jogi baba #Santosh yadav madhur jogi baba निर्मात्री:श्री मती ममता यादव गायक :संतोष ...",
        "publish_time": "14 hours ago",
        "thumbnails": [
            "https://i.ytimg.com/vi/zsWFnTAjois/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDhzX6Qokw1qRS6E-bQte7BkLXVFQ",
            "https://i.ytimg.com/vi/zsWFnTAjois/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDdwUFhoWkOk34MJ1V7U1qzal2XgA"
        ],
        "title": "jogi git | धोबी गीत | pardhani ki chunaw ||परधानी के चुनाव | santosh yadav madhur |pardhani git",
        "url_suffix": "/watch?v=zsWFnTAjois",
        "views": "20,006 views"
    }
]
"""