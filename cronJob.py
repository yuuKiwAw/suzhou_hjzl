# Author : Yuki
# python 3.8
# coding=utf-8
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import getWeatherinfoD2


def job1():
    print("调度成功！" + time.asctime(time.localtime(time.time())))
    print("---------------------------------------------------------")
    getWeatherinfoD2.main()


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(job1, 'cron', hour='8', minute='0')  # 每天 8 点 调度

    try:
        scheduler.start()
        while True:  # 终止方法(或者直接关闭终端)
            time.sleep(1)
    except Exception as ex:
        print('调度失败' + ex)


if __name__ == '__main__':
    main()
