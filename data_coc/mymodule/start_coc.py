import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def start_coc(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("start_coc")



        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\start\\sayoung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(670, 470, 900, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("sayoung")

            for x in range(10):

                full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                    v_.data_folder) + "\\imgs\\start\\sayoung.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 470, 900, 630, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("sayoung")

                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                            v_.data_folder) + "\\imgs\\start\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 470, 900, 630, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("max")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            break

                    for i in range(10):
                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                            v_.data_folder) + "\\imgs\\start\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 470, 900, 630, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            break

                else:
                    break
                time.sleep(0.1)

        #     time.sleep(1)
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0



