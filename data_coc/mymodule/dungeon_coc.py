import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, where):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import juljun_off, juljun_on, out_check
    from potion_coc import potion_check

    try:
        print("dungeon_start", where)

        result_dun_where = where.split("_")

        # result_dun_where[0] => 던전
        # result_dun_where[1] => 던전이름...언더어스의미궁, 고대드워프요새
        # result_dun_where[2] => 던전층수
        dun_in = False
        # 현재 던전중인지 파악 후 던전 진행중이 아니라면 dungeon_in, 던전이라면 물약 등 체크
        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_map_title1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 80, 860, 105, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("진행중...1")
            dun_in = True
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_map_title2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 30, 500, 70, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("진행중...2")
                dun_in = True
            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dead.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 130, 700, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("죽었다...")
                    click_pos_reg(imgs_.x - 100, imgs_.y + 300, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_map_title1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 80, 860, 105, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("진행중...1")
                            dun_in = True
                            click_pos_2(915, 910, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_map_title2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 30, 500, 70, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("진행중...2")
                                dun_in = True
                                click_pos_2(915, 910, cla)
                                break
                        time.sleep(1)

        if dun_in == False:

            sf = False

            if result_dun_where[1] == "언더어스의미궁":
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in_ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 190, 900, 220, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(780, 215, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_information.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 335, 520, 380, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)

            else:

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\moohan_success.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 70, 600, 200, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\re_dojun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(360, 900, 760, 1030, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("re_dojun")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        sf = True
                else:
                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\fail.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(360, 70, 600, 200, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dun_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 900, 760, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("dun_out")
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):

                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_information.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 335, 520, 380, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:

                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 590, 620, 630, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_out.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(130, 630, 830, 680, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.5)


                                else:
                                    if result_dun_where[1] == "언더어스의미궁":
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in_ready.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(800, 190, 900, 220, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(780, 215, cla)
                                time.sleep(0.5)


            if sf == False:
                potion_check(cla)
                dungeon_in(cla, where)
        else:
            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dun_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 900, 760, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("dun_out")

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\re_dojun.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 900, 760, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("re_dojun")


    except Exception as e:
        print(e)
        return 0

def dungeon_in(cla, where):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_coc import menu_open, loading, clean_screen, out_check
    from schedule import myQuest_play_add


    try:
        print("dungeon_in", where)

        result_dun_where = where.split("_")

        # result_dun_where[0] => 던전
        # result_dun_where[1] => 던전이름...언더어스의미궁, 고대드워프요새
        # result_dun_where[2] => 던전층수

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\boss.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 100, 600, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("hi")

        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\fail.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 100, 600, 200, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("fail 400, 900")



        dun_go = False
        dun_go_count = 0
        while dun_go is False:
            dun_go_count += 1
            if dun_go_count > 7:
                dun_go = True

            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_allow_55_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 360, 540, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\55_full.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 615, 460, 660, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_now.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 660, 610, 700, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_map_title1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(770, 80, 860, 105, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("진행중...1")
                                break
                            else:
                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_map_title2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 30, 500, 70, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("진행중...2")
                                    break
                                else:
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_now.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 660, 610, 700, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\loading\\loading.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(600, 900, 960, 1060, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            loading(cla)
                            time.sleep(0.5)
                        dun_go = True
                else:
                    dun_go = True

                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == False:
                            clean_screen(cla)
                        else:
                            break
                        time.sleep(0.5)


            else:
                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_information.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 335, 520, 380, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\mojib.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 690, 750, 720, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_ready.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(110, 450, 860, 640, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("대기", imgs_)
                        time.sleep(3)
                    else:
                        click_pos_2(480, 705, cla)
                        time.sleep(1)
                        clean_screen(cla)
                else:
                    if result_dun_where[1] == "언더어스의미궁":
                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in_ready.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 190, 900, 220, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(780, 215, cla)

                    else:

                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 400, 170, 440, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("underus_migoong_dun_in")

                            if result_dun_where[1] == "언더어스의미궁":

                                for i in range(5):
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 380, 540, 420, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break

                                    else:
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dungeon_join.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(40, 670, 200, 710, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dungeon_lock.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(40, 670, 200, 710, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                print("레벨이 안된다.")
                                                myQuest_play_add(cla, where)
                                    time.sleep(0.5)

                                case = 0
                                for c in range(5):
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 380, 540, 420, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:

                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(480, 590, 610, 660, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:

                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\end_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(420, 500, 490, 530, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                print("end")
                                                myQuest_play_add(cla, where)
                                                dun_go = True
                                                break
                                            else:
                                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 590, 610, 660, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    case = 1
                                                    break
                                        else:
                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_allow_55_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 360, 540, 400, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                case = 2
                                                break
                                            else:
                                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\dungeon_join.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(170, 620, 250, 660, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)
                                if case == 2:
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_allow_55_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 360, 540, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:

                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\55_full.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(340, 615, 460, 660, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:

                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\join_now.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 660, 610, 700, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            dun_go = True

                                            for i in range(10):
                                                result_out = out_check(cla)
                                                if result_out == False:
                                                    clean_screen(cla)
                                                else:
                                                    break
                                                time.sleep(0.5)

                                elif case == 1:
                                    for c in range(5):
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(480, 590, 610, 660, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_make_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(440, 340, 520, 380, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_make.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(560, 685, 660, 720, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)

                                    for c in range(5):
                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\party_information.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 335, 520, 380, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:

                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\mojib.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(660, 690, 750, 720, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break

                                        else:
                                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in_ready.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(800, 190, 900, 220, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(780, 215, cla)
                                        time.sleep(0.5)

                            elif result_dun_where[1] == "고대드워프요새":
                                print("아직 안 열림")
                                myQuest_play_add(cla, where)

                        else:
                            full_path = "c:\\my_games\\coc\\data_coc\\imgs\\title\\title_dungeon.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 30, 100, 80, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                for i in range(5):
                                    full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(70, 400, 170, 440, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(75, 110, cla)
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

                                        full_path = "c:\\my_games\\coc\\data_coc\\imgs\\dungeon\\underus_migoong_dun_in.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(70, 400, 170, 440, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(75, 110, cla)
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