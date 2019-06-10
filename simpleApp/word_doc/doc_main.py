#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpleApp.word_doc.python_doc import SimpleDocxService

if __name__ == "__main__":

    docx = SimpleDocxService()

    #フォント設定
    docx.set_normal_font("Courier New", 9)

    # タイトル表示
    docx.add_head(u"メインタイトル", 0)

    # 挿絵挿入
    docx.add_picture("report_top.png", 3.0)

    # 文節タイトル表示
    docx.add_head(u"一個目の話題", 1)

    # shift-jisのテキストファイルをdocxの文章に入れます
    f = open("sample.txt")
    text = f.read()
    f.close()
    docx.open_text()
    docx.add_text("\n")
    # text = docx.get_unicode_text(text, 'shift-jis')
    text = docx.adjust_return_code(text)
    docx.add_text(text)
    docx.close_text()

    # 挿絵挿入
    docx.add_picture("sample_pic.png", 5.0)

    # コードでテキストを生成、docxに入れ込みます。
    # 修飾の例もここで。
    docx.open_text()
    docx.add_text("\nThis is a my best book.")
    docx.add_text("\nThis is ")
    docx.add_text_bold("a my best")
    docx.add_text(" book.")
    docx.add_text("\nThis is ")
    docx.add_text_italic("a my best")
    docx.add_text(" book.")
    docx.add_text_color("\nThis is a my best book.", 0xff, 0x00, 0x00)
    docx.close_text()

    # 次の文節
    docx.add_head(u"二個目の話題", 1)

    # コードでテキストを生成、docxに入れ込みます。
    docx.open_text()
    docx.add_text(u"\nはい、おしまい。")
    docx.close_text()

    # セーブです。
    docx.save("test.docx")

    print("complete.")