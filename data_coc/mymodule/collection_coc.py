import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def collection_start_ex(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("collection_start")

        # 튜토리얼 즉시 이동 수락
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_collection.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0

def collection_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import menu_open

    try:
        print("collection_start")

        col_ = False
        col_count = 0
        while col_ is False:
            col_count += 1
            if col_count > 6:
                col_ = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 이제 포인트로 컬렉 시작
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\collection\\point_collection_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 70, 130, 105, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    click_pos_2(370, 100, cla)
                    time.sleep(0.1)

                    click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                    time.sleep(0.1)

                    for i in range(20):

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\collection\\point_collection_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 120, 700, 970, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            break_here = False

                            for n in range(4):
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\collection\\no_item.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 280, 600, 370, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break_here = True
                                    break
                                time.sleep(0.1)
                            if break_here == True:
                                break
                            time.sleep(0.1)

                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\collection\\anymore_look.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 540, 550, 600, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\collection\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 570, 600, 650, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                        else:
                            break

                        time.sleep(0.2)


            else:
                menu_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\collection\\menu_collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 130, 950, 210, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)

        for i in range(5):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 40, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 60, cla)
                time.sleep(0.1)
            else:
                break
            time.sleep(0.1)

    except Exception as e:
        print(e)
        return 0