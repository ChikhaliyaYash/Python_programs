In this article, I will show you how to convert an image to a pencil sketch using the Python programming language in just 12 lines of code! Python is a general-purpose programming language that was created in the late 1980s and has seen significant growth in popularity from big tech companies and communities over the years.

One of the reasons for its popularity growth is its ease of use and simplicity. Just think that we are about to transform an image in just 12 lines of code !!
Actually, it could be less.

Understanding The Concept Before The Code
Before writing any code let’s walk through some of the steps that will be used and try to understand them a bit.

Step 1. Find an image that we want to convert into a pencil sketch. I am going to use the image of a Labrador puppy (one of the most popular dogs in the world).

Step 2: Read in the Red, Blue, Green (RBG) image and then convert it to a gray scale image. This effectively makes the image a classic “black and white” photo. This will be our “gray scale image”.

Step 3: We are going to invert the “gray scaled image” also known as getting the image negative, this will be our “inverted gray scale image”. Inversion can be used to enhance details. The Logical NOT or invert is an operator which takes a binary or gray level image as input and produces its photographic negative, i.e. dark areas in the input image become light and light areas become dark. -homepages


Image: Invert formula Source: homepages
Step 4: Use a Gaussian function to blur the image. In image processing, a Gaussian blur (also known as Gaussian smoothing) is the result of blurring an image by a Gaussian function (named after mathematician and scientist Carl Friedrich Gauss). It is a widely used effect in graphics software, typically to reduce image noise and reduce detail. — Wikipedia

We will call this newly created image, the “blurred image”.


Image: Gaussian blur function Source: Wikipedia
Step 5: Invert the newly created “blurred image”, this will be called the “inverted blurred image”.

Step 6: Now we are going to create the pencil sketch image by blending the “gray scale image” with the “inverted blurred image”. This can be done by dividing the “gray scale image” by the “inverted blurred image”. Since images are just arrays we can easily do this in programming by using the divide function from the cv2 library.

Quick Steps:

1. Convert the RGB color image to grayscale.

2. Invert the grayscale image to get a negative.

3. Apply a Gaussian blur to the negative from step 2.

4. Blend the grayscale image from step 1 with the blurred negative from step 3.

