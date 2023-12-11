import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me

    try:
        print("_stop_please")
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 980, 200, 1060, cla, img, 0.6)
        if imgs_ is not None and imgs_ != False:
            print("18_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(1)
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\check\\jangsigan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 480, 470, 530, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan")
            why = "장시가니다..."
            line_to_me(cla, why)
            time.sleep(60000)
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                v_.data_folder) + "\\imgs\\check\\server_fix\\loss_connection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 490, 550, 520, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("loss_connection")
                why = "서버 연결 끊어짐...서버점검..."
                line_to_me(cla, why)
                time.sleep(60000)
                os.execl(sys.executable, sys.executable, *sys.argv)



    except Exception as e:
        print(e)
        return 0



