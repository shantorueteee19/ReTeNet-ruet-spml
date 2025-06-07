<h1 align="center">Detailed Architecture of ReTeNet</h1>

<div style="text-align: justify; line-height: 1.6; font-family: 'Arial', sans-serif;">
  <p align="justify">
    The Residual-Encoder and Transformer Encoder Network (ReTeNet) architecture comprises three fundamental processing stages, as illustrated in Fig. 1 of the main manuscript:
  </p>
  <ol type="i" style="margin: 12px 0; padding-left: 30px;">
    <li><strong>Initial Feature Extraction</strong></li>
    <li><strong>Parallel Encoder Paths</strong></li>
    <li><strong>Classification Stage</strong></li>
  </ol>
  <p style="margin-top: 8px;">
    The design specifications and implementation details of each stage are systematically presented below.
  </p>
  <h3 align="center">Initial Feature Extraction</h3>
  <p align="justify">
    The initial feature extraction stage employs a multi-branch architecture consisting of three parallel processing paths, each designed to capture distinct feature representations:
    <ol type="a" style="margin: 12px 0; padding-left: 30px;">
    <li><strong>Spatio-temporal path</strong></li>
    <li><strong>Global spatial path</strong></li>
    <li><strong>Local spatial path</strong></li>
  </ol>
  The detailed specifications of the Spatio-temporal path are provided in <strong> Table 1 </strong>.
  <table>
    <caption> Table 1: Specifications of the spatio-temporal path. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 3 </th> <th> 2 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> LSTM </th> <th> 16 </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> BiLSTM </th> <th> 16 </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 1 </th> <th> 2 </th> <th> ReLU </th>
    </tr>
  </table>
  Now, <strong> Table 2 </strong> thoroughly illustrates the specifications of the global spatial path.
  <table>
    <caption> Table 2: Specifications of the global spatial path. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 33 </th> <th> 2 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 5 </th> <th> 2 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
  </table>
  <p align="justify"> The first convolutional layer with a kernel size of 33 facilitates the extraction of long-range dependencies from the BVP signals, while the subsequent convolutional layer with a smaller kernel size of 5 fine-tunes the extracted features. This hierarchical design reduces convolutional parameters and enables efficient global feature representation. </p>
  </p>
  <p align="justify"> The local spatial path specializes in extracting fine-grained regional features, and the detailed specifications including kernel sizes, strides, number of filters etc. are discussed in <strong> Table 3 </strong>. </p>
  <table>
    <caption> Table 3: Specifications of the local spatial path. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 5 </th> <th> 2 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 3 </th> <th> 2 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
  </table>
    <p align="justify"> The corresponding ouputs from these three parallel paths are x from local spatial, y from global spatial, and z from spatio-temporal paths. </p>
  <h3 align="center">Parallel Encoder Paths</h3>
  <p align="justify"> The parallel encoder paths comprises two distinct parallel paths.
  The paths are:
    <ol type="a" style="margin: 12px 0; padding-left: 30px;">
    <li><strong>Residual encoder path</strong></li>
    <li><strong>Transformer encoder path</strong></li>
  </ol>
  </p>
  <p align="justify">
  The outputs <i>(x, y, z)</i> from the earlier stage are concatenated as 
  <i>h<sub>0</sub> = concat(x, y, z)</i>, and then passed into the residual encoder path.
  This path further processes the features through a combination of residual encoder and multi-resolution CNN (MRCNN) blocks.
  The residual encoder comprises a residual CNN block, a feature recalibration block inspired by the widely adopted squeeze-and-excitation network, and a CNN-based feed-forward network that together emulate the structure of a transformer encoder.
  The output from the residual encoder is subsequently forwarded to the MRCNN block for enhanced refinement and multi-scale feature extraction.
  The internal parameters of the constituent blocks within the residual encoder path are detailed below.
</p>
<p align="justify">
  The <i>h<sub>0</sub></i> is directly passed to the residual CNN block, which consists of two parallel paths along with a skip (residual) connection. 
  The specifications of these paths are detailed in Table 4 and Table 5. 
  The paths are represented as <i>&tau;(.)</i> and <i>&eta;(.)</i>, and the output is computed as 
  <i>h<sub>1</sub> = h<sub>0</sub> + concat(&tau;(&tau;(h<sub>0</sub>)), &eta;(h<sub>0</sub>))</i>.
</p>
<table>
    <caption> Table 4: Specifications of the path <i>&tau;(.)</i>. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 32 </th> <th> 3 </th> <th> 1 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 1 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 24 </th> <th> 3 </th> <th> 1 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 1 </th> <th> 1 </th> <th> - </th>
    </tr>
  </table>
  <table>
    <caption> Table 5: Specifications of the path <i>&eta;(.)</i>. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 24 </th> <th> 3 </th> <th> 1 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 1 </th> <th> 1 </th> <th> - </th>
    </tr>
  </table>
<p align="justify">
  The outputs of the two paths are concatenated and connected through a skip connection. 
  A pointwise convolution (i.e., kernel size = 1) is applied to the skip connection to match the dimensionality of the output tensors. 
  Subsequently, the resulting output is passed through the feature recalibration block, which is discussed in the following subsection.
</p>
<p align="justify">
  The feature recalibration block incorporates multiple processing components that refine and enhance the intermediate feature maps. 
  The specific configurations and operations within this block are summarized in Table 6.
</p>
<table>
    <caption> Table 6: Specifications of the feature recalibration block. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 48 </th> <th> 1 </th> <th> 1 </th> <th> None </th>
    </tr>
    <tr>
      <th> gelu </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> LayerNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> GlobalAveragePooling1D </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Dense </th> <th> 12 </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> ReLU </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> sigmoid </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
  </table>
  <p align="justify">
  After the sigmoid layer, the output is reshaped to a dimension of (1, 48). 
  This reshaped output is then multiplied with the output from the LayerNormalization layer. 
  Subsequently, the result is passed through a softmax layer to normalize the features before proceeding to the next block.
</p>
<p align="justify">
  In our implementation of the feed-forward block, we specifically utilize a convolutional feed-forward structure instead of the fully connected feed-forward network commonly used in standard transformer encoders. 
  The parameters and configuration details of this block are summarized in Table 7.
</p>
<table>
    <caption> Table 7: Specifications of the feed-forward block</i>. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 16 </th> <th> 5 </th> <th> 1 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> Conv1D </th> <th> 48 </th> <th> 3 </th> <th> 1 </th> <th> ReLU </th>
    </tr>
    <tr>
      <th> BatchNormalization </th> <th> - </th> <th> - </th> <th> - </th> <th> - </th>
    </tr>
    <tr>
      <th> MaxPooling1D </th> <th> - </th> <th> 3 </th> <th> 1 </th> <th> - </th>
    </tr>
    <tr>
      <th> Dropout </th> <th> - </th> <th> 0.3 </th> <th> - </th> <th> - </th>
    </tr>
  </table>
<p align="justify">
  Subsequently, the remaining processing steps follow the structure of standard transformer architectures.
</p>

  
</div>
