import json
from typing import Any, Dict

import pandas as pd
from pandas import json_normalize


def load_json_as_df(file_path: str) -> pd.DataFrame:
    """
    Load a JSON file and return it as a pandas DataFrame.
    Originally imported from app.processing.analyze but moved here for clarity.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def load_and_preprocess_watch_history() -> Dict[str, Any]:
    """
    Load and preprocess YouTube watch history data.
    Returns a dictionary containing various processed dataframes and statistics.
    """

    df = load_json_as_df("./watch_history.json")

    if "timestamp" in df.columns and not pd.api.types.is_datetime64_any_dtype(
        df["timestamp"]
    ):
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["date"] = df["timestamp"].dt.date

    music = df[df["video_url"].str.contains("music", na=False)].copy()
    videos = df[~df["video_url"].str.contains("music", na=False)].copy()

    music["date"] = music["timestamp"].dt.date
    videos["date"] = videos["timestamp"].dt.date

    total_yt_music = music["video_id"].nunique()
    total_videos_watched = videos["video_id"].nunique()

    avg_videos_per_day = videos.groupby("date").size().mean()
    avg_yt_music = music.groupby("date").size().mean()

    videos_timeline = (
        videos.groupby(videos["timestamp"].dt.to_period("W"))["video_id"]
        .count()
        .reset_index()
        .rename(columns={"video_id": "count"})
    )
    videos_timeline["timestamp"] = videos_timeline["timestamp"].dt.start_time

    watched_videos_count = (
        df.groupby(df["timestamp"].dt.to_period("W"))["video_id"]
        .count()
        .reset_index()
        .rename(columns={"video_id": "count"})
    )
    watched_videos_count["timestamp"] = watched_videos_count[
        "timestamp"
    ].dt.to_timestamp()

    top_videos = videos["video_title"].value_counts().nlargest(10).sort_values()
    top_channels = videos["channel_title"].value_counts().nlargest(50).sort_values()

    return {
        "raw_df": df,
        "music_df": music,
        "videos_df": videos,
        "videos_timeline": videos_timeline,
        "watched_videos_count": watched_videos_count,
        "total_yt_music": total_yt_music,
        "total_videos_watched": total_videos_watched,
        "avg_videos_per_day": avg_videos_per_day,
        "avg_yt_music": avg_yt_music,
        "top_videos": top_videos,
        "top_channels": top_channels,
    }


def load_category_data() -> pd.DataFrame:
    """
    Load and process category data from YouTube.
    Returns top 5 categories with their counts.
    """
    try:

        with open("youtube_data.json", "r") as f:
            data = json.load(f)
            yt_data_df = json_normalize(data)

        with open("categories.json", "r") as f:
            categories = json.load(f)
            categories_df = json_normalize(categories)

        categories_df.rename(
            columns={"id": "category_id", "title": "category_title"}, inplace=True
        )

        merged_df = pd.merge(
            yt_data_df,
            categories_df,
            left_on="snippet.categoryId",
            right_on="category_id",
        )

        categories = (
            merged_df.groupby("category_title")
            .agg({"id": "count"})
            .nlargest(5, columns=["id"])
            .reset_index()
        )

        return categories
    except Exception as e:
        print(f"Error loading category data: {e}")

        return pd.DataFrame(columns=["category_title", "id"])


try:
    youtube_data = load_and_preprocess_watch_history()
    categories = load_category_data()

    total_videos_watched = youtube_data["total_videos_watched"]
    avg_videos_per_day = youtube_data["avg_videos_per_day"]
    total_yt_music = youtube_data["total_yt_music"]
    avg_yt_music = youtube_data["avg_yt_music"]
    videos_timeline = youtube_data["videos_timeline"]
    watched_videos_count = youtube_data["watched_videos_count"]
    top_videos = youtube_data["top_videos"]
    top_channels = youtube_data["top_channels"]
except Exception as e:
    print(f"Error initializing data module: {e}")
    total_videos_watched = 0
    avg_videos_per_day = 0
    total_yt_music = 0
    avg_yt_music = 0
    videos_timeline = pd.DataFrame()
    watched_videos_count = pd.DataFrame()
    top_videos = pd.Series()
    top_channels = pd.Series()
    categories = pd.DataFrame(columns=["category_title", "id"])
