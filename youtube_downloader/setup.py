from setuptools import setup, find_packages

setup(
    name="youtube_downloader",
    version="1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "yt-dlp",
        "tkinter"
    ],
    entry_points={
        'console_scripts': [
            'youtube_downloader=main:YouTubeDownloader',
        ],
    },
    include_package_data=True,
    data_files=[
        ('', ['assets/app.ico']),
    ],
)