# 功能实现

## 监测功能

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062036637.png)

在spy.py中更改路径实现对特定目录的监测

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062036377.png)

可以更改监测时间

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037309.png)

## 邮件提醒功能

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037286.png)

在email.py中更改邮件接收者为自己的邮箱实现邮件提醒功能

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037349.png)

注意MonitoringLog.txt的位置，如果不同需要更改(一般在spy.py与email.py的同级目录下)

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037707.png)

## Docker部署

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037785.png)

同时也push到了我的dockerhub中

使用下面的命令拉取镜像

```
docker pull beatrueman/monitoring:6.0
```

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037393.png)

## Docker自动化更新

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062040055.png)

# Bug

## Docker运行不能同步监测文件目录变化

我尝试把宿主机的目录映射到容器中，还是不行
不过单独使用python可以运行
两个反馈的信息也有差异

![img](https://gitee.com/beatrueman/images/raw/master/img/202306062037803.png)



