from yt_concate.pipine.pipine import Pipline
from yt_concate.pipine.steps.get_video_list import GetVideoList
from yt_concate.pipine.steps.step import StepException

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipline(steps)
    p.run(inputs)


if __name__ == '__main__' :
    main()
