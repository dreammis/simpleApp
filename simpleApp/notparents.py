#-* coding:utf8 -*-
import json
from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import DotExporter


q = """
[{"id":"ZSD_11","text":" 初中英语 ","parent":"#"},{"id":"ZSD_11_0","text":"听力","parent":"ZSD_11"},{"id":"ZSD_11_0_0","text":"信息选择","parent":"ZSD_11_0"},{"id":"ZSD_11_0_2","text":"情景反应","parent":"ZSD_11_0"},{"id":"ZSD_11_0_3","text":"听录音选图","parent":"ZSD_11_0"},{"id":"ZSD_11_0_5","text":"对话理解","parent":"ZSD_11_0"},{"id":"ZSD_11_0_6","text":"短文理解/短文填空","parent":"ZSD_11_0"},{"id":"ZSD_11_1","text":"语音 ","parent":"ZSD_11"},{"id":"ZSD_11_1_0","text":"字母","parent":"ZSD_11_1"},{"id":"ZSD_11_1_2","text":"音标","parent":"ZSD_11_1"},{"id":"ZSD_11_2","text":"名词 ","parent":"ZSD_11"},{"id":"ZSD_11_2_0","text":"可数名词及其单复数","parent":"ZSD_11_2"},{"id":"ZSD_11_2_1","text":"不可数名词","parent":"ZSD_11_2"},{"id":"ZSD_11_2_2","text":"名词所有格","parent":"ZSD_11_2"},{"id":"ZSD_11_2_3","text":"专有名词","parent":"ZSD_11_2"},{"id":"ZSD_11_2_4","text":"名词辨析","parent":"ZSD_11_2"},{"id":"ZSD_11_2_5","text":"复合名词","parent":"ZSD_11_2"},{"id":"ZSD_11_3","text":"冠词","parent":"ZSD_11"},{"id":"ZSD_11_3_0","text":"定冠词","parent":"ZSD_11_3"},{"id":"ZSD_11_3_1","text":"不定冠词","parent":"ZSD_11_3"},{"id":"ZSD_11_3_2","text":"零冠词","parent":"ZSD_11_3"},{"id":"ZSD_11_4","text":"代词 ","parent":"ZSD_11"},{"id":"ZSD_11_4_0","text":"人称代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_0_0","text":"主格人称代词","parent":"ZSD_11_4_0"},{"id":"ZSD_11_4_0_1","text":"宾格人称代词","parent":"ZSD_11_4_0"},{"id":"ZSD_11_4_1","text":"物主代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_1_0","text":"形容词性物主代词","parent":"ZSD_11_4_1"},{"id":"ZSD_11_4_1_1","text":"名词性物主代词","parent":"ZSD_11_4_1"},{"id":"ZSD_11_4_2","text":"反身代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_3","text":"指示代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_4","text":"不定代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_4_0","text":"many/much 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_1","text":"both/all 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_2","text":"either/neither 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_3","text":"some/any 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_4","text":"none 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_5","text":"other/another 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_6","text":"each/every 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_7","text":"one/that/it 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_8","text":"few/little 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_9","text":"several/enough 的用法","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_4_10","text":"复合不定代词","parent":"ZSD_11_4_4"},{"id":"ZSD_11_4_5","text":"疑问代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_7","text":"相互代词","parent":"ZSD_11_4"},{"id":"ZSD_11_4_9","text":"it的用法","parent":"ZSD_11_4"},{"id":"ZSD_11_4_9_1","text":"it作形式主语","parent":"ZSD_11_4_9"},{"id":"ZSD_11_4_9_2","text":"it作形式宾语","parent":"ZSD_11_4_9"},{"id":"ZSD_11_5","text":"介词","parent":"ZSD_11"},{"id":"ZSD_11_5_0","text":"表示时间的介词","parent":"ZSD_11_5"},{"id":"ZSD_11_5_1","text":"表示地点、方向的介词","parent":"ZSD_11_5"},{"id":"ZSD_11_5_3","text":"表示原因的介词","parent":"ZSD_11_5"},{"id":"ZSD_11_5_4","text":"表示方式、手段或工具的介词","parent":"ZSD_11_5"},{"id":"ZSD_11_5_6","text":"其他主要介词的用法","parent":"ZSD_11_5"},{"id":"ZSD_11_5_7","text":"介词短语/介词的固定搭配","parent":"ZSD_11_5"},{"id":"ZSD_11_5_8","text":"介词辨析","parent":"ZSD_11_5"},{"id":"ZSD_11_6","text":"形容词","parent":"ZSD_11"},{"id":"ZSD_11_6_0","text":"形容词的位置","parent":"ZSD_11_6"},{"id":"ZSD_11_6_1","text":"形容词的比较级","parent":"ZSD_11_6"},{"id":"ZSD_11_6_1_0","text":"构成","parent":"ZSD_11_6_1"},{"id":"ZSD_11_6_1_1","text":"用法","parent":"ZSD_11_6_1"},{"id":"ZSD_11_6_1_2","text":"修饰语","parent":"ZSD_11_6_1"},{"id":"ZSD_11_6_2","text":"形容词的最高级","parent":"ZSD_11_6"},{"id":"ZSD_11_6_2_0","text":"构成","parent":"ZSD_11_6_2"},{"id":"ZSD_11_6_2_1","text":"用法","parent":"ZSD_11_6_2"},{"id":"ZSD_11_6_2_2","text":"修饰语","parent":"ZSD_11_6_2"},{"id":"ZSD_11_6_3","text":"复合形容词","parent":"ZSD_11_6"},{"id":"ZSD_11_6_4","text":"形容词辨析","parent":"ZSD_11_6"},{"id":"ZSD_11_6_5","text":"形容词短语","parent":"ZSD_11_6"},{"id":"ZSD_11_6_6","text":"形容词和名词的辨析","parent":"ZSD_11_6"},{"id":"ZSD_11_6_7","text":"形容词同级比较","parent":"ZSD_11_6"},{"id":"ZSD_11_6_8","text":"ing/ ed 形容词","parent":"ZSD_11_6"},{"id":"ZSD_11_7","text":"副词","parent":"ZSD_11"},{"id":"ZSD_11_7_0","text":"副词的比较级","parent":"ZSD_11_7"},{"id":"ZSD_11_7_0_0","text":"构成","parent":"ZSD_11_7_0"},{"id":"ZSD_11_7_0_1","text":"用法","parent":"ZSD_11_7_0"},{"id":"ZSD_11_7_0_2","text":"修饰语","parent":"ZSD_11_7_0"},{"id":"ZSD_11_7_1","text":"副词的最高级","parent":"ZSD_11_7"},{"id":"ZSD_11_7_1_0","text":"构成","parent":"ZSD_11_7_1"},{"id":"ZSD_11_7_1_1","text":"用法","parent":"ZSD_11_7_1"},{"id":"ZSD_11_7_1_2","text":"修饰语","parent":"ZSD_11_7_1"},{"id":"ZSD_11_7_3","text":"地点副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_4","text":"时间副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_5","text":"方式副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_6","text":"程度副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_7","text":"疑问副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_8","text":"频度副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_10","text":"不定副词","parent":"ZSD_11_7"},{"id":"ZSD_11_7_11","text":"副词的位置","parent":"ZSD_11_7"},{"id":"ZSD_11_7_12","text":"副词辨析","parent":"ZSD_11_7"},{"id":"ZSD_11_7_13","text":"副词短语","parent":"ZSD_11_7"},{"id":"ZSD_11_7_14","text":"形容词与副词的辨析","parent":"ZSD_11_7"},{"id":"ZSD_11_7_15","text":"副词同级比较","parent":"ZSD_11_7"},{"id":"ZSD_11_7_16","text":"连接副词","parent":"ZSD_11_7"},{"id":"ZSD_11_8","text":"数词","parent":"ZSD_11"},{"id":"ZSD_11_8_0","text":"基数词","parent":"ZSD_11_8"},{"id":"ZSD_11_8_0_1","text":"读法与写法","parent":"ZSD_11_8_0"},{"id":"ZSD_11_8_0_2","text":"基数词的用法","parent":"ZSD_11_8_0"},{"id":"ZSD_11_8_1","text":"序数词","parent":"ZSD_11_8"},{"id":"ZSD_11_8_1_1","text":"读法与写法","parent":"ZSD_11_8_1"},{"id":"ZSD_11_8_1_2","text":"序数词的用法","parent":"ZSD_11_8_1"},{"id":"ZSD_11_8_11","text":"数词的应用","parent":"ZSD_11_8"},{"id":"ZSD_11_8_11_0","text":"年月日表达法","parent":"ZSD_11_8_11"},{"id":"ZSD_11_8_11_1","text":"时间及编号的表达法","parent":"ZSD_11_8_11"},{"id":"ZSD_11_8_11_2","text":"加减乘除算式的读法和写法","parent":"ZSD_11_8_11"},{"id":"ZSD_11_8_11_3","text":"分数、小数、百分数表示法","parent":"ZSD_11_8_11"},{"id":"ZSD_11_8_11_6","text":"数量表示法","parent":"ZSD_11_8_11"},{"id":"ZSD_11_8_11_7","text":"年龄、生日、纪念日","parent":"ZSD_11_8_11"},{"id":"ZSD_11_9","text":"连词 ","parent":"ZSD_11"},{"id":"ZSD_11_9_0","text":"并列连词","parent":"ZSD_11_9"},{"id":"ZSD_11_9_0_0","text":"表示并列关系的并列连词","parent":"ZSD_11_9_0"},{"id":"ZSD_11_9_0_1","text":"表示转折关系的并列连词","parent":"ZSD_11_9_0"},{"id":"ZSD_11_9_0_2","text":"表示选择关系的并列连词","parent":"ZSD_11_9_0"},{"id":"ZSD_11_9_0_3","text":"表示因果关系的并列连词","parent":"ZSD_11_9_0"},{"id":"ZSD_11_9_1","text":"从属连词","parent":"ZSD_11_9"},{"id":"ZSD_11_9_1_0","text":"引导宾语从句的从属连词","parent":"ZSD_11_9_1"},{"id":"ZSD_11_9_1_1","text":"引导状语从句的从属连词","parent":"ZSD_11_9_1"},{"id":"ZSD_11_9_1_1_0","text":"引导时间状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_1","text":"引导原因状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_2","text":"引导地点状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_3","text":"引导条件状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_4","text":"引导目的状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_5","text":"引导结果状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_6","text":"引导让步状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_7","text":"引导方式状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_1_8","text":"引导比较状语从句的从属连词","parent":"ZSD_11_9_1_1"},{"id":"ZSD_11_9_1_2","text":"引导其他从句的从属连词","parent":"ZSD_11_9_1"},{"id":"ZSD_11_9_2","text":"常用连词的辨析","parent":"ZSD_11_9"},{"id":"ZSD_11_9_2_0","text":"不能同时出现在一个句子中的连词","parent":"ZSD_11_9_2"},{"id":"ZSD_11_9_2_1","text":"until和before","parent":"ZSD_11_9_2"},{"id":"ZSD_11_9_2_2","text":"and和or用于否定句中的区别","parent":"ZSD_11_9_2"},{"id":"ZSD_11_9_2_3","text":"if的两种意思及其与whether的区别","parent":"ZSD_11_9_2"},{"id":"ZSD_11_9_2_4","text":"because, for, since, as的区别","parent":"ZSD_11_9_2"},{"id":"ZSD_11_9_2_5","text":"as, when, while, as soon as的区别","parent":"ZSD_11_9_2"},{"id":"ZSD_11_10","text":"动词 ","parent":"ZSD_11"},{"id":"ZSD_11_10_0","text":" 基本形式","parent":"ZSD_11_10"},{"id":"ZSD_11_10_0_0","text":"第三人称单数形式","parent":"ZSD_11_10_0"},{"id":"ZSD_11_10_0_1","text":"过去式  ","parent":"ZSD_11_10_0"},{"id":"ZSD_11_10_0_2","text":"过去分词","parent":"ZSD_11_10_0"},{"id":"ZSD_11_10_0_3","text":"现在分词","parent":"ZSD_11_10_0"},{"id":"ZSD_11_10_0_4","text":"动词辨析","parent":"ZSD_11_10_0"},{"id":"ZSD_11_10_1","text":"分类","parent":"ZSD_11_10"},{"id":"ZSD_11_10_1_2","text":"情态动词","parent":"ZSD_11_10_1"},{"id":"ZSD_11_10_1_3","text":"助动词","parent":"ZSD_11_10_1"},{"id":"ZSD_11_10_1_4","text":"使役动词","parent":"ZSD_11_10_1"},{"id":"ZSD_11_10_1_5","text":"连系动词","parent":"ZSD_11_10_1"},{"id":"ZSD_11_10_1_5_0","text":"状态连系动词","parent":"ZSD_11_10_1_5"},{"id":"ZSD_11_10_1_5_1","text":"转变或结果连系动词","parent":"ZSD_11_10_1_5"},{"id":"ZSD_11_10_1_6","text":"动词短语/动词的固定搭配","parent":"ZSD_11_10_1"},{"id":"ZSD_11_10_2","text":"时态","parent":"ZSD_11_10"},{"id":"ZSD_11_10_2_0","text":"一般现在时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_1","text":"一般过去时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_2","text":"一般将来时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_3","text":"现在进行时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_4","text":"现在完成时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_5","text":"过去完成时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_6","text":"过去进行时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_7","text":"过去将来时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_8","text":"现在完成进行时","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_2_9","text":"常用时态的区别","parent":"ZSD_11_10_2"},{"id":"ZSD_11_10_3","text":"语态","parent":"ZSD_11_10"},{"id":"ZSD_11_10_3_0","text":"动词的主动语态","parent":"ZSD_11_10_3"},{"id":"ZSD_11_10_3_0_1","text":"主动表被动","parent":"ZSD_11_10_3_0"},{"id":"ZSD_11_10_3_1","text":"动词的被动语态","parent":"ZSD_11_10_3"},{"id":"ZSD_11_10_3_1_0","text":"一般现在时的被动语态 ","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_1","text":"一般过去时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_2","text":"一般将来时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_3","text":"现在进行时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_4","text":"现在完成时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_5","text":"过去进行时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_6","text":"过去将来时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_7","text":"过去完成时的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_8","text":"含有情态动词的被动语态 ","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_3_1_9","text":"带to的被动语态","parent":"ZSD_11_10_3_1"},{"id":"ZSD_11_10_4","text":"非谓语动词","parent":"ZSD_11_10"},{"id":"ZSD_11_10_4_0","text":"动词不定式","parent":"ZSD_11_10_4"},{"id":"ZSD_11_10_4_0_0","text":"动词不定式的句法功能","parent":"ZSD_11_10_4_0"},{"id":"ZSD_11_10_4_0_1","text":"动词不定式符号to的省略","parent":"ZSD_11_10_4_0"},{"id":"ZSD_11_10_4_0_2","text":"使用动词不定式的主要句型","parent":"ZSD_11_10_4_0"},{"id":"ZSD_11_10_4_1","text":"分词","parent":"ZSD_11_10_4"},{"id":"ZSD_11_10_4_1_0","text":"现在分词","parent":"ZSD_11_10_4_1"},{"id":"ZSD_11_10_4_1_1","text":"过去分词","parent":"ZSD_11_10_4_1"},{"id":"ZSD_11_10_4_2","text":"动名词","parent":"ZSD_11_10_4"},{"id":"ZSD_11_10_4_2_0","text":"动名词的句法功能","parent":"ZSD_11_10_4_2"},{"id":"ZSD_11_10_4_2_1","text":"动词后接不定式和动名词的区别","parent":"ZSD_11_10_4_2"},{"id":"ZSD_11_10_4_2_2","text":"常用动名词的句型","parent":"ZSD_11_10_4_2"},{"id":"ZSD_11_10_5","text":"主谓一致","parent":"ZSD_11_10"},{"id":"ZSD_11_10_5_0","text":"就近一致原则","parent":"ZSD_11_10_5"},{"id":"ZSD_11_10_5_2","text":"语法一致原则","parent":"ZSD_11_10_5"},{"id":"ZSD_11_10_5_3","text":"意义一致原则","parent":"ZSD_11_10_5"},{"id":"ZSD_11_11","text":"句子种类","parent":"ZSD_11"},{"id":"ZSD_11_11_0","text":"陈述句","parent":"ZSD_11_11"},{"id":"ZSD_11_11_1","text":"疑问句 ","parent":"ZSD_11_11"},{"id":"ZSD_11_11_1_0","text":"一般疑问句","parent":"ZSD_11_11_1"},{"id":"ZSD_11_11_1_1","text":"特殊疑问句","parent":"ZSD_11_11_1"},{"id":"ZSD_11_11_1_2","text":"选择疑问句","parent":"ZSD_11_11_1"},{"id":"ZSD_11_11_1_3","text":"反意疑问句","parent":"ZSD_11_11_1"},{"id":"ZSD_11_11_1_4","text":"否定疑问句","parent":"ZSD_11_11_1"},{"id":"ZSD_11_11_2","text":"祈使句","parent":"ZSD_11_11"},{"id":"ZSD_11_11_3","text":"感叹句","parent":"ZSD_11_11"},{"id":"ZSD_11_11_4","text":"特殊句式","parent":"ZSD_11"},{"id":"ZSD_11_11_4_0","text":"There be 结构","parent":"ZSD_11_11_4"},{"id":"ZSD_11_11_4_2","text":"倒装句","parent":"ZSD_11_11_4"},{"id":"ZSD_11_11_4_3","text":"省略句","parent":"ZSD_11_11_4"},{"id":"ZSD_11_11_5","text":"主从复合句","parent":"ZSD_11"},{"id":"ZSD_11_11_5_0","text":"定语从句","parent":"ZSD_11_11_5"},{"id":"ZSD_11_11_5_0_0","text":"关系代词用法","parent":"ZSD_11_11_5_0"},{"id":"ZSD_11_11_5_0_1","text":"关系副词用法","parent":"ZSD_11_11_5_0"},{"id":"ZSD_11_11_5_0_2","text":"非限制性定语从句","parent":"ZSD_11_11_5_0"},{"id":"ZSD_11_11_5_1","text":"状语从句","parent":"ZSD_11_11_5"},{"id":"ZSD_11_11_5_1_0","text":"时间状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_1_1","text":"地点状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_1_2","text":"原因状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_1_3","text":"目的状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_1_4","text":"结果状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_1_5","text":"条件状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_1_6","text":"让步状语从句","parent":"ZSD_11_11_5_1"},{"id":"ZSD_11_11_5_2","text":"名词性从句","parent":"ZSD_11_11_5"},{"id":"ZSD_11_11_5_2_0","text":"主语从句","parent":"ZSD_11_11_5_2"},{"id":"ZSD_11_11_5_2_1","text":"宾语从句","parent":"ZSD_11_11_5_2"},{"id":"ZSD_11_11_5_2_2","text":"表语从句","parent":"ZSD_11_11_5_2"},{"id":"ZSD_11_11_7","text":"强调句","parent":"ZSD_11"},{"id":"ZSD_11_11_8","text":"虚拟语气","parent":"ZSD_11"},{"id":"ZSD_11_11_9","text":"直接引语和间接引语","parent":"ZSD_11"},{"id":"ZSD_11_12","text":"情景交际","parent":"ZSD_11"},{"id":"ZSD_11_12_0","text":"社会交往类","parent":"ZSD_11_12"},{"id":"ZSD_11_12_0_0","text":"问候和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_2","text":"问路与应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_3","text":"打电话","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_4","text":"购物","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_5","text":"谈论天气","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_6","text":"就医","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_8","text":"劝告和建议","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_11","text":"感谢和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_13","text":"道歉、遗憾、同情和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_14","text":"介绍和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_15","text":"祝愿、祝贺和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_16","text":"赞美和恭维及应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_17","text":"邀请和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_18","text":"告别和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_19","text":"请求允许和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_20","text":"提供（帮助等）和应答","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_22","text":"约会","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_23","text":"语言困难","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_24","text":"提醒与警告","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_0_25","text":"就餐","parent":"ZSD_11_12_0"},{"id":"ZSD_11_12_1","text":"态度类","parent":"ZSD_11_12"},{"id":"ZSD_11_12_1_0","text":"同意和不同意/喜欢和厌恶","parent":"ZSD_11_12_1"},{"id":"ZSD_11_12_1_6","text":"肯定和不肯定/判断和意见","parent":"ZSD_11_12_1"},{"id":"ZSD_11_12_1_7","text":"意愿和打算/订正或澄清错误","parent":"ZSD_11_12_1"},{"id":"ZSD_11_12_2","text":"情感类","parent":"ZSD_11_12"},{"id":"ZSD_11_12_2_0","text":"喜悦/惊奇/焦虑/安慰/满意","parent":"ZSD_11_12_2"},{"id":"ZSD_11_12_2_7","text":"遗憾/同情/失望/沮丧","parent":"ZSD_11_12_2"},{"id":"ZSD_11_13","text":"完形填空","parent":"ZSD_11"},{"id":"ZSD_11_14","text":"阅读理解","parent":"ZSD_11"},{"id":"ZSD_11_14_1","text":"细节理解题","parent":"ZSD_11_14"},{"id":"ZSD_11_14_2","text":"推理判断题","parent":"ZSD_11_14"},{"id":"ZSD_11_14_3","text":"词义猜测题","parent":"ZSD_11_14"},{"id":"ZSD_11_14_4","text":"主旨大意题","parent":"ZSD_11_14"},{"id":"ZSD_11_16","text":"书面表达","parent":"ZSD_11"},{"id":"ZSD_11_16_0","text":"提纲作文","parent":"ZSD_11_16"},{"id":"ZSD_11_16_1","text":"图画作文","parent":"ZSD_11_16"},{"id":"ZSD_11_16_3","text":"图表作文","parent":"ZSD_11_16"},{"id":"ZSD_11_16_4","text":"（半）开放式作文","parent":"ZSD_11_16"},{"id":"ZSD_11_17","text":"填空题","parent":"ZSD_11"},{"id":"ZSD_11_17_0","text":"单词/短语拼写","parent":"ZSD_11_17"},{"id":"ZSD_11_17_1","text":"句型转换/改写句子","parent":"ZSD_11_17"},{"id":"ZSD_11_17_3","text":"短文填空","parent":"ZSD_11_17"},{"id":"ZSD_11_17_4","text":"适当形式填空","parent":"ZSD_11_17"},{"id":"ZSD_11_17_6","text":"连词成句","parent":"ZSD_11_17"},{"id":"ZSD_11_17_14","text":"根据汉语提示完成句子","parent":"ZSD_11_17"},{"id":"ZSD_11_17_15","text":"选词填空","parent":"ZSD_11_17"},{"id":"ZSD_11_18","text":"任务型阅读","parent":"ZSD_11"},{"id":"ZSD_11_18_0","text":"回答问题型","parent":"ZSD_11_18"},{"id":"ZSD_11_18_1","text":"填写表格型","parent":"ZSD_11_18"},{"id":"ZSD_11_18_2","text":"判断正误型","parent":"ZSD_11_18"},{"id":"ZSD_11_18_3","text":"还原句子型","parent":"ZSD_11_18"},{"id":"ZSD_11_18_4","text":"综合任务型","parent":"ZSD_11_18"},{"id":"ZSD_11_19","text":"其他","parent":"ZSD_11"},{"id":"ZSD_11_19_0","text":"谚语","parent":"ZSD_11_19"},{"id":"ZSD_11_19_1","text":"中英文姓名差异","parent":"ZSD_11_19"},{"id":"ZSD_11_19_2","text":"中西方礼仪文化","parent":"ZSD_11_19"}]
"""

q = json.loads(q)
udo = None
d = {}
for item in q:
    tmp = None
    i = item['id']
    p = item['parent']
    if p == "#":
        udo = Node(i)
        d[i] = udo
        continue
    tmp = Node(i, parent=d.get(p))
    d[i] = tmp


# print(RenderTree(udo))


for pre, fill, node in RenderTree(udo):
    if not node.is_leaf:
        print("3=" + node.name)
    # print("%s%s" % (pre, node.name))

# print(RenderTree(udo, style=AsciiStyle()).by_attr())

'3=ZSD_11','3=ZSD_11_0','3=ZSD_11_1','3=ZSD_11_2','3=ZSD_11_3','3=ZSD_11_4','3=ZSD_11_4_0','3=ZSD_11_4_1','3=ZSD_11_4_4','3=ZSD_11_4_9','3=ZSD_11_5','3=ZSD_11_6','3=ZSD_11_6_1','3=ZSD_11_6_2','3=ZSD_11_7','3=ZSD_11_7_0','3=ZSD_11_7_1','3=ZSD_11_8','3=ZSD_11_8_0','3=ZSD_11_8_1','3=ZSD_11_8_11','3=ZSD_11_9','3=ZSD_11_9_0','3=ZSD_11_9_1','3=ZSD_11_9_1_1','3=ZSD_11_9_2','3=ZSD_11_10','3=ZSD_11_10_0','3=ZSD_11_10_1','3=ZSD_11_10_1_5','3=ZSD_11_10_2','3=ZSD_11_10_3','3=ZSD_11_10_3_0','3=ZSD_11_10_3_1','3=ZSD_11_10_4','3=ZSD_11_10_4_0','3=ZSD_11_10_4_1','3=ZSD_11_10_4_2','3=ZSD_11_10_5','3=ZSD_11_11','3=ZSD_11_11_1','3=ZSD_11_11_4','3=ZSD_11_11_5','3=ZSD_11_11_5_0','3=ZSD_11_11_5_1','3=ZSD_11_11_5_2','3=ZSD_11_12','3=ZSD_11_12_0','3=ZSD_11_12_1','3=ZSD_11_12_2','3=ZSD_11_14','3=ZSD_11_16','3=ZSD_11_17','3=ZSD_11_18','3=ZSD_11_19',