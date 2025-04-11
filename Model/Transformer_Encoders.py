def transformer_encoder_cross(paths):
  dim = 16
  heads = 4
  x_concat = concatenate(paths)
  # Extract paths for Q, K, V
  Q, K, V = paths
  #Multi Head Cross Attention
  mha_layer = MultiHeadAttention(num_heads=heads, key_dim=dim)
  attention_output, attention_scores = mha_layer(query=Q, value=V, key=K, return_attention_scores=True)
  #Shape matching
  x_concat = Conv1D(filters=attention_output.shape[-1], kernel_size=1, strides=1, padding='same', activation='relu')(x_concat)
  #Add
  attention_output = Add()([attention_output, x_concat])
  attention_output = LayerNormalization()(attention_output)
  #FFN
  keep_attention_out = attention_output
  attention_out = Dense(units=dim)(attention_output)
  attention_out = ReLU()(attention_out)
  attention_out = Dense(units=dim)(attention_out)
  attention_out = Add()([attention_out, keep_attention_out])
  attention_out = LayerNormalization()(attention_out)
  return attention_out

def transformer_encoder_self(input_layer):
  #Multi Head Self attention
  dim = 16
  heads = 4
  x_old = input_layer
  mha_layer = MultiHeadAttention(num_heads=heads, key_dim=dim)
  attention_output, attention_scores = mha_layer(query=input_layer, value=input_layer, key=input_layer, return_attention_scores=True)
  #Shape matching
  x_old = Conv1D(filters=attention_output.shape[-1], kernel_size=1, strides=1, padding='same', activation='relu')(x_old)
  #Add
  attention_output = Add()([attention_output, x_old])
  attention_output = LayerNormalization()(attention_output)
  #FFN
  keep_attention_out = attention_output
  attention_out = Dense(units=dim)(attention_output)
  attention_out = ReLU()(attention_out)
  attention_out = Dense(units=dim)(attention_out)
  attention_out = Add()([attention_out, keep_attention_out])
  attention_out = LayerNormalization()(attention_out)
  return attention_out