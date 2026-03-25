import json
import urllib
import requests
import os
from loguru import logger



def download_ts_categories(ts_file_uri):
    try:
        with open(r'E:\python_projects\craw_movie_trail\default_param\request_data.json','r') as f:
            request_data = json.load(f)
            logger.debug(request_data)

            r = requests.get(ts_file_uri,headers=request_data)
            categories_file_store_path = r'E:\python_projects\craw_movie_trail\core\ts_file_download'
            file_name = 'movie_files_categories.txt'
            final_store_path = os.path.join(categories_file_store_path, file_name)
            logger.debug(r)
            try:
                with open(final_store_path, 'wb') as w:
                    w.write(r.content)

            except Exception as b:
                logger.error(b)

    except Exception as a:
        logger.error(a)

if __name__ == '__main__':
    download_ts_categories(ts_file_uri='https://vip.dytt-network.com/20260218/19961_b6e58b6a/3000k/hls/mixed.m3u8')
