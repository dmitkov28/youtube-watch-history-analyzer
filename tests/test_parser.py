
from parse import process_youtube_watch_history_data, read_data

test_html = """
<div class="mdl-grid">
   <div class="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp">
      <div class="mdl-grid">
         <div class="header-cell mdl-cell mdl-cell--12-col">
            <p class="mdl-typography--title">YouTube<br></p>
         </div>
         <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Watched&nbsp;<a href="https://www.youtube.com/watch?v=1k37OcjH7BM">Andrew Ng: Advice on Getting Started in Deep Learning | AI Podcast Clips</a><br><a href="https://www.youtube.com/channel/UCSHZKyawb77ixDdsGog4iWA">Lex Fridman</a><br>Mar 15, 2025, 4:49:42 PM EET</div>
         <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1 mdl-typography--text-right"></div>
         <div class="content-cell mdl-cell mdl-cell--12-col mdl-typography--caption"><b>Products:</b><br> YouTube<br><b>Why is this here?</b><br> This activity was saved to your Google Account because the following settings were on:&nbsp;YouTube watch history.&nbsp;You can control these settings &nbsp;<a href="https://myaccount.google.com/activitycontrols">here</a>.</div>
      </div>
   </div>
   <div class="mdl-grid">
      <div class="header-cell mdl-cell mdl-cell--12-col">
         <p class="mdl-typography--title">YouTube<br></p>
      </div>
      <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Watched&nbsp;<a href="https://www.youtube.com/watch?v=OAKNiSmpDOA">How To Gain Code Execution | Prime Reacts</a><br><a href="https://www.youtube.com/channel/UCUyeluBRhGPCW4rPe_UvBZQ">ThePrimeTime</a><br>Mar 15, 2025, 4:49:02 PM EET</div>
      <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1 mdl-typography--text-right"></div>
      <div class="content-cell mdl-cell mdl-cell--12-col mdl-typography--caption"><b>Products:</b><br> YouTube<br><b>Why is this here?</b><br> This activity was saved to your Google Account because the following settings were on:&nbsp;YouTube watch history.&nbsp;You can control these settings &nbsp;<a href="https://myaccount.google.com/activitycontrols">here</a>.</div>
   </div>
   <div class="mdl-grid">
      <div class="header-cell mdl-cell mdl-cell--12-col">
         <p class="mdl-typography--title">YouTube<br></p>
      </div>
      <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Watched&nbsp;<a href="https://www.youtube.com/watch?v=OAKNiSmpDOA">How To Gain Code Execution | Prime Reacts</a><br><a href="https://www.youtube.com/channel/UCUyeluBRhGPCW4rPe_UvBZQ">ThePrimeTime</a><br>Mar 15, 2025, 4:49:02 PM EET</div>
      <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1 mdl-typography--text-right"></div>
      <div class="content-cell mdl-cell mdl-cell--12-col mdl-typography--caption"><b>Products:</b><br> YouTube<br><b>Why is this here?</b><br> This activity was saved to your Google Account because the following settings were on:&nbsp;YouTube watch history.&nbsp;You can control these settings &nbsp;<a href="https://myaccount.google.com/activitycontrols">here</a>.</div>
   </div>
</div>
"""


def test_process_data():
    expected = [
        {
            "video_title": "Andrew Ng: Advice on Getting Started in Deep Learning | AI Podcast Clips",
            "video_url": "https://www.youtube.com/watch?v=1k37OcjH7BM",
            "video_id": "1k37OcjH7BM",
            "channel_title": "Lex Fridman",
            "channel_url": "https://www.youtube.com/channel/UCSHZKyawb77ixDdsGog4iWA",
            "timestamp": "2025-03-15 16:49:42",
        },
        {
            "video_title": "How To Gain Code Execution | Prime Reacts",
            "video_url": "https://www.youtube.com/watch?v=OAKNiSmpDOA",
            "video_id": "OAKNiSmpDOA",
            "channel_title": "ThePrimeTime",
            "channel_url": "https://www.youtube.com/channel/UCUyeluBRhGPCW4rPe_UvBZQ",
            "timestamp": "2025-03-15 16:49:02",
        },
        {
            "video_title": "How To Gain Code Execution | Prime Reacts",
            "video_url": "https://www.youtube.com/watch?v=OAKNiSmpDOA",
            "video_id": "OAKNiSmpDOA",
            "channel_title": "ThePrimeTime",
            "channel_url": "https://www.youtube.com/channel/UCUyeluBRhGPCW4rPe_UvBZQ",
            "timestamp": "2025-03-15 16:49:02",
        },
    ]

    got = process_youtube_watch_history_data(test_html)
    assert expected == got


def test_read_data(tmp_path):
    f = tmp_path / "test.html"
    f.write_text("Hello, World!")

    result = read_data(str(f))
    assert result == "Hello, World!"
