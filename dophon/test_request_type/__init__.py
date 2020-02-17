from dophon import dophon_boot
from dophon.boot import *


@dophon_boot
@BeanScan()
def run(boot):
    boot.run()


run()
