import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


class GenerateImgResult:
    file = {}
    folder = ""


# Constructor
    def __init__(self, file, folder):
        self.file = file
        self.folder = folder    # "Biden/" or "Trump/"


# Function Main
    def execute(self):
        self.tagCouldImg()
        self.usFlagTagCloud()
        self.caricatureTagCloud("1")
        self.caricatureTagCloud("2")
        self.graphStatHorizontal()


# Generate Tag Cloud
    def tagCouldImg(self):
        tagCloud = WordCloud(background_color="white", width=700, height=500,
            max_words=100, relative_scaling=0.5, normalize_plurals=False)
        tagCloud.generate_from_frequencies(self.file)
        plt.imshow(tagCloud)
        self.wordCloudSave(tagCloud, "ClassicTagCloud.png")


# Generate Us Flag Tag Cloud
    def usFlagTagCloud(self):
        # Generate a word cloud image
        mask = np.array(Image.open("Ressources/Img/UsFlag.png"))
        usFlag = WordCloud(background_color="white",mode="RGBA", max_words=500,
            relative_scaling=0.1, normalize_plurals=False, mask=mask)
        usFlag.generate_from_frequencies(self.file)

        # Create coloring from image
        image_colors = ImageColorGenerator(mask)
        plt.figure(figsize = (10,6))
        plt.imshow(usFlag.recolor(color_func = image_colors),
            interpolation = "bilinear")
        plt.axis("off")

        # Save
        self.matplotlibSave("UsFlagTagCloud.png")


# Generate Caricature Tag Cloud
    def caricatureTagCloud(self, number):
        folder = "Ressources/Img/" + self.folder + "Caricature" + number

        # Generate a word cloud image
        mask = np.array(Image.open(folder + ".jpg"))
        usFlag = WordCloud(background_color="white",mode="RGBA", max_words=500,
            relative_scaling=0.1, normalize_plurals=False, mask=mask)
        usFlag.generate_from_frequencies(self.file)

        # Create coloring from image
        image_colors = ImageColorGenerator(mask)
        if self.folder != "Biden/":
            plt.figure(figsize = (10,6))
        else:
            plt.figure(figsize = (6,10))
        plt.imshow(usFlag.recolor(color_func = image_colors),
            interpolation = "bilinear")
        plt.axis("off")

        # Save
        self.matplotlibSave("Caricature" + number + ".png")


# Generate Graph
    def graphStatHorizontal(self):
        # Recuperation words : occurences
        word = list(self.file.keys())
        occu = list(self.file.values())

        # Figure Size
        fig, ax = plt.subplots(figsize = (16, 9))

        # Horizontal Bar Plot
        ax.barh(word[:30], occu[:30])

        # Remove axes splines
        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)

        # Remove x, y Ticks
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')

        # Add padding between axes and labels
        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)

        # Add x, y gridlines
        ax.grid(b = True, color = 'grey', linestyle = '-.',
            linewidth = 0.5, alpha = 0.2)

        # Show top values
        ax.invert_yaxis()

        # Add annotation to bars
        for i in ax.patches:
            plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                str(round((i.get_width()), 2)), fontsize = 10,
                fontweight = 'bold', color = 'grey')

        # Add Plot Title
        ax.set_title('Words and their occurences', loc = 'left')

        # Add Text watermark
        fig.text(0.9, 0.15, 'US Election 2020', fontsize = 12,
            color = 'grey', ha = 'right', va = 'bottom', alpha = 0.7)

        # Save
        self.matplotlibSave("GraphStatHorizontal.png")


# WordCloud Save
    def wordCloudSave(self, elem, name):
        WordCloud.to_file(elem, "Result/" + self.folder + name)



# MathplotLib Save
    def matplotlibSave(self, name):
        plt.savefig("Result/" + self.folder + name, format = "png")












#
