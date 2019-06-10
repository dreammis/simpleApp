#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from simpleApp.word_doc.python_doc1 import SimpleDocxService

if __name__ == "__main__":

    docx = SimpleDocxService()
    RED = (0xff, 0x00, 0x00)  # (Red, Green, Blue)

    #フォント設定
    docx.set_normal_font("Courier New", 9)

    # タイトル表示
    docx.add_head(u"メインタイトル", 0)

    # 挿絵挿入
    docx.add_picture("report_top.png", 3.0)

    # 文節タイトル表示
    docx.add_head(u"一個目の話題", 1)

    # shift-jisのテキストファイルをdocxの文章に入れます
    with open("sample.txt") as lines, docx.open_text() as text:
        for line in lines:
            text.add("\n").add(line.rstrip("\r\n"), encode="shift-jis")

    # 挿絵挿入
    docx.add_picture("sample_pic.png", 5.0)

    # コードでテキストを生成、docxに入れ込みます。
    # 修飾の例もここで。
    with docx.open_text() as text:
        text.add("\nThis is a my best book.")
        text.add("\nThis is ")
        text.add("a my best").bold()
        text.add(" book.")
        text.add("\nThis is ")
        text.add("a my best").italic()
        text.add(" book.")
        text.add("\nThis is a my best book.").color(*RED)

    # 次の文節
    docx.add_head(u"二個目の話題", 1)

    # コードでテキストを生成、docxに入れ込みます。
    with docx.open_text() as text:
        text.add(u"\nはい、おしまい。")

    # セーブです。
    docx.save("test.docx")

    print ("complete.")