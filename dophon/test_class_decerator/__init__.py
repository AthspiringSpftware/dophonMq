from dophon import webboot


# from dophon.annotation import *


@webboot.d_web(webboot.TORNADO)
def run():
    print(111)


# @DefBean
# class RootBean:
#     pass

run()
