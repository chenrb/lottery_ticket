# -*- coding: utf-8 -*-
import random


def two_color_ball(bet=1):
    """
    双色球由红球和蓝球两部份组成，从33个红球号码(01~33)中选择6个，再从16个蓝球号码(01~16)中选择1个。
    开奖时，在红色球中随机摇出六个红号，在蓝色球中随机摇出一个蓝号。
    :param bet: 投注数
    :return:
    """
    print("双色球： ")
    for i in range(1, bet + 1):
        balls = [n for n in range(1, 34)]
        red = random.sample(balls, 6)
        blue = random.randint(1, 16)
        print("{}:红: {: >2}, {: >2}, {: >2}, {: >2}, {: >2}, {: >2} -- 蓝：{: >2}".format(i, *red, blue))


def big_lotto(bet=1):
    """
    超级大乐透基本投注是指从前区号码(01-35)中任选五个号码，并从后区号码(01-12)中任选两个号码的组合进行投注。
    :param bet: 投注数
    :return:
    """
    print("大乐透： ")
    for i in range(1, bet + 1):
        front_balls = [n for n in range(1, 36)]
        back_balls = [n for n in range(1, 13)]
        front = random.sample(front_balls, 5)
        back = random.sample(back_balls, 2)
        print("{}:前区：{: >2}, {: >2}, {: >2}, {: >2}, {: >2} -- 后区：{: >2}, {: >2}".format(i, *front, *back))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    two_color_ball(5)
    big_lotto(5)
