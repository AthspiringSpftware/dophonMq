from dophon.cluster_boot import *

if '__main__' == __name__:
    main_freeze()
    run_clusters(3, multi_static_fix=True, outer_port=True)
