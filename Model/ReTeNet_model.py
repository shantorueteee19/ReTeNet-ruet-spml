import tensorflow as tf
from tensorflow.keras.layers import (
    Conv1D, MaxPooling1D, BatchNormalization, Dropout,
    Dense, GlobalAveragePooling1D, Reshape, Multiply, Add, concatenate, Input,
    ReLU, Softmax, LayerNormalization, LSTM, Bidirectional, MultiHeadAttention,
    GlobalAveragePooling1D
)
from tensorflow.keras.models import Model
from tensorflow.keras.activations import gelu, sigmoid

def ReTeNet(input_shape, num_class):
  input_layer = Input(shape=input_shape)
  #Initial Feature Exctraction
  x_fexc = init_feature_exc(input_layer)
  #Transformer Encoder
  x_trans1 = transformer_encoder_cross(x_fexc)
  x_trans2 = transformer_encoder_self(x_trans1)
  x_trans3 = transformer_encoder_self(x_trans2)
  x_trans_con = concatenate([x_trans1, x_trans2, x_trans3])
  x_trans_con = mrcnn(x_trans_con)
  #residual encoder
  x_fexc_con = concatenate(x_fexc)
  x_res = residual_encoder(x_fexc_con)
  x_res = mrcnn(x_res)
  #Hierarchical Features Concat
  x_concat = Concatenate(axis=1)([x_res, x_trans_con])
  #Classification Stage
  x_concat = Conv1D(filters=64, kernel_size=3, strides=1, padding='same', activation='relu')(x_concat)
  x_concat = MaxPooling1D(pool_size=2, strides=2, padding='same')(x_concat)
  x_concat = BatchNormalization()(x_concat)
  x_concat = Dropout(0.3)(x_concat)
  x_concat = Conv1D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu')(x_concat)
  x_concat = MaxPooling1D(pool_size=2, strides=2, padding='same')(x_concat)
  x_concat = BatchNormalization()(x_concat)
  x_concat = Dropout(0.3)(x_concat)
  x_concat = Conv1D(filters=16, kernel_size=3, strides=1, padding='same', activation='relu')(x_concat)
  x_concat = MaxPooling1D(pool_size=2, strides=2, padding='same')(x_concat)
  x_concat = BatchNormalization()(x_concat)
  x_concat = Dropout(0.3)(x_concat)
  x_concat = GlobalAveragePooling1D()(x_concat)
  out = Dense(units=num_class, activation='softmax')(x_concat)
  model = Model(inputs=input_layer, outputs=out)
  return model