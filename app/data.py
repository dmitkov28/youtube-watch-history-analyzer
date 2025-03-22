from app.processing.analyze import load_json_as_df

df = load_json_as_df("./watch_history.json")
music = df[df["video_url"].str.contains("music")]
videos = df[~df["video_url"].str.contains("music")]

total_yt_music = len(music["video_id"].unique())
total_videos_watched = len(videos["video_id"].unique())

df["date"] = df["timestamp"].dt.date
avg_videos_per_day = df.groupby("date").size().mean()

watched_videos_count = df.groupby(df["timestamp"].dt.to_period("W")).agg(
    {"video_id": "count"}
)
watched_videos_count = watched_videos_count.reset_index()
watched_videos_count["timestamp"] = watched_videos_count["timestamp"].dt.to_timestamp()

top_videos = videos["video_title"].value_counts().head(50).sort_values(ascending=True)
top_channels = (
    videos["channel_title"].value_counts().head(50).sort_values(ascending=True)
)
