# YouTube Downloader

This project is a simple YouTube downloader application built using Python. It utilizes the `yt-dlp` library for downloading videos and `Tkinter` for the graphical user interface (GUI).

## Features

- Download videos in various resolutions (4K, 1080p, 720p) or as MP3 audio.
- User-friendly interface for entering YouTube URLs and selecting download options.
- Progress updates during the download process.

## Requirements

To run this application, you need to have Python installed along with the following dependencies:

- `yt-dlp`
- `tkinter`

You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Run the application by executing the `main.py` file located in the `src` directory.
2. Enter the YouTube video URL in the provided input field.
3. Select the desired resolution or format for the download.
4. Choose the folder where you want to save the downloaded file.
5. Click the "Download" button to start the download process.

## Packaging

To create an executable version of the application, run the following command:

```
python setup.py build
```

This will generate an executable file that you can place on your desktop for easy access.

## Icon

The application uses an icon located in the `assets` directory. This icon will be displayed on the desktop when the executable is created.

## License

This project is open-source and available for personal use. Please refer to the license file for more details.