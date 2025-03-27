import requests
import re
import json
import urllib.parse
from bs4 import BeautifulSoup
import time
import random

class Spider():
    def __init__(self):
        self.site = "河马剧场"
        self.siteUrl = "https://www.kuaikaw.cn"
        self.nextData = None  # 缓存NEXT_DATA数据
        self.cateManual = {
            "首页": "home",
            "青春": "青春",
            # "民国": "民国",
            # "萌宝": "萌宝",
            # "超能": "超能",
            # "甜宠": "甜宠",
            # "学院": "学院",
            # "都市": "都市",
            # "穿越": "穿越",
            # "古装": "古装",
            # "悬疑": "悬疑",
            # "创业": "创业"
        }

    def getName(self):
        # 返回爬虫名称
        return "河马短剧"
    
    def init(self, extend=""):                
        return {}
    
    def fetch(self, url, headers=None):
        """统一的网络请求接口"""
        if headers is None:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
                "Referer": self.siteUrl,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
            }
        
        try:
            response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"请求异常: {url}, 错误: {str(e)}")
            return None
    
    def homeContent(self, filter=False):
        """获取首页分类及筛选"""
        # result = {}
        # # 分类列表，使用已初始化的cateManual
        # classes = []
        # for k in self.cateManual:
        #     classes.append({
        #         'type_name': k,
        #         'type_id': self.cateManual[k]
        #     })
        # result['class'] = classes
        # # 获取首页推荐视频
        # try:
        #     result['list'] = self.homeVideoContent()['list']
        # except:
        #     result['list'] = []

        result = {'class': [{'type_name': '首页', 'type_id': 'home'}, {'type_name': '青春', 'type_id': '青春'}], 'list': [{'vod_id': '/drama/41000100525', 'vod_name': '金马玉堂', 'vod_pic': 'https://seoimg.zqkanshu.com/others/seoHmjcBannerManage/date20240110/1704869291106.png', 'vod_remarks': ''}, {'vod_id': '/drama/41000101091', 'vod_name': '悬我济世', 'vod_pic': 'https://seoimg.zqkanshu.com/others/seoHmjcBannerManage/date20240110/1704869352225.png', 'vod_remarks': ''}, {'vod_id': '/drama/41000113011', 'vod_name': '爱意凋亡', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000113011/41000113011.jpg?t=1741073442252&imageView2/0/w/200/h/267', 'vod_remarks': '完本 44集'}, {'vod_id': '/drama/41000113174', 'vod_name': '故山犹负平生月', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000113174/41000113174.jpg?t=1741313615913&imageView2/0/w/200/h/267', 'vod_remarks': '完本 50集'}, {'vod_id': '/drama/41000105997', 'vod_name': '团宠老妈惹不起', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105997/41000105997.jpg?t=1726048602830&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000106145', 'vod_name': '薇霜御守情长', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000106145/41000106145.jpg?t=1735708244766&imageView2/0/w/200/h/267', 'vod_remarks': '完本 62集'}, {'vod_id': '/drama/41000106104', 'vod_name': '丈夫的陷阱', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000106104/41000106104.jpg?t=1727153046984&imageView2/0/w/200/h/267', 'vod_remarks': '完本 42集'}, {'vod_id': '/drama/41000105436', 'vod_name': '金榜题名之状元归乡', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105436/41000105436.jpg?t=1724032498628&imageView2/0/w/200/h/267', 'vod_remarks': '完本 92集'}, {'vod_id': '/drama/41000105459', 'vod_name': '桃花马上请长缨', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105459/41000105459.jpg?t=1724166484152&imageView2/0/w/200/h/267', 'vod_remarks': '完本 91集'}, {'vod_id': '/drama/41000103116', 'vod_name': '相逢如初见', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000103116/41000103116.jpg?t=1735720290804&imageView2/0/w/200/h/267', 'vod_remarks': '完本 102集'}, {'vod_id': '/drama/41000100936', 'vod_name': '下一站遇见', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100936/41000100936.jpg?t=1700549347245&imageView2/0/w/200/h/267', 'vod_remarks': '完本 92集'}, {'vod_id': '/drama/41000103185', 'vod_name': '九十九封家书，震惊全国', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000103185/41000103185.jpg?t=1713515468865&imageView2/0/w/200/h/267', 'vod_remarks': '完本 84集'}, {'vod_id': '/drama/41000102004', 'vod_name': '琅琊', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000102004/41000102004.jpg?t=1706235052066&imageView2/0/w/200/h/267', 'vod_remarks': '完本 94集'}, {'vod_id': '/drama/41000101445', 'vod_name': '仙帝归来', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000101445/41000101445.jpg?t=1703817610481&imageView2/0/w/200/h/267', 'vod_remarks': '完本 82集'}, {'vod_id': '/drama/41000102143', 'vod_name': '霸道龙尊', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000102143/41000102143.jpg?t=1706927032539&imageView2/0/w/200/h/267', 'vod_remarks': '完本 93集'}, {'vod_id': '/drama/41000102118', 'vod_name': '化龙', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000102118/41000102118.jpg?t=1706878564255&imageView2/0/w/200/h/267', 'vod_remarks': '完本 98集'}, {'vod_id': '/drama/41000102070', 'vod_name': '绝望派对', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000102070/41000102070.jpg?t=1706599132573&imageView2/0/w/200/h/267', 'vod_remarks': '完本 86集'}, {'vod_id': '/drama/41000100687', 'vod_name': '日落时分爱上你', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100687/41000100687.jpg?t=1693998666904&imageView2/0/w/200/h/267', 'vod_remarks': '完本 92集'}, {'vod_id': '/drama/41000100040', 'vod_name': '我的傲娇女神', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100040/41000100040.jpg?t=1732775041261&imageView2/0/w/200/h/267', 'vod_remarks': '完本 174集'}, {'vod_id': '/drama/41000100615', 'vod_name': '大梁败家少爷', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100615/41000100615.jpg?t=1719755317168&imageView2/0/w/200/h/267', 'vod_remarks': '完本 92集'}, {'vod_id': '/drama/41000101008', 'vod_name': '你是人间烟火', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000101008/41000101008.jpg?t=1701308341679&imageView2/0/w/200/h/267', 'vod_remarks': '完本 101集'}, {'vod_id': '/drama/41000100147', 'vod_name': '天尊归来', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100147/41000100147.jpg?t=1692685143424&imageView2/0/w/200/h/267', 'vod_remarks': '完本 102集'}, {'vod_id': '/drama/41000100611', 'vod_name': '这个皇子不好惹', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100611/41000100611.jpg?t=1701079625730&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000100928', 'vod_name': '隐世千金', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100928/41000100928.jpg?t=1700126306255&imageView2/0/w/200/h/267', 'vod_remarks': '完本 81集'}, {'vod_id': '/drama/41000113082', 'vod_name': '半缘修道半缘君', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000113082/41000113082.jpg?t=1741159111931&imageView2/0/w/200/h/267', 'vod_remarks': '完本 55集'}, {'vod_id': '/drama/41000105923', 'vod_name': '小花和爷爷', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105923/41000105923.jpg?t=1725708610096&imageView2/0/w/200/h/267', 'vod_remarks': '完本 80集'}, {'vod_id': '/drama/41000105926', 'vod_name': '夫妻本是同林鸟', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105926/41000105926.jpg?t=1725848906536&imageView2/0/w/200/h/267', 'vod_remarks': '完本 76集'}, {'vod_id': '/drama/41000106070', 'vod_name': '我为自己而活', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000106070/41000106070.jpg?t=1735714844546&imageView2/0/w/200/h/267', 'vod_remarks': '完本 42集'}, {'vod_id': '/drama/41000105462', 'vod_name': '老无所依', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105462/41000105462.jpg?t=1724207788322&imageView2/0/w/200/h/267', 'vod_remarks': '完本 57集'}, {'vod_id': '/drama/41000102581', 'vod_name': '无极归来', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000102581/41000102581.jpg?t=1709622679308&imageView2/0/w/200/h/267', 'vod_remarks': '完本 87集'}, {'vod_id': '/drama/41000100712', 'vod_name': '逆苍天', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100712/41000100712.jpg?t=1735698897637&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000100839', 'vod_name': '陆家夫人是女侠', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100839/41000100839.jpg?t=1698310617924&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000100845', 'vod_name': '沉睡恋人', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100845/41000100845.jpg?t=1698379880187&imageView2/0/w/200/h/267', 'vod_remarks': '完本 103集'}, {'vod_id': '/drama/41000100759', 'vod_name': '世上无人再似她', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100759/41000100759.jpg?t=1695979156858&imageView2/0/w/200/h/267', 'vod_remarks': '完本 98集'}, {'vod_id': '/drama/41000101006', 'vod_name': '裴少，夫人又离家出走了', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000101006/41000101006.jpg?t=1701311895575&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000100734', 'vod_name': '第一次爱的人', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100734/41000100734.jpg?t=1695604822738&imageView2/0/w/200/h/267', 'vod_remarks': '完本 95集'}, {'vod_id': '/drama/41000100780', 'vod_name': '逃跑的灰姑娘', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100780/41000100780.jpg?t=1697091487439&imageView2/0/w/200/h/267', 'vod_remarks': '完本 105集'}, {'vod_id': '/drama/41000100506', 'vod_name': '拨开云雾见晴天', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100506/41000100506.jpg?t=1692683044287&imageView2/0/w/200/h/267', 'vod_remarks': '完本 95集'}, {'vod_id': '/drama/41000100590', 'vod_name': '顾总的幸孕宠妻', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100590/41000100590.jpg?t=1692682799863&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000100732', 'vod_name': '节目表白被拒，女神为我撑腰', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100732/41000100732.jpg?t=1732776555905&imageView2/0/w/200/h/267', 'vod_remarks': '完本 99集'}, {'vod_id': '/drama/41000100445', 'vod_name': '医心倾卿', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100445/41000100445.jpg?t=1735705938015&imageView2/0/w/200/h/267', 'vod_remarks': '完本 118集'}, {'vod_id': '/drama/41000112591', 'vod_name': '自坠深渊', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000112591/41000112591.jpg?t=1740710655461&imageView2/0/w/200/h/267', 'vod_remarks': '完本 52集'}, {'vod_id': '/drama/41000113456', 'vod_name': '我终于可以不再爱你了', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000113456/41000113456.jpg?t=1741920923442&imageView2/0/w/200/h/267', 'vod_remarks': '完本 60集'}, {'vod_id': '/drama/41000113133', 'vod_name': '婆婆把我捧上天', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000113133/41000113133.jpg?t=1741244550941&imageView2/0/w/200/h/267', 'vod_remarks': '完本 52集'}, {'vod_id': '/drama/41000113092', 'vod_name': '假如爱情看不见', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000113092/41000113092.jpg?t=1741662146153&imageView2/0/w/200/h/267', 'vod_remarks': '完本 55集'}, {'vod_id': '/drama/41000105522', 'vod_name': '大剑', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105522/41000105522.jpg?t=1724376259607&imageView2/0/w/200/h/267', 'vod_remarks': '完本 71集'}, {'vod_id': '/drama/41000105744', 'vod_name': '生女当如此', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105744/41000105744.jpg?t=1725243806499&imageView2/0/w/200/h/267', 'vod_remarks': '完本 77集'}, {'vod_id': '/drama/41000105639', 'vod_name': '重逢自有天意', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105639/41000105639.jpg?t=1724741841190&imageView2/0/w/200/h/267', 'vod_remarks': '完本 78集'}, {'vod_id': '/drama/41000104697', 'vod_name': '老婆相信我，咱家真是普通家庭', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000104697/41000104697.jpg?t=1721995901183&imageView2/0/w/200/h/267', 'vod_remarks': '完本 60集'}, {'vod_id': '/drama/41000105259', 'vod_name': '六十大寿', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105259/41000105259.jpg?t=1723426824903&imageView2/0/w/200/h/267', 'vod_remarks': '完本 50集'}, {'vod_id': '/drama/41000105402', 'vod_name': '丑妻', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105402/41000105402.jpg?t=1723715635718&imageView2/0/w/200/h/267', 'vod_remarks': '完本 66集'}, {'vod_id': '/drama/41000105237', 'vod_name': '我最亲爱的', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105237/41000105237.jpg?t=1723113438394&imageView2/0/w/200/h/267', 'vod_remarks': '完本 44集'}, {'vod_id': '/drama/41000105431', 'vod_name': '替身为凰', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000105431/41000105431.jpg?t=1723790755755&imageView2/0/w/200/h/267', 'vod_remarks': '完本 92集'}, {'vod_id': '/drama/41000104408', 'vod_name': '大夏傻神', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000104408/41000104408.jpg?t=1721182170448&imageView2/0/w/200/h/267', 'vod_remarks': '完本 82集'}, {'vod_id': '/drama/41000103797', 'vod_name': '金榜题名之寒门状元', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000103797/41000103797.jpg?t=1717465798685&imageView2/0/w/200/h/267', 'vod_remarks': '完本 80集'}, {'vod_id': '/drama/41000103074', 'vod_name': '逆转', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000103074/41000103074.jpg?t=1712642841863&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000102478', 'vod_name': '绝世狂枭', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000102478/41000102478.jpg?t=1709281154417&imageView2/0/w/200/h/267', 'vod_remarks': '完本 99集'}, {'vod_id': '/drama/41000100893', 'vod_name': '恋爱暴击', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100893/41000100893.jpg?t=1735733644862&imageView2/0/w/200/h/267', 'vod_remarks': '完本 97集'}, {'vod_id': '/drama/41000100612', 'vod_name': '镇北王', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100612/41000100612.jpg?t=1692676569902&imageView2/0/w/200/h/267', 'vod_remarks': '完本 99集'}, {'vod_id': '/drama/41000101010', 'vod_name': '南瓷北城', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000101010/41000101010.jpg?t=1701315705514&imageView2/0/w/200/h/267', 'vod_remarks': '完本 95集'}, {'vod_id': '/drama/41000100248', 'vod_name': '贤德皇子：志耀山河', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100248/41000100248.jpg?t=1735748813028&imageView2/0/w/200/h/267', 'vod_remarks': '完本 106集'}, {'vod_id': '/drama/41000100819', 'vod_name': '缘定心上人', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100819/41000100819.jpg?t=1740032747553&imageView2/0/w/200/h/267', 'vod_remarks': '完本 93集'}, {'vod_id': '/drama/41000101030', 'vod_name': '此生逍遥天休问', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000101030/41000101030.jpg?t=1735731680770&imageView2/0/w/200/h/267', 'vod_remarks': '完本 100集'}, {'vod_id': '/drama/41000100637', 'vod_name': '请君入我相思局', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100637/41000100637.jpg?t=1692759919580&imageView2/0/w/200/h/267', 'vod_remarks': '完本 102集'}, {'vod_id': '/drama/41000100466', 'vod_name': '龙域帝尊', 'vod_pic': 'https://seoali.zqkanshu.com/cppartner/4x1/41x0/410x0/41000100466/41000100466.jpg?t=1692683150522&imageView2/0/w/200/h/267', 'vod_remarks': '完本 99集'}]}
        return result
    
    def homeVideoContent(self):
        """获取首页推荐视频内容"""
        url = self.siteUrl
        videos = []
        try:
            response = self.fetch(url)
            html_content = response.text
            
            # 提取NEXT_DATA JSON数据
            next_data_pattern = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
            next_data_match = re.search(next_data_pattern, html_content, re.DOTALL)
            
            if next_data_match:
                next_data_json = json.loads(next_data_match.group(1))
                page_props = next_data_json.get("props", {}).get("pageProps", {})
                
                # 获取轮播图数据 - 这些通常是推荐内容
                if "bannerList" in page_props and isinstance(page_props["bannerList"], list):
                    banner_list = page_props["bannerList"]
                    for banner in banner_list:
                        book_id = banner.get("bookId", "")
                        book_name = banner.get("bookName", "")
                        cover_url = banner.get("coverWap", banner.get("wapUrl", ""))
                        
                        # 获取状态和章节数
                        status = banner.get("statusDesc", "")
                        total_chapters = banner.get("totalChapterNum", "")
                        
                        if book_id and book_name:
                            videos.append({
                                "vod_id": f"/drama/{book_id}",
                                "vod_name": book_name,
                                "vod_pic": cover_url,
                                "vod_remarks": f"{status} {total_chapters}集" if total_chapters else status
                            })
                
                # SEO分类下的推荐
                if "seoColumnVos" in page_props and isinstance(page_props["seoColumnVos"], list):
                    for column in page_props["seoColumnVos"]:
                        book_infos = column.get("bookInfos", [])
                        for book in book_infos:
                            book_id = book.get("bookId", "")
                            book_name = book.get("bookName", "")
                            cover_url = book.get("coverWap", "")
                            status = book.get("statusDesc", "")
                            total_chapters = book.get("totalChapterNum", "")
                            
                            if book_id and book_name:
                                videos.append({
                                    "vod_id": f"/drama/{book_id}",
                                    "vod_name": book_name,
                                    "vod_pic": cover_url,
                                    "vod_remarks": f"{status} {total_chapters}集" if total_chapters else status
                                })
            
            # 如果没有提取到视频，尝试从HTML解析
            if not videos:
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # 查找所有带有bookId属性的元素
                book_elements = soup.select('[data-bookid], [data-book-id], [bookid]')
                for elem in book_elements:
                    book_id = elem.get('data-bookid') or elem.get('data-book-id') or elem.get('bookid')
                    
                    # 查找标题和图片
                    title_elem = elem.select_one('.title, h3, h2, .book-name, .name')
                    title = title_elem.text.strip() if title_elem else "未知标题"
                    
                    img_elem = elem.select_one('img')
                    img_url = img_elem.get('src', '') if img_elem else ""
                    
                    # 备注信息
                    remark_elem = elem.select_one('.remark, .status, .episode')
                    remark = remark_elem.text.strip() if remark_elem else ""
                    
                    if book_id and title:
                        videos.append({
                            "vod_id": f"/drama/{book_id}",
                            "vod_name": title,
                            "vod_pic": img_url,
                            "vod_remarks": remark
                        })
            
            # 去重
            seen = set()
            unique_videos = []
            for video in videos:
                if video["vod_id"] not in seen:
                    seen.add(video["vod_id"])
                    unique_videos.append(video)
            
            videos = unique_videos
        
        except Exception as e:
            print(f"获取首页推荐内容出错: {e}")
        
        result = {
            "list": videos
        }
        return result
    
    def categoryContent(self, tid, pg, filter, extend):
        """获取分类内容"""
        result = {}
        videos = []
        
        if tid == "home":
            # 首页内容直接返回homeVideoContent的结果
            return self.homeVideoContent()
        
        # 网站分类路径已变更，使用搜索接口进行替代
        # 根据分类ID构建搜索查询
        search_key = tid
        
        # 使用分类名称作为搜索关键词
        for name, id_ in self.cateManual.items():
            if id_ == tid:
                search_key = name
                break
        
        # 使用搜索接口获取分类内容
        url = f"{self.siteUrl}/search?searchValue={urllib.parse.quote(search_key)}&page={pg}"
        
        try:
            response = self.fetch(url)
            html_content = response.text
            
            # 提取NEXT_DATA JSON数据
            next_data_pattern = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
            next_data_match = re.search(next_data_pattern, html_content, re.DOTALL)
            
            if next_data_match:
                next_data_json = json.loads(next_data_match.group(1))
                page_props = next_data_json.get("props", {}).get("pageProps", {})
                
                # 获取总页数和当前页
                current_page = page_props.get("page", 1)
                total_pages = page_props.get("pages", 1)
                
                # 获取书籍列表
                book_list = page_props.get("bookList", [])
                
                # 转换为通用格式
                for book in book_list:
                    book_id = book.get("bookId", "")
                    book_name = book.get("bookName", "")
                    cover_url = book.get("coverWap", "")
                    status_desc = book.get("statusDesc", "")
                    total_chapters = book.get("totalChapterNum", "")
                    
                    if book_id and book_name:
                        videos.append({
                            "vod_id": f"/drama/{book_id}",
                            "vod_name": book_name,
                            "vod_pic": cover_url,
                            "vod_remarks": f"{status_desc} {total_chapters}集" if total_chapters else status_desc
                        })
                
                # 构建返回结果
                # result = {
                #     "list": videos,
                #     "page": int(current_page),
                #     "pagecount": total_pages,
                #     "limit": len(videos),
                #     "total": total_pages * len(videos) if videos else 0
                # }
                result = {
                    "list": videos,
                    "page": pg,
                    "pagecount": 9999,
                    "limit": 90,
                    "total": 999999
                }
            else:
                # 如果未提取到NEXT_DATA，直接解析HTML
                soup = BeautifulSoup(html_content, 'html.parser')
                book_items = soup.select('.book-item, .card, [data-bookid]')
                
                for item in book_items:
                    # 提取链接获取ID
                    href = item.get('href', '')
                    book_id = None
                    
                    match = re.search(r'/episode/(\d+)', href)
                    if match:
                        book_id = match.group(1)
                    else:
                        book_id = item.get('data-bookid', '')
                    
                    if not book_id:
                        continue
                    
                    # 查找标题
                    title_elem = item.select_one('.title, h3, h2, .book-name')
                    title = title_elem.text.strip() if title_elem else "未知标题"
                    
                    # 查找图片
                    img_elem = item.select_one('img')
                    img_url = img_elem.get('src', '') if img_elem else ""
                    
                    # 查找备注信息
                    remark_elem = item.select_one('.remark, .status, .episode')
                    remark = remark_elem.text.strip() if remark_elem else ""
                    
                    if book_id and title:
                        videos.append({
                            "vod_id": f"/drama/{book_id}",
                            "vod_name": title,
                            "vod_pic": img_url,
                            "vod_remarks": remark
                        })
                
                # 构建返回结果
                # result = {
                #     "list": videos,
                #     "page": int(pg),
                #     "pagecount": 1,  # 无法获取总页数时默认为1
                #     "limit": len(videos),
                #     "total": len(videos)
                # }
                result = {
                    "list": videos,
                    "page": pg,
                    "pagecount": 9999,
                    "limit": 90,
                    "total": 999999
                }
        
        except Exception as e:
            print(f"获取分类内容出错: {e}")
            result = {
                "list": [],
                "page": int(pg),
                "pagecount": 1,
                "limit": 0,
                "total": 0
            }
        
        return result
    
    def searchContent(self, key, quick=False):
        # 搜索功能
        search_results = []
        # URL编码搜索关键词
        encoded_key = urllib.parse.quote(key)
        # 获取第一页结果，并检查总页数
        url = f"{self.siteUrl}/search?searchValue={encoded_key}&page=1"
        try:
            response = self.fetch(url)
            html_content = response.text
            
            # 提取NEXT_DATA JSON数据
            next_data_pattern = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
            next_data_match = re.search(next_data_pattern, html_content, re.DOTALL)
            
            if next_data_match:
                next_data_json = json.loads(next_data_match.group(1))
                page_props = next_data_json.get("props", {}).get("pageProps", {})
                
                # 获取总页数
                current_page = page_props.get("page", 1)
                total_pages = page_props.get("pages", 1)
                
                # 处理所有页的数据
                all_book_list = []
                
                # 添加第一页的书籍列表
                book_list = page_props.get("bookList", [])
                all_book_list.extend(book_list)
                
                # 如果有多页，获取其他页的数据
                if total_pages > 1 and not quick:  # quick模式只获取第一页
                    for page in range(2, total_pages + 1):
                        time.sleep(random.uniform(0.5, 1.5))  # 添加随机延迟避免频繁请求
                        next_page_url = f"{self.siteUrl}/search?searchValue={encoded_key}&page={page}"
                        next_page_response = self.fetch(next_page_url)
                        next_page_html = next_page_response.text
                        
                        next_page_match = re.search(next_data_pattern, next_page_html, re.DOTALL)
                        if next_page_match:
                            next_page_json = json.loads(next_page_match.group(1))
                            next_page_props = next_page_json.get("props", {}).get("pageProps", {})
                            next_page_books = next_page_props.get("bookList", [])
                            all_book_list.extend(next_page_books)
                
                # 转换为统一的搜索结果格式
                for book in all_book_list:
                    book_id = book.get("bookId", "")
                    book_name = book.get("bookName", "")
                    cover_url = book.get("coverWap", "")
                    total_chapters = book.get("totalChapterNum", "0")
                    status_desc = book.get("statusDesc", "")
                    
                    # 构建视频项
                    vod = {
                        "vod_id": f"/drama/{book_id}",
                        "vod_name": book_name,
                        "vod_pic": cover_url,
                        "vod_remarks": f"{status_desc} {total_chapters}集"
                    }
                    search_results.append(vod)
            
            # 如果未提取到结果，尝试直接从HTML解析
            if not search_results:
                soup = BeautifulSoup(html_content, 'html.parser')
                video_items = soup.select('a[href*="/episode/"]')
                
                for item in video_items:
                    # 提取链接获取ID
                    href = item.get('href', '')
                    match = re.search(r'/episode/(\d+)', href)
                    if not match:
                        continue
                    
                    book_id = match.group(1)
                    
                    # 查找标题
                    title_elem = item.select_one('.title, h3, h2, strong, span, div')
                    title = title_elem.text.strip() if title_elem else "未知标题"
                    
                    # 查找图片
                    img_elem = item.select_one('img')
                    img_url = img_elem.get('src', '') if img_elem else ""
                    
                    # 查找备注信息（集数、状态等）
                    remark_elem = item.select_one('.remark, .status, .episode, span')
                    remark = remark_elem.text.strip() if remark_elem else ""
                    
                    if book_id and title:
                        search_results.append({
                            "vod_id": f"/drama/{book_id}",
                            "vod_name": title,
                            "vod_pic": img_url,
                            "vod_remarks": remark
                        })
        
        except Exception as e:
            print(f"搜索出错: {e}")
        
        result = {
            "list": search_results,
            "page": 1
        }
        print(result)
        return result
    
    def detailContent(self, ids):
        # 获取视频详情和剧集列表
        # 传入的ids是一个列表，取第一个元素作为视频ID
        video_id = ids[0]
        video_url = f"{self.siteUrl}/episode/{video_id}"
        
        try:
            response = self.fetch(video_url)
            html_content = response.text
            
            # 提取NEXT_DATA JSON数据
            next_data_pattern = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
            next_data_match = re.search(next_data_pattern, html_content, re.DOTALL)
            
            if next_data_match:
                next_data_json = json.loads(next_data_match.group(1))
                page_props = next_data_json.get("props", {}).get("pageProps", {})
                
                # 获取书籍基本信息 - 正确的路径是bookInfoVo
                book_info = page_props.get("bookInfoVo", {})
                book_name = book_info.get("bookName", "")
                cover_url = book_info.get("coverWap", "")
                introduction = book_info.get("introduction", "")
                author = book_info.get("author", "")
                actor = book_info.get("actor", "")
                actress = book_info.get("actress", "")
                
                # 获取章节信息
                chapter_list = page_props.get("chapterList", [])
                total_chapters = book_info.get("totalChapterNum", 0)
                
                # 处理分页逻辑 - 河马剧场一页最多显示25集
                chapters_per_page = 25
                total_pages = (int(total_chapters) + chapters_per_page - 1) // chapters_per_page
                
                # 获取所有章节
                all_chapters = []
                all_chapters.extend(chapter_list)
                
                # 如果有多页，获取其他页的章节
                if total_pages > 1:
                    for page in range(2, total_pages + 1):
                        time.sleep(random.uniform(0.5, 1.5))  # 添加随机延迟避免频繁请求
                        next_chapter_url = f"{self.siteUrl}/episode/{video_id}?page={page}"
                        next_chapter_response = self.fetch(next_chapter_url)
                        next_chapter_html = next_chapter_response.text
                        
                        next_chapter_match = re.search(next_data_pattern, next_chapter_html, re.DOTALL)
                        if next_chapter_match:
                            next_chapter_json = json.loads(next_chapter_match.group(1))
                            next_chapter_props = next_chapter_json.get("props", {}).get("pageProps", {})
                            next_chapter_list = next_chapter_props.get("chapterList", [])
                            all_chapters.extend(next_chapter_list)
                
                # 提取MP4视频URL
                play_urls = []
                for chapter in all_chapters:
                    chapter_index = chapter.get("chapterIndex", 0)
                    chapter_name = chapter.get("chapterName", f"第{chapter_index}集")
                    chapter_id = chapter.get("chapterId", "")
                    
                    # 获取章节视频信息 - 视频信息在chapterVideoVo中
                    chapter_video = chapter.get("chapterVideoVo", {})
                    mp4_url = None
                    
                    # 直接从chapterVideoVo获取mp4链接
                    if chapter_video:
                        mp4_url = chapter_video.get("mp4", "")
                    
                    if mp4_url:
                        play_urls.append(f"{chapter_name}${mp4_url}")
                
                # 构建播放列表
                vod_play_from = "河马剧场"
                vod_play_url = "#".join(play_urls)

                # 提取类型标签
                type_tags = []
                if book_info.get("bookTypeThree"):
                    for tag in book_info["bookTypeThree"]:
                        if tag.get("name"):
                            type_tags.append(tag["name"])
                
                # 构建视频信息对象
                vod = {
                    "vod_id": video_id,
                    "vod_name": book_name,
                    "vod_pic": cover_url,
                    "type_name": ",".join(type_tags),
                    "vod_year": "",   # 年份信息可能不可用
                    "vod_area": "中国大陆",   # 大部分是大陆短剧
                    "vod_remarks": f"{total_chapters}集",
                    "vod_actor": f"{actor},{actress}".strip(','),
                    "vod_director": author,
                    "vod_content": introduction,
                    "vod_play_from": vod_play_from,
                    "vod_play_url": vod_play_url
                }
                
                result = {
                    "list": [vod]
                }
                return result
            
            # 如果无法从JSON提取，尝试从HTML中解析基本信息
            else:
                soup = BeautifulSoup(html_content, 'html.parser')
                title_elem = soup.select_one('h1, .title, .drama-title')
                book_name = title_elem.text.strip() if title_elem else "未知剧集"
                
                # 尝试提取图片
                img_elem = soup.select_one('.poster img, .cover img, img')
                cover_url = img_elem.get('src', '') if img_elem else ""
                
                # 尝试提取简介
                intro_elem = soup.select_one('.introduction, .desc, .summary')
                introduction = intro_elem.text.strip() if intro_elem else ""
                
                # 尝试提取演员
                actor_elem = soup.select_one('.actor, .cast')
                actor_text = actor_elem.text.strip() if actor_elem else ""
                
                # 视频默认只有第一集
                result = {
                    "list": [{
                        "vod_id": video_id,
                        "vod_name": book_name,
                        "vod_pic": cover_url,
                        "type_name": "",
                        "vod_year": "",
                        "vod_area": "中国大陆",
                        "vod_remarks": "",
                        "vod_actor": actor_text,
                        "vod_director": "",
                        "vod_content": introduction,
                        "vod_play_from": "河马剧场",
                        "vod_play_url": ""
                    }]
                }
                return result
        
        except Exception as e:
            print(f"获取详情出错: {e}")
        
        return {"list": []}
    
    def playerContent(self, flag, id, vipFlags):
        # 播放器内容获取
        # 直接返回解析好的MP4 URL
        result = {}
        try:
            # id就是我们之前传入的格式: 章节名$视频URL
            parts = id.split('$', 1)
            if len(parts) == 2:
                chapter_name = parts[0]
                video_url = parts[1]
                print(f"解析播放: {chapter_name}, URL: {video_url}")
                
                result = {
                    "parse": 0,      # 不需要解析
                    "playUrl": "",   # 直接播放，不需要前缀
                    "url": video_url, # 直接使用MP4视频URL
                    "header": {      # 请求头
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
                        "Referer": "https://www.kuaikaw.cn/"
                    }
                }
                return result
        except Exception as e:
            print(f"解析播放内容出错: {e}")
        
        # 如果上面的处理失败，直接返回原始URL
        result = {
            "parse": 0, 
            "playUrl": "",
            "url": id,
            "header": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
                "Referer": "https://www.kuaikaw.cn/"
            }
        }
        return result
    
    def isVideoFormat(self, url):
        # 检查是否为视频格式
        video_formats = ['.mp4', '.mkv', '.avi', '.wmv', '.m3u8', '.flv', '.rmvb']
        for format in video_formats:
            if format in url.lower():
                return True
        return False
    
    def localProxy(self, param):
        # 本地代理处理，此处简单返回传入的参数
        return [200, "video/MP2T", {}, param]

def newSpider():
    # 创建爬虫实例的工厂方法
    return Spider() 
