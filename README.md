
# Pycaffe配置（Ubuntu16.04 ）

## 安装依赖
    $ sudo apt-get install python-numpy python-scipy python-matplotlib python-sklearn python-skimage python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags Cython ipython
    $ sudo apt-get install protobuf-c-compiler protobuf-compiler
     
OR

    cd caffe
    cat python/requirements.txt | xargs -L 1 sudo pip install

## 编译
    $ cd ~/caffe
    $ make pycaffe
## 添加~/caffe/python到$PYTHONPATH：
    $ sudo gedit /etc/profile

    # 添加： export PYTHONPATH=你的路径/caffe/python:$PYTHONPATH
    $ source /etc/profile # 使之生效
## 测试是否可以引用：
    $ python
    Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import caffe

# My-caffe
## 输入
输入部分包括 init.sh, create_mean.sh , create_lablefile.sh ,create_lmdb.sh,各脚本可独立运行，也可直接运行 input.py。
## 输出
输出类打包在 output.py 中，目前图片以文件形式输入。
