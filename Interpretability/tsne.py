from keras.models import Model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Reverse layer indices to easily access desired layer
model_layer = model.layers[::-1]
print(model_layer[17])  # Update index based on model summary
layer = model_layer[17]
print(f"layer-{layer.name}")

# Create an intermediate model for the selected layer
intermediate_model = Model(inputs=model.input, outputs=layer.output)
layer_output = intermediate_model.predict(X_test)

# Map classes to colors
class_colors = {0: 'red', 1: 'blue'}  # Update if more classes exist
colors = [class_colors[label] for label in y_test]

# Flatten layer output for t-SNE
layer_output_reshaped = np.reshape(layer_output, (layer_output.shape[0], -1))

# Apply t-SNE
tsne = TSNE(n_components=2, random_state=42)
layer_tsne = tsne.fit_transform(layer_output_reshaped)

# Plot
plt.figure(figsize=(4, 3))
plt.scatter(layer_tsne[:, 0], layer_tsne[:, 1], c=colors, s=8)
plt.title(f"t-SNE on {layer.name}")
plt.show()