#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json
import requests

class Spider(Spider):
	def init(self,extend=""):
		pass
		# self.base_url='http://api.hclyz.com:81/mf'
		# self.data = self.fetch(f'{self.base_url}/json.txt').json()

	def homeContent(self,filter):
		self.base_url = 'http://api.hclyz.com:81/mf'
		res = requests.get(f'{self.base_url}/json.txt')
		data = json.loads(res.text)
		pingtai = data["pingtai"]
		classes = [{"type_name": p["title"],"type_id":"/"+p["address"]} for p in pingtai]
		classes = [{"type_name": "pingtai","type_id":"/json.txt"}]
		result = {"class": classes}
		return result
	def homeVideoContent(self):
		res = requests.get(f'{self.base_url}/json.txt')
		data = json.loads(res.text)
		vods = [{"vod_id":"/"+item['address'],"vod_name": item['title'],"vod_pic": item['xinimg'].replace("http://cdn.gcufbd.top/img/", "https://slink.ltd/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/"),"vod_remarks": item['Number']} for item in data]
		result = {'list': vods}
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
