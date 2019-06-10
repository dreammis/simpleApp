#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from simpleApp.word_doc.python_doc1 import SimpleDocxService

if __name__ == "__main__":

    docx = SimpleDocxService('yj_elephant_template.docx')
    docx.fill_information("刘啸虎", str(20), str(30))
    front_name = "{user_id}_{create_time}".format(user_id=12, create_time="2018")
    filename = "".join([front_name, ".docx"])

    if not os.path.exists(front_name):
        os.mkdir(front_name)
    img = "http://cdn-qa-static.zgyjyx.net/mgr/FmQdeySas0c0mlrGp5MS54Q_cBtD.png"


    # 修飾の例もここで。
    with docx.open_text() as text:
        text.add("\nThis is a my best book.")
        text.add("\nThis is ")
        text.add("a my best").bold()
        text.add(" book.")
        text.add("\nThis is ")
        text.add("a my best").italic()
        text.add(" book.")

    # 次の文節
    docx.add_head(u"二個目の話題", 1)

    # コードでテキストを生成、docxに入れ込みます。
    with docx.open_text() as text:
        text.add(u"\nはい、おしまい。")

    # セーブです。
    docx.save(filename)
