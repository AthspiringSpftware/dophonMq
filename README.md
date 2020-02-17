# dophonMq
dophon框架中的消息队列模块,包括本地消息中心,远程消息中心,以及生产消费相关装饰器以及内部操作模块等
dophon-mq
项目介绍
dophon框架中的消息队列模块,包括本地消息中心,远程消息中心,以及生产消费相关装饰器以及内部操作模块等

有问题可发送邮件联系作者:athspiring_admin@athspiring.com

一个轻量级消息队列,承载能力中等,高频巨量消息请选择成熟的消息队列(rocket-mq,kafuka等)
即使使用线程池处理消息,极为消耗cpu资源
该队列基于io作为消息持久化(消息延迟主要为消息中心的读写延迟)
可通过配置选择本地消息中心以及远程消息中心
软件架构
软件架构说明

安装教程
<<<<<<< HEAD

pip install dophon_mq =======
pip install dophon-mq
e822369e3d8eac4b4bdbcaa2f1613c902a8c4815

使用说明
1 配置
自定义配置:

<application.py>

msg_queue_max_num = 30   # 消息队列线程池承载话题上限

mq={
    'remote_center':True,   # 使用远程消息中心
    # 若为false或不配置,则字典内下面的配置无效
    'remote_address':'127.0.0.1',  # 消息中心地址
    'remote_port':58800  # 消息中心端口
}
2 生产者配置
推荐使用json格式传递数据(便于消费者转义数据)

from dophon_mq import *

@producer(
    tag='DEMO_TAG', # 消息发送的话题
    delay = 3 # 消息发送的延迟时间(秒)
)
def producer():
    return 'aaa'
3 消费者配置
方式一:

from dophon_mq import *

@consumer(
    tag='DEMO_TAG', # 消息消费的话题
    delay = 1, # 消息消费的延迟
    arg_name = 'args' # 承载消息的参数名(默认使用名为args的参数承载) 
)
def consumer(args):
    print(args)
consumer()
4 统一管理消费者
from dophon_mq import *

class TestConsumer(ConsumerCenter):

    @consumer(tag='test_msg_tag|test_msg_tag2', delay=1, arg_name = 'msg')
    def consume_msg(
        msg  # 统一配置的消费入口方法以承载参数取代实例参数(self)
    ):
        print(msg)
        print(timestamp)
        print(tag)

# 实例化衍生类启动消费者
TestConsumer()
参与贡献
Fork 本项目
新建 Feat_xxx 分支
提交代码
新建 Pull Request
