from dophon import webboot


@webboot.d_web(webboot.TORNADO)
def run():
    webboot.fix_static(enhance_power=True)
    webboot.fix_template()
    # boot.run_app_ssl()
    # webboot.run_app()


run()
