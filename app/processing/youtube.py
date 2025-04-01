async def get_video_metadata(client, video_id):
    response = (
        client.videos()
        .list(part="snippet,statistics,contentDetails", id=video_id)
        .execute()
    )

    if response["items"]:
        return response["items"]


def get_video_categories(client, region_code="US"):
    response = (
        client.videoCategories().list(part="snippet", regionCode=region_code).execute()
    )

    categories = []
    for item in response.get("items", []):
        categories.append({"id": item["id"], "title": item["snippet"]["title"]})

    return categories


async def get_channel_metadata(client, channel_id):
    request = client.channels().list(part="snippet,statistics", id=channel_id)
    response = request.execute()
    channels = []

    for channel in response.get("items", []):
        _id = channel["id"]
        title = channel["snippet"]["title"]
        description = channel["snippet"]["description"]
        date_created = channel["snippet"]["publishedAt"]
        thumbnails = channel["snippet"]["thumbnails"]
        url = channel["snippet"].get("customUrl")
        subscribers = channel["statistics"]["subscriberCount"]
        videos = channel["statistics"]["videoCount"]
        views = channel["statistics"]["viewCount"]

        channels.append(
            {
                "channel_id": _id,
                "channel_url": url,
                "channel_title": title,
                "channel_description": description,
                "channel_date_created": date_created,
                "channel_subscribers": subscribers,
                "channel_total_videos": videos,
                "channel_total_views": views,
                "channel_thumbnails": thumbnails,
            }
        )
    return channels
