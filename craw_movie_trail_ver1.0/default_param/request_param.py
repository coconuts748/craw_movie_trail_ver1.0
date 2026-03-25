import json
import os
from loguru import logger

request_param_data = {

    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}



def request_param():
    source_path = r'E:\python_projects\craw_movie_trail\default_param'
    request_data_name = 'request_data.json'
    request_data_path = os.path.join(source_path, request_data_name)
    logger.debug(request_data_path)

    try:
        with open(request_data_path, 'w') as f:
            f.write(json.dumps(request_param_data, ensure_ascii=False))

    except Exception as a:
        logger.error(a)

if __name__ == '__main__':
    request_param()
