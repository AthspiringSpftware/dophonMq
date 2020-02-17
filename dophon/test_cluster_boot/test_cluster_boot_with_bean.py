if '__main__' == __name__:
    from multiprocessing import freeze_support
    freeze_support()
    from dophon import cluster_boot
    from dophon.boot import BeanConfig
    BeanConfig(['Beans.py'])
    cluster_boot.run_clusters(3)