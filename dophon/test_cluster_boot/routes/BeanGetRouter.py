from dophon.annotation import *


@Get
@ResponseBody()
def get_a():
    return Bean('a')


@Get
@ResponseBody()
def get_b():
    return Bean('c')


@Get
@ResponseBody()
def get_c():
    return Bean('c')
