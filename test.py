import tensorflow as tf
import numpy as np
import scipy.misc
import os
import scipy.io

# net = scipy.io.loadmat('/Users/Naiding/Matlab/VGG/imagenet-vgg-verydeep-16.mat')
# for i in range(len(net['layers'][0])):
#     print(net['layers'][0][i][0][0][0], net['layers'][0][i][0][0][1])

data = np.load('/Users/Naiding/TensorFlow/VGG16-pretrained-model/vgg16.npy', encoding='latin1').item()
# print(data.keys())

print(type(data['conv1_1']))

# net = scipy.io.loadmat('/Users/Naiding/Matlab/demo/model/5input_net.mat')
# # layers info
# print(len(net['net'][0][0][0][0]))
# # 1000 classes number
# print(len(net['net'][0][0][1][0][0][0][0]))
# # 1000 classes name
# print(len(net['net'][0][0][1][0][0][1][0]))
# # normalization info
# print(len(net['net'][0][0][2][0][0]))
#
#
# for i in range(len(net['net'][0][0][0][0])):
#     print(type(net['net'][0][0][0][0][i]))