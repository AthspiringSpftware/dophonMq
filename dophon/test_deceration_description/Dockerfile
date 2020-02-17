FROM python:3.6.2
ADD . ./test_deceration_description
WORKDIR ./test_deceration_description
ADD site-packages ./.package_cache
ENV PYTHONPATH=/test_deceration_description/.package_cache
RUN pip install --no-cache-dir -r requirements.txt
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python","./Bootstrap.py"]
