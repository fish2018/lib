#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json

class Spider(Spider):
	def init(self,extend=""):
		self.base_url='http://api.hclyz.com:81/mf/'
		self.data = self.fetch(f'{self.base_url}/json.txt').json()
	def getName(self):
		return "色播平台"
	def homeContent(self,filter):
		pingtai = self.data["pingtai"]
		classes = [{"tpye_name": p["title"],"type_id":p["address"]} for p in pingtai]
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
		result = {}
		return result
	def playerContent(self,flag,id,vipFlags):
		result = {}
		return result
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def searchContent(self,key,quick):
		result = {}
		return result
