import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	sigmoid = lambda x: 1/(1+np.exp(-x))
	forward = lambda x, w, b: sigmoid(x@w+b)
	mse_loss = lambda preds, labels: np.mean((preds-labels)**2) 
	eps = 1e-5
	totrain_weights = initial_weights
	totrain_bias = initial_bias
	
	mse_values = []
	for i in range(epochs):
		orig_preds = forward(features, totrain_weights, totrain_bias)
		orig_loss = mse_loss(orig_preds, labels)
		mse_values.append(orig_loss)

		I_weights = np.eye(len(totrain_weights))
		weights_grad = []
		for j in range(len(totrain_weights)):
			diff_weights = totrain_weights + I_weights[j]*eps
			diff_preds = forward(features, diff_weights, totrain_bias)
			diff_loss = mse_loss(diff_preds, labels)
			weights_grad.append((diff_loss - orig_loss)/eps)
		weights_grad = np.array(weights_grad)
		diff_bias = totrain_bias + eps
		diff_preds = forward(features, totrain_weights, diff_bias)
		diff_loss = mse_loss(diff_preds, labels)
		bias_grad = np.array((diff_loss - orig_loss)/eps)

		totrain_weights = totrain_weights - learning_rate*weights_grad
		totrain_bias = totrain_bias - learning_rate*bias_grad

	updated_weights = totrain_weights.tolist()
	updated_bias = totrain_bias
	return updated_weights, updated_bias, mse_values