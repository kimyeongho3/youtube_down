import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import yt_dlp

RESOLUTIONS = ["4K", "1080p", "720p", "mp3"]
YDL_FORMATS = {
    "4K": "bestvideo[height>=2160]+bestaudio/best[height>=2160]",
    "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
    "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
    "mp3": "bestaudio/best"
}

def download_with_ytdlp(url, path, res, status_callback):
    try:
        if not url.strip():
            status_callback("URL을 입력하세요.")
            return
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': YDL_FORMATS[res],
            'noplaylist': True,
            'progress_hooks': [lambda d: status_callback(f"{d['status'].capitalize()}... {d.get('filename', '')}")],
        }
        if res == "mp3":
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_callback("다운로드 완료!")
    except Exception as e:
        status_callback(f"오류 발생: {e}")

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader (yt-dlp)")
        self.geometry("500x300")
        self.resizable(False, False)
        self.create_widgets()
        self.download_thread = None

    def create_widgets(self):
        tk.Label(self, text="YouTube URL:").pack(pady=5)
        self.url_entry = tk.Entry(self, width=60)
        self.url_entry.pack(pady=5)

        tk.Label(self, text="저장 경로:").pack(pady=5)
        path_frame = tk.Frame(self)
        path_frame.pack(pady=5)
        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(path_frame, textvariable=self.path_var, width=45)
        self.path_entry.pack(side=tk.LEFT)
        tk.Button(path_frame, text="폴더 선택", command=self.select_folder).pack(side=tk.LEFT, padx=5)

        tk.Label(self, text="해상도/포맷 선택:").pack(pady=5)
        self.res_var = tk.StringVar(value=RESOLUTIONS[0])
        res_frame = tk.Frame(self)
        res_frame.pack(pady=5)
        for res in RESOLUTIONS:
            tk.Radiobutton(res_frame, text=res, variable=self.res_var, value=res).pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(self, text="", fg="blue")
        self.status_label.pack(pady=10)

        tk.Button(self, text="다운로드", command=self.start_download).pack(pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)

    def set_status(self, msg):
        self.status_label.config(text=msg)
        self.update_idletasks()

    def start_download(self):
        url = self.url_entry.get().strip()
        path = self.path_var.get().strip()
        res = self.res_var.get()
        if not url:
            messagebox.showwarning("입력 오류", "URL을 입력하세요.")
            return
        if not path:
            messagebox.showwarning("입력 오류", "저장 경로를 선택하세요.")
            return
        self.set_status("다운로드 시작...")
        self.download_thread = threading.Thread(target=download_with_ytdlp, args=(url, path, res, self.set_status))
        self.download_thread.start()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()