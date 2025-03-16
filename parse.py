import json
from argparse import ArgumentParser
from typing import Dict, List
from datetime import datetime
from bs4 import BeautifulSoup, Tag


def extract_timestamp(div: Tag) -> str:
    br_tags = div.find_all("br")
    if br_tags:
        timestamp = br_tags[-1].next_sibling

        if timestamp and isinstance(timestamp, str):
            return datetime.strftime(
                datetime.strptime(timestamp.strip(), "%b %d, %Y, %I:%M:%S %p %Z"),
                "%Y-%m-%d %H:%M:%S",
            )

    return ""


def save_to_json(data: List[Dict[str, str]], file_name: str) -> None:
    with open(file_name, "w") as f:
        json.dump(data, f)


def read_data(file_name: str) -> str:
    with open(file_name, "r") as f:
        html = f.read()
    return html


def process_data(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all(
        "div", {"class": "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"}
    )
    result = []
    for div in divs:
        if isinstance(div, Tag):
            links = div.find_all("a")
            timestamp = extract_timestamp(div)

        if len(links) == 2:
            video, channel = links
            if isinstance(video, Tag) and isinstance(channel, Tag):
                item = {
                    "video_title": video.get_text(strip=True),
                    "video_url": video.get("href"),
                    "channel_title": channel.get_text(strip=True),
                    "channel_url": channel.get("href"),
                    "timestamp": timestamp,
                }
                result.append(item)
    return result


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file-path")
    args = parser.parse_args()
    if not args.file_path:
        raise ValueError("File path is required")

    html = read_data(args.file_path)
    parsed_divs = process_data(html)
    save_to_json(parsed_divs, "watch_history.json")
