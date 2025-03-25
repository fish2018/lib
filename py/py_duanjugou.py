#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
from urllib.parse import quote_plus, urljoin
import urllib.parse
import re
from bs4 import BeautifulSoup
import time

from spider import Spider

class Duanjugou(Spider):
    def __init__(self):
        super().__init__()
        self.siteUrl = 'https://duanjugou.top'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    
    def homeContent(self, filter):
        result = {}
        
        # 标签分类
        cateManual = {
            "最新内容": "latest",
            "24小时热门": "hot-day",
            "1周热门": "hot-week",
            "女性标签": "tag-female",
            "男性标签": "tag-male",
            "场景职业": "tag-scene",
            "爽设标签": "tag-power",
            "单字标签": "tag-single"
        }
        
        classes = []
        for k in cateManual:
            classes.append({
                'type_id': cateManual[k],
                'type_name': k
            })
        
        result['class'] = classes
        
        if filter:
            # 定义过滤器
            result['filters'] = {
                # 女性标签过滤器
                "tag-female": [
                    {
                        "key": "tag", 
                        "name": "标签",
                        "value": [
                            {"n": "全部", "v": ""},
                            {"n": "娇妻", "v": "娇妻"},
                            {"n": "阿姨", "v": "阿姨"},
                            {"n": "夫人", "v": "夫人"},
                            {"n": "女友", "v": "女友"},
                            {"n": "老婆", "v": "老婆"},
                            {"n": "前妻", "v": "前妻"},
                            {"n": "千金", "v": "千金"},
                            {"n": "公主", "v": "公主"},
                            {"n": "宠妻", "v": "宠妻"},
                            {"n": "女王", "v": "女王"},
                            {"n": "女神", "v": "女神"},
                            {"n": "甜妻", "v": "甜妻"},
                            {"n": "萌宝", "v": "萌宝"},
                            {"n": "妈咪", "v": "妈咪"}
                        ]
                    }
                ],
                # 男性标签过滤器
                "tag-male": [
                    {
                        "key": "tag", 
                        "name": "标签",
                        "value": [
                            {"n": "全部", "v": ""},
                            {"n": "少爷", "v": "少爷"},
                            {"n": "王爷", "v": "王爷"},
                            {"n": "男友", "v": "男友"},
                            {"n": "狂少", "v": "狂少"},
                            {"n": "老公", "v": "老公"},
                            {"n": "前夫", "v": "前夫"},
                            {"n": "龙帅", "v": "龙帅"},
                            {"n": "赘婿", "v": "赘婿"},
                            {"n": "爸爸", "v": "爸爸"},
                            {"n": "爹地", "v": "爹地"},
                            {"n": "陛下", "v": "陛下"}
                        ]
                    }
                ],
                # 其他分类也可以添加类似的过滤器
            }
        
        return result
        
    def homeVideoContent(self):
        url = self.siteUrl
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                return []
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 获取首页推荐的视频列表
            videos = []
            items = soup.select('div:has(a:has(time))')  # 根据网页结构选择短剧条目
            
            for item in items[:12]:  # 仅获取前12个
                title_elem = item.select_one('a')
                if not title_elem:
                    continue
                
                title = title_elem.text.strip()
                if not title.startswith('[短剧]'):
                    continue
                
                title = title.replace('[短剧]', '').strip()
                
                # 提取集数信息
                episode_match = re.search(r'（(\d+)集）', title)
                episode_count = ''
                if episode_match:
                    episode_count = episode_match.group(1) + '集'
                
                link = title_elem.get('href')
                if not link:
                    link = ''
                else:
                    link = urljoin(self.siteUrl, link)
                
                video_id = link  # 使用链接作为视频ID
                
                # 由于没有直接的图片，使用默认图标
                img = "https://duanjugou.top/favicon.ico"
                
                videos.append({
                    "vod_id": video_id,
                    "vod_name": title,
                    "vod_pic": img,
                    "vod_remarks": episode_count
                })
            
            return videos
        except Exception as e:
            print(f"获取首页视频异常: {str(e)}")
            return []
    
    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        
        url = self.siteUrl
        if pg != '1':  # 分页处理
            url = f"{self.siteUrl}/page/{pg}"
        
        if tid == 'latest':
            # 最新内容
            pass  # 默认就是最新内容
        elif tid == 'hot-day':
            # 24小时热门
            url = f"{self.siteUrl}/?order=hot-day"
        elif tid == 'hot-week':
            # 一周热门
            url = f"{self.siteUrl}/?order=hot-week"
        elif tid.startswith('tag-'):
            # 标签过滤
            tag_category = tid.split('-')[1]
            search_tag = ""
            
            if extend and 'tag' in extend:
                search_tag = extend['tag']
            
            if search_tag:
                url = f"{self.siteUrl}/search?q={quote_plus(search_tag)}"
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                return result
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            videos = []
            items = soup.select('div:has(a:has(time))')  # 根据网页结构选择短剧条目
            
            for item in items:
                title_elem = item.select_one('a')
                if not title_elem:
                    continue
                
                title = title_elem.text.strip()
                if not title.startswith('[短剧]'):
                    continue
                
                title = title.replace('[短剧]', '').strip()
                
                # 提取集数信息
                episode_match = re.search(r'（(\d+)集）', title)
                episode_count = ''
                if episode_match:
                    episode_count = episode_match.group(1) + '集'
                
                link = title_elem.get('href')
                if not link:
                    link = ''
                else:
                    link = urljoin(self.siteUrl, link)
                
                video_id = link  # 使用链接作为视频ID
                
                # 由于没有直接的图片，使用默认图标
                img = "https://duanjugou.top/favicon.ico"
                
                videos.append({
                    "vod_id": video_id,
                    "vod_name": title,
                    "vod_pic": img,
                    "vod_remarks": episode_count
                })
            
            # 判断是否有下一页
            next_page = soup.select_one('a.next')
            
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 999 if next_page else int(pg)
            result['limit'] = 90
            result['total'] = 999999
            
            return result
        except Exception as e:
            print(f"获取分类内容异常: {str(e)}")
            return result
    
    def detailContent(self, ids):
        video_id = ids[0]  # 视频页面URL
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl
        }
        
        try:
            response = requests.get(video_id, headers=headers, timeout=10)
            if response.status_code != 200:
                return {}
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 获取标题
            title_elem = soup.select_one('h1.entry-title')
            if not title_elem:
                return {}
                
            title = title_elem.text.strip()
            title = title.replace('[短剧]', '').strip()
            
            # 获取内容描述（如果有的话）
            content_elem = soup.select_one('div.entry-content')
            desc = ""
            if content_elem:
                desc = content_elem.text.strip()
            
            # 获取网盘链接（如果有的话）
            pan_links = []
            link_elems = soup.select('a[href*="pan.baidu.com"]')
            
            for link in link_elems:
                link_text = link.text.strip() or "百度网盘"
                link_url = link['href']
                pan_links.append(f"{link_text}${link_url}")
            
            # 如果没有找到网盘链接，使用分享文本
            if not pan_links:
                share_text = "请在浏览器中打开并复制网盘链接"
                pan_links.append(f"{share_text}${video_id}")
            
            # 封装为标准格式
            vod = {
                "vod_id": video_id,
                "vod_name": title,
                "vod_pic": "https://duanjugou.top/favicon.ico",
                "type_name": "短剧",
                "vod_year": time.strftime("%Y", time.localtime()),
                "vod_area": "中国大陆",
                "vod_remarks": "",
                "vod_actor": "",
                "vod_director": "",
                "vod_content": desc,
                "vod_play_from": "网盘",
                "vod_play_url": "#".join(pan_links)
            }
            
            result = {
                'list': [vod]
            }
            return result
        except Exception as e:
            print(f"获取详情页异常: {str(e)}")
            return {}
    
    def searchContent(self, key, quick):
        search_url = f"{self.siteUrl}/search?q={quote_plus(key)}"
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl
        }
        
        try:
            response = requests.get(search_url, headers=headers, timeout=10)
            if response.status_code != 200:
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            videos = []
            items = soup.select('div:has(a:has(time))')  # 根据网页结构选择短剧条目
            
            for item in items:
                title_elem = item.select_one('a')
                if not title_elem:
                    continue
                
                title = title_elem.text.strip()
                if not title.startswith('[短剧]'):
                    continue
                
                title = title.replace('[短剧]', '').strip()
                
                # 提取集数信息
                episode_match = re.search(r'（(\d+)集）', title)
                episode_count = ''
                if episode_match:
                    episode_count = episode_match.group(1) + '集'
                
                link = title_elem.get('href')
                if not link:
                    link = ''
                else:
                    link = urljoin(self.siteUrl, link)
                
                video_id = link  # 使用链接作为视频ID
                
                # 由于没有直接的图片，使用默认图标
                img = "https://duanjugou.top/favicon.ico"
                
                videos.append({
                    "vod_id": video_id,
                    "vod_name": title,
                    "vod_pic": img,
                    "vod_remarks": episode_count
                })
            
            return videos
        except Exception as e:
            print(f"搜索异常: {str(e)}")
            return []
    
    def playerContent(self, flag, id, vipFlags):
        # 对于网盘链接，直接返回原始链接让用户在浏览器中打开
        result = {
            'parse': 0,
            'playUrl': '',
            'url': id,
            'header': {
                "User-Agent": self.userAgent
            }
        }
        
        return result
    
    def isVideoFormat(self, url):
        # 对于网盘链接，不是直接的视频格式
        return False
    
    def manualVideoCheck(self):
        # 不需要手动检查
        return False
    
    def localProxy(self, param):
        # 当前场景不需要本地代理
        return None 