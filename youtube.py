async def get_video_metadata(client, video_id):
    response = (
        client.videos()
        .list(part="snippet,statistics,contentDetails", id=video_id)
        .execute()
    )

    if response["items"]:
        return response["items"]
