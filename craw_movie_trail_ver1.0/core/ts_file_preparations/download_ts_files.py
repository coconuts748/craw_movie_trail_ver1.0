import json
import os
import requests
from core.ts_file_preparations.tidy_up_ts_files import tidy_up_ts_files
from loguru import logger


def download_ts_files():

    pure_ts_files_category = tidy_up_ts_files()

    ts_num = len(pure_ts_files_category)
    request_header = 'https://vip.dytt-network.com/20260218/19961_b6e58b6a/3000k/hls/'

    record_process = {}

    for o in range(0, ts_num):
        limited_url = f"{request_header + pure_ts_files_category[o]}".strip()
        logger.debug(limited_url)
        logger.debug('**********************')

        ts_file_save_path = r'E:\python_projects\craw_movie_trail\core\ts_file_download'
        file_name = f'num_{o}.ts'
        final_file_save_path = os.path.join(ts_file_save_path, file_name)


        # request_param_path = r'E:\python_projects\craw_movie_trail\default_param\request_data.json'
        try:
            request_data = {
                'referer' : 'https://vip.dyttzyplay.com/',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
            }

            r = requests.get(limited_url, params=request_data)
            with open(final_file_save_path, 'wb') as f1:
                f1.write(r.content)
            record_process[f'{limited_url}'] = 'done'



        except Exception as a:
            logger.error(a)
            record_process[f'{limited_url}'] = 'error'



if __name__ == '__main__':
    download_ts_files()