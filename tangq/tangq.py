# -*- coding: utf-8 -*-
import requests
import pandas as pd
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class TangQ(object):
    url = "http://crdietitian.cnsoc.org/practicetest/"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

    def __init__(self):
        pass

    def get_html(self):
        return requests.get(self.url, headers=self.headers).content.decode('utf-8')

    def handle_content(self, content):
        html = etree.HTML(content)
        dataList = []
        for index in xrange(1, 21):
            questionList = []
            question = html.xpath('//*[@id="div_%s"]/div[1]/text()'% index)[0].strip().split('. ')[1]
            choices = [html.xpath('//*[@id="div_%s"]/div[2]/div[%s]/label/text()' %(index, item))[1].strip() for item in range(1, 5)]
            choices.insert(0, question)
            dataList.append(choices)
        return dataList

    def save_pandas(self, data, existData=None):
        if not existData.empty:
        # if existData:
            for item in data:
                tmpSeries = pd.Series(item, index=['question', 'choiceA', 'choiceB', 'choiceC', 'choiceD'])
                existData = existData.append(tmpSeries, ignore_index=True)
            return existData
        else:
            df = pd.DataFrame(data=data, columns=['question', 'choiceA', 'choiceB', 'choiceC', 'choiceD'])
            writer = pd.ExcelWriter(
                'tangq01.xlsx', engine='xlsxwriter')
            df.to_excel(writer, 'Sheet1')
            writer.save()

    def read_pandas(self):
        return pd.read_excel('tangq01.xlsx')

    def save_excel(self, data):
        writer = pd.ExcelWriter('tangq01.xlsx')
        data.to_excel(writer, 'Sheet1')
        writer.save()


tangObj = TangQ()
pandasData = None
pandasData = tangObj.read_pandas()
# while True:

for i in xrange(100):
    html = tangObj.get_html()
    data = tangObj.handle_content(html)
    pandasData = tangObj.save_pandas(data, pandasData)
    # if len(filter(lambda x: x, pandasData.duplicated().values)) > 0:
    #     pandasData.drop_duplicates(['question'], keep='last', inplace=True)
    # else:
    #     tangObj.save_excel(pandasData)
    #     break
pandasData.drop_duplicates(['question'], keep='last', inplace=True)
tangObj.save_excel(pandasData)
