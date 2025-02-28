#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json

class Spider(Spider):
	def init(self,extend=""):
		self.base_url='http://api.hclyz.com:81/mf'
		self.data = self.fetch(f'{self.base_url}/json.txt').json()

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-full-version': '"133.0.6943.98"',
		'sec-ch-ua-arch': '"x86"',
		'sec-ch-ua-platform': '"Windows"',
		'sec-ch-ua-platform-version': '"19.0.0"',
		'sec-ch-ua-model': '""',
		'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.98", "Chromium";v="133.0.6943.98"',
		'dnt': '1',
		'upgrade-insecure-requests': '1',
		'sec-fetch-site': 'none',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-user': '?1',
		'sec-fetch-dest': 'document',
		'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
		'priority': 'u=0, i'
	}
	
	def homeContent(self,filter):
		pingtai = self.data["pingtai"]
		classes = [{"type_name": p["title"],"type_id":p["address"]} for p in pingtai]
		result = {"class": classes}
		return result
	def homeVideoContent(self):
		data = self.fetch(f'{self.base_url}/jsonLOVE.txt').json()
		vods = [{"vod_id":item['address'],"vod_name": item['title'],"vod_pic": item['xinimg'].replace("http://cdn.gcufbd.top/img/", "https://slink.ltd/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/"),"vod_remarks": item['Number']} for item in data]
		result = {'list': vods}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		data = self.fetch(f'{self.base_url}/{tid}').json()
		videos = [{"vod_id": item['address'], "vod_name": item['title'],
				 "vod_pic": item['xinimg'].replace("http://cdn.gcufbd.top/img/",
												   "https://slink.ltd/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/"),
				 "vod_remarks": item['Number'],
				 "style": {"type": "rect", "ratio": 1.33}} for item in data]
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
		pass
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
