# coding=utf-8

from os import path
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#d = path.dirname("")

mask = np.array(Image.open("C:\Study\\f4f846691ade18c2bfea80b89051cb5d_b.jpg"))
wordcloud = WordCloud(background_color="white",font_path="C:\Windows\Fonts\FZYTK.TTF",max_font_size=4000,stopwords=STOPWORDS.add("said"))
#text = open("C:\Study\schools.txt").read()
#wordcloud.generate(text)
dict={}
f = open("C:\study\schools.txt","r")
#Use Cosine Similarity
for line in f:
    list = line.split("\t")
    #Set vector[600,600] as vector_basis,make every passing score to vector_score[600,passing score],
    #then calculate Cosine<vector_basis,vector_score>,so that score 600 will got max weight which means that
    #we have most opportunity to get offer from this school.
    vector_basis = np.array([600,600])
    vector_score = np.array([600,int(list[1])])
    num = float(vector_basis.T.dot(vector_score))
    cos = num / (np.linalg.norm(vector_basis) * np.linalg.norm(vector_score))
    #Normalization
    cos_nor = 0.5 + cos * 0.5
    dict[list[0]] = cos_nor
wordcloud.generate_from_frequencies(dict)
#image_colors = ImageColorGenerator(mask)
plt.imshow(wordcloud)
plt.axis("off")

plt.show()
