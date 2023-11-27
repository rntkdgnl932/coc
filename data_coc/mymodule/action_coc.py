import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def confirm_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("confirm_all")

        # 튜토리얼 즉시 이동 수락
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\click\\tuto_move_immediately_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 650, 620, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0


def clean_screen(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from potion_coc import potion_check

    try:
        print("clean_screen")

        confirm_all(cla)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dead.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 300, 700, 700, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("죽었다...")
            click_pos_reg(imgs_.x - 100, imgs_.y + 300, cla)
            time.sleep(1)
            result_out = out_check(cla)
            if result_out == True:
                potion_check(cla)

        # 포션 닫기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\potion_exit_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(660, 800, 700, 980, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("potion_exit_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\potion_exit_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 800, 700, 980, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("potion_exit_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\tuto\\take_on\\take_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 500, 900, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    # 창닫기 1
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\exit_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("exit_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 30, 960, 1060, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        # 창닫기 2
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\exit_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 960, 1060, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("exit_2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            # 아바타 소환
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\all_look.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(410, 970, 550, 1060, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("all_look", imgs_)
                                x_reg = imgs_.x
                                y_reg = imgs_.y

                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\sohwan\\avatar\\skip_not_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(840, 980, 960, 1060, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("skip_not_checked", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                click_pos_reg(x_reg, y_reg, cla)
        # 메뉴 열렸을 경우 닫기
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\cleen_screen\\menu_opened.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 30, 940, 90, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu_opened", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("menu_open")

        for i in range(5):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\action\\menu_open\\menu_character.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 350, 950, 420, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                out_check(cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\out\\menu_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 30, 950, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)




    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("out_check")

        out_ = False

        for i in range(3):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\out\\menu_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 30, 950, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                out_ = True
                break
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\out\\out_check_event.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(230, 30, 320, 90, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    out_ = True
                    break
                else:
                    clean_screen(cla)
                time.sleep(0.3)

        return out_

    except Exception as e:
        print(e)
        return 0

def bag_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("bag_open")

        bag_opened = False
        bag_opened_count = 0
        while bag_opened is False:
            bag_opened_count += 1
            if bag_opened_count > 7:
                bag_opened = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\bag_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 340, 830, 380, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("this is bag")
                bag_opened = True
            else:
                clean_screen(cla)
                time.sleep(0.2)
                click_pos_2(870, 60, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\boonhae\\bag_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 340, 830, 380, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)



    except Exception as e:
        print(e)
        return 0


def loading(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("loading")

        load = True
        load_count = 0
        while load is False:
            load_count += 1
            if load_count > 7:
                load = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\loading\\loading.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 900, 960, 1060, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                load_count = 0
            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0

def juljun_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("juljun_on")

        juljun_ = False
        juljun_count = 0
        while juljun_ is False:
            juljun_count += 1
            if juljun_count > 7:
                juljun_ = True
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\juljun_mode.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 95, 85, 135, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                juljun_ = True
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\fast_juljun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 150, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(500, 500, cla)
                else:
                    clean_screen(cla)
                    time.sleep(0.1)
                    click_pos_2(25, 925, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\fast_juljun.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 150, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def juljun_off(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    try:
        print("juljun_off")

        result_out = out_check(cla)

        if result_out == False:

            juljun_ = False
            juljun_count = 0
            while juljun_ is False:
                juljun_count += 1
                if juljun_count > 7:
                    juljun_ = True

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\juljun_mode.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 95, 85, 135, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    juljun_ = True

                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\juljun_mode.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 95, 85, 135, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            drag_pos(365, 635, 765, 635, cla)
                        else:
                            break
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\fast_juljun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 150, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(500, 500, cla)
                time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

