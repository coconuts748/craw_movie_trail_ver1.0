import json
from loguru import logger
import os


def verify_messages():
    default_path = r'E:\python_projects\craw_movie_trail\default_param'
    verify_file_name = 'verify_messages.json'
    creat_path = os.path.join(default_path, verify_file_name)
    logger.info(creat_path)

    try:
        with open(creat_path, 'r',) as f:
            data = json.load(f)
            logger.info(data)


    except FileNotFoundError:
        with open(creat_path, 'w') as f:
            write_content = {
                'account' : 'aaa',
                'code' : 'bbb'
            }
            f.write(json.dumps(write_content,ensure_ascii=False))

if __name__ == '__main__':
    verify_messages()