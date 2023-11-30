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
    from action_coc import juljun_off, juljun_on, clean_screen
    from jadong_coc import jadong_start


    from get_item_coc import get_item, get_post, get_chulsuk_bosang, get_event_bosang, get_server_post, get_start_sayoung
    from collection_coc import collection_start
    from boonhae_coc import boonhae_setting, boonhae_start
    from potion_coc import potion_buy

    from tuto_coc import tuto_start


    print("test")
    cla = "four"

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
    clean_screen(cla)
    # jadong_start(cla, "남매평원")

    # get_item(cla)
    #
    # full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\exit_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(680 + plus, 90, 40, 170), confidence=0.7):
    #     last_x = i.left
    #     last_y = i.top
    #     print("last_x", last_x)
    #     print("last_y", last_y)
    # if last_x != 0:
    #     print("얏호")

    # full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\potion_small_no_have.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(660, 960, 700, 1030, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("hi", imgs_)
    # else:
    #     print("noooooooooooooo")

    # file_path = "C:\\my_games\\coc\\data_coc\\imgs\\jadong\\jadong_list.txt"
    #
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     read_jadong_list = file.read().splitlines()
    #     for i in range(len(read_jadong_list)):
    #         read_jadong = read_jadong_list[i].split(":")
    #         print("where", read_jadong)


    # get_event_bosang(cla)

    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\" + pic_ + ".PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         for i in pyautogui.locateAllOnScreen(img, region=(680 + plus, 90, 40, 170), confidence=0.7):
    #             last_x = i.left
    #             last_y = i.top
    #             print("last_x", last_x)
    #             print("last_y", last_y)
    #         if last_x != 0:
    #             print("얏호")