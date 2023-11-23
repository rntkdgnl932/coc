import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg, drag_pos


    from get_item_coc import get_item, get_post, get_chulsuk_bosang, get_event_bosang
    from collection_coc import collection_start
    from boonhae_coc import boonhae_setting, boonhae_start

    from tuto_coc import tuto_start


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    #
    # get_item(cla)

    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\quest_end.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(80, 150, 170, 180, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("레벨 제한...")

    # get_event_bosang(cla)