import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("get_item")

        get_contents_bosang(cla)

        get_event_bosang(cla)

        get_chulsuk_bosang(cla)

    except Exception as e:
        print(e)
        return 0

def get_contents_bosang(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen

    try:
        print("get_contents_bosang")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\contents_bosang\\point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(260, 30, 300, 60, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\contents_bosang\\contents_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 380, 540, 440, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.3)
            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\contents_bosang\\get_bosang_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, 610, 840, 670, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(0.3)

            clean_screen(cla)



    except Exception as e:
        print(e)
        return 0

def get_event_bosang(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen

    try:
        print("get_event_bosang")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(730, 30, 770, 60, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)

            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\event_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 310, 540, 355, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.3)
            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, 330, 185, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                    time.sleep(0.5)

                    # 미션정보 받기
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\mission_information.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(610, 430, 700, 480, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for t in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\mission_information_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 320, 520, 360, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\mission_information_get_all_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(410, 690, 550, 730, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                break
                            time.sleep(0.2)
                        for t in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\mission_information_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 320, 520, 360, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(765, 345, cla)
                            else:
                                break
                            time.sleep(0.2)

                    # 모두 수령하기
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\get_all_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 430, 840, 480, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                else:
                    break
                time.sleep(0.3)

            clean_screen(cla)


    except Exception as e:
        print(e)
        return 0

def get_chulsuk_bosang(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen

    try:
        print("get_chulsuk_bosang")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(780, 30, 810, 60, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)

            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\chulsuk_bosang\\chulsuk_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 310, 540, 355, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.3)
            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\event_bosang\\point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, 330, 185, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\chulsuk_bosang\\get_bosang_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(720, 480, 860, 530, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                else:
                    break
                time.sleep(0.3)

            clean_screen(cla)



    except Exception as e:
        print(e)
        return 0

def get_post(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen, menu_open

    try:
        print("get_post")

        post = True
        post_count = 0
        while post is True:
            post_count += 1
            if post_count > 7:
                post = False
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\action\\post\\post_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 300, 510, 340, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\action\\post\\post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 330, 460, 370, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)

                    click_pos_2(870, 740, cla)
                    time.sleep(0.2)
                    click_pos_2(870, 740, cla)
                    time.sleep(0.2)
                else:
                    post = False

                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\action\\post\\post_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 300, 510, 340, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\exit_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("exit_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(0.3)


            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\action\\post\\menu_post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 350, 950, 430, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\action\\post\\post_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 300, 510, 340, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
                else:
                    menu_open(cla)
            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

def get_start_sayoung(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen

    try:
        print("get_start_sayoung")

        sayoung = True
        sayoung_count = 0
        while sayoung is True:
            sayoung_count += 1
            if sayoung_count > 7:
                sayoung = False
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\start\\sayoung.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 500, 900, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\start\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 650, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.3)
                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\start\\confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 550, 650, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        break
                    time.sleep(0.3)

            else:
                sayoung_count += 1
                time.sleep(0.1)



    except Exception as e:
        print(e)
        return 0