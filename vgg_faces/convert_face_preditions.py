import numpy as np
import scipy.io as sio

npy_name = 'weight_vgg_faces_probs.npy'
weight_vgg_faces_test = np.load(npy_name)


weight_vgg_faces_unpositive = np.zeros((weight_vgg_faces_test.shape[0],weight_vgg_faces_test.shape[1]))
weight_vgg_faces_positive = np.zeros((weight_vgg_faces_test.shape[0],weight_vgg_faces_test.shape[1]))
print weight_vgg_faces_unpositive.shape
print weight_vgg_faces_positive.shape


for index in range(weight_vgg_faces_test.shape[0]):
    print weight_vgg_faces_test[index,:]
    predict = weight_vgg_faces_test[index,:] .argmax()
    print predict
    if weight_vgg_faces_test[index,0]!=0 or weight_vgg_faces_test[index,1]!=0 or weight_vgg_faces_test[index,2]!=0:
        if predict==2:            
            weight_vgg_faces_positive[index,2]=1
        else:
            weight_vgg_faces_unpositive[index,0]=0.5
            weight_vgg_faces_unpositive[index,1]=0.5
    print weight_vgg_faces_unpositive[index,:]
    print weight_vgg_faces_positive[index,:]

np.save('weight_vgg_faces_unpositive.npy',weight_vgg_faces_unpositive)
np.save('weight_vgg_faces_positive.npy',weight_vgg_faces_positive)
     



    
