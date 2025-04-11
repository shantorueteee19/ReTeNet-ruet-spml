def init_feature_exc(input_layer):

  # path1 for global spatial feature extraction
  path1 = Conv1D(filters=16, kernel_size=33, strides=2, padding='same', activation='relu')(input_layer)
  path1 = BatchNormalization()(path1)
  path1 = MaxPooling1D(pool_size=3, strides=1, padding='same')(path1)
  path1 = Dropout(0.3)(path1)
  path1 = Conv1D(filters=16, kernel_size=5, strides=2, padding='same', activation='relu')(path1)
  path1 = BatchNormalization()(path1)
  path1 = MaxPooling1D(pool_size=3, strides=1, padding='same')(path1)
  path1 = Dropout(0.3)(path1)

  # path2 local spatial features
  path2 = Conv1D(filters=16, kernel_size=5, strides=2, padding='same', activation='relu')(input_layer)
  path2 = BatchNormalization()(path2)
  path2 = MaxPooling1D(pool_size=3, strides=1, padding='same')(path2)
  path2 = Dropout(0.3)(path2)
  path2 = Conv1D(filters=16, kernel_size=3, strides=2, padding='same', activation='relu')(path2)
  path2 = BatchNormalization()(path2)
  path2 = MaxPooling1D(pool_size=3, strides=1, padding='same')(path2)
  path2 = Dropout(0.3)(path2)

  # path3 spatio temporal features extraction
  path3 = Conv1D(filters=16, kernel_size=3, strides=2, padding='same', activation='relu')(input_layer)
  path3 = BatchNormalization()(path3)
  path3 = MaxPooling1D(pool_size=3, strides=1, padding='same')(path3)
  path3 = Dropout(0.3)(path3)
  path3 = LSTM(units=16, return_sequences=True)(path3)
  path3 = Dropout(0.3)(path3)
  path3 = Bidirectional(LSTM(units=16, return_sequences=True))(path3)
  path3 = Dropout(0.3)(path3)
  path3 = Conv1D(filters=16, kernel_size=1, strides=2, padding='same', activation='relu')(path3)

  return path1, path2, path3