from loguru import logger


def tidy_up_ts_files():

    load_source_path = r'E:\python_projects\craw_movie_trail\core\ts_file_download\movie_files_categories.txt'
    with open(load_source_path,'r') as r:
        source_content = str(r.read())
        split_source_content = source_content.split('\n')
        # logger.debug(split_source_content)
        pure_ts_list = []
        for i in split_source_content:
            # logger.debug(i)
            # logger.error("@@@@@@@@@@@@@@@@@@@@@@@@@@")
            if '.ts' in i:
                pure_ts_list.append(i)
            else:
                pass

        # for j in pure_ts_list:
        #     logger.info(j)
        #     logger.info("!!!!!!!!!!!!!!!!!!!!")

        return pure_ts_list

if __name__ == '__main__':
    tidy_up_ts_files()
