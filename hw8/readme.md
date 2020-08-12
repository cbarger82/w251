### Part 1

1. In the time allowed, how many images did you annotate?

Only took about an hour and a half, but in that time, I annotated 140 images.

2. Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?

Annotated 107 instances of TIE Fighters and 103 instances of Millennium Falcons

3. Based on this experience, how would you handle the annotation of large image data set?

Seems like a good side job for someone looking to make extra money - like a crowd source type of project where you just get people who want to help, but can get a little compensation out of the deal. Or could offer the job in the data entry category or use interns sporadically who are interested in what goes in to CV.

4. Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?

The bounding boxes would have different coordinates in the cases of flip, rotation, scale, cropping, etc. As long as the class were the same, the augmentations add extra data points for model training.


### Part 2
1. Describe the following augmentations in your own words
* Flip - flipping is where you flip the image either horizontally or vertically. So the original could be upside-down or look like a mirror image
* Rotation - rotatiing is where you rotate the image by some amount of degrees, like spinning it around its center point
* Scale - scaling the image is like looking in a funhouse mirror. You can change the x and y scale so the image appears smooshed or stretched.
* Crop - cropping is when you draw boxes within the original image to zoom in on particular parts of an image, like only an eye or only an ear.
* Translation - is like when you are doing a power point and you have a picture that takes up the whole slide. if you then move it so its off the screen, but still only look at the portion that is within the powerpoint slide box and then draw your bounding box accordingly
* Noise - adding noise can be thought of as trying to watch an old-school rabbit ears TV with a signal that isn't pristine. You're watching your cowboy show but the picture looks like it is overlaid with the "snow" bleeding in from the edges of the spectrum.


### Part 3
1. Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation?

An audio annotation appears to need the type of container (ie audio_visual), the color of the spectrogram wave, the progress color, the fftSamples (fast fourier transform samples), the height of the soundwave, and the spectrogram colormap (components include colormap, nshades, format, and alpha)
