import asyncio
import itertools
import json
import os
from argparse import ArgumentParser
from typing import Any, Dict, List

from dotenv import load_dotenv
from googleapiclient.discovery import build

from app.processing.youtube import get_channel_metadata, get_video_metadata


def save_to_json(data: List[Dict[str, str]], file_name: str) -> None:
    with open(file_name, "w") as f:
        json.dump(data, f)


def read_data(file_name: str) -> List[Dict]:
    with open(file_name, "r") as f:
        videos = json.load(f)
    return videos


def process_video_ids(data: List[Dict]) -> List[str]:
    video_ids = [str(video.get("video_id")) for video in data]
    return video_ids


def process_channel_ids(data: List[Dict]) -> List[str]:
    channel_ids = [str(video.get("channel_url")) for video in data]
    return channel_ids


def save_data(data: List[Any], file_path: str):
    with open(file_path, "w") as f:
        json.dump(data, f)


async def get_videos_metadata(client, video_ids: List[str], batch_size=50):
    tasks = []
    for i in range(0, len(video_ids), batch_size):
        batch_ids = ",".join(video_ids[i : i + batch_size])
        task = asyncio.create_task(get_video_metadata(client, batch_ids))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def get_channels_metadata(client, channel_ids: List[str], batch_size=50):
    tasks = []
    for i in range(0, len(channel_ids), batch_size):
        batch_ids = ",".join(channel_ids[i : i + batch_size])
        task = asyncio.create_task(get_channel_metadata(client, batch_ids))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file-path")
    args = parser.parse_args()
    if not args.file_path:
        raise ValueError("File path is required")

    load_dotenv()

    API_KEY = os.getenv("YOUTUBE_API_KEY")
    client = build("youtube", "v3", developerKey=API_KEY)

    watch_history_videos = read_data(args.file_path)
    watch_history_video_ids = list(set(process_video_ids(watch_history_videos)))
    watch_history_channel_ids = list(
        set(
            [
                channel.split("/")[-1]
                for channel in process_channel_ids(watch_history_videos)
            ]
        )
    )
    youtube_videos_data = asyncio.run(
        get_videos_metadata(client, watch_history_video_ids)
    )
    save_data(
        list(itertools.chain(*youtube_videos_data)), file_path="youtube_data.json"
    )

    youtube_channels_data = asyncio.run(
        get_channels_metadata(client, watch_history_channel_ids)
    )
    save_data(
        list(itertools.chain(*youtube_channels_data)),
        file_path="youtube_channels_data.json",
    )
