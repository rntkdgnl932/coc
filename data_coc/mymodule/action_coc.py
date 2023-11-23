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

    try:
        print("clean_screen")

        confirm_all(cla)

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

        for i in range(5):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\out\\menu_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 30, 950, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                clean_screen(cla)
            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0