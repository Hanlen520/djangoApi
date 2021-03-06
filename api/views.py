from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api import tasks
from api.base.BaseViewTaskModule import BaseViewTaskModule
from .base.BaseReport import BaseReport
from .base.BaseViewLogin import BaseViewLogin
from .base.BaseViewModule import BaseViewModule
from .base.BaseViewCase import BaseViewCase
from .base import BaseViewTask as bc
from .base.BaseViewDashBoard import BaseViewDashBoard
from .base.BaseViewFuzz import BaseViewFuzz
from .base.BaseViewTask import BaseViewTask


# =====dashBoard Start============

def dashBoard(request):
    return BaseViewDashBoard.dashBoard(request, "api/dashBoard.html")


def dashBoard_module_case(request):
    return BaseViewDashBoard.dashBoard_module_case(request)


def dashBoard_top10_task(request):
    return BaseViewDashBoard.dashBoard_top10_task(request)


def dashBoard_top100_case_time(request):
    return BaseViewDashBoard.dashBoard_top100_case_time(request)


# =====dashBoard End============

# ========测试报告 Start============

def index(request):
    page = request.GET.get('page')
    return BaseReport.index(request, page, "api/index.html")


@csrf_exempt
def report_del(request):
    return BaseReport.report_del(request.POST["rid"])


# 测试模块的用例列表接口
def report_detail(request, id):
    return BaseReport.report_detail(request, "api/reportDetail.html", id)


# 下载日志
@csrf_exempt
def download_log(request):
    return BaseReport.download_log(request.POST["log"])


# 下载excel
@csrf_exempt
def download_excel(request):
    return BaseReport.download_excel(request.POST["excel"])


# ========测试报告 End============


# 接口测试需要登录
def login(request):
    return BaseViewLogin.login(request, "api/login.html")


# 编辑登录接口参数
@csrf_exempt
def login_edit(request):
    url = request.POST["url"]
    params = request.POST["params"]
    return BaseViewLogin.login_edit({"url": url, "params": params})


# ========模块 Start============

# 模块列表
def module(request):
    return BaseViewModule.module(request, "api/module.html")


@csrf_exempt
def module_new(request):
    return BaseViewModule.module_new(request.POST["name"])


# 编辑模块
@csrf_exempt
def module_edit(request):
    m_id = request.POST["id"]
    name = request.POST["name"]
    return BaseViewModule.module_edit({"id": m_id, "name": name})


# 删除模块
@csrf_exempt
def module_del(request):
    m_id = request.POST["mid"]
    return BaseViewModule.module_del(m_id)


# ========模块 End============


# ========模块下用例 Start============


# 模块下的用例列表
def case(request, id):
    return BaseViewCase.case(request, 'api/case.html', id)


# 新建用例
@csrf_exempt
def case_new(request):
    id = request.POST["mid"]
    name = request.POST["name"]
    url = request.POST["url"]
    protocol = request.POST["protocol"]
    method = request.POST["method"]
    params = request.POST["params"]
    hope = request.POST.get("hope", "")
    return BaseViewCase.case_new(
        {"mid": id, "name": name, "url": url, "protocol": protocol, "method": method, "params": params, "hope": hope})


# 编辑用例
@csrf_exempt
def case_edit(request):
    c_id = request.POST["cid"]
    name = request.POST["name"]
    url = request.POST["url"]
    protocol = request.POST["protocol"]
    method = request.POST["method"]
    params = request.POST["params"]
    hope = request.POST["hope"]
    return BaseViewCase.case_edit(
        {"cid": c_id, "name": name, "url": url, "protocol": protocol, "method": method, "params": params, "hope": hope})


# 删除用例
@csrf_exempt
def case_del(request):
    return BaseViewCase.case_del(request.POST["cid"])

# ========模块下用例 End============

# ========模块的用例下的模糊用例 Start============


# 模糊用列表
def fuzz(request, mid, cid):
    return BaseViewFuzz.fuzz(request, "api/fuzz.html", mid, cid)


# 生成模糊用例
@csrf_exempt
def batch_fuzz(request):
    return BaseViewFuzz.batch_fuzz(request.POST["cid"])


# 新建模糊用例
@csrf_exempt
def fuzz_new(request):
    cid = request.POST["cid"]
    name = request.POST["name"]
    url = request.POST["url"]
    protocol = request.POST["protocol"]
    method = request.POST["method"]
    params = request.POST["params"]
    hope = request.POST.get("hope", "")
    return BaseViewFuzz.fuzz_new(
        {"cid": cid, "name": name, "url": url, "protocol": protocol, "method": method, "params": params, "hope": hope})


# 编辑模糊用例
@csrf_exempt
def fuzz_edit(request):
    fid = request.POST["fid"]
    name = request.POST["name"]
    url = request.POST["url"]
    protocol = request.POST["protocol"]
    method = request.POST["method"]
    params = request.POST["params"]
    hope = request.POST["hope"]
    return BaseViewFuzz.fuzz_edit(
        {"fid": fid, "name": name, "url": url, "protocol": protocol, "method": method, "params": params, "hope": hope})


# 删除模糊用例
@csrf_exempt
def fuzz_del(request):
    fid = request.POST["fid"]
    return BaseViewFuzz.fuzz_del(fid)


# ========模块的用例下的模糊用例 End============

# ========任务 Start============

def task(request):
    return BaseViewTask.tasks(request, "api/task.html")


@csrf_exempt
def task_new(request):
    name = request.POST["name"]
    return BaseViewTask.task_new(name)


@csrf_exempt
def task_edit(request):
    name = request.POST["name"]
    id = request.POST["id"]
    return BaseViewTask.task_edit({"name": name, "id": id})


@csrf_exempt
def task_del(request):
    id = request.POST["id"]
    return BaseViewTask.task_del(id)



@csrf_exempt
def task_run(request):
    bc.task_run.delay(request.POST["tid"])
    result = {'code': 0, 'msg': '这是一个后台任务'}
    return JsonResponse(result)


def add(request, *args, **kwargs):
    tasks.add.delay(1, 2)
    result = {'code': 0, 'msg': '这是一个后台任务'}
    return JsonResponse(result)

# ========任务 End============


# ========任务关联模块 Start============

def task_module(request, id):
    return BaseViewTaskModule.task_module(request, "api/taskModule.html", id)


@csrf_exempt
def task_module_new(request):
    tid = request.POST["tid"]
    mid = request.POST["mid"]
    # name = request.POST.getlist("mid")
    name = request.POST["name"]
    return BaseViewTaskModule.task_module_new(tid, name, mid)


@csrf_exempt
def task_module_edit(request):
    tmid = request.POST["tmid"]
    mid = request.POST["mid"]
    name = request.POST["name"]
    return BaseViewTaskModule.task_module_edit({"tmid": tmid, "mid": mid, "name": name})


@csrf_exempt
def task_module_del(request):
    return BaseViewTaskModule.task_module_del(request.POST["tmid"])
# ========任务关联模块 End============
