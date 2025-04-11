def feature_recalib_block(x):
  x = Conv1D(filters=x.shape[-1], kernel_size=1, strides=1, padding='same')(x)
  x = gelu(x)
  x = LayerNormalization()(x)
  #SE Block
  se = GlobalAveragePooling1D()(x)
  se = Dense(x.shape[-1] // 4)(se)
  se = ReLU()(se)
  se = Dense(x.shape[-1])(se)
  se = sigmoid(se)
  # Reshape to match input tensor shape
  se = Reshape((1, x.shape[-1]))(se)
  # Scale the input tensor by the excitation output
  se = Multiply()([x, se])
  se = Add()([x, se])
  se = Softmax()(se)
  return se

def residual_block(inp):
  x_old = inp
  x = inp
  path1 = Conv1D(filters=24, kernel_size=3, strides=1, padding='same', activation='relu')(x)
  path1 = BatchNormalization()(path1)
  path1 = MaxPooling1D(pool_size=1, strides=1, padding='same')(path1)

  path2 = Conv1D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu')(x)
  path2 = BatchNormalization()(path2)
  path2 = MaxPooling1D(pool_size=1, strides=1, padding='same')(path2)
  path2 = Conv1D(filters=24, kernel_size=3, strides=1, padding='same', activation='relu')(path2)
  path2 = BatchNormalization()(path2)
  path2 = MaxPooling1D(pool_size=3, strides=1, padding='same')(path2)
  x = concatenate([path1, path2])
  # Adjust the number of filters in the shortcut connection to match the output of the residual block
  x_old = Conv1D(filters=48, kernel_size=1, strides=1, padding='same', activation='relu')(x_old)

  x = Add()([x, x_old])
  x = feature_recalib_block(x)
  return x

def residual_encoder(x):
  x_old = x
  x = residual_block(x)
  x = LayerNormalization()(x)
  # Adjust the number of filters in the shortcut connection to match the output of the residual block
  x_old = Conv1D(filters=48, kernel_size=1, strides=1, padding='same', activation='relu')(x_old)
  x_multihead = Add()([x, x_old])

  x = x_multihead
  x_multihead = Conv1D(filters=48, kernel_size=1, strides=1, padding='same', activation='relu')(x_multihead)
  #Feed-Forward
  x = Conv1D(filters=16, kernel_size=5, strides=1, padding='same', activation='relu')(x)
  x = BatchNormalization()(x)
  x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
  x = Dropout(0.3)(x)
  x = Conv1D(filters=48, kernel_size=3, strides=1, padding='same', activation='relu')(x)
  x = BatchNormalization()(x)
  x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
  x = Dropout(0.3)(x)
  #Add
  x = Add()([x, x_multihead])
  x = LayerNormalization()(x)
  return x