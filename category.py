from gensim.models.fasttext import FastText as FT_gensim
import  pandas  as pd


def tbCategory(str):

    categoryFile = "taobao_noblank.xlsx"

    dfkeyword = pd.read_excel(categoryFile, usecols='C')

    dfcatalog = pd.read_excel(categoryFile, usecols='A,B')

    line_commodities = 0

    for i_item_commodities in dfkeyword.to_numpy():
        if str in i_item_commodities[0]:
            return dfcatalog.to_numpy()[line_commodities][0] + ":" + dfcatalog.to_numpy()[line_commodities][1]

        line_commodities = line_commodities + 1

    return ""

def ftCategory(str):

    model = FT_gensim.load("allwancibiao_tb_FT")

    return model.most_similar(str)[0][0]
