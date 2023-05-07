# 搜索结果：

问题：image fusion实现过程?

## 答案 51：

该专利是关于在图像处理过程中进行自适应抖动的系统和方法。其中，通过检查距离所选像素一定距离处的像素的平均像素值来确定像素是否处于高对比度区域。如果像素处于平滑的颜色渐变过渡区域，则可以使用额外的抖动或抖动模式来调整像素值，以减少超过下限阈值的附加平均像素值与所选像素值之间的差异。这可以用于图像融合的实现过程中。该专利由苹果公司申请。

### 专利信息：


专利号: US13669338
发明名称: Adaptive Dithering During Image Processing
摘要: Systems and method are provided for adjusting certain pixel values in an image. In an embodiment of the invention, an average pixel value of pixels at given distances from a selected pixel are examined to determine if the pixel is in a high-contrast area. If the pixel is in a smooth color gradient transition area, the pixel value may be adjusted in some embodiments using an additional dither or dither pattern to reduce differences between the pixel values of the selected pixel and the additional average pixel values exceeding the lower threshold.
申请人: Apple Inc.

### 相关描述片段：

The text discusses image processing and the need to reduce banding artifacts in smooth color gradient transition areas of an image while maintaining definite transitions between colors in areas with greater contrast. It also describes an embodiment of an image processing system that includes a smooth transition detector, dither pattern, mixer, and adder to identify and reduce banding artifacts in smooth areas of an image.

## 答案 64：

该专利信息并不涉及到image fusion实现过程，而是关于一种调整缓冲窗口大小的方法和装置。具体实现包括确定一个估计大小的窗口，分配一个足够大的窗口缓冲区来缓冲该窗口，并将窗口的第二个像素图像以第二个大小缓冲到第二个窗口缓冲区中。该方法可以用于数据处理系统中。该专利由苹果公司申请。

### 专利信息：


专利号: US13595695
发明名称: METHOD AND APPARATUS FOR RESIZING BUFFERED WINDOWS
摘要: Methods and apparatuses for resizing buffered windows. In one aspect of the invention, a method to resize a buffered window on a data processing system includes: determining an estimated size for a window which has a first pixel image of a first size buffered in a first window buffer; allocating a second window buffer which is large enough to buffer the window in the estimated size; and buffering a second pixel image of the window in a second size in the second window buffer. In one example according to this aspect, a portion of a frame buffer is updated to the second pixel image to display the window in the second size. A portion of the second window buffer, storing the data that represents the second pixel image, is clipped to update the corresponding portion of the frame buffer.
申请人: Apple Inc.

### 相关描述片段：

无法提取相关部分，因为文本中没有任何信息。

## 答案 30：

该专利信息介绍了一种利用手持个人电子设备进行位置传感器辅助全景摄影技术的设备、方法和计算机可读介质。实现全景图像融合的一般步骤包括：1）从电子设备的图像传感器获取图像数据；2）对获取的图像数据进行“运动滤波”，例如使用电子设备的位置传感器返回的信息来指导图像数据的处理；3）在相邻捕获的图像之间进行图像配准；4）对捕获的图像数据进行几何校正，例如由于透视变化和/或相机围绕非中心透视（COP）相机点旋转而引起的校正；5）将捕获的图像拼接在一起以创建全景场景，例如在相邻捕获的图像之间混合图像数据。最终拼接的全景图像可以在存储之前进行裁剪。该技术可以应用于苹果公司的电子设备中。

### 专利信息：


专利号: US13109941
发明名称: Intelligent Image Blending for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for performing positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The disclosed embodiments relate to techniques for improving panoramic photography for handheld personal electronic devices with image sensors. The panoramic photography techniques disclosed herein are designed to handle a range of panoramic scenes as captured by handheld personal electronic devices. Generalized steps to carry out the panoramic photography techniques described herein include: 1.) acquiring image data from the electronic device's image sensor's image stream; 2.) performing “motion filtering” on the acquired image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data; and 5.) “stitching” the captured images together to create the panoramic scene, i.e., blending the image data in the overlap area between adjacent captured images.

## 答案 31：

该专利介绍了一种利用位置传感器辅助的全景摄影技术，包括从电子设备的图像传感器获取图像数据、对获取的图像数据进行“运动滤波”处理、对相邻捕获的图像进行图像配准、对捕获的图像数据进行几何校正、将捕获的图像拼接在一起以创建全景场景等步骤。最终拼接的全景图像可以在存储之前进行裁剪。该技术可以应用于手持个人电子设备中。

### 专利信息：


专利号: US13109889
发明名称: Positional Sensor-Assisted Image Registration for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for performing positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The disclosed embodiments relate to techniques for improving panoramic photography for handheld personal electronic devices with image sensors. The panoramic photography techniques disclosed herein are designed to handle a range of panoramic scenes as captured by handheld personal electronic devices. Generalized steps to carry out the panoramic photography techniques described herein include: 1.) acquiring image data from the electronic device's image sensor's image stream; 2.) performing “motion filtering” on the acquired image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data; and 5.) “stitching” the captured images together to create the panoramic scene, i.e., blending the image data in the overlap area between adjacent captured images.

## 答案 62：

该专利描述了一种显示器的结构，其中包含了一些开口，通过这些开口可以控制显示器中的像素电极。像素电极按照行和列排列，并通过与行相关的门线和与列相关的数据线进行控制。每个像素电极产生的电场通过液晶层传递到与之相关的地面层。地面层中的开口具有一定的宽度，数据线位于地面层下方并且与开口不对齐，以最小化来自寄生电场的串扰。在向显示器中输入数据线信号时，使用三列反转方案，使跨越开口的像素对具有相同的极性。同时，使用门线扫描模式来增强显示器的均匀性。这种结构可以实现图像融合。该专利由苹果公司申请。

### 专利信息：


专利号: US13762276
发明名称: DISPLAYS WITH MINIMIZED CROSSTALK
摘要: Display ground plane structures may contain slits. Image pixel electrodes in the display may be arranged in rows and columns. Image pixels in the display may be controlled using gate lines that are associated with the rows and data lines that are associated with the columns. An electric field may be produced by each image pixel electrode that extends through a liquid crystal layer to an associated portion of the ground plane. The slits in the ground plane may have a slit width. Data lines may be located sufficiently below the ground plane and sufficiently out of alignment with the slits to minimize crosstalk from parasitic electric fields. A three-column inversion scheme may be used when driving data line signals into the display, so that pairs of pixels that straddle the slits are each driven with a common polarity. Gate line scanning patterns may be used that enhance display uniformity.
申请人: Apple Inc.

### 相关描述片段：

Displays such as liquid crystal displays may be provided that include ground plane structures with slits. A display may include rows and columns of image pixel electrodes. Image pixels in the display may be controlled using gate lines that are associated with the rows and data lines that are associated with the columns. An electric field may be produced by each image pixel electrode that extends through a liquid crystal layer to an associated portion of the ground plane. Data lines may be located sufficiently below the ground plane and sufficiently out of alignment with the slits to minimize parasitic electric fields. Display driver circuitry in the display may drive the data lines using a polarity pattern that promotes color uniformity.

## 答案 28：

该专利介绍了一种利用位置传感器辅助的全景摄影技术，包括从电子设备的图像传感器获取图像数据、对获取的图像数据进行运动滤波、对相邻捕获的图像进行图像配准、对捕获的图像数据进行几何校正、并将捕获的图像拼接在一起创建全景场景的步骤。最终拼接的全景图像可以在存储之前进行裁剪。该技术可以在手持个人电子设备上实现。该技术的申请人为苹果公司。

### 专利信息：


专利号: US13109878
发明名称: Positional Sensor-Assisted Perspective Correction for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for performing positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The disclosed embodiments relate to techniques for improving panoramic photography for handheld personal electronic devices with image sensors. The panoramic photography techniques disclosed herein are designed to handle a range of panoramic scenes as captured by handheld personal electronic devices. Generalized steps to carry out the panoramic photography techniques described herein include: 1.) acquiring image data from the electronic device's image sensor's image stream; 2.) performing “motion filtering” on the acquired image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data; and 5.) “stitching” the captured images together to create the panoramic scene, i.e., blending the image data in the overlap area between adjacent captured images.

## 答案 76：

该专利是关于视频编码系统和方法，用于保护解码图像内容免受条纹伪影的影响。该方法通过识别视频数据帧中像素块内容，确定哪些像素块可能会出现条纹伪影，并根据它们的位置组装可能出现伪影的区域。视频编码器可以对识别出的一个或多个区域内的像素块进行抗条纹处理，然后通过压缩操作对处理后的帧进行编码。这是一种实现图像融合的方法。该专利由苹果公司申请。

### 专利信息：


专利号: US13631428
发明名称: SIGNAL SHAPING TECHNIQUES FOR VIDEO DATA THAT IS SUSCEPTIBLE TO BANDING ARTIFACTS
摘要: Video coding systems and methods protect against banding artifacts in decoded image content. According to the method, a video coder may identify, from content of pixel blocks of a frame of video data, which pixel blocks are likely to exhibit banding artifacts from the video coding/decoding processes. The video coder may assemble regions of the frame that are likely to exhibit banding artifacts based on the identified pixel blocks' locations with respect to each other. The video coder may apply anti-banding processing to pixel blocks within one or more of the identified regions and, thereafter, may code the processed frame by a compression operation.
申请人: Apple Inc.

### 相关描述片段：

Embodiments of the present invention provide video coding systems and methods that protect against banding artifacts in decoded image content. According to the method, a video coder may identify from the content of pixel blocks of a frame of video data which pixel blocks are likely to exhibit banding artifacts from the video coding/decoding processes. The video coder may identify regions of the frame that are likely to exhibit banding artifacts based on the identified pixel blocks' locations with respect to each other. The video coder may apply anti-banding processing to pixel blocks within one or more of the identified regions and, thereafter, may code the processed frame by a compression operation.

## 答案 55：

该专利涉及的系统和方法可以在应用程序的图形用户界面中显示和更新图像预览。在应用程序中，给定主图像的图像预览包括该主图像的各种图像大小和分辨率，并且最好编译为数据库中的图像预览数据集。当在应用程序中操作图像预览时，可以从数据库中查询适当的图像预览分辨率并显示。例如，在滚动时，与不滚动时使用的图像预览数据集相比，可能会使用较低分辨率的图像预览数据集，从而使它们的显示和更新计算量更小。同样，在放大时，可以从数据库中查询适当的图像预览数据集，而不是或与上下缩放图像预览一起使用。这些方法可以实现图像融合。该专利由苹果公司申请。

### 专利信息：


专利号: US13543799
发明名称: Manipulation of Image Content Using Various Image Representations
摘要: Disclosed herein are embodiments of systems and methods for displaying and updating image previews in the graphical user interface of an application program. The image previews for a given master image within the application program constitute various image sizes and resolutions of that master image, and are preferably compiled as image preview data sets in a database. When the image previews are manipulated in the application program an appropriate resolution for that image preview can be queried from the database and displayed. For example, while scrolling, a lower-resolution image preview data set might he used when compared to image preview data sets used while the image previews are not scrolled, thus making them less computationally intensive to display and update. Likewise, while magnifying, an appropriate image preview data set can be queried from the database instead of, or in conjunction with, up or downscaling the image preview.
申请人: Apple Inc.

### 相关描述片段：

Disclosed herein are embodiments of systems and methods for displaying and updating image previews in the graphical user interface of an application program running on a computer. The image previews for a given master image within the application program constitute various image sizes and resolution of that master image, and are preferably compiled as image preview data sets in a database accessible by the application program. When the image previews are manipulated in the applications program by a user, an appropriate resolution for that image preview can be queried from the database and displayed. The appropriate resolution for the image previews can be used by the computer in response to the user's manipulation (scrolling, magnification) of the image previews. Such pre-processing and population of the database itself requires computation and the use of computer resources.

## 答案 100：

该专利信息中提到的错误校正方法和移动通信设备可以实现图像融合。该方法首先接收包含一组样本的指纹图像信息。然后将接收到的第一个样本与边缘处的第二个样本进行匹配。根据需要进行的处理量和指纹图像错误量，确定指纹图像操作的度量。最后，根据度量的最优值对指纹图像信息进行操作，从而实现图像融合。该专利由苹果公司申请。

### 专利信息：


专利号: US13842052
发明名称: Edge Detection and Stitching
摘要: An error correction method and a mobile communication device incorporating the error correction method. The error correction method begins with receiving fingerprint image information that includes a set of swatches. A first one of the received swatches is matched to a second one of the swatches at an edge. A measure of fingerprint image manipulation is determined responsive to an amount of processing to perform and an amount of fingerprint image error. Then the fingerprint image information is manipulated in response to an optimum value of the measure.
申请人: Apple Inc.

### 相关描述片段：

The text does not provide information on the implementation process of image fusion.

## 答案 42：

该专利提供了一种为视力受损用户提供图像捕捉和图像回顾的技术和机制。其中，预捕捉功能和捕捉图像回顾功能可以实现图像融合。预捕捉功能通过提供音频信息帮助用户正确定位图像捕捉机构，使所需主题在图片中得到捕捉，正确地在图片中框定主题，使主题在图片中得到适当的大小等。捕捉图像回顾功能通过提供音频信息帮助用户欣赏和“可视化”已捕捉并显示给用户的视觉图像。通过这些功能，视力受损用户能够比目前更好地捕捉和回顾图像。

### 专利信息：


专利号: US13247901
发明名称: Facilitating Image Capture and Image Review by Visually Impaired Users
摘要: Techniques and mechanisms are provided for facilitating the capture and review of visual images by visually impaired users. In one implementation, these techniques and mechanisms provide pre image capture functionality and captured image review functionality. With the pre image capture functionality, audio messages are provided to the user to help the user position an image capturing mechanism properly to capture the desired subjects in a picture, to frame the subjects properly within the picture, to size the subjects properly within the picture, etc. With the image review functionality, audio messages are provided to the user to help the user enjoy and “visualize” a visual image that has been captured and is being displayed to the user. With these functionalities, a visually impaired user is able capture and review images to a much greater degree than is currently possible.
申请人: Apple Inc.

### 相关描述片段：

"In accordance with one embodiment of the present invention, techniques and mechanisms are provided for facilitating the capture and review of visual images by visually impaired users. In one embodiment, these techniques and mechanisms include pre image capture functionality and captured image review functionality. With the pre image capture functionality, audio messages are provided to the user to help the user position an image capturing mechanism properly to capture the desired subjects in a picture, to frame the subjects properly within the picture, to size the subjects properly within the picture, etc. With the image review functionality, audio messages are provided to the user to help the user enjoy and “visualize” a visual image that has been captured and is being displayed. After the image is pre-captured, the device analyzes the image. For example, the device may apply facial detection techniques to determine how many faces are in the image. The device may also identify the pixels that make up each face so that the location of each face within the pre-captured image is determined. In addition, the device may apply facial recognition techniques to identify the faces. Thus, rather than referring to a face in the pre-captured image as “face ”, the device may identify the face as “Zachary”. Furthermore, the device may analyze the pre-captured image to determine whether any of the faces are too close to an edge (e.g. left, right, top and bottom) of the picture. The device may further analyze the pre-captured image to determine the sizes of the faces relative to the overall size of the picture."

## 答案 81：

该专利描述了一种图像传感器组件的设计，其中图像传感器芯片附着在一个空腔和一个预制包装的下表面上，该包装具有从下表面延伸到包装上表面的垂直表面。图像传感器芯片提供接收光线的表面以捕捉图像。在盖子上应用了一个吸光层，使得吸光层防止光线落在预制包装的垂直表面上，而不会阻止落在图像传感器芯片的接收光线表面上的光线通过。吸光层包括开口，提供对至少一个接收光线表面和图像传感器芯片的两个对角线的视线，以便将盖子放置在包装的上表面上，与图像传感器芯片对准。这种设计可以实现图像融合。

### 专利信息：


专利号: US13961587
发明名称: COVER FOR IMAGE SENSOR ASSEMBLY WITH LIGHT ABSORBING LAYER AND ALIGNMENT FEATURES
摘要: An image sensor assembly includes an image sensor die attached adjacent to a cavity and a lower surface in a preformed package having substantially vertical surfaces extending from the lower surface to an upper surface of the package. The image sensor die provides the light receiving surface for capturing the image. A light absorbing layer is applied to a cover such that the light absorbing layer prevents light from falling on the substantially vertical surfaces of the preformed package without preventing the passage of light that falls on the light receiving surface of the image sensor die. The light absorbing layer includes openings that provide a line-of-sight view of two opposing corners of at least one of the light receiving surface and the image sensor die to facilitate placing the cover over the upper surface of the package in registry with the image sensor die.
申请人: Apple Inc.

### 相关描述片段：

The text does not provide information on the implementation process of image fusion.

## 答案 65：

该专利信息并未涉及到image fusion实现过程，而是介绍了一种用于图像传感器组件的覆盖物，其中包括一个具有吸光层的覆盖物，该吸光层可以防止光线落在预制包装的垂直表面上，而不会阻止落在图像传感器上的光线通过。因此，该专利信息与image fusion实现过程无关。

### 专利信息：


专利号: US13344486
发明名称: COVER FOR IMAGE SENSOR ASSEMBLY WITH LIGHT ABSORBING LAYER
摘要: An image sensor assembly includes an image sensor die attached adjacent to a cavity and a lower surface in a preformed package having substantially vertical surfaces extending from the lower surface to an upper surface of the package. The image sensor die may include a charge-coupled device or an active pixel sensor imager that provides the light receiving surface for capturing the image. A cover is placed over the upper surface of the package. The cover may be a glass cover or an infrared cut filter. A light absorbing layer is applied to the cover in registry with the image sensor die such that the light absorbing layer prevents light from falling on the substantially vertical surfaces of the preformed package without preventing the passage of light that falls on the light receiving surface of the image sensor die.
申请人: Apple Inc

### 相关描述片段：

The text discusses an image sensor assembly that reduces image degradation caused by light reflected from the vertical walls of the package cavity that houses the image sensor die. The assembly includes an image sensor die attached adjacent to a cavity and a lower surface in a preformed package, such as a ceramic member, having substantially vertical surfaces extending from the lower surface to an upper surface of the package. A cover is placed over the upper surface of the package. The cover may be a glass cover or an infrared cut filter. A light absorbing layer is applied to the cover in registry with the image sensor die such that the light absorbing layer prevents light from falling on the substantially vertical surfaces of the preformed package without preventing the passage of light that falls on the light receiving surface of the image sensor die.

## 答案 29：

该专利介绍了一种利用位置传感器辅助的全景摄影技术的设备、方法和计算机可读介质。实现全景摄影技术的一般步骤包括：从电子设备的图像传感器获取图像数据；对获取的图像数据执行“运动滤波”，例如使用电子设备的位置传感器返回的信息来指导图像数据的处理；对相邻捕获的图像进行图像配准；对捕获的图像数据进行几何校正，例如由于透视变化和/或相机围绕非中心透视（COP）相机点旋转而引起的校正；将捕获的图像拼接在一起以创建全景场景，例如在相邻捕获的图像之间混合图像数据的重叠区域。最终拼接的全景图像可以在存储之前进行裁剪。该技术可以应用于手持个人电子设备中。

### 专利信息：


专利号: US13109883
发明名称: Positional Sensor-Assisted Motion Filtering for Panoramic Photography
摘要: This disclosure pertains to devices, methods, and computer readable media for perforating positional sensor-assisted panoramic photography techniques in handheld personal electronic devices. Generalized steps that may be used to carry out the panoramic photography techniques described herein include, but are not necessarily limited to: 1.) acquiring image data from the electronic device's image sensor; 2.) performing “motion filtering” on the acquired image data, e.g., using information returned from positional sensors of the electronic device to inform the processing of the image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data, e.g., due to perspective changes and/or camera rotation about a non-center of perspective (COP) camera point; and 5.) “stitching” the captured images together to create the panoramic scene, e.g., blending the image data in the overlap area between adjacent captured images. The resultant stitched panoramic image may be cropped before final storage.
申请人: Apple Inc.

### 相关描述片段：

The disclosed embodiments relate to techniques for improving panoramic photography for handheld personal electronic devices with image sensors. The panoramic photography techniques disclosed herein are designed to handle a range of panoramic scenes as captured by handheld personal electronic devices. Generalized steps to carry out the panoramic photography techniques described herein include: 1.) acquiring image data from the electronic device's image sensor's image stream; 2.) performing “motion filtering” on the acquired image data; 3.) performing image registration between adjacent captured images; 4.) performing geometric corrections on captured image data; and 5.) “stitching” the captured images together to create the panoramic scene, i.e., blending the image data in the overlap area between adjacent captured images.

## 答案 92：

该专利提供了一种图像颜色平衡的方法。该方法使用一个包含多种不同颜色平衡模式的颜色平衡工具，并接收第一个选择第一个模式。每个颜色平衡模式都用于对图像应用颜色平衡操作。该方法使用颜色平衡工具的第一个模式对图像应用第一组颜色平衡操作。该方法接收第二个选择，从第一个模式切换到颜色平衡工具的第二个模式。该方法使用颜色平衡工具的第二个模式对图像应用第二组颜色平衡操作，从而实现图像融合。该专利的申请人为苹果公司。

### 专利信息：


专利号: US13629529
发明名称: COLOR BALANCE TOOLS FOR EDITING IMAGES
摘要: Some embodiments provide a method for color balancing an image. The method receives a first selection of a first mode of a color balance tool that includes several different color balance modes. Each color balance mode is for applying color balance operations to the image. The method uses the first mode of the color balance tool to apply a first set of color balance operations to the image. The method receives a second selection to switch from the first mode to a second mode of the color balance tool. The method uses the second mode of the color balance tool to apply a second set of color balance operations to the image.
申请人: Apple Inc.

### 相关描述片段：

"In some embodiments, the color balance tool includes a mode for performing color balance operations on an image based on skin tones identified in the image, a mode for performing color balance operations on the image based on a color cast identified in the image, and a mode for performing color balance operations on the image based on temperature and tint adjustments. The color balance tool of some embodiments allows a user to select one of the modes of the color balance tool to perform a color balance operation on the image."

## 答案 5：

根据专利信息，实现image fusion的过程是通过使用三维图像感应设备来捕捉包括一个或多个物体的图像。其中，该设备包括第一个图像设备，用于捕捉第一张图像并提取一个或多个物体的深度信息；此外，该设备还包括第二个图像设备，用于捕捉第二张图像并确定一个或多个物体表面的方向。最终，通过将这两个图像信息进行融合，实现image fusion。该专利由Apple Inc.申请。

### 专利信息：


专利号: US13246821
发明名称: IMAGE CAPTURE USING THREE-DIMENSIONAL RECONSTRUCTION
摘要: Embodiments may take the form of three-dimensional image sensing devices configured to capture an image including one or more objects. In one embodiments, the three-dimensional image sensing device includes a first image device configured to capture a first image and extract depth information for the one or more objects. Additionally, the image sensing device includes a second imaging device configured to capture a second image and determine an orientation of a surface of the one or more objects.
申请人: Apple Inc.

### 相关描述片段：

Embodiments described herein relate to systems, apparatuses and methods for capturing a three-dimensional image using one or more dedicated imaging devices. One embodiment may take the form of a three-dimensional imaging apparatus configured to capture at least one image including one or more objects, comprising: a first sensor for capturing a polarized image, the first sensor including a first imaging device and a polarized filter associated with the first imaging device; a second sensor for capturing a first non-polarized image; a third sensor for capturing a second non-polarized image; and at least one processing module for deriving depth information for the one or more objects utilizing at least the first non-polarized image and the second non-polarized image, the processing module further operative to combine the polarized image, the first non-polarized image, and the second non-polarized image to form a composite three-dimensional image. Another embodiment may take the form of three-dimensional imaging apparatus configured to capture at least one image including one or more objects, comprising: a first sensor for capturing a polarized chrominance image and determining surface information for the one or more objects, the first sensor including a color imaging device and a polarized filter associated with the color imaging device; a second sensor for capturing a first luminance image; a third sensor for capturing a second luminance image; and at least one processing module for deriving depth information for the one or more objects utilizing at least the first luminance image and the second luminance image and combining the polarized chrominance image, the first luminance image, and the second luminance image to form a composite three-dimensional image utilizing the surface information and the depth information.

## 答案 71：

该专利描述了一种图像传感器异常像素列检测和校准的方法。该方法通过对暗场景进行数字图像捕捉，计算每个像素列的列值，然后将该列值与参考值进行比较，根据比较结果计算每个像素列的列分数，并存储标识一个或多个像素列为异常的指示。该方法可以用于图像融合等应用中。该专利由苹果公司申请。

### 专利信息：


专利号: US13629455
发明名称: IMAGING SENSOR ANOMALOUS PIXEL COLUMN DETECTION AND CALIBRATION
摘要: An imaging sensor is signaled to capture a digital image of a dark scene. For each of the pixel columns in the image, a respective column value is computed that represents at least some of the pixels in the column. For each of the pixel columns in the image, a respective comparison is made between the respective column value of the pixel column and a reference value. A respective column score is computed, for each of the pixel columns, based on the respective comparison. An indication that identifies one or more of the pixel columns as anomalous is stored, when the respective column score of the one or more the pixel columns does not meet a criterion. Other embodiments are also described and claimed.
申请人: Apple Inc.

### 相关描述片段：

"An embodiment of the invention is related to techniques for testing an imaging sensor by finding anomalous pixel columns in a digital image produced by the sensor, and providing a calibration map for calibrating the imaging sensor. [...] An embodiment of the invention is a method for finding an anomalous pixel column produced by an imaging sensor, as follows. [...] A calibration map is then stored (in non-volatile storage) that identifies which of the pixel columns are anomalous, i.e. their column noise scores do not meet a predetermined criterion."

## 答案 50：

该专利描述了一种数字相机组件，其中包括一个光分束立方体，该立方体具有一个入口面，用于接收来自相机场景的入射光。该立方体将入射光分成第一、第二和第三个颜色分量，这些分量分别从立方体的第一面、第二面和第三面出射。提供了第一、第二和第三个图像传感器，每个传感器都被定位在接收从立方体的第一、第二和第三个面出射的相应颜色分量。这种技术可以实现图像融合。

### 专利信息：


专利号: US13229363
发明名称: DIGITAL CAMERA WITH LIGHT SPLITTER
摘要: A digital camera component is described that has a light splitter cube having an entrance face to receive incident light from a camera scene. The cube splits the incident light into first, second, and third color components that emerge from the cube through a first face, a second face, and a third face of the cube, respectively. First, second, and third image sensors are provided, each being positioned to receive a respective one of the color components that emerge from the first, second, and third faces of the cube. Other embodiments are also described and claimed.
申请人: Apple Inc.

### 相关描述片段：

An embodiment of the invention is a digital camera component that has a light splitter cube having an entrance face to receive incident light from a camera scene. The cube splits the incident light into three color components that emerge from the cube through respective faces of the cube. Three image sensors are also provided, where each sensor is positioned to receive a respective one of the color components that emerge from the respective face of the cube. The light splitter cube may be combined with a deflector that is positioned to reflect the incident light from the camera scene, and an optical lens system, such as a zoom lens, an autofocus lens, or a fixed focus lens, that is positioned in the path of the deflected incident light between the deflector and the entrance face of the light splitter cube.

## 答案 1：

image fusion的实现过程可以通过使用专利号为US12857903的发明名称为"IMAGE CAPTURE USING LUMINANCE AND CHROMINANCE SENSORS"的专利技术来实现。该专利技术提供了一种图像感应设备，其中包括第一图像传感器用于捕捉亮度图像，第二图像传感器用于捕捉第一色度信息，第三图像传感器用于捕捉第二色度图像。该图像感应设备还包括图像处理模块，用于将第一图像传感器捕捉的亮度图像、第二图像传感器捕捉的第一色度图像和第三图像传感器捕捉的第二色度图像组合起来，形成一个复合图像。该技术由申请人Apple Inc.提出。

### 专利信息：


专利号: US12857903
发明名称: IMAGE CAPTURE USING LUMINANCE AND CHROMINANCE SENSORS
摘要: Methods and apparatuses disclosed herein relate to image sensing devices. One embodiment may take the form of an image sensing device that includes a first image sensor for capturing a luminance image, a second image sensor for capturing a first chrominance, and a third image sensor for capturing a second chrominance image. The image sensing device may further include an image processing module for combining the luminance image captured by the first image sensor, the first chrominance image captured by the second image sensor, and the second chrominance image captured by the third image sensor, to form a composite image.
申请人: Apple Inc.

### 相关描述片段：

Embodiments described herein relate to systems, apparatuses and methods for capturing an image using one or more dedicated image sensors to capture luminance and chrominance portions of an image. One embodiment may take the form of an image sensing device that includes a first image sensor for capturing a luminance image, a second image sensor for capturing a first chrominance, and a third image sensor for capturing a second chrominance image. The image sensing device may further include an image processing module for combining the luminance image captured by the first image sensor, the first chrominance image captured by the second image sensor, and the second chrominance image captured by the third image sensor, to form a composite image.

## 答案 22：

该专利涉及一种将特定用户交互（例如手势）映射到各种图像滤镜的输入参数的装置、方法和计算机可读介质，同时根据适当的底层图像传感器数据设置自动曝光、自动对焦、自动白平衡和/或其他图像处理技术的输入参数，从而为用户和客户端应用程序开发人员提供无缝、动态和直观的体验。这些技术可以处理应用基于位置的扭曲的图像滤镜以及不应用基于位置的扭曲的图像滤镜处理捕获的图像数据。此外，还提供了一些技术，用于在与不需要所有图像传感器捕获的图像数据来产生所需的图像滤镜效果的图像滤镜一起使用时，提高各种图像处理系统的性能和效率。该专利未直接涉及image fusion实现过程。

### 专利信息：


专利号: US13052895
发明名称: Gesture-Based Configuration of Image Processing Techniques
摘要: This disclosure pertains to apparatuses, methods, and computer readable medium for mapping particular user interactions, e.g., gestures, to the input parameters of various image filters, while simultaneously setting auto exposure, auto focus, auto white balance, and/or other image processing technique input parameters based on the appropriate underlying image sensor data in a way that provides a seamless, dynamic, and intuitive experience for both the user and the client application software developer. Such techniques may handle the processing of image filters applying location-based distortions as well as those image filters that do not apply location-based distortions to the captured image data. Additionally, techniques are provided for increasing the performance and efficiency of various image processing systems when employed in conjunction with image filters that do not require all of an image sensor's captured image data to produce their desired image filtering effects.
申请人: Apple Inc.

### 相关描述片段：

The text discusses image processing techniques, including auto exposure, auto focus, and automatic white balance, that are often performed by cameras in personal electronic devices. It also mentions the use of touch-sensitive displays with a graphical user interface for interacting with these devices, including performing various image processing techniques such as focusing, exposing, optimizing, or otherwise adjusting captured images, as well as image filtering techniques. The text further discusses the need for techniques to implement a programmatic interface to map particular user interactions, e.g., gestures, to the input parameters of various image filtering routines, while simultaneously setting auto exposure, auto focus, and/or auto white balance or other image processing technique input parameters based on the appropriate underlying image sensor data.

## 答案 14：

该专利信息并未涉及到image fusion实现过程，而是关于一种用于小型电子设备的光隔离保护盖的发明。该发明描述了一种便携式设备，具有后置摄像头组件和前置显示屏组件，其中包括至少一个保护盖层、一个显示堆叠，其中包括多个显示组件排列在多个互连层中，该显示堆叠提供成像服务，以及一个平坦的支撑底盘，用于为显示堆叠提供支撑。在所描述的实施例中，保护盖可以包裹并保护便携式设备的至少后部，而不会对由后置摄像头组件执行的图像捕获过程产生不利影响。

### 专利信息：


专利号: US13401575
发明名称: LIGHT ISOLATING PROTECTIVE COVER FOR SMALL FORM FACTOR ELECTRONIC DEVICE
摘要: A portable device has a rear facing camera assembly and a front facing display assembly that includes at least a protective cover layer, a display stack that includes a plurality of display components arranged in a plurality of interconnected layers, the display stack providing an imaging service, and a flat support chassis arranged to provide support for the display stack. In the described embodiment, a protective cover can wrap around and protect at least the rear portion of the portable device without adversely affecting an image capture process carried out by the rear facing camera assembly.
申请人: Apple Inc.

### 相关描述片段：

The described embodiments relate to a protective cover for a small form factor electronic device having a rear facing camera assembly, the protective cover prevents light bleed from the light source interfering with the image capture by the rear facing camera assembly. The protective cover includes at least a housing having a shape in accordance with the small form factor electronic device, the shape being suitable for enclosing at least some of the rear portion of the small form factor electronic device. The housing, in turn, includes at least an opening suitably sized and positioned relative to the camera assembly that allows light from the light source to illuminate the subject. At least some of the light emitted by the light source is then reflected back to the lens assembly for image capture. The protective cover also includes at least a light blocking mechanism that prevents light emitted by the light source and reflected by anything other than the subject being illuminated from reaching the lens assembly.
