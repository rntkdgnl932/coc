import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def moohan_top_start(cla, where):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import juljun_off, juljun_on
    from potion_coc import potion_check

    try:
        print("moohan_top_start", where)

        result_dun_where = where.split("_")

        # result_dun_where[0] => 던전
        # result_dun_where[1] => 던전이름...무한의탑
        # result_dun_where[2] => 층수(무한의탑은 의미 없는 듯)


        # 현재 무한의탑 진행중인지 파악 후 진행중이 아니라면 dungeon_in, 던전이라면 물약 등 체크
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_top_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 90, 880, 130, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("moohan_top_ing")

        else:

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_success.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 70, 580, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("moohan_success")
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_next.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 710, 545, 745, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                print("실패시 나가기 버튼 누르기")
                moohan_top_in(cla, where)


    except Exception as e:
        print(e)
        return 0

def moohan_top_in(cla, where):
    import numpy as np
    import cv2
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import menu_open, loading, clean_screen
    from schedule import myQuest_play_add


    try:
        print("moohan_top_in", where)

        result_dun_where = where.split("_")

        # result_dun_where[0] => 던전
        # result_dun_where[1] => 던전이름...무한의탑
        # result_dun_where[2] => 층수(무한의탑은 의미 없는 듯)

        dun_go = False
        dun_go_count = 0
        while dun_go is False:
            dun_go_count += 1
            if dun_go_count > 7:
                dun_go = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_top_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 400, 820, 440, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("moohan_top_in")

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dungeon_lock.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(460, 980, 490, 1020, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("레벨이 안된다.")

                    # 자원획득


                    # 즉시수령
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\soolyung.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 630, 580, 665, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(430, 650, cla)
                            break
                        else:
                            click_pos_2(155, 540, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 630, 580, 670, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\soolyung_ready.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 605, 480, 630, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(430, 650, cla)
                            else:
                                click_pos_2(530, 650, cla)
                            break
                        time.sleep(0.5)

                    # 수령
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\soolyung.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 630, 580, 665, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(530, 650, cla)
                            time.sleep(0.5)
                            click_pos_2(530, 650, cla)
                            time.sleep(0.5)
                            break
                        else:
                            click_pos_2(155, 540, cla)
                        time.sleep(0.5)





                    # 심연탐사

                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_simyuntamsa_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 320, 530, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            result_ran = random.randint(1, 5)
                            y_reg = 360 + (50 * int(result_ran))
                            break
                        else:
                            click_pos_2(155, 725, cla)
                        time.sleep(0.5)

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_simyuntamsa_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 320, 530, 360, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(300, y_reg, cla)
                        time.sleep(0.2)
                        click_pos_2(710, 555, cla)
                        time.sleep(0.2)
                        click_pos_2(770, 720, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 590, 580, 670, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(0.3)

                        dun_go = True

                    # 나가기
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_simyuntamsa_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 320, 530, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            clean_screen(cla)
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            clean_screen(cla)
                        time.sleep(0.2)
                    # 완료하기
                    if where == "무한의탑":
                        myQuest_play_add(cla, where)

                else:
                    print("무한의탑 실행하자")
                    click_pos_2(480, 1000, cla)

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_top_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 900, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        for i in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 590, 620, 630, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(480, 1000, cla)
                            else:
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\loading\\loading.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(600, 900, 960, 1060, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    loading(cla)
                                else:
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_top_ing.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(820, 90, 880, 130, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                            time.sleep(0.5)
                    dun_go = True

                # 뒤에 시작하는지 체크


            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    for i in range(5):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_top_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 400, 820, 440, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            click_pos_2(175, 110, cla)
                            time.sleep(0.5)
                else:
                    menu_open(cla)
                    time.sleep(0.1)
                    for i in range(5):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_top_in.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(740, 400, 820, 440, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(175, 110, cla)
                                time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\menu_dungeon.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 180, 950, 300, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0