import time
import datetime as dt
import subprocess
import signal
import os
import psutil
import yt_dlp

# import record

# url_stream = 'https://www.youtube.com/live/hg4jV_kXw68'
# url_stream = 'https://rus.bongacams16.com/redfury69'
# url_stream = 'https://rus.bongacams16.com/pasha0864'
# url_stream = 'https://rus.bongacams16.com/taanni'
url_stream = 'https://rus.bongacams16.com/sweetpupsa'

start_time = "2023-04-08 00:30:00"
end_time = "2023-04-16 08:00:00"
time_rec = 300

start = dt.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
end = dt.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

folder = url_stream.split('/')[-1]
if not os.path.isdir(folder):
    os.mkdir(folder)


def time_now():
    return dt.datetime.now().strftime("%H:%M:%S")


def record(url_stream):
    rec = False
    time_connect = 20
    attempts = 5

    pro = f'yt-dlp -P {folder} {url_stream}'

    # pid = os.getpid()
    # print(pid)

    print(time_now(), f'| Попытка подключения')

    try:
        pr = subprocess.run(pro, shell=True, stdin=None, stderr=subprocess.PIPE)
        # p1 = subprocess.Popen(pro, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # time.sleep(5)

        # print(time_now(), 'Подключение не удалось..')
        # p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)
        # p1.stdout.close()
        # out, err = p2.communicate()

        # pr = subprocess.run(pro, timeout=10)
        # out = pr.communicate()
        # print(out)

        # print(pr)
        # pr.send_signal(signal.CTRL_C_EVENT)

        # pr.kill()

    # except subprocess.TimeoutExpired:
    #     print(time_now(), 'TIME!!!!!!')



    except BaseException:
        print(time_now(), '| Какая-то ошибка..')

    time.sleep(5)
    for proc in psutil.process_iter():
        # print(proc)
        if proc.name() == 'ffmpeg.exe':
            print(time_now(), '| Идет запись.')
            rec = True

    if not rec:
        print(time_now(), '| Не удалось подключиться.. ')

    if rec:
        time.sleep(time_rec)
        for proc in psutil.process_iter():
            if proc.name() == 'ffmpeg.exe':
                print(time_now(), '| Провека записи - ок')
                pr.kill()
                rec = False


for i in range(1000):
    print('цикл', i, '-----------------------------------------------')

    if start <= dt.datetime.now() < end:
        print(time_now(), '| До конца записи осталось', str(end - dt.datetime.now())[:-7])

        record(url_stream)
        print(time_now(), '| Подождем минут 30..')
        time.sleep(1800)

    elif dt.datetime.now() < start:
        print(time_now(), '| До начала записи осталось', str(start - dt.datetime.now())[:-7])
        time.sleep(3600)

    elif dt.datetime.now() > end:
        print(time_now(), '| Время для записи окончено')
        os.system('python processing.py')
        exit()

# process_call_str = 'yt-dlp "ytsearch3:angelina joly" --get-id --get-title'
# output = subprocess.check_output(process_call_str, shell=True)
# print(output)
#
# # time.sleep(10)
# process_call_str.terminate()
# print('конец')

# n = 5
#
# # Open a text file on write mode (w)
# with open("out.txt", "w+") as f:
#     for i in range(n):
#         # loop n times and write the
#         # loop index to the file
#         # each number in a new line
#         f.write(str(i) + "\n")
#         # sleep for 10 seconds
#         time.sleep(3)

# execute another Python script in subprocess

# process_call_str = 'yt-dlp "ytsearch3:angelina joly" --get-id --get-title'
# output = subprocess.check_output(process_call_str, shell=True)
# print(output)


# for proc in psutil.process_iter():
#     print(proc)
#     if proc.name() == 'conhost.exe':
#         # proc.terminate()
#         proc.send_signal(signal.CTRL_C_EVENT)

# pro.kill()
# def handler(x):
#     pass
#
# os.kill(signal.CTRL_C_EVENT)

# pro.stdin.flush()
# pro.send_signal(signal.CTRL_BREAK_EVENT)
# os.killpg(os.getpgid(pro.pid), signal.SIGTERM)

