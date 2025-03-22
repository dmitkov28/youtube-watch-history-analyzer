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
