<h1 align="center">Detailed Architecture of ReTeNet</h1>

<div style="text-align: justify; line-height: 1.6; font-family: 'Arial', sans-serif;">
  <p align="justify">
    The Residual-Encoder and Transformer Encoder Network (ReTeNet) architecture comprises three fundamental processing stages, as illustrated in Fig. 1 of the main manuscript:
  </p>
  <ol type="i" style="margin: 12px 0; padding-left: 30px;">
    <li><strong>Initial Feature Extraction</strong></li>
    <li><strong>Parallel Encoder Pathways</strong></li>
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
</div>
