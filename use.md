# 部署说明
## 迁移数据库

```buildoutcfg
 python manage.py makemigrations api
 python manage.py migrate
```

- Login数据库，指定一个默认数据,id必须为1

```buildoutcfg
Login(ur="test",params="").save()
```

##  局域网访问

### 设置apache的ip和目录

```buildoutcfg
 DocumentRoot "E:/demo/mysite"
 Listen 192.168.1.100:8001  

```

- 设置权限  ```Require all granted```

### 日志和报告下载ip设置
- 在views.py中

```buildoutcfg
def download_excel(request):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    file_path = request.POST["excel"]
    file_name1 = os.path.join(settings.BASE_DIR, "api/Report", file_path + ".xlsx")
    http_file = "http://192.168.1.100:8001/api/Report/" + file_path + ".xlsx"

    response = HttpResponse(file_iterator(file_name1))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format("report.xlsx")
    result = {'code': 0, 'msg': '下载成功', "path": http_file}
    return JsonResponse(result)

```

## 使用说明

- 新建模块
- 新建用例
	- 管理模糊用例（基于PICT自动生成，暂时只支持windows平台），在lib目下有安装文件
- 任务管理，关联模块，然后运行任务
- 在DashBorad中查看报告





