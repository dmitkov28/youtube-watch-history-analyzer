# YouTube Watch History Analyzer (WIP)

This tool helps you visualize and analyze your YouTube viewing habits by processing your watch history data from Google Takeout.

## Features

- Analyzes your personal YouTube watch history
- Creates interactive visualizations using Plotly Dash
- Reveals insights about your viewing patterns, including:
  - Most watched channels
  - Viewing trends over time
  - Time of day viewing habits
  - Video category preferences

## Installation

```bash
# Clone the repository
git clone https://github.com/dmitkov28/youtube-watch-history-analyzer
cd youtube-watch-analyzer

# Create a virtual environment and install the dependencies
pipenv install
pipenv shell
```

## How to Use

### Step 1: Get Your YouTube Data

1. Go to [Google Takeout](https://takeout.google.com/)
2. Select only "YouTube and YouTube Music" → "History" → "Watch history"
3. Choose your preferred file format (JSON recommended)
4. Create and download the export

### Step 2: Parse your Google Takeout Data

```bash
python parse.py -f "/path/to/your/watch-history.html"
```

### Step 3: Fetch additional metadata passing the json generated in the above step

```bash
python get_additional_metadata.py -f "/path/to/your/watch_history.json"
```


### Step 4: Spin up the dashboard
```bash
python dashboard.py
```

Then open your browser and navigate to `http://localhost:8050`


## Privacy

This tool runs completely on your local machine. Your watch history data is never uploaded or shared with any external service.

## License

Distributed under the MIT License. See `LICENSE` for more information.