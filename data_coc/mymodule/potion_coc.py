import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import juljun_off

    try:
        print("potion_check", v_.potion_count)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\juljun_mode.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 95, 85, 135, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\juljun_potion_have.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 990, 570, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("potion have", v_.potion_count)
                if v_.potion_count > 0:
                    v_.potion_count -= 1
            else:
                print("no......", v_.potion_count)
                v_.potion_count += 1

        else:

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\potion_small_no_have.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 960, 700, 1030, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("no potion 1", v_.potion_count, imgs_)
                v_.potion_count += 1
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\potion_small.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(660, 960, 700, 1030, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("no potion 2", v_.potion_count, imgs_)
                    v_.potion_count += 1
                else:
                    print("포션 있다.")
                    if v_.potion_count > 0:
                        v_.potion_count -= 1

        if v_.potion_count > 2:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\juljun_mode.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 95, 85, 135, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                juljun_off(cla)
                time.sleep(0.2)

            v_.potion_count = 0
            potion_buy(cla)

    except Exception as e:
        print(e)
        return 0


def potion_buy(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen
    from massenger import line_to_me

    try:
        print("potion_buy")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("sangjum", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            for i in range(10):
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum_in.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 330, 200, 380, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)
        else:
            potion_buy_ready_maul_move(cla)

        potionbuy_ = False
        potionbuy_count = 0
        while potionbuy_ is False:
            potionbuy_count += 1
            if potionbuy_count > 7:
                potionbuy_ = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 330, 200, 380, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_in")

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum_small_potion_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 360, 850, 400, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\potion_1000.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 600, 525, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_1000", imgs_)
                        # click_pos_2(375, 625, cla)
                        # time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)


                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 630, 450, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(420, 655, cla)

                        buy_ = False
                        for i in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\confirm_potion_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 590, 610, 620, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                buy_ = True
                                potionbuy_ = True
                                break
                            time.sleep(0.2)
                        if buy_ == True:
                            for i in range(10):
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\potion_1000.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 600, 525, 650, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    clean_screen(cla)
                                    break
                                time.sleep(0.5)
                        else:
                            print("돈 없어 못 샀다.")
                            why = "돈 없어서 물약 못 샀다. 주인님 기다린다."
                            line_to_me(cla, why)
                            time.sleep(60000)
                            os.execl(sys.executable, sys.executable, *sys.argv)


                else:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum_small_potion_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(65, 370, 170, 410, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum_small_potion_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(740, 360, 850, 400, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)



            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1030, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("sangjum", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\sangjum_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 330, 200, 380, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)





    except Exception as e:
        print(e)
        return 0


def potion_buy_ready_maul_move(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import clean_screen

    try:
        print("potion_buy_ready_maul_move")

        potionbuy_ = False
        potionbuy_count = 0
        while potionbuy_ is False:
            potionbuy_count += 1
            if potionbuy_count > 7:
                potionbuy_ = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_worldmap")

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\jabhwa_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(710, 800, 930, 850, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\now_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 980, 930, 1030, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\confrim_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 580, 630, 630, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                potionbuy_ = True
                                break
                            time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\jabhwa_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(710, 800, 930, 850, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\jabhwa_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(710, 800, 930, 850, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:

                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\maul_joomin.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(870, 850, 950, 900, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("maul_joomin")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\now_move.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(810, 980, 930, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.2)

                            else:

                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\worldmap_maul.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 100, 160, 200, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("worldmap_maul")
                                    click_pos_reg(imgs_.x + 50, imgs_.y, cla)

                                    for i in range(10):
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\maul_joomin.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(870, 850, 950, 900, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.15)

            else:
                clean_screen(cla)
                time.sleep(0.1)
                click_pos_2(825, 145, cla)
                for i in range(5):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_worldmap.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)





    except Exception as e:
        print(e)
        return 0