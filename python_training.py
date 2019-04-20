import numpy as np       #Input array
X=np.array([[18,8],[11,4],[13,2],[4,8],[18,6],[14,11],[3,4],[13,19],[7,4],[12,0],[13,8],[18,22],[0,11],[10,8],[13,6],[8,13],[19,7],[4,17],[0,8],[13,19],[7,4],[3,14],[6,18],[0,17],[4,1]])
#Output
y=np.array([[0.766],[0.4977],[0.5732],[0.2325],[0.7652],[0.6147],[0.1928],[0.5796],[0.3453],[0.5343],[0.5755],[0.7713],[0.0812],[0.4611],[0.5747],[0.3868],[0.8037],[0.2359],[0.08],[0.5796],[0.3453],[0.1966],[0.3125],[0.0835],[0.2298]])

#Sigmoid Function
def sigmoid (x):
 return (1)/(np.exp(-x) + 1)
#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
 return (x) * (1 - x)
#Variable initialization
epoch=5000 #Setting training iterations
lr=0.1 #Setting learning rate
inputlayer_neurons = X.shape[1] #number of features in data set
print(inputlayer_neurons)
hiddenlayer_neurons = 3 #number of hidden layers neurons
output_neurons = 1 #number of neurons at output layer
#weight and bias initialization
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))
for i in range(epoch):
 #Forward Propogation
 hidden_layer_input1=np.dot(X,wh)
 hidden_layer_input=hidden_layer_input1 + bh
 hiddenlayer_activations = sigmoid(hidden_layer_input)
 output_layer_input1=np.dot(hiddenlayer_activations,wout)
 output_layer_input= output_layer_input1+ bout
 output = sigmoid(output_layer_input)
 #Backpropagation
 E = y-output
 slope_output_layer = derivatives_sigmoid(output)
 slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
 d_output = E * slope_output_layer
 Error_at_hidden_layer = d_output.dot(wout.T)
 d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
 wout += hiddenlayer_activations.T.dot(d_output) *lr
 bout += np.sum(d_output, axis=0,keepdims=True) *lr
 wh += X.T.dot(d_hiddenlayer) *lr
 bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr
j=len(y);
print (j);
e=0;
i=0
while i<j:
 e+=(y[i]-output[i])*(y[i]-output[i])
 i+=1
e=e/j;
print (output)
print (e)
