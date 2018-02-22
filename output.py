#coding=utf-8
#加载必要的库
import numpy as np

import sys,os

#设置当前目录

caffe_root = '/home/caffe/' #caffe 根目录
sys.path.insert(0, caffe_root + 'python')  #引入caffe python
import caffe
os.chdir(caffe_root)
# Myout 类
#首先初始化实例
#执行predicted 方法
# 结束后 使用out 或get_labels 方法打印或获得标签（字符串）数组
class Myout:

    def _init_(self,net_file,caffe_model,mean_file,imagenet_labels_filename):
        self.net_file=caffe_root + net_file                            #网络文件
        self.caffe_model=caffe_root + caffe_model                      #model文件
        self.mean_file=caffe_root + mean_file                          #均值文件
        self.imagenet_labels_filename = caffe_root + imagenet_labels_filename       #标签文件
        self.net = caffe.Net(net_file,caffe_model,caffe.TEST)

        #数据转换
        transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        transformer.set_transpose('data', (2,0,1))
        transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
        transformer.set_raw_scale('data', 255) 
        transformer.set_channel_swap('data', (2,1,0))

        self.labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

    #执行预测
    def predicted(self,images):
        for i in images:
            im=caffe.io.load_image(caffe_root+i)
            self.net.blobs['data'].data[...] = transformer.preprocess('data',im)
            out = self.net.forward()
    def out(self,re_file): 
        f=open(re_file)
        top_k = self.net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
        for i in np.arange(top_k.size):
            f.write(top_k[i]+'\t'+self.labels[top_k[i]]+'/n')
    
        #    print top_k[i], labels[top_k[i]]
    def get_labels(self):
        label_out=[]
        top_k = self.net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
        for i in np.arange(top_k.size):
            label_out.append(self.labels[top_k[i]])
        return label_out    