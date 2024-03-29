# Fetch Colors From Image
Mini-project that runs a Python script to generate a list of major colours in the input image file. Uses Open-CV and the concept of K-Means clustering.

### Dependencies:
- Python version: 3.7.4
- Python modules: [Open CV](https://pypi.org/project/opencv-python/), pandas, numpy, [Sci Kit Learn](https://scikit-learn.org/stable/), math
- colors.csv file generated using [the wonderful project](https://github.com/codebrainz/color-names) developed by @codebrainz
- Input image to be in .jpg/.jpeg format (as of now). PNG might work too.

### Further improvements
- Try to use separate K-Means clustering code to remove dependency over sklearn
- Expand the colors.csv look-up table to include more colours although it works okay as of now
- Try to optimize the code

### Steps
- Run ```script.py``` inside Run
- Be sure to modify the path of the input image and no of colours to be fetched at the relevant locations

### Inspiration
[The amazing work](https://github.com/rodartha/ColorPalette) by @rodartha
