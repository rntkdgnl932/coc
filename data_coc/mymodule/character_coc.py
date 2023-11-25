import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def character_select_screen(cla, character_id):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("character_select_screen")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\character\\title_server_select.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 40, 140, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            character_change(cla, character_id)



    except Exception as e:
        print(e)
        return 0

def character_change(cla, character_id):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import menu_open, loading


    try:
        print("character_change", character_id)

        int_id = int(character_id)

        y_reg = 70 + (int_id * 65)

        click_pos_2(100, y_reg, cla)
        time.sleep(0.5)
        click_pos_2(820, 995, cla)

        for i in range(10):
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\loading\\loading.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 900, 960, 1060, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                loading(cla)
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\check\\out\\menu_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 30, 950, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break

            time.sleep(0.3)


    except Exception as e:
        print(e)
        return 0