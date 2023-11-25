import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def sub_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen
    from get_item_coc import get_item
    from schedule import myQuest_play_add
    from collection_coc import collection_start
    from boonhae_coc import boonhae_start
    from potion_coc import potion_check

    try:
        print("sub_start")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_junjig.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            sub_description(cla)
        else:
            clean_screen(cla)
            potion_check(cla)

        contents_exist = False
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\contents_bosang\\point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(260, 30, 300, 60, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            contents_exist = True
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\get_item\\contents_bosang\\point_1_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(260, 30, 300, 60, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                contents_exist = True

        if contents_exist == True:
            get_item(cla)
            time.sleep(0.1)
            collection_start(cla)
            time.sleep(0.1)
            boonhae_start(cla)
            time.sleep(0.1)
            clean_screen(cla)

        for i in range(5):

            sub_take_on(cla)

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 920, 530, 960, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("이동중1")
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\move\\move_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 920, 530, 960, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("이동중2")
                else:
                    des_result = sub_description(cla)
                    if des_result == False:

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\quest_end.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(80, 150, 170, 180, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("레벨 제한...")
                            myQuest_play_add(cla, "서브퀘스트")
                        else:
                            sub_click(cla)
                time.sleep(0.2)



    except Exception as e:
        print(e)
        return 0

def sub_description(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_coc import clean_screen

    try:
        print("sub_description")

        description = False

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_bosang_soolyung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 590, 620, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_junjig.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\scout.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 360, 840, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(460, 990, cla)
            else:
                click_pos_2(80, 550, cla)
                time.sleep(0.5)
                click_pos_2(460, 990, cla)
            time.sleep(0.5)

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\scout2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 430, 520, 480, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(555, 985, cla)
                time.sleep(0.5)

            clean_screen(cla)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_tgsung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(610, 320, cla)
            time.sleep(0.5)
            click_pos_2(882, 962, cla)
            time.sleep(0.5)
            click_pos_2(825, 1005, cla)
            time.sleep(0.5)
            click_pos_2(930, 60, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\attack_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 960, 960, 1060, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            description = True

            click_pos_2(805, 915, cla)
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\jadong_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(670, 870, 960, 1060, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                description = True

                click_pos_2(915, 910, cla)
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\quick_slot_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 870, 960, 1060, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    description = True

                    click_pos_2(680, 1000, cla)
                    time.sleep(0.5)
                    click_pos_2(680, 950, cla)
                else:

                    upper = False

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_up.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        description = True
                        upper = True
                        click_pos_reg(imgs_.x, imgs_.y - 35, cla)
                    else:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_up2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            description = True
                            upper = True
                            click_pos_reg(imgs_.x, imgs_.y - 35, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y - 50, cla)

                    if upper == True:

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_get_title_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 320, 500, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_immediately_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 650, 620, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_bosang_soolyung.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 590, 620, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)


                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_down.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        description = True

                        click_pos_reg(imgs_.x, imgs_.y + 35, cla)

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\quick_slot_drag_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(590, 860, 690, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            description = True

                            drag_pos(740, 985, 740, 930, cla)


                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_down2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        description = True

                        click_pos_reg(imgs_.x, imgs_.y + 35, cla)

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\quick_slot_drag_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(590, 860, 690, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            description = True

                            drag_pos(740, 985, 740, 930, cla)

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_right.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        description = True

                        click_pos_reg(imgs_.x + 35, imgs_.y, cla)

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\skill_select_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 400, 640, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(800, 430, cla)


                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_left.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        description = True

                        click_pos_reg(imgs_.x - 35, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\description\\click_ready_left2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            description = True

                            click_pos_reg(imgs_.x - 35, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 60, cla)
        return description
    except Exception as e:
        print(e)
        return 0

def sub_click(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    try:
        print("sub_click")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\sub\\power_10000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 130, 200, 185, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            drag_pos(100, 200, 100, 100, cla)
            time.sleep(0.2)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 130, 200, 185, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 370, 520, 420, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\sub_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 130, 150, 185, cla, img, 0.65)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\sub_ready_click2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 130, 150, 185, cla, img, 0.65)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\sub_ready_click3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 130, 150, 185, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_immediately_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 380, 540, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_immediately_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 650, 620, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(140, 130, 200, 185, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    x_reg = imgs_.x
                                    y_reg = imgs_.y

                                    screen_0_1 = False
                                    for i in range(10):
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\0_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(460, 550, 500, 580, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            screen_0_1 = True
                                            click_pos_2(410, 600, cla)
                                            time.sleep(0.5)
                                            click_pos_reg(x_reg - 50, y_reg, cla)
                                            break
                                        time.sleep(0.1)
                                    if screen_0_1 == False:
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_immediately_confirm2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 585, 620, 620, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                else:
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\junjig.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 130, 150, 185, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_get_title_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 320, 500, 400, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_immediately_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(470, 650, 620, 700, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_bosang_soolyung.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(470, 590, 620, 700, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_bosang_soolyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(470, 590, 620, 700, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def sub_take_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("sub_take_on")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\take_on\\take_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 500, 900, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0