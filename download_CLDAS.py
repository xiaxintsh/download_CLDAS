import os
import requests
from glob import glob

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    local_filename = url.split('/')[-1][0:70]
    print(local_filename)
    local_path = os.path.join(dest_folder, local_filename)
    # print(local_path)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_path

def download_files_from_txt(directory, dest_folder):
    txt_files = glob(os.path.join(directory, '*.txt'))
    for txt_file in txt_files:
        with open(txt_file, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url:  # Check if the line is not empty
                    try:
                        download_file(url, dest_folder)
                        # print(f'Successfully downloaded {url}')
                    except Exception as e:
                        print(f'Failed to download {url}: {e}')

# 调用示例
directory = 'C:\\Users\\xiaxi\\Desktop\\cldas'  # txt所在路径
dest_folder = 'F:\\CLDAS\\202106'  # 下载到的目标路径
download_files_from_txt(directory, dest_folder)