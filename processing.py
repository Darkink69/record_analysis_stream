import time
import datetime as dt
import subprocess
import signal
import os
import psutil
import yt_dlp
from ffprobe import FFProbe
import math
import nsfw


folder = 'sweetpupsa'


def time_now():
    return dt.datetime.now().strftime("%H:%M:%S")


def get_video_info(folder, file):
    metadata = FFProbe(f'{folder}/{file}')
    # print(metadata)
    for stream in metadata.streams:
        # print(stream)
        if stream.is_video():
            # print(stream.frame_size())
            # print(stream.duration_seconds())
            w = stream.frame_size()[0] // 10
            h = stream.frame_size()[1] // 10
            tile_h = math.ceil(stream.duration_seconds() / 20)
            if tile_h < 1:
                tile_h = 1
            duration = math.floor(stream.duration_seconds() / 60)
            if duration < 1:
                duration = 1

            return w, h, tile_h, duration


def get_name_files(folder):
    files_dir = os.listdir(folder)
    files_video = []
    for file in files_dir:
        if os.path.isfile(f'{folder}/{file}'):
            new_name = file.replace(' ', '_')
            os.rename(f'{folder}/{file}', f'{folder}/{new_name}')
            files_video.append(new_name)

    print(f'В папке {folder} - {len(files_video)} файла(ов)')
    return files_video


def make_screens(folder, file):
    print(folder, file)
    if not os.path.isdir(f'{folder}/{file[:-4]}'):
        path = f'{os.getcwd()}\\{folder}/' + file[:-4]
        os.mkdir(path)

        # try:
    pro = f'ffmpeg -i {folder}/{file} -r 0.016 {folder}/{file[:-4]}/frame_%03d.jpg'
    pr = subprocess.check_call(pro, shell=True)
        # except BaseException:
        #     print(time_now(), 'Ошибка создания картинок')


def process_files(folder, files):
    for file in files:
        try:
            print(time_now(), f'| обрабатывается папка - {folder}, видео - {file}')

            make_screens(folder, file)

            results_nsfw_all = nsfw.get_nsfw_frames(f'{folder}/{file[:-4]}')
            print(time_now(), '| Кадров, содержащих nsfw -', len(results_nsfw_all))

            print(time_now(), f'| {file} успешно обработан')
        except BaseException:
            print('Ошибка с файлом', file)


print(time_now(), '| начало обработки')

files = get_name_files(folder)
print(files)
process_files(folder, files)




print(time_now(), '| обработка завершена')


# pr = subprocess.run(pro, shell=True, stdin=None, stderr=subprocess.PIPE)
# ffmpeg -i 1.mp4 -r 0.01 output_%04d.jpg
# ffmpeg -ss 01:01:43 -i 1.mp4 -c copy -t 00:01:08  cut_1_test.mp4

# concat.txt
# file Video-01.mp4
# file Video-02.mp4
# file Video-03.mp4

# ffmpeg -f concat -i concat.txt -c copy output.mp4

# ffmpeg -i 2.mp4 -i metadata -map_metadata 1 MyVideo_1.mp4  # долго, потому что пережимает


# pro = f'ffmpeg -i {folder}/{file} -vf select="eq(pict_type\,PICT_TYPE_I)",scale={w}:{h},tile={tile_w}x{tile_h} -frames:v 1 -y {folder}/{file}.jpg'
# pr = subprocess.check_call(pro, shell=True)

