#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGO = (By.ID, 'nav-logo')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')


class SipLoginLocators(object):
    # todo 补全login locators
    username = (By.ID, '')
    password = (By.ID, '')
    submit = (By.ID, '')


class SipMainLocators(object):
    update_page = (By.LINK_TEXT, '升级')   # 页按钮 - 升级
    update_select_file = (By.CLASS_NAME, 'btninput_l lit_btninput')  # 选择文件
    update_submit = (By.CLASS_NAME, 'WebUpdate')    # 升级按钮

    config_page = (By.LINK_TEXT, '系统配置')  # 系统配置 - 页按钮
    config_select_file = (By.XPATH, '//*[@id="ImportBody"]/table/tbody/tr/td[5]/input')  # 导入配置 按钮
    config_submit = (By.XPATH, '//*[@id="System"]')  # 选择文件 按钮

    dj_page = (By.ID, 'XSTR_HLP_SETTING_PHONE')  # 对讲设置 竖向 页按钮
    mt_page = (By.LINK_TEXT, '媒体设置')  # 媒体设置 页按钮
    camera_page = (By.LINK_TEXT, '相机设置')  # 相机设置 页按钮

    mt_bro = (By.ID, 'XSTR_LBL_GEN_MEDIA')  # 媒体设置 之 >>

    camera_outer_box = (By.ID, 'Native_Camera_Connect_Mode_RW')  # 相机设置 外接 ComBox
    camera_btn_submit = (By.XPATH, '//*[@id="ipcMode"]/div[2]/input[2]')  # 相机设置 外接 提交

class SipMainLocators(object):
    update_page = (By.LINK_TEXT, '升级')
    select_btn = (By.CLASS_NAME, 'btninput_l lit_btninput')
    update_btn = (By.CLASS_NAME, 'WebUpdate')

    system_page = (By.LINK_TEXT, '系统配置')
    daoru_btn_system = (By.XPATH, '//*[@id="ImportBody"]/table/tbody/tr/td[5]/input')
    select_btn_system = (By.XPATH, '//*[@id="System"]')

    djsz_page = (By.ID, 'XSTR_HLP_SETTING_PHONE')  # 对讲设置
    djsz_page_meiti = (By.LINK_TEXT, '媒体设置')
    djsz_page_xiangji = (By.LINK_TEXT, '相机设置')

    m1 = (By.ID, 'XSTR_LBL_GEN_MEDIA')  # 媒体设置>>

    m1 = (By.ID, 'Native_Camera_Connect_Mode_RW')  # xiang ji waijie  box
    m1 = (By.XPATH, '//*[@id="ipcMode"]/div[2]/input[2]')  # tijiao btn





class BaiduPageLocators(object):
    # input = (By.ID, 'kw')
    logo = (By.ID, 's_mp')
    news_lab = (By.CLASS_NAME, 'mnav c-font-normal c-color-t')
    btn_baidu = (By.ID, "s_btn_wr")
    input = (By.CLASS_NAME, "s_ipt")
    some = (By.NAME, "tj_briicon")