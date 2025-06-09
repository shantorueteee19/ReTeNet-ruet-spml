<h1 align="center">Detailed Protocol for RUET SPML Data Collection</h1>

<div style="text-align: justify; line-height: 1.6; font-family: 'Arial', sans-serif;">
  <h3>Task Recording Algorithm</h3>

  <ol>
    <li>Start recording</li>
    <li>Initialize counter <code>i = 0</code></li>
    <li>Repeat while <code>i ≤ 3</code>:
      <ol type="a">
        <li>Record <strong>Task-i</strong> for 3 minutes</li>
        <li>Wait for 30 seconds (interval)</li>
        <li>Increment <code>i</code> by 1 (<code>i = i + 1</code>)</li>
      </ol>
    </li>
    <li>End</li>
  </ol>
</div>

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
      <td> Conv1D </td> <td> 16 </td> <td> 3 </td> <td> 2 </td> <td> ReLU </td>
    </tr>
    <tr>
      <td> BatchNormalization </td> <td> - </td> <td> - </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> MaxPooling1D </td> <td> - </td> <td> 3 </td> <td> 1 </td> <td> - </td>
    </tr>
    <tr>
      <td> Dropout </td> <td> - </td> <td> 0.3 </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> LSTM </td> <td> 16 </td> <td> - </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> Dropout </td> <td> - </td> <td> 0.3 </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> BiLSTM </td> <td> 16 </td> <td> - </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> Dropout </td> <td> - </td> <td> 0.3 </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> Conv1D </td> <td> 16 </td> <td> 1 </td> <td> 2 </td> <td> ReLU </td>
    </tr>
  </table>
  Now, <strong> Table 2 </strong> thoroughly illustrates the specifications of the global spatial path.
  <table>
    <caption> Table 2: Specifications of the global spatial path. </caption>
    <tr>
      <th> Layer </th> <th> Units </th> <th> Size </th> <th> Strides </th> <th> Activation </th>
    </tr>
    <tr>
      <td> Conv1D </td> <td> 16 </td> <td> 33 </td> <td> 2 </td> <td> ReLU </td>
    </tr>
    <tr>
      <td> BatchNormalization </td> <td> - </td> <td> - </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> MaxPooling1D </td> <td> - </td> <td> 3 </td> <td> 1 </td> <td> - </td>
    </tr>
    <tr>
      <td> Dropout </td> <td> - </td> <td> 0.3 </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> Conv1D </td> <th> 16 </td> <td> 5 </td> <td> 2 </td> <td> ReLU </td>
    </tr>
    <tr>
      <td> BatchNormalization </td> <td> - </td> <td> - </td> <td> - </td> <td> - </td>
    </tr>
    <tr>
      <td> MaxPooling1D </td> <td> - </td> <td> 3 </td> <td> 1 </td> <td> - </td>
    </tr>
    <tr>
      <td> Dropout </td> <td> - </td> <td> 0.3 </td> <td> - </td> <td> - </td>
    </tr>
  </table>
  <p align="justify"> The first convolutional layer with a kernel size of 33 facilitates the extraction of long-range dependencies from the BVP signals, while the subsequent convolutional layer with a smaller kernel size of 5 fine-tunes the extracted features. This hierarchical design reduces convolutional parameters and enables efficient global feature representation. </p>
  </p>
  <p align="justify"> The local spatial path specializes in extracting fine-grained regional features, and the detailed specifications including kernel sizes, strides, number of filters etc. are discussed in <strong> Table 3 </strong>. </p>
  <table>
  <caption><b>Table 3:</b> Specifications of the local spatial path.</caption>
  <tr>
    <th>Layer</th>
    <th>Units</th>
    <th>Size</th>
    <th>Strides</th>
    <th>Activation</th>
  </tr>
  <tr>
    <td>Conv1D</td><td>16</td><td>5</td><td>2</td><td>ReLU</td>
  </tr>
  <tr>
    <td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td><td>-</td><td>3</td><td>1</td><td>-</td>
  </tr>
  <tr>
    <td>Dropout</td><td>-</td><td>0.3</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td><td>16</td><td>3</td><td>2</td><td>ReLU</td>
  </tr>
  <tr>
    <td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td><td>-</td><td>3</td><td>1</td><td>-</td>
  </tr>
  <tr>
    <td>Dropout</td><td>-</td><td>0.3</td><td>-</td><td>-</td>
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
  <caption><b>Table 4:</b> Specifications of the path <i>&tau;(.)</i>.</caption>
  <tr>
    <th>Layer</th><th>Units</th><th>Size</th><th>Strides</th><th>Activation</th>
  </tr>
  <tr><td>Conv1D</td><td>32</td><td>3</td><td>1</td><td>ReLU</td></tr>
  <tr><td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>MaxPooling1D</td><td>-</td><td>1</td><td>1</td><td>-</td></tr>
  <tr><td>Conv1D</td><td>24</td><td>3</td><td>1</td><td>ReLU</td></tr>
  <tr><td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>MaxPooling1D</td><td>-</td><td>1</td><td>1</td><td>-</td></tr>
</table>
<table>
  <caption><b>Table 5:</b> Specifications of the path <i>&eta;(.)</i>.</caption>
  <tr>
    <th>Layer</th><th>Units</th><th>Size</th><th>Strides</th><th>Activation</th>
  </tr>
  <tr><td>Conv1D</td><td>24</td><td>3</td><td>1</td><td>ReLU</td></tr>
  <tr><td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>MaxPooling1D</td><td>-</td><td>1</td><td>1</td><td>-</td></tr>
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
  <caption><b>Table 6:</b> Specifications of the feature recalibration block.</caption>
  <tr>
    <th>Layer</th>
    <th>Units</th>
    <th>Size</th>
    <th>Strides</th>
    <th>Activation</th>
  </tr>
  <tr><td>Conv1D</td><td>48</td><td>1</td><td>1</td><td>None</td></tr>
  <tr><td>gelu</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>LayerNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>GlobalAveragePooling1D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>Dense</td><td>12</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>ReLU</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>sigmoid</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
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
  <caption><b>Table 7:</b> Specifications of the feed-forward block.</caption>
  <tr>
    <th>Layer</th>
    <th>Units</th>
    <th>Size</th>
    <th>Strides</th>
    <th>Activation</th>
  </tr>
  <tr><td>Conv1D</td><td>16</td><td>5</td><td>1</td><td>ReLU</td></tr>
  <tr><td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>MaxPooling1D</td><td>-</td><td>3</td><td>1</td><td>-</td></tr>
  <tr><td>Dropout</td><td>-</td><td>0.3</td><td>-</td><td>-</td></tr>
  <tr><td>Conv1D</td><td>48</td><td>3</td><td>1</td><td>ReLU</td></tr>
  <tr><td>BatchNormalization</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  <tr><td>MaxPooling1D</td><td>-</td><td>3</td><td>1</td><td>-</td></tr>
  <tr><td>Dropout</td><td>-</td><td>0.3</td><td>-</td><td>-</td></tr>
</table>
<p align="justify">
  Subsequently, the remaining processing steps follow the structure of standard transformer architectures and yield <i>h<sub>2</sub></i>.
</p>
<p align="justify">
  Finally, <i>h<sub>2</sub></i> is passed through an MRCNN block consisting of two parallel paths—one employing a large kernel size and the other using a small kernel size—to capture multi-resolution features. The outputs of both paths are then concatenated. An identical MRCNN block is also utilized in the transformer encoder path. The specifications are detailed in Table 8 and Table 9 respectively.
</p>
<table>
  <caption><b>Table 8:</b> Specifications of the MRCNN path with large kernel path.</caption>
  <tr>
    <th>Layer</th> <th>Filters</th> <th>Kernel Size</th> <th>Strides</th> <th>Activation</th>
  </tr>
  <tr>
    <td>Conv1D</td> <td>16</td> <td>21</td> <td>4</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>3</td> <td>1</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td> <td>32</td> <td>7</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>3</td> <td>1</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td> <td>16</td> <td>3</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>3</td> <td>1</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
</table>
<table>
  <caption><b>Table 9:</b> Specifications of the MRCNN path with small kernel path.</caption>
  <tr>
    <th>Layer</th> <th>Filters</th> <th>Kernel Size</th> <th>Strides</th> <th>Activation</th>
  </tr>
  <tr>
    <td>Conv1D</td> <td>16</td> <td>3</td> <td>4</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>3</td> <td>1</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td> <td>32</td> <td>5</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>3</td> <td>1</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td> <td>16</td> <td>3</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>3</td> <td>1</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
</table>
  <p align="justify">
 The MRCNN yields <i>h<sub>re</sub></i> for further processing.
</p>
<p align="justify">
 The transformer encoder path consists of three encoders, where the encoder-1 comprises a multihead cross attention (MHCA) layer unlike other two encoders multihead self attention (MHSA). The encoders posseses a same number of dimensions and heads. The parameters are summarized in Table 10.
</p>
<table>
  <caption><b>Table 9:</b> Specifications of the MRCNN path with small kernel path.</caption>
  <tr>
    <th>Component</th> <th>Dimension/Unit</th> <th>head</th> <th>Activation</th>
  </tr>
  <tr>
    <td>MHCA</td> <td>16</td> <th>4</td> <td>-</td>
  </tr>
  <tr>
    <td>MHSA</td> <td>16</td> <th>4</td> <td>-</td>
  </tr>
  <tr>
    <td>Dense</td> <td>16</td> <th>-</td> <td>-</td>
  </tr>
</table>
<p align="justify">
  The remaining processes are clearly illustrated in Fig. 1 of the main manuscript. 
  The outputs from each encoder are concatenated and passed through an MRCNN block, producing <i>h<sub>te</sub></i>. 
  This is then concatenated with <i>h<sub>re</sub></i> and forwarded to the classification stage for final prediction.
</p>
<h3 align="center">Classification Stage</h3>
<p align="justify">
  The detailed insights into the classification stage are summarized in Table 11.
</p>
<table>
  <caption><b>Table 11:</b> Specifications of the Classification Stage.</caption>
  <tr>
    <th>Layer</th> <th>Units</th> <th>Kernel</th> <th>Strides</th> <th>Activation</th>
  </tr>
  <tr>
    <td>Conv1D</td> <td>64</td> <td>3</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>2</td> <td>2</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td> <td>32</td> <td>3</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>2</td> <td>2</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Conv1D</td> <td>16</td> <td>3</td> <td>1</td> <td>ReLU</td>
  </tr>
  <tr>
    <td>MaxPooling1D</td> <td>-</td> <td>2</td> <td>2</td> <td>-</td>
  </tr>
  <tr>
    <td>BatchNormalization</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dropout</td> <td>-</td> <td>0.3</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>GlobalAveragePooling1D</td> <td>-</td> <td>-</td> <td>-</td> <td>-</td>
  </tr>
  <tr>
    <td>Dense</td> <td><i>2</i></td> <td>-</td> <td>-</td> <td>Softmax</td>
  </tr>
</table>
</div>
