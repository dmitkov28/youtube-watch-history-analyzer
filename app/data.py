import json
from typing import Any, Dict

import pandas as pd
from pandas import json_normalize


def load_json_as_df(file_path: str) -> pd.DataFrame:
    with open(file_path, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def load_csv_as_df(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def load_and_preprocess_subscriptions(file_path: str) -> pd.DataFrame:
    df = load_csv_as_df(file_path)
    df.rename(
        columns={
            "Channel Id": "channel_id",
            "Channel Url": "channel_url",
            "Channel Title": "channel_name",
        },
        inplace=True,
    )
    return df


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

    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["hour"] = df["timestamp"].dt.hour

    music = df[df["video_url"].str.contains("music", na=False)].copy()
    videos = df[~df["video_url"].str.contains("music", na=False)].copy()

    music["date"] = music["timestamp"].dt.date
    videos["date"] = videos["timestamp"].dt.date

    heatmap_data = df.groupby(["day_of_week", "hour"]).size().reset_index(name="count")
    days_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    heatmap_data["day_of_week"] = pd.Categorical(
        heatmap_data["day_of_week"], categories=days_order, ordered=True
    )
    heatmap_data = heatmap_data.sort_values("day_of_week", ascending=False)

    return {
        "raw_df": df,
        "heatmap_data": heatmap_data,
    }


def load_and_preprocess_youtube_data() -> pd.DataFrame:
    with open("youtube_data.json", "r") as f:
        data = json.load(f)
        yt_data_df = json_normalize(data)

    subscriptions = load_and_preprocess_subscriptions("./subscriptions.csv")

    yt_data_df["is_subscribed"] = yt_data_df["snippet.channelId"].isin(
        subscriptions["channel_id"]
    )

    return yt_data_df


try:
    watch_history_data = load_and_preprocess_watch_history()
    youtube_data = load_and_preprocess_youtube_data()
    subbed_vs_unsubbed = (
        youtube_data[~youtube_data["snippet.categoryId"].str.contains("10")][
            ["is_subscribed"]
        ]
        .value_counts()
        .reset_index()
    )
    word_cloud_data = " ".join(youtube_data["snippet.title"].dropna().astype(str))
    heatmap_data = watch_history_data["heatmap_data"]
except Exception:
    heatmap_data = pd.DataFrame()
    youtube_data = pd.DataFrame()


def load_watch_history() -> pd.DataFrame:
    df = load_json_as_df("./watch_history.json")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def load_categories() -> pd.DataFrame:
    with open("categories.json", "r") as f:
        categories = json.load(f)
        df = json_normalize(categories)
        df.rename(
            columns={"id": "category_id", "title": "category_title"}, inplace=True
        )
    return df


def load_youtube_video_data() -> pd.DataFrame:
    with open("youtube_data.json", "r") as f:
        data = json.load(f)
    df = json_normalize(data)
    df = df[
        [
            "id",
            "snippet.publishedAt",
            "snippet.channelId",
            "snippet.channelTitle",
            "snippet.title",
            "snippet.description",
            "snippet.description",
            "snippet.thumbnails.standard.url",
            "snippet.tags",
            "snippet.categoryId",
            "contentDetails.duration",
            "statistics.viewCount",
            "statistics.likeCount",
            "statistics.commentCount",
        ]
    ].rename(
        columns={
            "snippet.publishedAt": "date_published",
            "snippet.channelId": "channel_id",
            "snippet.channelTitle": "channel_title",
            "snippet.title": "video_title",
            "snippet.description": "video_description",
            "snippet.thumbnails.standard.url": "video_thumbnail_url",
            "snippet.tags": "video_tags",
            "snippet.categoryId": "video_category_id",
            "contentDetails.duration": "video_duration",
            "statistics.viewCount": "video_views",
            "statistics.likeCount": "video_likes",
            "statistics.commentCount": "video_comments",
        }
    )
    df["video_views"] = df["video_views"].astype(float, errors="ignore")
    df["video_likes"] = df["video_likes"].astype(float, errors="ignore")
    df["video_comments"] = df["video_comments"].astype(float, errors="ignore")
    df["video_duration"] = pd.to_timedelta(df["video_duration"]).dt.total_seconds()
    return df


def load_youtube_channel_data() -> pd.DataFrame:
    with open("youtube_channels_data.json", "r") as f:
        data = json.load(f)
    df = json_normalize(data)

    df = df[
        [
            "channel_id",
            "channel_url",
            "channel_title",
            "channel_date_created",
            "channel_subscribers",
            "channel_total_videos",
            "channel_total_views",
            "channel_thumbnails.medium.url",
        ]
    ].rename(
        columns={
            "channel_url": "channel_custom_url",
            "channel_thumbnails.medium.url": "channel_thumbnail_url",
        }
    )

    return df


def merge_dataframes(
    watch_history: pd.DataFrame,
    youtube: pd.DataFrame,
    categories: pd.DataFrame,
    channels: pd.DataFrame,
) -> pd.DataFrame:
    merged_df = pd.merge(watch_history, youtube, left_on="video_id", right_on="id")
    merged_df.drop(columns=["video_title_y", "channel_title_y"], inplace=True)
    merged_df.rename(
        columns={"video_title_x": "video_title", "channel_title_x": "channel_title"},
        inplace=True,
    )
    merged_df = pd.merge(
        merged_df, categories, left_on="video_category_id", right_on="category_id"
    )
    merged_df = pd.merge(
        merged_df, channels, left_on="channel_title", right_on="channel_title"
    )
    merged_df.drop(columns=["video_category_id", "channel_id_y"], inplace=True)
    merged_df.rename(columns={"channel_id_x": "channel_id"}, inplace=True)
    merged_df = merged_df[~merged_df.duplicated(subset=["timestamp"], keep="first")]

    return merged_df


wh = load_watch_history()
categories = load_categories()
yt = load_youtube_video_data()
channels = load_youtube_channel_data()

merged_data = merge_dataframes(wh, yt, categories, channels)

videos = merged_data[~merged_data["video_url"].str.contains("music")]
yt_music = merged_data[merged_data["video_url"].str.contains("music")]

total_videos = videos["video_id"].nunique()
total_yt_music = yt_music["video_id"].nunique()

avg_videos_per_day = (
    videos.assign(date=videos["timestamp"].dt.date)
    .groupby("date")["video_id"]
    .size()
    .mean()
)

avg_yt_music_per_day = (
    yt_music.assign(date=yt_music["timestamp"].dt.date)
    .groupby("date")["video_id"]
    .size()
    .mean()
)


longest_video = videos.loc[videos["video_duration"].idxmax()].to_dict()
video_with_most_views = videos.loc[videos["video_views"].idxmax()].to_dict()
video_with_most_comments = videos.loc[videos["video_comments"].idxmax()].to_dict()

most_watched_videos = (
    videos.groupby("video_id")
    .agg(
        {
            "video_id": "count",
            "video_title": lambda x: x.iloc[0],
            "channel_title": lambda x: x.iloc[0],
            "video_url": lambda x: x.iloc[0],
            "video_thumbnail_url": lambda x: x.iloc[0],
        }
    )
    .nlargest(columns=["video_id"], n=12)
    .rename(columns={"video_id": "times_watched"})
)

channels_with_most_videos_watched = (
    merged_data[~merged_data["video_url"].str.contains("music")]
    .groupby(by="channel_id")
    .agg(
        {
            "video_id": "count",
            "channel_title": lambda x: x.iloc[0],
            "channel_custom_url": lambda x: x.iloc[0],
            "channel_thumbnail_url": lambda x: x.iloc[0],
        }
    )
    .sort_values(by="video_id", ascending=False)
    .head(12)
    .reset_index()
    .rename(columns={"video_id": "watched_videos"})
)

category_counts = (
    merged_data.groupby("category_title")
    .size()
    .reset_index(name="count")
    .nlargest(columns="count", n=5)
)


videos_timeline = (
    videos.groupby(videos["timestamp"].dt.to_period("W"))["video_id"]
    .count()
    .reset_index()
    .rename(columns={"video_id": "count"})
    .assign(timestamp=lambda x: x["timestamp"].dt.start_time)
)


bins = [0, 60, 300, 900, 1800, float("inf")]
labels = ["<1 min", "1-5 min", "5-15 min", "15-30 min", "30+ min"]
videos.loc[:, "duration_group"] = pd.cut(
    videos["video_duration"], bins=bins, labels=labels, right=False
)
preferred_durations = (
    videos.groupby("duration_group", observed=True)
    .size()
    .reset_index(name="videos")
    .sort_values(by="videos", ascending=False)
)
