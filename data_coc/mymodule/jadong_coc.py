import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla, where):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import juljun_off, juljun_on, clean_screen
    from potion_coc import potion_check
    from get_item_coc import get_item

    try:
        print("jadong_start", where)

        file_path = "C:\\my_games\\coc\\data_coc\\imgs\\jadong\\jadong_list.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_jadong_list = file.read().splitlines()
            for i in range(len(read_jadong_list)):
                read_jadong = read_jadong_list[i].split(":")
                if str(read_jadong[0]) == str(where):
                    print("where", read_jadong)
                    break

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
            clean_screen(cla)

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\juljun_mode.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 95, 85, 135, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_mode")
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\jadong\\list_juljun\\" + str(read_jadong[1]) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 120, 130, 170, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\juljun\\jadong_ing.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 650, 530, 690, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("자동사냥중", v_.attack_count)
                    potion_check(cla)
                    if v_.attack_count > 0:
                        v_.attack_count -= 1
                else:
                    print("절전모드 해제 후 오토 버튼 누르기", v_.attack_count)

                    v_.attack_count += 1

                    if v_.attack_count > 2:

                        juljun_off(cla)
                        time.sleep(0.1)
                        click_pos_2(911, 911, cla)
                        time.sleep(0.2)
                        juljun_on(cla)

            else:
                print("자동사냥터로 ㄱㄱ")
                juljun_off(cla)
                jadong_spot_go(cla, where)
        else:
            juljun_on(cla)


    except Exception as e:
        print(e)
        return 0

def jadong_spot_go(cla, where):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import menu_open, loading, clean_screen


    try:
        print("jadong_spot_go", where)

        file_path = "C:\\my_games\\coc\\data_coc\\imgs\\jadong\\jadong_list.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_jadong_list = file.read().splitlines()
            for i in range(len(read_jadong_list)):
                read_jadong = read_jadong_list[i].split(":")
                if str(read_jadong[0]) == str(where):
                    print("where", read_jadong)
                    break

        # read_jadong[0] => 한글장소
        # read_jadong[1] => 영어 그림 파일 이름
        # read_jadong[2] => 월드맵 지역 이름
        # read_jadong[3] => 월드맵 세부 y 값


        jadong_go = False
        jadong_go_count = 0
        while jadong_go is False:
            jadong_go_count += 1
            if jadong_go_count > 7:
                jadong_go = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_worldmap")

                if str(read_jadong[2]) == "라브스섬":
                    click_pos_2(60, 135, cla)
                elif str(read_jadong[2]) == "샤스텔북동부":
                    click_pos_2(60, 185, cla)
                elif str(read_jadong[2]) == "샤스텔서남부":
                    click_pos_2(60, 225, cla)
                time.sleep(0.5)

                click_pos_2(180, int(read_jadong[3]), cla)

                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\potion\\now_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 980, 930, 1030, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)

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
                            jadong_go = True
                            break
                        time.sleep(0.2)


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