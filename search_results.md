# 搜索结果：

问题：image noise reduction流程是什么?

## 答案 51：

该专利提供了一种图像处理的自适应抖动方法，通过检查距离选定像素一定距离的像素的平均像素值来确定像素是否处于高对比度区域。如果像素处于平滑的颜色渐变过渡区域，则可以使用额外的抖动或抖动模式来调整像素值，以减少超过较低阈值的选定像素和额外平均像素值之间的差异，从而实现图像降噪的效果。

### 专利信息：


专利号: US13669338
发明名称: Adaptive Dithering During Image Processing
摘要: Systems and method are provided for adjusting certain pixel values in an image. In an embodiment of the invention, an average pixel value of pixels at given distances from a selected pixel are examined to determine if the pixel is in a high-contrast area. If the pixel is in a smooth color gradient transition area, the pixel value may be adjusted in some embodiments using an additional dither or dither pattern to reduce differences between the pixel values of the selected pixel and the additional average pixel values exceeding the lower threshold.
申请人: Apple Inc.

### 相关描述片段：

The text discusses image processing and the need to reduce banding artifacts in smooth color gradient transition areas of an image while maintaining definite transitions between colors in areas with greater contrast. It describes an embodiment of the invention where each pixel may be compared to average values of neighboring pixels at a variety of sampling distances to determine if the pixel is in a smooth gradient area. When the selected pixel is in a smooth gradient area, the pixel may be modified by a dither effect. The text also describes an exemplary image processor to identify and reduce banding artifacts in smooth areas of an image in an embodiment.

## 答案 31：

image noise reduction流程不在该专利信息中提到。该专利信息主要介绍了手持个人电子设备中的位置传感器辅助全景摄影技术，其中包括从电子设备的图像传感器获取图像数据、对获取的图像数据进行“运动滤波”、对相邻捕获的图像进行图像配准、对捕获的图像数据进行几何校正以及将捕获的图像拼接在一起创建全景场景等步骤。

### 专利信息：


专利号: US13109889
发明名称: Positional Sensor-Assisted Image Registration for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for performing positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The panoramic photography techniques disclosed herein include a step-by-step process for improving the capture and processing of panoramic photographs on handheld, personal electronic devices. One of the steps in this process is "performing motion filtering" on the acquired image data, which involves using information obtained from positional sensors for the handheld personal electronic device to inform the processing of the image data. This step helps to filter out image slits that would produce only redundant image data and reduces the memory footprint of the panoramic image processing operation.

## 答案 28：

该专利信息中提到的image noise reduction流程并未被具体描述，而是介绍了一种手持个人电子设备中使用位置传感器辅助进行全景摄影技术的方法，其中包括从图像传感器获取图像数据、对获取的图像数据进行运动滤波、对相邻捕获的图像进行图像配准、对捕获的图像数据进行几何校正以及将捕获的图像拼接在一起创建全景场景等步骤。

### 专利信息：


专利号: US13109878
发明名称: Positional Sensor-Assisted Perspective Correction for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for performing positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The panoramic photography techniques disclosed herein include a step-by-step process for improving the capture and processing of panoramic photographs on handheld, personal electronic devices such as mobile phones, personal data assistants (PDAs), portable music players, digital cameras, as well as laptop and tablet computer systems. The process includes acquiring image data from the electronic device's image sensor's image stream, performing “motion filtering” on the acquired image data, performing image registration between adjacent captured images, performing geometric corrections on captured image data, and “stitching” the captured images together to create the panoramic scene, i.e., blending the image data in the overlap area between adjacent captured images.

## 答案 76：

该专利描述了一种视频编码系统和方法，用于保护解码图像内容免受条纹伪影的影响。该方法通过识别视频数据帧中像素块内容中可能出现条纹伪影的像素块，组装这些像素块的位置，应用抗条纹处理，并进行压缩操作。因此，image noise reduction流程包括识别可能出现条纹伪影的像素块、组装这些像素块的位置、应用抗条纹处理和压缩操作。

### 专利信息：


专利号: US13631428
发明名称: SIGNAL SHAPING TECHNIQUES FOR VIDEO DATA THAT IS SUSCEPTIBLE TO BANDING ARTIFACTS
摘要: Video coding systems and methods protect against banding artifacts in decoded image content. According to the method, a video coder may identify, from content of pixel blocks of a frame of video data, which pixel blocks are likely to exhibit banding artifacts from the video coding/decoding processes. The video coder may assemble regions of the frame that are likely to exhibit banding artifacts based on the identified pixel blocks' locations with respect to each other. The video coder may apply anti-banding processing to pixel blocks within one or more of the identified regions and, thereafter, may code the processed frame by a compression operation.
申请人: Apple Inc.

### 相关描述片段：

The text discusses video coding systems and methods, including the use of predictive coding techniques to achieve compression and the identification and processing of pixel blocks likely to exhibit banding artifacts. The text also describes the components of a video coding system, including a video source, pre-processor, video coder, transmitter, and controller. The video coder performs coding operations on the video sequence to reduce the bit rate, including motion compensated predictive coding and the use of reference frames. The controller manages coding operations to meet target bit rate, quality, and error resiliency requirements.

## 答案 64：

该专利信息并未涉及到image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US13595695
发明名称: METHOD AND APPARATUS FOR RESIZING BUFFERED WINDOWS
摘要: Methods and apparatuses for resizing buffered windows. In one aspect of the invention, a method to resize a buffered window on a data processing system includes: determining an estimated size for a window which has a first pixel image of a first size buffered in a first window buffer; allocating a second window buffer which is large enough to buffer the window in the estimated size; and buffering a second pixel image of the window in a second size in the second window buffer. In one example according to this aspect, a portion of a frame buffer is updated to the second pixel image to display the window in the second size. A portion of the second window buffer, storing the data that represents the second pixel image, is clipped to update the corresponding portion of the frame buffer.
申请人: Apple Inc.

### 相关描述片段：

无相关部分，需要提供更多信息或更明确的问题。

## 答案 29：

image noise reduction流程在该专利信息中未被提及。该专利信息主要介绍了一种利用位置传感器辅助的全景摄影技术，其中包括从电子设备的图像传感器获取图像数据、对获取的图像数据进行“运动滤波”、对相邻捕获的图像进行图像配准、对捕获的图像数据进行几何校正以及将捕获的图像拼接在一起创建全景场景等步骤。

### 专利信息：


专利号: US13109883
发明名称: Positional Sensor-Assisted Motion Filtering for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for perforating positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The panoramic photography techniques disclosed herein include a step-by-step process for improving the capture and processing of panoramic photographs on handheld, personal electronic devices such as mobile phones, personal data assistants (PDAs), portable music players, digital cameras, as well as laptop and tablet computer systems. One of the steps in this process is performing "motion filtering" on the acquired image data, using information obtained from positional sensors for the handheld personal electronic device to inform the processing of the image data. This step helps to filter out image slits that would produce only redundant image data, reducing the memory footprint of the panoramic image processing operation.

## 答案 30：

该专利中提到的image noise reduction流程并未被具体描述，但是该专利涉及到手持个人电子设备进行全景摄影技术的方法，其中包括从电子设备的图像传感器获取图像数据、对获取的图像数据进行运动滤波、对相邻捕获的图像进行图像配准、对捕获的图像数据进行几何校正以及将捕获的图像拼接在一起创建全景场景等步骤。在相邻捕获的图像重叠区域中，还需要进行图像融合以减少噪声。

### 专利信息：


专利号: US13109941
发明名称: Intelligent Image Blending for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for performing positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The panoramic photography techniques disclosed herein include a step-by-step process for improving the capture and processing of panoramic photographs on handheld, personal electronic devices such as mobile phones, personal data assistants (PDAs), portable music players, digital cameras, as well as laptop and tablet computer systems. The process includes acquiring image data from the electronic device's image sensor's image stream, performing “motion filtering” on the acquired image data, performing image registration between adjacent captured images, performing geometric corrections on captured image data, and “stitching” the captured images together to create the panoramic scene, i.e., blending the image data in the overlap area between adjacent captured images.

## 答案 62：

该专利信息并未提及image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US13762276
发明名称: DISPLAYS WITH MINIMIZED CROSSTALK
摘要: Display ground plane structures may contain slits. Image pixel electrodes in the display may be arranged in rows and columns. Image pixels in the display may be controlled using gate lines that are associated with the rows and data lines that are associated with the columns. An electric field may be produced by each image pixel electrode that extends through a liquid crystal layer to an associated portion of the ground plane. The slits in the ground plane may have a slit width. Data lines may be located sufficiently below the ground plane and sufficiently out of alignment with the slits to minimize crosstalk from parasitic electric fields. A three-column inversion scheme may be used when driving data line signals into the display, so that pairs of pixels that straddle the slits are each driven with a common polarity. Gate line scanning patterns may be used that enhance display uniformity.
申请人: Apple Inc.

### 相关描述片段：

Displays such as liquid crystal displays may be provided that include ground plane structures with slits. A display may include rows and columns of image pixel electrodes. Image pixels in the display may be controlled using gate lines that are associated with the rows and data lines that are associated with the columns. An electric field may be produced by each image pixel electrode that extends through a liquid crystal layer to an associated portion of the ground plane. Data lines may be located sufficiently below the ground plane and sufficiently out of alignment with the slits to minimize parasitic electric fields. Display driver circuitry in the display may drive the data lines using a polarity pattern that promotes color uniformity.

## 答案 55：

该专利信息并未涉及到image noise reduction流程，无法提供相关答案。

### 专利信息：


专利号: US13543799
发明名称: Manipulation of Image Content Using Various Image Representations
摘要: Disclosed herein are embodiments of systems and methods for displaying and updating image previews in the graphical user interface of an application program. The image previews for a given master image within the application program constitute various image sizes and resolutions of that master image, and are preferably compiled as image preview data sets in a database. When the image previews are manipulated in the application program an appropriate resolution for that image preview can be queried from the database and displayed. For example, while scrolling, a lower-resolution image preview data set might he used when compared to image preview data sets used while the image previews are not scrolled, thus making them less computationally intensive to display and update. Likewise, while magnifying, an appropriate image preview data set can be queried from the database instead of, or in conjunction with, up or downscaling the image preview.
申请人: Apple Inc.

### 相关描述片段：

Disclosed herein are embodiments of systems and methods for displaying and updating image previews in the graphical user interface of an application program running on a computer. The image previews for a given master image within the application program constitute various image sizes and resolution of that master image, and are preferably compiled as image preview data sets in a database accessible by the application program. The image preview data sets may be compressed or uncompressed, and may be memory-map formatted to facilitate their display. When the image previews are manipulated in the applications program by a user, for example by scrolling or magnifying them, an appropriate resolution for that image preview can be queried from the database and displayed.

## 答案 65：

该专利信息并未提及image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US13344486
发明名称: COVER FOR IMAGE SENSOR ASSEMBLY WITH LIGHT ABSORBING LAYER
摘要: An image sensor assembly includes an image sensor die attached adjacent to a cavity and a lower surface in a preformed package having substantially vertical surfaces extending from the lower surface to an upper surface of the package. The image sensor die may include a charge-coupled device or an active pixel sensor imager that provides the light receiving surface for capturing the image. A cover is placed over the upper surface of the package. The cover may be a glass cover or an infrared cut filter. A light absorbing layer is applied to the cover in registry with the image sensor die such that the light absorbing layer prevents light from falling on the substantially vertical surfaces of the preformed package without preventing the passage of light that falls on the light receiving surface of the image sensor die.
申请人: Apple Inc

### 相关描述片段：

The text describes an image sensor assembly that includes an image sensor die attached to a cavity in a preformed package with substantially vertical surfaces. The assembly includes a cover placed over the upper surface of the package, which may be a glass cover or an infrared cut filter. A light absorbing layer is applied to the cover in registry with the image sensor die to prevent light from falling on the substantially vertical surfaces of the package and degrading the image formed. The text does not provide a detailed description of an image noise reduction process.

## 答案 42：

该专利信息中未提及image noise reduction流程。

### 专利信息：


专利号: US13247901
发明名称: Facilitating Image Capture and Image Review by Visually Impaired Users
摘要: Techniques and mechanisms are provided for facilitating the capture and review of visual images by visually impaired users. In one implementation, these techniques and mechanisms provide pre image capture functionality and captured image review functionality. With the pre image capture functionality, audio messages are provided to the user to help the user position an image capturing mechanism properly to capture the desired subjects in a picture, to frame the subjects properly within the picture, to size the subjects properly within the picture, etc. With the image review functionality, audio messages are provided to the user to help the user enjoy and “visualize” a visual image that has been captured and is being displayed to the user. With these functionalities, a visually impaired user is able capture and review images to a much greater degree than is currently possible.
申请人: Apple Inc.

### 相关描述片段：

"With the pre image capture functionality, a user may direct an electronic device having an image capturing mechanism (e.g. a camera) at a scene. Periodically, or in response to user invocation of some control of the device (e.g. by touching some control or making some gesture or movement), the device pre-captures an image of the scene. After the image is pre-captured, the device analyzes the image. For example, the device may apply facial detection techniques to determine how many faces are in the image. The device may also identify the pixels that make up each face so that the location of each face within the pre-captured image is determined. In addition, the device may apply facial recognition techniques to identify the faces. Thus, rather than referring to a face in the pre-captured image as “face ”, the device may identify the face as “Zachary”. Furthermore, the device may analyze the pre-captured image to determine whether any of the faces are too close to an edge (e.g. left, right, top and bottom) of the picture. The device may further analyze the pre-captured image to determine the sizes of the faces relative to the overall size of the picture."

## 答案 81：

该专利信息并未提及image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US13961587
发明名称: COVER FOR IMAGE SENSOR ASSEMBLY WITH LIGHT ABSORBING LAYER AND ALIGNMENT FEATURES
摘要: An image sensor assembly includes an image sensor die attached adjacent to a cavity and a lower surface in a preformed package having substantially vertical surfaces extending from the lower surface to an upper surface of the package. The image sensor die provides the light receiving surface for capturing the image. A light absorbing layer is applied to a cover such that the light absorbing layer prevents light from falling on the substantially vertical surfaces of the preformed package without preventing the passage of light that falls on the light receiving surface of the image sensor die. The light absorbing layer includes openings that provide a line-of-sight view of two opposing corners of at least one of the light receiving surface and the image sensor die to facilitate placing the cover over the upper surface of the package in registry with the image sensor die.
申请人: Apple Inc.

### 相关描述片段：

本文没有提到image noise reduction流程，没有相关部分。

## 答案 100：

该专利信息并未提及image noise reduction流程，而是介绍了一种指纹图像纠错方法和移动通信设备。该方法通过匹配指纹图像信息中的一组样本，确定指纹图像处理的程度和错误程度，并根据最佳值对指纹图像信息进行处理。因此，该专利信息与image noise reduction流程无关。

### 专利信息：


专利号: US13842052
发明名称: Edge Detection and Stitching
摘要: An error correction method and a mobile communication device incorporating the error correction method. The error correction method begins with receiving fingerprint image information that includes a set of swatches. A first one of the received swatches is matched to a second one of the swatches at an edge. A measure of fingerprint image manipulation is determined responsive to an amount of processing to perform and an amount of fingerprint image error. Then the fingerprint image information is manipulated in response to an optimum value of the measure.
申请人: Apple Inc.

### 相关描述片段：

The text describes techniques for fingerprint image processing, including image noise reduction. In one embodiment, techniques can include providing a fingerprint recognition sensor in which one or more portions of each fingerprint image are examined for blurring, motion, and other artifacts. The degree of correction applied to each individual portion of each fingerprint image is responsive to a tradeoff between image quality and time needed for image capture. The degree of correction applied is also responsive to a target signal to noise ratio (SNR) as well as to a minimal acceptable signal to noise ratio.

## 答案 71：

该专利信息中并未提及image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US13629455
发明名称: IMAGING SENSOR ANOMALOUS PIXEL COLUMN DETECTION AND CALIBRATION
摘要: An imaging sensor is signaled to capture a digital image of a dark scene. For each of the pixel columns in the image, a respective column value is computed that represents at least some of the pixels in the column. For each of the pixel columns in the image, a respective comparison is made between the respective column value of the pixel column and a reference value. A respective column score is computed, for each of the pixel columns, based on the respective comparison. An indication that identifies one or more of the pixel columns as anomalous is stored, when the respective column score of the one or more the pixel columns does not meet a criterion. Other embodiments are also described and claimed.
申请人: Apple Inc.

### 相关描述片段：

The text describes a technique for detecting and calibrating column noise in imaging sensors. It involves capturing a digital image of a dark scene and computing a respective column value for each column of the image. One or more comparisons are made between the respective column value and one or more reference values, and a column noise score is computed for each column based on the comparisons. A calibration map is then stored that identifies which of the pixel columns are anomalous, i.e. their column noise scores do not meet a predetermined criterion.

## 答案 50：

该专利信息并未涉及到image noise reduction流程的具体内容，因此无法回答该问题。

### 专利信息：


专利号: US13229363
发明名称: DIGITAL CAMERA WITH LIGHT SPLITTER
摘要: A digital camera component is described that has a light splitter cube having an entrance face to receive incident light from a camera scene. The cube splits the incident light into first, second, and third color components that emerge from the cube through a first face, a second face, and a third face of the cube, respectively. First, second, and third image sensors are provided, each being positioned to receive a respective one of the color components that emerge from the first, second, and third faces of the cube. Other embodiments are also described and claimed.
申请人: Apple Inc.

### 相关描述片段：

An embodiment of the invention is a digital camera component that has a light splitter cube having an entrance face to receive incident light from a camera scene. The cube splits the incident light into three color components that emerge from the cube through respective faces of the cube. Three image sensors are also provided, where each sensor is positioned to receive a respective one of the color components that emerge from the respective face of the cube. The image sensors may be clear pixel array sensors that have no color filter array or color separation capabilities, making them relatively inexpensive yet more accurate (due to no color interpolation or demosaicing required).

## 答案 92：

以上专利信息并未提及image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US13629529
发明名称: COLOR BALANCE TOOLS FOR EDITING IMAGES
摘要: Some embodiments provide a method for color balancing an image. The method receives a first selection of a first mode of a color balance tool that includes several different color balance modes. Each color balance mode is for applying color balance operations to the image. The method uses the first mode of the color balance tool to apply a first set of color balance operations to the image. The method receives a second selection to switch from the first mode to a second mode of the color balance tool. The method uses the second mode of the color balance tool to apply a second set of color balance operations to the image.
申请人: Apple Inc.

### 相关描述片段：

"In some embodiments, the color balance tool includes a mode for performing color balance operations on an image based on skin tones identified in the image, a mode for performing color balance operations on the image based on a color cast identified in the image, and a mode for performing color balance operations on the image based on temperature and tint adjustments."

## 答案 17：

该专利信息并未涉及到image noise reduction流程的内容。

### 专利信息：


专利号: US13010692
发明名称: DISPLAY RESOLUTION INCREASE WITH MECHANICAL ACTUATION
摘要: There are provided apparatuses and methods for increasing the pixel density of a digital display through mechanical actuation. In some embodiments, a display device is described having a processor configured to provide an image for display and a memory coupled to the processor. The memory stores the image and is configured to map the image to a pixel matrix. A display controller is coupled to the memory and configured to sample portions of the image and to store the portions of the image into planes. Each sampled portion comprises a different set of pixels of the pixel matrix. A display is coupled to the display controller and is configured to display the contents of the sampled planes. In particular, the display controller is configured to sequentially provide the sampled planes to the display for sequential display. At least one actuator is coupled to the display to displace the display for the displaying of the sampled planes, so that pixels of each plane are displayed in a unique location from the pixels of other planes.
申请人: Apple Inc.

### 相关描述片段：

提供了通过机械作用增加数字显示器像素密度的装置和方法。一般地，数字显示器的像素密度通过将图像分成不同的平面并将平面的内容顺序提供给显示器来增加。为了显示每个平面的内容，显示器被位移，以便每个平面的像素在与其他平面不同的位置显示。因此，原始图像的所有内容都在单个刷新帧内显示，显示器的像素密度似乎比显示器的物理像素密度更高。此外，还提供了一种通过机械作用增加分辨率的方法，其中将图像发送到内存缓冲区并将图像映射到像素矩阵中。像素矩阵可以分成多个平面，每个平面具有图像的不同像素集。平面可以按顺序显示其各自的像素，并且显示器可以通过执行器移位，以便每个平面的像素在唯一位置显示。因此，尽管显示设备的物理像素数量有限，通过移动物理像素并显示另一组像素，像素密度似乎已经增加。

## 答案 1：

该专利信息中未提及image noise reduction流程，因此无法回答该问题。

### 专利信息：


专利号: US12857903
发明名称: IMAGE CAPTURE USING LUMINANCE AND CHROMINANCE SENSORS
摘要: Methods and apparatuses disclosed herein relate to image sensing devices. One embodiment may take the form of an image sensing device that includes a first image sensor for capturing a luminance image, a second image sensor for capturing a first chrominance, and a third image sensor for capturing a second chrominance image. The image sensing device may further include an image processing module for combining the luminance image captured by the first image sensor, the first chrominance image captured by the second image sensor, and the second chrominance image captured by the third image sensor, to form a composite image.
申请人: Apple Inc.

### 相关描述片段：

Embodiments described herein relate to systems, apparatuses and methods for capturing an image using one or more dedicated image sensors to capture luminance and chrominance portions of an image. One embodiment may take the form of an image sensing device that includes a first image sensor for capturing a luminance image, a second image sensor for capturing a first chrominance, and a third image sensor for capturing a second chrominance image. The image sensing device may further include an image processing module for combining the luminance image captured by the first image sensor, the first chrominance image captured by the second image sensor, and the second chrominance image captured by the third image sensor, to form a composite image.

## 答案 5：

该专利信息中未提及image noise reduction流程，无法回答该问题。

### 专利信息：


专利号: US13246821
发明名称: IMAGE CAPTURE USING THREE-DIMENSIONAL RECONSTRUCTION
摘要: Embodiments may take the form of three-dimensional image sensing devices configured to capture an image including one or more objects. In one embodiments, the three-dimensional image sensing device includes a first image device configured to capture a first image and extract depth information for the one or more objects. Additionally, the image sensing device includes a second imaging device configured to capture a second image and determine an orientation of a surface of the one or more objects.
申请人: Apple Inc.

### 相关描述片段：

The text describes embodiments of a three-dimensional imaging apparatus that captures at least one image including one or more objects. The apparatus includes a first sensor for capturing a polarized image, a second sensor for capturing a first non-polarized image, a third sensor for capturing a second non-polarized image, and at least one processing module for deriving depth information for the one or more objects utilizing at least the first non-polarized image and the second non-polarized image, the processing module further operative to combine the polarized image, the first non-polarized image, and the second non-polarized image to form a composite three-dimensional image. The text does not specifically mention an image noise reduction process.

## 答案 14：

该专利信息并未提及image noise reduction流程，无法回答该问题。

### 专利信息：


专利号: US13401575
发明名称: LIGHT ISOLATING PROTECTIVE COVER FOR SMALL FORM FACTOR ELECTRONIC DEVICE
摘要: A portable device has a rear facing camera assembly and a front facing display assembly that includes at least a protective cover layer, a display stack that includes a plurality of display components arranged in a plurality of interconnected layers, the display stack providing an imaging service, and a flat support chassis arranged to provide support for the display stack. In the described embodiment, a protective cover can wrap around and protect at least the rear portion of the portable device without adversely affecting an image capture process carried out by the rear facing camera assembly.
申请人: Apple Inc.

### 相关描述片段：

The described embodiments relate generally to small form factor electronic devices. More particularly, providing a protective cover for a small form factor electronic device having a rear facing camera assembly, the protective cover prevents light bleed from the light source interfering with the image capture by the rear facing camera assembly. A protective cover for a small form factor electronic is described. The small form factor electronic device has at least a rear facing camera assembly, the camera assembly having a lens assembly and a light source in close proximity to the lens assembly, the light source arranged to emit light used to illuminate a subject, the lens assembly arranged to capture at least some of the light reflected from the subject wherein a portion of the light reflected from the subject is provided by the light source. The protective cover also includes at least a light blocking mechanism that prevents light emitted by the light source and reflected by anything other than the subject being illuminated from reaching the lens assembly.
