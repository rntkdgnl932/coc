import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_coc import bag_open, clean_screen


    try:
        print("boonhae_start")
        bag_open(cla)

        bag_opened = False
        bag_opened_count = 0
        while bag_opened is False:
            bag_opened_count += 1
            if bag_opened_count > 7:
                bag_opened = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\boolga.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 410, 930, 650, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("this is boolga")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\boonhae_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(460, 330, 530, 380, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\boonhae_click_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 630, 620, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\jadong_boonhae_setting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 360, 530, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        boonhae_setting(cla)
                        time.sleep(0.1)

                        break
                    else:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\boonhae_setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 600, 680, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\jadong_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 620, 460, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\boonhae_click_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 620, 510, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                    time.sleep(0.1)
                bag_opened = True
            else:
                drag_pos(810, 610, 810, 440, cla)
                time.sleep(0.1)

        clean_screen(cla)

    except Exception as e:
        print(e)
        return 0

def boonhae_setting(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("boonhae_setting")

        # 자동분해설정
        # 무기 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(170, 440, 210, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("무기 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 방어구 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(270, 440, 320, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("방어구 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 장신구 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 440, 440, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("방어구 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 일반 등급 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(495, 440, 535, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("일반 등급 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 고급 등급 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 440, 640, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("고급 등급 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 775, 560
        # 755, 355
        time.sleep(0.2)
        click_pos_2(775, 560, cla)
        time.sleep(0.2)
        click_pos_2(755, 355, cla)
        time.sleep(0.2)

        # 착용장비보다 전투력 낮은 장비만 분해 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 590, 370, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("착용장비보다 전투력 낮은 장비만 분해 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 다른 클래스 장비는 전투력 비교 안함 체크하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\not_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 620, 370, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("다른 클래스 장비는 전투력 비교 안함 not_checked")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\checked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 620, 370, 660, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("다른 클래스 장비는 전투력 비교 안함 checked")
            else:
                click_pos_2(350, 640, cla)
            time.sleep(0.2)

        # 실수로 체크된 것 해제하기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 440, 420, 490, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("장신구 체크 해제")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 440, 750, 490, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("희귀 체크 해제")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        for i in range(5):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\checked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(160, 470, 750, 520, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("체크 해제", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
            time.sleep(0.1)

        for i in range(10):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\jadong_boonhae_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 360, 530, 410, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 600, 630, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0