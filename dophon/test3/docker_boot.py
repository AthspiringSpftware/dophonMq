from dophon import docker_boot


def run():
    docker_boot.run_as_docker('Bootstrap.py', package_repository='https://mirrors.aliyun.com/pypi/simple/',container_alias='test_alias')


run()
