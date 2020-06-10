from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('用户名',max_length=20,unique=True,null=False)
    password = models.CharField('密码',max_length=20,null=False)
    station = models.CharField('岗位',max_length=20,null=False)
    auth = models.CharField('项目权限',max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.username

class Project(models.Model):
    project_name = models.CharField('项目名称',max_length=50,unique=True,null=False)
    tester = models.CharField('测试人员',max_length=200, null=True)
    version = models.CharField('版本',max_length=25,null=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.project_name

class Server(models.Model):
    server_name = models.CharField('服务名称', max_length=50, unique=True, null=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.server_name

class Task(models.Model):
    task_name = models.CharField('任务名称',max_length=50,unique=True,null=False)
    branch_no = models.CharField('比对分支',max_length=50)
    rel_name = models.CharField('发布名称',max_length=100,null=True)
    belong_pro = models.ForeignKey(Project, on_delete=models.CASCADE)
    belong_server = models.ForeignKey(Server,on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.task_name
