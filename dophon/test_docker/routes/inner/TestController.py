from dophon.annotation import *

PREFIX = '/inner'


@GetRoute('/test/dese')
@ResponseBody()
@Desc(
    param_des={
        'test_arg': '这是一个测试参数描述'
    },
    return_demo=(1, 2, 3, 4, 5, 6, Exception(), Exception),
    remark='这是一个测试参数描述,属于TestController'
)
def test_desc_decr(test_arg='this is test args') -> dict:
    """
    this is test for description decoration
    :param test_arg:
    :return:
    """
    print(f'this.is decr {test_arg}')
    return {}


@Post
@ResponseBody()
@Desc(
    demo={
        'test_arg': 'any str'
    }
)
def test_desc_with_no_default(test_arg) -> dict:
    """
    this is test for description decoration without default parm value
    :param test_arg:
    :return:
    """
    print('this.is decr without any default value')
    return {}


class ParamObj:
    a = 1
    b = 2
    c = 3
    d = {
        1, 2, 3
    }
    e = {
        'aaa': 'aaa',
        'bbb': 123
    }

    def aa(self):
        pass


@Get
@ResponseBody()
@Desc(param_des={
    'arg_1': '字符串类型的参数',
    'arg_4': '元组类型的参数',
    'arg_2': '整数类型的参数',
    'arg_6': '对象类型的参数',
}, demo={
    'arg_1': 'any str',
    'arg_2': 666,
    'arg_3': {},
    'arg_4': ('a', 1, object()),
    'arg_5': [1, 2, 3, 4, 5, 6],
    'arg_6': ParamObj()
})
def test_multiple_param(arg_1: str,
                        arg_2: int = 666,
                        arg_3: dict = {},
                        arg_4: tuple = ('a', 1, object()),
                        arg_5: list = [1, 2, 3, 4, 5, 6],
                        arg_6: ParamObj = ParamObj()):
    """
    this is test_multiple_param

    :param arg_1:
    :param arg_2:
    :param arg_3:
    :param arg_4:
    :param arg_5:
    :return:
    """
    return {}
