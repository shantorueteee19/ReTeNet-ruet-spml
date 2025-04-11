def cnn_large(input_layer):
    # Convolutional Layer 1
    x = Conv1D(filters=16, kernel_size=21, strides=4, padding='same', activation='relu')(input_layer)
    x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    # Convolutional Layer 2
    x = Conv1D(filters=32, kernel_size=7, strides=1, padding='same', activation='relu')(x)
    x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    # Convolutional Layer 3
    x = Conv1D(filters=16, kernel_size=3, strides=1, padding='same', activation='relu')(x)
    x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    return x

def cnn_small(input_layer):
    x = Conv1D(filters=16, kernel_size=3, strides=4, padding='same', activation='relu')(input_layer)
    x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    x = Conv1D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu')(x)
    x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    x = Conv1D(filters=16, kernel_size=3, strides=1, padding='same', activation='relu')(x)
    x = MaxPooling1D(pool_size=3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    return x

def mrcnn(input_layer):
    inputs = input_layer

    smrcnn = cnn_small(inputs)
    lmrcnn = cnn_large(inputs)
    
    # Pointwise conv
    input_point_wise = Conv1D(filters=32, kernel_size=1, strides=4, padding='same', activation='relu')(inputs)
    input_point_wise = MaxPooling1D(pool_size=3, strides=1, padding='same')(input_point_wise)
    input_point_wise = Conv1D(filters=16, kernel_size=1, strides=1, padding='same', activation='relu')(input_point_wise)
    input_point_wise = MaxPooling1D(pool_size=3, strides=1, padding='same')(input_point_wise)
    
    # Concat
    x = concatenate([smrcnn, lmrcnn, input_point_wise])
    return x