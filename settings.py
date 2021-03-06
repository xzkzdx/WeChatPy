# -*- encoding: utf-8 -*-
# !/usr/bin/python3
# @Time   : 2019/3/15 14:21
# @File   : settings.py

import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

ABS_DIR_PATH = PROJECT_PATH

IMAGE_DIR_NAME = 'image'

IMAGE_SAVE_PATH = os.path.join(ABS_DIR_PATH, IMAGE_DIR_NAME)

HANDLE_PIXEL_RATIO = 1.5

LOGIN_UPDATE_TIME = 1

ERROR_IGNORE_TIME = 0.1
