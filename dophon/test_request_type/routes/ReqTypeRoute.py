from dophon.annotation import *


class SelfHandler(BaseHandler):
    pass


@Get
@AutoParam()
@ResponseBody()
def test_get(data):
    return data


@Post
@AutoParam()
@ResponseBody()
def test_post(data):
    return data


@Post
@AutoParam(content_handler=SelfHandler({
    'text/xml': lambda x: {'data': 'is my owd data'}
}))
@ResponseBody()
def test_self_handler(data):
    return data


@Get
@AutoParam(mix=True,mix_param='mix_dict')
@ResponseBody()
def test_mix_req(a, b, mix_dict):
    print(f'{a} --- {b} --- {mix_dict}')
    return f'{a} --- {b} --- {mix_dict}'


class DataObj:
    d_param1 = 1
    d_param2 = 2
    d_param3 = 3
    d_param4 = 4
    d_param5 = 5

    _p = None

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p = value

    @p.getter
    def p(self):
        return self._p


@Post
@AutoParam()
@ResponseBody()
def test_param_in_type_dec(data: DataObj, num: int, dictionary: dict, sz: tuple, lb: list):
    print(data)
    print(num)
    print(dictionary)
    print(sz)
    print(lb)
    return data
