from core.ts_file_preparations.download_ts_files import download_ts_files
from plugins.about_ui_parts.verify_process.login_progress import login_progress
from tkinter import messagebox


def main_process():
    login_progress()

    if messagebox.askyesno('tips', '确认下载该视频?\n如需下载\n请耐心等待...'):
        download_ts_files()


if __name__ == '__main__':
    main_process()