import jieba
from gensim.models.fasttext import FastText as FT_gensim
import  pandas  as pd

def preCategory(item_str):
    df = pd.read_excel("preprocess.xlsx")

    for _, row in df.iterrows():
        if row[0] in item_str:
            return row[1]

    return ""

def tbCategory(item_str):

    categoryFile = "taobao_noblank.xlsx"

    df = pd.read_excel(categoryFile)

    for _, row in df.iterrows():
        if item_str in str(row[2]):
            return str(row[0]) + ":" + str(row[1])
        if item_str in str(row[1]):
            return str(row[0])
        if item_str in str(row[0]):
            return str(row[0])

    return ""

def tbfcCategory(item_str):
    df = pd.read_excel("taobao_noblank.xlsx")

    document_cut = jieba.cut(item_str)

    for word in document_cut:

        for index, row in df.iterrows():
            if word in str(row[2]):
                return str(row[0]) + ":" + str(row[1])
            if word in str(row[1]):
                return str(row[0])
            if word in str(row[0]):
                return str(row[0])

    return ""

def baseCategory(item_str):
    categoryFile = "base2020825.xlsx"

    df = pd.read_excel(categoryFile)

    for _, row in df.iterrows():
        if item_str in str(row[3]):
            return str(row[0]) + ":" + str(row[1])
        if item_str in str(row[2]):
            return str(row[0]) + ":" + str(row[1])
        if item_str in str(row[1]):
            return str(row[0])
        if item_str in str(row[0]):
            return str(row[0])

    return ""

def basefcCategory(item_str):
    categoryFile = "base2020825.xlsx"

    df = pd.read_excel(categoryFile)

    document_cut = jieba.cut(item_str)

    for word in document_cut:

        for _, row in df.iterrows():
            if word in str(row[3]):
                return str(row[0]) + ":" + str(row[1])
            if word in str(row[2]):
                return str(row[0]) + ":" + str(row[1])
            if word in str(row[1]):
                return str(row[0])
            if word in str(row[0]):
                return str(row[0])

    return ""

def ftCategory(item_str):

    model = FT_gensim.load("allwancibiao_tb_FT")

    return model.most_similar(item_str)[0][0]
