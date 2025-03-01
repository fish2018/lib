#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json
import requests

home = {
"pingtai": [
{ "address":"jsonweishizhibo.txt","xinimg":"http://cdn.gcufbd.top/img/weishi.jpg","Number":"36","title":"\u536B\u89C6\u76F4\u64AD"},
{ "address":"jsonlongzhu.txt","xinimg":"http://cdn.gcufbd.top/img/baobao.png","Number":"0","title":"\u9F99\u73E0"},
{ "address":"jsonyingke.txt","xinimg":"http://cdn.gcufbd.top/img/yingke.jpg","Number":"2","title":"\u6620\u5BA2"},
{ "address":"jsonkawayi.txt","xinimg":"http://cdn.gcufbd.top/img/kawayi.jpg","Number":"87","title":"\u5361\u54C7\u4F0A"},
{ "address":"jsonmihu.txt","xinimg":"http://cdn.gcufbd.top/img/mihu.jpg","Number":"91","title":"\u54AA\u72D0"},
{ "address":"jsonhuahudie.txt","xinimg":"http://cdn.gcufbd.top/img/huahudie.jpg","Number":"107","title":"\u82B1\u8774\u8776"},
{ "address":"jsonmitao.txt","xinimg":"http://cdn.gcufbd.top/img/mitao.jpg","Number":"94","title":"\u871C\u6843"},
{ "address":"jsonfanjiashequ.txt","xinimg":"http://cdn.gcufbd.top/img/fanqie.png","Number":"115","title":"\u756A\u8304\u793E\u533A"},
{ "address":"jsonLOVE.txt","xinimg":"http://cdn.gcufbd.top/img/LOVE.jpg","Number":"110","title":"LOVE"},
{ "address":"jsonxiaodaji.txt","xinimg":"http://cdn.gcufbd.top/img/xiaodaji.jpg","Number":"74","title":"\u5C0F\u59B2\u5DF1"},
{ "address":"json77zhibo.txt","xinimg":"http://cdn.gcufbd.top/img/77.jpg","Number":"98","title":"77\u76F4\u64AD"},
{ "address":"jsonyiyi.txt","xinimg":"http://cdn.gcufbd.top/img/yiyi.jpg","Number":"90","title":"\u4F9D\u4F9D"},
{ "address":"jsonrichu.txt","xinimg":"http://cdn.gcufbd.top/img/richu.jpg","Number":"113","title":"\u65E5\u51FA"},
{ "address":"jsoncaihong.txt","xinimg":"http://cdn.gcufbd.top/img/caihong.jpg","Number":"109","title":"\u5F69\u8679"},
{ "address":"jsonjiujiu.txt","xinimg":"http://cdn.gcufbd.top/img/jiujiu.jpg","Number":"82","title":"\u4E45\u4E45"},
{ "address":"jsonyami.txt","xinimg":"http://cdn.gcufbd.top/img/yami.jpg","Number":"104","title":"\u4E9A\u7C73"},
{ "address":"jsondielian.txt","xinimg":"http://cdn.gcufbd.top/img/dielian.jpg","Number":"113","title":"\u8776\u604B"},
{ "address":"jsonyeyaoji.txt","xinimg":"http://cdn.gcufbd.top/img/yeyaoji.jpg","Number":"89","title":"\u591C\u5996\u59EC"},
{ "address":"jsontaolu.txt","xinimg":"http://cdn.gcufbd.top/img/taolu.jpg","Number":"90","title":"\u5957\u8DEF"},
{ "address":"jsonyinghua.txt","xinimg":"http://cdn.gcufbd.top/img/yinghua.jpg","Number":"70","title":"\u6A31\u82B1"},
{ "address":"jsonxiangse.txt","xinimg":"http://cdn.gcufbd.top/img/xiangse.png","Number":"109","title":"\u4EAB\u8272"},
{ "address":"jsonhonglangman.txt","xinimg":"http://cdn.gcufbd.top/img/hongliangman.jpg","Number":"81","title":"\u7EA2\u6D6A\u6F2B"},
{ "address":"jsonjinyu.txt","xinimg":"http://cdn.gcufbd.top/img/jinyu.jpg","Number":"64","title":"\u91D1\u9C7C"},
{ "address":"jsontaohua.txt","xinimg":"http://cdn.gcufbd.top/img/taohua.png","Number":"73","title":"\u6843\u82B1"},
{ "address":"jsonhuafang.txt","xinimg":"http://cdn.gcufbd.top/img/huahuang.jpg","Number":"79","title":"\u82B1\u623F"},
{ "address":"jsonxiaoxiannu.txt","xinimg":"http://cdn.gcufbd.top/img/xiaoxiannv.jpg","Number":"84","title":"\u5C0F\u4ED9\u5973"},
{ "address":"jsonshijuexiu.txt","xinimg":"http://cdn.gcufbd.top/img/shijuexiu.png","Number":"111","title":"\u89C6\u89C9\u79C0"},
{ "address":"jsonxiaotianshi.txt","xinimg":"http://cdn.gcufbd.top/img/xiaotianshi.jpg","Number":"90","title":"\u5C0F\u5929\u4F7F"},
{ "address":"jsonyizhibo.txt","xinimg":"http://cdn.gcufbd.top/img/yizhibo.jpg","Number":"95","title":"\u4E00\u76F4\u64AD"},
{ "address":"jsoncaiyun.txt","xinimg":"http://cdn.gcufbd.top/img/caiyun.png","Number":"114","title":"\u5F69\u4E91"},
{ "address":"jsonanyu.txt","xinimg":"http://cdn.gcufbd.top/img/anyu.jpg","Number":"89","title":"\u6697\u8BED"},
{ "address":"jsonmimi.txt","xinimg":"http://cdn.gcufbd.top/img/mimi.jpg","Number":"108","title":"\u54AA\u54AA"},
{ "address":"jsonjiaomei.txt","xinimg":"http://cdn.gcufbd.top/img/jiaomei.jpg","Number":"84","title":"\u5A07\u5A9A"},
{ "address":"jsonhuanggua.txt","xinimg":"http://cdn.gcufbd.top/img/huagngua.jpg","Number":"78","title":"\u9EC4\u74DC"},
{ "address":"jsonsequ.txt","xinimg":"http://cdn.gcufbd.top/img/sequ.jpg","Number":"98","title":"\u8272\u8DA3"},
{ "address":"jsonnuomi.txt","xinimg":"http://cdn.gcufbd.top/img/nuomi.jpg","Number":"66","title":"\u7CEF\u7C73"},
{ "address":"jsonxiaomifeng.txt","xinimg":"http://cdn.gcufbd.top/img/xiaomifeng.jpg","Number":"89","title":"\u5C0F\u871C\u8702"},
{ "address":"jsonxiaohongmao.txt","xinimg":"http://cdn.gcufbd.top/img/xiaohongmao.jpg","Number":"104","title":"\u5C0F\u7EA2\u5E3D"},
{ "address":"jsontaohuayun.txt","xinimg":"http://cdn.gcufbd.top/img/taohuayun.jpg","Number":"95","title":"\u6843\u82B1\u8FD0"},
{ "address":"jsonkugua.txt","xinimg":"http://cdn.gcufbd.top/img/kugua2.png","Number":"118","title":"\u82E6\u74DC"},
{ "address":"jsonaiaini.txt","xinimg":"http://cdn.gcufbd.top/img/aiaini.jpg","Number":"106","title":"\u7231\u7231\u4F60"},
{ "address":"jsonyinghuayui.txt","xinimg":"http://cdn.gcufbd.top/img/yinghuayu.jpg","Number":"108","title":"\u6A31\u82B1\u96E8i"},
{ "address":"jsonpanta.txt","xinimg":"http://cdn.gcufbd.top/img/panta.jpg","Number":"71","title":"\u76D8\u4ED6"},
{ "address":"jsonyese.txt","xinimg":"http://cdn.gcufbd.top/img/yese.jpg","Number":"91","title":"\u591C\u8272"},
{ "address":"jsonhudie.txt","xinimg":"http://cdn.gcufbd.top/img/hudie.png","Number":"70","title":"\u8774\u8776"},
{ "address":"jsonxiaotianxian.txt","xinimg":"http://cdn.gcufbd.top/img/xiaotianxian2.png","Number":"68","title":"\u5C0F\u5929\u4ED9"},
{ "address":"jsonxingqu.txt","xinimg":"http://cdn.gcufbd.top/img/xingqu.jpg","Number":"110","title":"\u674F\u8DA3"},
{ "address":"jsonxiaohuaidan.txt","xinimg":"http://cdn.gcufbd.top/img/xiaohuaidao.jpg","Number":"90","title":"\u5C0F\u574F\u86CB"},
{ "address":"jsonpiaoxue.txt","xinimg":"http://cdn.gcufbd.top/img/piaoxue.png","Number":"74","title":"\u98D8\u96EA"},
{ "address":"jsonyingtao.txt","xinimg":"http://cdn.gcufbd.top/img/yingtao.jpg","Number":"84","title":"\u6A31\u6843"},
{ "address":"jsonaosika.txt","xinimg":"http://cdn.gcufbd.top/img/aosika.jpg","Number":"99","title":"\u5965\u65AF\u5361"},
{ "address":"jsonkaluli.txt","xinimg":"http://cdn.gcufbd.top/img/kaluli.jpg","Number":"74","title":"\u5361\u8DEF\u91CC"},
{ "address":"jsonhonggaoliang.txt","xinimg":"http://cdn.gcufbd.top/img/honggaoliang.png","Number":"74","title":"\u7EA2\u9AD8\u7CB1"},
{ "address":"jsonfubao.txt","xinimg":"http://cdn.gcufbd.top/img/fubao.jpg","Number":"127","title":"\u4ED8\u5B9D"},
{ "address":"jsonxiaohuangshu.txt","xinimg":"http://cdn.gcufbd.top/img/xiaohuangshu.png","Number":"70","title":"\u5C0F\u9EC4\u4E66"},
{ "address":"jsonersao.txt","xinimg":"http://cdn.gcufbd.top/img/ersao.jpg","Number":"79","title":"\u4E8C\u5AC2"},
{ "address":"jsonhuaguoshan.txt","xinimg":"http://cdn.gcufbd.top/img/huaguoshan.png","Number":"95","title":"\u82B1\u679C\u5C71"},
{ "address":"jsonyunlu.txt","xinimg":"http://cdn.gcufbd.top/img/yunlu.jpg","Number":"80","title":"\u4E91\u9E7F"},
{ "address":"jsonboluo.txt","xinimg":"http://cdn.gcufbd.top/img/boluo.jpg","Number":"105","title":"\u83E0\u841D"},
{ "address":"jsonxingbaobei.txt","xinimg":"http://cdn.gcufbd.top/img/xingbaobei.jpg","Number":"73","title":"\u661F\u5B9D\u8D1D"},
{ "address":"jsonyeyan.txt","xinimg":"http://cdn.gcufbd.top/img/yeyan.jpg","Number":"105","title":"\u591C\u8273"},
{ "address":"jsonqixiannus.txt","xinimg":"http://cdn.gcufbd.top/img/qixiannv.jpg","Number":"63","title":"\u4E03\u4ED9\u5973s"},
{ "address":"jsonyelaixiang.txt","xinimg":"http://cdn.gcufbd.top/img/yelaixiang.jpg","Number":"12","title":"\u591C\u6765\u9999"},
{ "address":"jsonailing.txt","xinimg":"http://cdn.gcufbd.top/img/20.jpg","Number":"88","title":"\u7231\u96F6"},
{ "address":"jsonshibajin.txt","xinimg":"http://cdn.gcufbd.top/img/shibajing.jpg","Number":"109","title":"\u5341\u516B\u7981"},
{ "address":"jsonlanguifang.txt","xinimg":"http://cdn.gcufbd.top/img/languifan.jpg","Number":"81","title":"\u5170\u6842\u574A"},
{ "address":"jsonDancelife.txt","xinimg":"http://cdn.gcufbd.top/img/Dancelife.jpg","Number":"101","title":"Dancelife"},
{ "address":"jsonxiaomengzhu.txt","xinimg":"http://cdn.gcufbd.top/img/xiaomengzhu.png","Number":"90","title":"\u5C0F\u840C\u732A"},
{ "address":"jsonhudiefei.txt","xinimg":"http://cdn.gcufbd.top/img/hudiefei.jpg","Number":"114","title":"\u8774\u8776\u98DE"},
{ "address":"jsonyoumeng.txt","xinimg":"http://cdn.gcufbd.top/img/youmeng.jpg","Number":"74","title":"\u5E7D\u68A6"},
{ "address":"jsonliguiting.txt","xinimg":"http://cdn.gcufbd.top/img/liguiting.jpg","Number":"86","title":"\u4E3D\u67DC\u5385"},
{ "address":"jsonjiaolong.txt","xinimg":"http://cdn.gcufbd.top/img/jiaolong.jpg","Number":"99","title":"\u86DF\u9F99"},
{ "address":"jsonyanruyu.txt","xinimg":"http://cdn.gcufbd.top/img/yanruyu.jpg","Number":"87","title":"\u989C\u5982\u7389"},
{ "address":"jsonchengxiu.txt","xinimg":"http://cdn.gcufbd.top/img/chengxiu.jpg","Number":"71","title":"\u6A59\u79C0"},
{ "address":"jsonbaoyul.txt","xinimg":"http://cdn.gcufbd.top/img/baoyu.jpg","Number":"114","title":"\u8C79\u5A31l"},
{ "address":"jsonxiaohualuo.txt","xinimg":"http://cdn.gcufbd.top/img/xiaohualuo.jpg","Number":"85","title":"\u5C0F\u82B1\u87BA"},
{ "address":"jsonhuanghou.txt","xinimg":"http://cdn.gcufbd.top/img/huanghou.png","Number":"65","title":"\u7687\u540E"},
{ "address":"jsonxinzhilian.txt","xinimg":"http://cdn.gcufbd.top/img/xinzhilian.jpg","Number":"67","title":"\u5FC3\u4E4B\u604B"},
{ "address":"jsonoumeiFEATURED.txt","xinimg":"http://cdn.gcufbd.top/img/ouTRANS.jpg","Number":"91","title":"\u6B27\u7F8EFEATURED"},
{ "address":"jsonoumeiFEMALE.txt","xinimg":"http://cdn.gcufbd.top/img/ouTRANS.jpg","Number":"89","title":"\u6B27\u7F8EFEMALE"},
{ "address":"jsonoumeiMALE.txt","xinimg":"http://cdn.gcufbd.top/img/ouTRANS.jpg","Number":"91","title":"\u6B27\u7F8EMALE"},
{ "address":"jsonoumeiCOUPLE.txt","xinimg":"http://cdn.gcufbd.top/img/ouTRANS.jpg","Number":"89","title":"\u6B27\u7F8ECOUPLE"},
{ "address":"jsonoumeiTRANS.txt","xinimg":"http://cdn.gcufbd.top/img/ouTRANS.jpg","Number":"88","title":"\u6B27\u7F8ETRANS"},
{ "address":"jsontaimeil.txt","xinimg":"http://cdn.gcufbd.top/img/taimei.jpg","Number":"80","title":"\u53F0\u59B9l"},
{ "address":"jsonailian.txt","xinimg":"http://cdn.gcufbd.top/img/ailian.jpg","Number":"79","title":"\u7231\u604B"},
{ "address":"json903yule.txt","xinimg":"http://cdn.gcufbd.top/img/903.jpg","Number":"71","title":"903\u5A31\u4E50"},
{ "address":"jsonjiuweihu.txt","xinimg":"http://cdn.gcufbd.top/img/jiuweihu.jpg","Number":"0","title":"\u4E5D\u5C3E\u72D0"},
{ "address":"jsonyouwudao.txt","xinimg":"http://cdn.gcufbd.top/img/youwudao.jpg","Number":"91","title":"\u5C24\u7269\u5C9B"},
{ "address":"jsontanke.txt","xinimg":"http://cdn.gcufbd.top/img/tanke.png","Number":"94","title":"\u5766\u514B"},
{ "address":"jsonhaojiyou.txt","xinimg":"http://cdn.gcufbd.top/img/haojiyou.jpg","Number":"72","title":"\u597D\u57FA\u53CB"},
{ "address":"jsonyenulang.txt","xinimg":"http://cdn.gcufbd.top/img/yenvlang.jpg","Number":"112","title":"\u591C\u5973\u90CE"},
{ "address":"jsonjiaochuan.txt","xinimg":"http://cdn.gcufbd.top/img/jiaochuan.jpg","Number":"69","title":"\u5A07\u5598"},
{ "address":"jsonmangguopai.txt","xinimg":"http://cdn.gcufbd.top/img/magnguopai.jpg","Number":"118","title":"\u8292\u679C\u6D3E"},
{ "address":"jsonmeiyan.txt","xinimg":"http://cdn.gcufbd.top/img/meiyan'.jpg","Number":"95","title":"\u5A9A\u989C"},
{ "address":"jsonfengliu.txt","xinimg":"http://cdn.gcufbd.top/img/fengliu.jpg","Number":"0","title":"\u98CE\u6D41"},
{ "address":"jsonyelu.txt","xinimg":"http://cdn.gcufbd.top/img/yelu.jpg","Number":"93","title":"\u591C\u5F8B"},
{ "address":"jsonlinglong.txt","xinimg":"http://cdn.gcufbd.top/img/linglong.jpg","Number":"16","title":"\u73B2\u73D1"},
{ "address":"jsonyuhuo.txt","xinimg":"http://cdn.gcufbd.top/img/yuhuo.jpg","Number":"0","title":"\u6D74\u706B"},
{ "address":"jsoncuiniao.txt","xinimg":"http://cdn.gcufbd.top/img/cuiniao.jpg","Number":"90","title":"\u7FE0\u9E1F"},
{ "address":"jsonxingyunxing.txt","xinimg":"http://cdn.gcufbd.top/img/xingyunxin.jpg","Number":"0","title":"\u5E78\u8FD0\u661F"},
{ "address":"jsontaxiu.txt","xinimg":"http://cdn.gcufbd.top/img/taxiu.jpg","Number":"111","title":"\u5979\u79C0"},
{ "address":"jsonzhaocaimao.txt","xinimg":"http://cdn.gcufbd.top/img/zhaocaimao.jpg","Number":"90","title":"\u62DB\u8D22\u732B"},
{ "address":"jsonshuangdie.txt","xinimg":"http://cdn.gcufbd.top/img/shuangdie.jpg","Number":"106","title":"\u53CC\u789F"},
{ "address":"jsontangguo.txt","xinimg":"http://cdn.gcufbd.top/img/tangguo.jpg","Number":"0","title":"\u7CD6\u679C"},
{ "address":"jsonmemeda.txt","xinimg":"http://cdn.gcufbd.top/img/memeda.jpg","Number":"66","title":"\u4E48\u4E48\u54D2"},
{ "address":"jsonxiaoxinggan.txt","xinimg":"http://cdn.gcufbd.top/img/xiaoxinggan.jpg","Number":"80","title":"\u5C0F\u6027\u611F"},
{ "address":"jsonxiaomiaochong.txt","xinimg":"http://cdn.gcufbd.top/img/xiaomaochong.jpg","Number":"104","title":"\u5C0F\u55B5\u5BA0"},
{ "address":"jsontunulang.txt","xinimg":"http://cdn.gcufbd.top/img/tunvlang.jpg","Number":"86","title":"\u5154\u5973\u90CE"},
{ "address":"jsonshuimeiren.txt","xinimg":"http://cdn.gcufbd.top/img/shuimeiren.jpg","Number":"88","title":"\u7761\u7F8E\u4EBA"},
{ "address":"jsonjinbei.txt","xinimg":"http://cdn.gcufbd.top/img/jinbei.jpg","Number":"94","title":"\u91D1\u5457"},
{ "address":"jsonmeixi.txt","xinimg":"http://cdn.gcufbd.top/img/meixi.jpg","Number":"72","title":"\u7F8E\u5915"},
{ "address":"jsonxiaoyao.txt","xinimg":"http://cdn.gcufbd.top/img/xiaoyao.jpg","Number":"97","title":"\u5C0F\u5996"},
{ "address":"jsonyuezhibo.txt","xinimg":"http://cdn.gcufbd.top/img/yuezhibo.jpg","Number":"91","title":"\u7EA6\u76F4\u64AD"},
{ "address":"jsonhuaxianzi.txt","xinimg":"http://cdn.gcufbd.top/img/huaxianzi.jpg","Number":"102","title":"\u82B1\u4ED9\u5B50"},
{ "address":"jsontuhao.txt","xinimg":"http://cdn.gcufbd.top/img/tuhao.jpg","Number":"0","title":"\u571F\u8C6A"},
{ "address":"jsonhongzhuang.txt","xinimg":"http://cdn.gcufbd.top/img/hongzhuang.jpg","Number":"105","title":"\u7EA2\u5986"},
{ "address":"jsonniuniu.txt","xinimg":"http://cdn.gcufbd.top/img/niuniu.jpg","Number":"93","title":"\u599E\u599E"},
{ "address":"jsonyanhou.txt","xinimg":"http://cdn.gcufbd.top/img/yanhou.png","Number":"82","title":"\u8273\u540E"},
{ "address":"jsonmoon.txt","xinimg":"http://cdn.gcufbd.top/img/moon.jpg","Number":"61","title":"moon"},
{ "address":"jsonlanmao.txt","xinimg":"http://cdn.gcufbd.top/img/lanmao.jpg","Number":"102","title":"\u84DD\u732B"},
{ "address":"jsonmeirenzhuang.txt","xinimg":"http://cdn.gcufbd.top/img/meirenzhuang.jpg","Number":"90","title":"\u7F8E\u4EBA\u5986"},
{ "address":"jsonruxiang.txt","xinimg":"http://cdn.gcufbd.top/img/ruxiang.jpg","Number":"87","title":"\u5165\u5DF7"},
{ "address":"jsonchijiunan.txt","xinimg":"http://cdn.gcufbd.top/img/chijiunan.jpg","Number":"102","title":"\u6301\u4E45\u7537"},
{ "address":"jsonqingxin.txt","xinimg":"http://cdn.gcufbd.top/img/qingxin.jpg","Number":"75","title":"\u503E\u5FC3"},
{ "address":"jsonxiaojingling.txt","xinimg":"http://cdn.gcufbd.top/img/xiaojingling.jpg","Number":"110","title":"\u5C0F\u7CBE\u7075"},
{ "address":"jsonouyu.txt","xinimg":"http://cdn.gcufbd.top/img/ouyu.jpg","Number":"74","title":"\u5076\u9047"},
{ "address":"jsonhuihui.txt","xinimg":"http://cdn.gcufbd.top/img/huihui.jpg","Number":"117","title":"\u7070\u7070"},
{ "address":"jsonmaotouying.txt","xinimg":"http://cdn.gcufbd.top/img/maotouying.jpg","Number":"97","title":"\u732B\u5934\u9E70"},
{ "address":"jsonxihuanni.txt","xinimg":"http://cdn.gcufbd.top/img/xihuanni.jpg","Number":"76","title":"\u559C\u6B22\u4F60"},
{ "address":"jsonyechun.txt","xinimg":"http://cdn.gcufbd.top/img/yechun.jpg","Number":"122","title":"\u591C\u7EAF"},
{ "address":"jsonxingbo.txt","xinimg":"http://cdn.gcufbd.top/img/xingbo.jpg","Number":"70","title":"\u674F\u64AD"},
{ "address":"jsonmingliu.txt","xinimg":"http://cdn.gcufbd.top/img/mingliu.jpg","Number":"104","title":"\u540D\u6D41"},
{ "address":"jsonxiaolajiao.txt","xinimg":"http://cdn.gcufbd.top/img/xiaolajiao.jpg","Number":"83","title":"\u5C0F\u8FA3\u6912"},
{ "address":"jsonwenxiangshe.txt","xinimg":"http://cdn.gcufbd.top/img/weixiangshe.jpg","Number":"88","title":"\u868A\u9999\u793E"},
{ "address":"jsonqianshou.txt","xinimg":"http://cdn.gcufbd.top/img/qianshou.jpg","Number":"87","title":"\u7275\u624B"},
{ "address":"jsonqingqu.txt","xinimg":"http://cdn.gcufbd.top/img/qingqu.jpg","Number":"95","title":"\u60C5\u8DA3"}
]
}



class Spider(Spider):
	def init(self,extend=""):
		self.base_url='http://api.hclyz.com:81/mf'
		# self.data = self.fetch(f'{self.base_url}/json.txt').json()

	def homeContent(self,filter):
		# self.base_url = 'http://api.hclyz.com:81/mf'
		# res = requests.get(f'{self.base_url}/json.txt')
		# data = json.loads(res.text)
		# pingtai = data["pingtai"]
		# classes = [{"type_name": p["title"],"type_id":"/"+p["address"]} for p in pingtai]
		classes = [{"type_name": "pingtai","type_id":"/json.txt"}]
		result = {"class": classes}
		return result
	def homeVideoContent(self):
		# res = requests.get(f'{self.base_url}/json.txt')
		# data = json.loads(res.text)
		# vods = [{"vod_id":"/"+item['address'],"vod_name": item['title'],"vod_pic": item['xinimg'].replace("http://cdn.gcufbd.top/img/", "https://slink.ltd/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/"),"vod_remarks": item['Number']} for item in data]
		# result = {'list': vods}
		result = {
			"list": {
				"vod_id": "/jsonLOVE.txt",
				"vod_name": "Love",
				"vod_pic": "https://slink.ltd/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/LOVE.jpg",
				"vod_remarks": 110
			}
		}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		res = requests.get(f'{self.base_url}/json.txt')
		# res = self.fetch(f'{self.base_url}/json.txt')
		data = json.loads(res.text)
		# data = res.json()
		data = home.get("pingtai")
		videos = [
			{
				"vod_id":"/"+item['address'],
				"vod_name": item['title'],
				"vod_pic": item['xinimg'].replace("http://cdn.gcufbd.top/img/", "https://slink.ltd/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/"),
				# "vod_remarks": item['Number'],
				"vod_remarks": 120,
				"style": {"type": "rect", "ratio": 1.33}
			} for item in data]
		result = {
			"page": pg,
			"pagecount": 9999,
			"limit": 99,
			"total": 9999,
			"list": videos
		}
		return result
	def detailContent(self,array):
		id = array[0]
		data = self.fetch(f'{self.base_url}/{id}').json()
		zhubo = data['zhubo']
		playUrls = '#'.join([f"{vod['title']}${vod['address']}" for vod in zhubo])
		vod = [{
			"vod_play_from": 'Leospring',
			"vod_play_url": playUrls,
			"vod_content": 'github.com/fish2018',
		}]
		result = {"list": vod}
		return result
	def playerContent(self,flag,id,vipFlags):
		result = {
			'parse': 0,
			'url': id
		}
		return result
	def getName(self):
		return 'pingtai'
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def searchContent(self,key,quick):
		result = {}
		return result
	def destroy(self):
		pass
	def localProxy(self, param):
		pass
