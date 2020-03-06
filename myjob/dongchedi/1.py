import requests
from bs4 import BeautifulSoup as bs
import pprint
header={
    'user-agent':'user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
# print(rs)
temp={"status": "success", "data": {"brands": {"1": 1, "2": 4, "3": 10, "4": 7, "5": 1, "7": 1, "258": 1, "14": 2, "272": 1, "145": 1, "19": 7, "20": 3, "22": 3, "24": 3, "29": 3, "30": 2, "31": 2, "38": 1, "41": 1, "42": 1, "45": 1, "47": 2, "51": 1, "52": 1, "62": 4, "63": 1, "80": 1, "96": 1, "236": 2, "112": 2, "248": 1}, "series": [{"count": 1, "outter_name": "\u5954\u9a70GLC", "dealer_max_price": 54.78, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/49ab4be185fc5b449af4a1378cc5a92e~tplv-resize:480:0.png", "max_price": 58.78, "brand_id": 3, "min_price": 39.28, "sub_brand_id": 31, "dealer_price": "35.28-54.78\u4e07", "dealer_min_price": 35.28, "car_ids": [39815], "business_status": 0, "id": 216, "concern_id": 216}, {"count": 8, "outter_name": "\u666e\u62c9\u591a", "dealer_max_price": 60.48, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/cb955ed96102c420206cd1b1e744150a~tplv-resize:480:0.png", "max_price": 60.48, "brand_id": 5, "min_price": 43.58, "sub_brand_id": 60, "dealer_price": "43.58-60.48\u4e07", "dealer_min_price": 43.58, "car_ids": [34711, 34713, 25910, 25911, 25912, 25913, 25914, 25915], "business_status": 0, "id": 547, "concern_id": 547}, {"count": 8, "outter_name": "\u5b9d\u9a6cX5", "dealer_max_price": 84.99, "cover_url": "https://p9-dcd.byteimg.com/img/mosaic-legacy/beef000066ae434f96d8~tplv-resize:480:0.png", "max_price": 84.99, "brand_id": 4, "min_price": 69.99, "sub_brand_id": 24, "dealer_price": "69.99-84.99\u4e07", "dealer_min_price": 69.99, "car_ids": [43200, 34209, 43202, 43203, 40742, 43201, 34365, 40735], "business_status": 0, "id": 128, "concern_id": 128}, {"count": 11, "outter_name": "\u63fd\u80dc", "dealer_max_price": 321.3, "cover_url": "https://p3-dcd.byteimg.com/img/motor-img/2ce7ac4ec21a9117866248a200a25237~tplv-resize:480:0.png", "max_price": 321.3, "brand_id": 19, "min_price": 122.5, "sub_brand_id": 124, "dealer_price": "111.47-321.30\u4e07", "dealer_min_price": 111.47, "car_ids": [34019, 34020, 40037, 40038, 34023, 34024, 42707, 42708, 42709, 42710, 34021], "business_status": 0, "id": 991, "concern_id": 991}, {"count": 5, "outter_name": "\u5965\u8feaQ7", "dealer_max_price": 75.1, "cover_url": "https://p6-dcd.byteimg.com/img/motor-img/e524372e66c2180c0362510fe4ac7d9c~tplv-resize:480:0.png", "max_price": 96.28, "brand_id": 2, "min_price": 68.38, "sub_brand_id": 21, "dealer_price": "53.34-75.10\u4e07", "dealer_min_price": 53.34, "car_ids": [34431, 34427, 34428, 34429, 34430], "business_status": 0, "id": 87, "concern_id": 87}, {"count": 2, "outter_name": "\u7267\u9a6c\u4eba", "dealer_max_price": 53.99, "cover_url": "https://p3-dcd.byteimg.com/img/motor-img/189bee2f3c01c707c1c0e39e0e732fc7~tplv-resize:480:0.png", "max_price": 53.99, "brand_id": 14, "min_price": 42.99, "sub_brand_id": 8, "dealer_price": "42.99-53.99\u4e07", "dealer_min_price": 42.99, "car_ids": [36228, 37754], "business_status": 0, "id": 14, "concern_id": 14}, {"count": 4, "outter_name": "Macan", "dealer_max_price": 92.5, "cover_url": "https://p3-dcd.byteimg.com/img/motor-img/c2a1c90025734293cf03e64f550ee30f~tplv-resize:480:0.png", "max_price": 92.5, "brand_id": 20, "min_price": 54.5, "sub_brand_id": 27, "dealer_price": "54.50-92.50\u4e07", "dealer_min_price": 54.5, "car_ids": [42905, 34411, 32107, 39887], "business_status": 0, "id": 154, "concern_id": 154}, {"count": 6, "outter_name": "Cayenne", "dealer_max_price": 190.8, "cover_url": "https://p9-dcd.byteimg.com/img/motor-img/b4c6feef3c2f5dc632d6ed0bfa637a7c~tplv-resize:480:0.png", "max_price": 190.8, "brand_id": 20, "min_price": 91.3, "sub_brand_id": 27, "dealer_price": "91.30-190.80\u4e07", "dealer_min_price": 91.3, "car_ids": [35691, 35694, 34097, 26229, 26230, 41525], "business_status": 0, "id": 155, "concern_id": 155}, {"count": 3, "outter_name": "\u5954\u9a70G\u7ea7", "dealer_max_price": 189.88, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/7f90b833cd07e2f2ab178abe9637437b~tplv-resize:480:0.png", "max_price": 189.88, "brand_id": 3, "min_price": 158.8, "sub_brand_id": 33, "dealer_price": "158.80-189.88\u4e07", "dealer_min_price": 158.8, "car_ids": [40161, 29404, 42422], "business_status": 0, "id": 230, "concern_id": 230}, {"count": 8, "outter_name": "\u9014\u9510", "dealer_max_price": 81.98, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/a865259f0fa54225e32a96b6b43efeb2~tplv-resize:480:0.png", "max_price": 81.98, "brand_id": 1, "min_price": 56.98, "sub_brand_id": 50, "dealer_price": "56.98-81.98\u4e07", "dealer_min_price": 56.98, "car_ids": [35179, 33162, 33163, 33164, 42261, 39356, 39357, 39358], "business_status": 0, "id": 385, "concern_id": 385}, {"count": 1, "outter_name": "Urus", "dealer_max_price": 291.2, "cover_url": "https://p9-dcd.byteimg.com/img/motor-img/0ca41891759ac8bf6cbf014953e8c9b4~tplv-resize:480:0.png", "max_price": 291.2, "brand_id": 42, "min_price": 291.2, "sub_brand_id": 109, "dealer_price": "291.20\u4e07", "dealer_min_price": 291.2, "car_ids": [24577], "business_status": 0, "id": 1643, "concern_id": 1643}, {"count": 5, "outter_name": "\u5965\u8feaQ8", "dealer_max_price": 101.88, "cover_url": "https://p6-dcd.byteimg.com/img/motor-img/ff787b18a7cad8fa580c0d633f4a304d~tplv-resize:480:0.png", "max_price": 101.88, "brand_id": 2, "min_price": 76.88, "sub_brand_id": 21, "dealer_price": "76.88-101.88\u4e07", "dealer_min_price": 76.88, "car_ids": [32473, 39884, 36252, 40029, 40030], "business_status": 0, "id": 1646, "concern_id": 1646}, {"count": 16, "outter_name": "\u96f7\u514b\u8428\u65afRX", "dealer_max_price": 79.9, "cover_url": "https://p6-dcd.byteimg.com/img/motor-img/935449762116409e54a73aae1c90ccd8~tplv-resize:480:0.png", "max_price": 79.9, "brand_id": 22, "min_price": 39.8, "sub_brand_id": 111, "dealer_price": "39.80-79.90\u4e07", "dealer_min_price": 39.8, "car_ids": [40192, 40193, 40194, 40195, 40196, 39582, 39583, 39584, 39585, 39586, 39587, 39588, 39589, 40189, 40190, 40191], "business_status": 0, "id": 894, "concern_id": 894}, {"count": 2, "outter_name": "\u51ef\u8fea\u62c9\u514bXT6", "dealer_max_price": 52.97, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/b533e7d3caddddde5f88cda8900a80e8~tplv-resize:480:0.png", "max_price": 54.97, "brand_id": 30, "min_price": 41.97, "sub_brand_id": 102, "dealer_price": "39.97-52.97\u4e07", "dealer_min_price": 39.97, "car_ids": [38727, 34988], "business_status": 0, "id": 3164, "concern_id": 3164}, {"count": 7, "outter_name": "\u6c83\u5c14\u6c83XC90", "dealer_max_price": 70.9, "cover_url": "https://p3-dcd.byteimg.com/img/motor-img/dd68fedb81527885ad980bd2a004077c~tplv-resize:480:0.png", "max_price": 83.39, "brand_id": 24, "min_price": 63.39, "sub_brand_id": 169, "dealer_price": "49.80-70.90\u4e07", "dealer_min_price": 49.8, "car_ids": [40000, 40001, 40002, 40003, 40004, 39881, 39882], "business_status": 0, "id": 1277, "concern_id": 1277}, {"count": 3, "outter_name": "\u5b9d\u9a6cX6", "dealer_max_price": 93.69, "cover_url": "https://p3-dcd.byteimg.com/img/motor-img/49a0871000ad5af119de78a89562e0a2~tplv-resize:480:0.png", "max_price": 93.69, "brand_id": 4, "min_price": 76.69, "sub_brand_id": 24, "dealer_price": "76.69-93.69\u4e07", "dealer_min_price": 76.69, "car_ids": [42008, 42320, 41994], "business_status": 0, "id": 127, "concern_id": 127}, {"series_status_tag": {"text": "2020\u65b0\u6b3e", "type": 2}, "count": 14, "outter_name": "\u5b9d\u9a6cX7", "dealer_max_price": 162.8, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/fd07c0793299f5fd721a8d80b873ffbf~tplv-resize:480:0.png", "max_price": 162.8, "brand_id": 4, "min_price": 100.0, "sub_brand_id": 24, "dealer_price": "100.00-162.80\u4e07", "dealer_min_price": 100.0, "car_ids": [34369, 33474, 43601, 42136, 43602, 43603, 43604, 43605, 43606, 42137, 35960, 35961, 35962, 35963], "business_status": 0, "id": 2825, "concern_id": 2825}, {"count": 5, "outter_name": "\u63fd\u80dc\u661f\u8109", "dealer_max_price": 75.58, "cover_url": "https://p3-dcd.byteimg.com/img/motor-img/45b93a9f150e5e28c20af48ad7d25dd1~tplv-resize:480:0.png", "max_price": 87.88, "brand_id": 19, "min_price": 57.28, "sub_brand_id": 124, "dealer_price": "49.26-75.58\u4e07", "dealer_min_price": 49.26, "car_ids": [40722, 40723, 40724, 40725, 40726], "business_status": 0, "id": 989, "concern_id": 989}, {"count": 14, "outter_name": "\u5954\u9a70GLE", "dealer_max_price": 135.38, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/9c32334018e6d31a8f10594ef4eb30b9~tplv-resize:480:0.png", "max_price": 135.38, "brand_id": 3, "min_price": 70.98, "sub_brand_id": 33, "dealer_price": "68.98-135.38\u4e07", "dealer_min_price": 68.98, "car_ids": [35776, 42208, 42210, 42211, 42209, 42213, 35911, 33547, 42956, 42957, 30548, 30549, 30550, 42212], "business_status": 0, "id": 228, "concern_id": 228}, {"count": 3, "outter_name": "\u5954\u9a70G\u7ea7AMG", "dealer_max_price": 245.88, "cover_url": "https://p1-dcd.byteimg.com/img/motor-img/de4b05c8a2b575af6913fb05da759b5c~tplv-resize:480:0.png", "max_price": 245.88, "brand_id": 3, "min_price": 220.8, "sub_brand_id": 34, "dealer_price": "220.80-245.88\u4e07", "dealer_min_price": 220.8, "car_ids": [42400, 37226, 37227], "business_status": 0, "id": 255, "concern_id": 255}], "series_count": 72}}

# pprint.pprint(temp['data']['series'])
def insert_into_car():
    import pymysql
    account = ("rm-uf641076h06m5vvtayo.mysql.rds.aliyuncs.com", "tsxx736", 'Password88!', 'interest')
    conn = pymysql.connect(*account)
    cur =conn.cursor()

    for i in temp['data']['series']:
        id = str(i['concern_id'])
        name = str(i['outter_name'])
        minp =str(i['min_price'])
        maxp =str(i['max_price'])
        cur.execute('insert into suv (page_id,carname,min_price,max_price) values(%s,%s,%s,%s)',(id,name,minp,maxp))
        conn.commit()
        print('yeap!')
    conn.close()


def tmep():
    import pandas as pd
    import pymysql
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

    plt.style.use('seaborn-pastel')
    fig,ax =plt.subplots(2,2)
    doc1=doc[:2]
    print(doc1)
    doc2 = doc[2:10]
    print(doc2)
    doc3 =doc[10:]
    s1=suv[:10]
    s2=suv[10:]
    for no,i in zip(
            [[n,r]for n in range(2) for r in range(2)],
            [s1,s2,doc2,doc3]
    ):
        minp =i['MIN_PRICE']
        maxp =i['MAX_PRICE']
        a=np.arange(len(i))
        ax[no[0],no[1]].barh(a-0.05,maxp,label='MAX',)
        ax[no[0],no[1]].barh(a+0.05,minp,label='MIN',edgecolor='grey')
        ax[no[0],no[1]].set_yticks(np.arange(len(i)))
        ax[no[0],no[1]].set_yticklabels(i['CARNAME'])
        [ax[no[0],no[1]].spines[i].set_color('none') for i in ['top', 'bottom', 'left', 'right']]
        plt.legend()
        plt.tight_layout()
    ax[0,0].set_xlabel('金额（万）',fontdict=dict(fontsize=6,style='italic'))
    plt.savefig('dongchedi')
tmep()