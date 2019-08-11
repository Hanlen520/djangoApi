# -*- coding=utf-8 -*-
__author__ = 'shikun'
__CreateAt__ = '2019/6/7-13:07'
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Element(object):
    # selenium关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    find_element_by_name = "by_name"
    find_element_by_link_text = "link_text"
    CLICK = "click"
    GET_TEXT = "get_text"
    SEND_KEYS = "send_keys"
    GET_VALUE = "get_value"
    WAIT_TIME = 20  # 查找元素等待时间
    MOVE_TO_ELEMENT = "move_to_element"  # 鼠标悬停
    NO_OPERATE = "0" # 无操作
    DEFAULT_OPERATE = "default_operate"  # 默认值
    SWITCH_TO_WINDOW = "switch_to_window"
    SWITCH_TO_FRAME = "switch_to_frame"
    SWITCH_TO_DEFAULT_CONTENT = "switch_to_default_content"

    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval"  # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check"  # 默认检查点，就是查找页面元素
    COMPARE = "compare"  # 历史数据和实际数据对比

    RE_CONNECT = 1  # 是否打开失败后再次运行一次用例

    REPORT_FILE = PATH("../Report/")  # 测试报告

    C_CHECK = {"passed": 0, "failed": -1, "no_check": -2}
