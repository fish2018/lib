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
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
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
    
    def debugPrint(self, msg, data=None):
        """辅助调试函数，打印信息"""
        try:
            print(f"【短剧狗爬虫调试】: {msg}")
            if data:
                if isinstance(data, str):
                    print(f"数据: {data[:200]}{'...' if len(data) > 200 else ''}")
                else:
                    print(f"数据: {data}")
        except:
            pass
        
    def homeVideoContent(self):
        url = self.siteUrl
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache"
        }
        
        try:
            self.debugPrint(f"正在请求首页: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                self.debugPrint(f"请求失败，状态码: {response.status_code}")
                return []
            
            html_content = response.text
            self.debugPrint(f"获取到HTML内容，长度: {len(html_content)}")
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 获取首页推荐的视频列表，尝试多种选择器
            videos = []
            
            # 方法1: 直接查找所有包含[短剧]的链接
            items = soup.find_all('a')
            
            self.debugPrint(f"找到的链接数量: {len(items)}")
            
            for item in items:
                try:
                    title = item.text.strip()
                    if not '[短剧]' in title:
                        continue
                    
                    self.debugPrint(f"找到短剧链接: {title}")
                    
                    title = title.replace('[短剧]', '').strip()
                    
                    # 提取集数信息
                    episode_match = re.search(r'（(\d+)集）', title)
                    episode_count = ''
                    if episode_match:
                        episode_count = episode_match.group(1) + '集'
                    
                    link = item.get('href')
                    if not link:
                        continue
                    
                    if not link.startswith('http'):
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
                    
                    if len(videos) >= 20:  # 限制数量
                        break
                except Exception as e:
                    self.debugPrint(f"处理单个短剧时出错: {str(e)}")
                    continue
            
            # 如果方法1失败，尝试方法2：查找列表项
            if not videos:
                self.debugPrint("方法1未找到短剧，尝试方法2")
                
                # 尝试找到内容列表
                content_lists = soup.find_all(['ul', 'ol', 'div'], class_=lambda x: x and ('list' in x.lower() or 'content' in x.lower()))
                
                for content_list in content_lists:
                    links = content_list.find_all('a')
                    for link in links:
                        try:
                            title = link.text.strip()
                            if not title or len(title) < 2:
                                continue
                                
                            # 如果不是短剧但有明显的标题特征也收录
                            title_clean = title
                            if '[短剧]' in title:
                                title_clean = title.replace('[短剧]', '').strip()
                            
                            # 提取集数信息
                            episode_match = re.search(r'（(\d+)集）', title_clean)
                            episode_count = ''
                            if episode_match:
                                episode_count = episode_match.group(1) + '集'
                            
                            link_url = link.get('href')
                            if not link_url:
                                continue
                                
                            if not link_url.startswith('http'):
                                link_url = urljoin(self.siteUrl, link_url)
                            
                            # 由于没有直接的图片，使用默认图标
                            img = "https://duanjugou.top/favicon.ico"
                            
                            videos.append({
                                "vod_id": link_url,
                                "vod_name": title_clean,
                                "vod_pic": img,
                                "vod_remarks": episode_count
                            })
                            
                            if len(videos) >= 20:  # 限制数量
                                break
                        except Exception as e:
                            continue
                    
                    if videos:  # 如果找到了视频，就不继续查找其他列表了
                        break
            
            self.debugPrint(f"最终找到的视频数量: {len(videos)}")
            return videos
        except Exception as e:
            self.debugPrint(f"获取首页视频异常: {str(e)}")
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
            "Referer": self.siteUrl,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache"
        }
        
        try:
            self.debugPrint(f"正在请求分类页: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                self.debugPrint(f"请求失败，状态码: {response.status_code}")
                return result
            
            html_content = response.text
            self.debugPrint(f"获取到HTML内容，长度: {len(html_content)}")
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 使用更通用的方法获取短剧列表
            videos = []
            
            # 方法1: 直接查找所有包含[短剧]的链接
            items = soup.find_all('a')
            
            self.debugPrint(f"找到的链接数量: {len(items)}")
            processed_links = set()  # 用于去重
            
            for item in items:
                try:
                    title = item.text.strip()
                    if not title or '[短剧]' not in title:
                        continue
                    
                    link = item.get('href')
                    if not link or link in processed_links:
                        continue
                    
                    processed_links.add(link)
                    self.debugPrint(f"找到短剧链接: {title}")
                    
                    title = title.replace('[短剧]', '').strip()
                    
                    # 提取集数信息
                    episode_match = re.search(r'（(\d+)集）', title)
                    episode_count = ''
                    if episode_match:
                        episode_count = episode_match.group(1) + '集'
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 由于没有直接的图片，使用默认图标
                    img = "https://duanjugou.top/favicon.ico"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": episode_count
                    })
                except Exception as e:
                    self.debugPrint(f"处理单个短剧时出错: {str(e)}")
                    continue
            
            # 如果方法1失败，尝试方法2：查找列表项
            if not videos:
                self.debugPrint("方法1未找到短剧，尝试方法2")
                
                # 尝试找到内容列表
                content_lists = soup.find_all(['ul', 'ol', 'div'], class_=lambda x: x and ('list' in x.lower() or 'content' in x.lower()))
                
                for content_list in content_lists:
                    links = content_list.find_all('a')
                    for link in links:
                        try:
                            title = link.text.strip()
                            if not title or len(title) < 2:
                                continue
                                
                            link_url = link.get('href')
                            if not link_url or link_url in processed_links:
                                continue
                                
                            processed_links.add(link_url)
                                
                            # 如果不是短剧但有明显的标题特征也收录
                            title_clean = title
                            if '[短剧]' in title:
                                title_clean = title.replace('[短剧]', '').strip()
                            
                            # 提取集数信息
                            episode_match = re.search(r'（(\d+)集）', title_clean)
                            episode_count = ''
                            if episode_match:
                                episode_count = episode_match.group(1) + '集'
                            
                            if not link_url.startswith('http'):
                                link_url = urljoin(self.siteUrl, link_url)
                            
                            # 由于没有直接的图片，使用默认图标
                            img = "https://duanjugou.top/favicon.ico"
                            
                            videos.append({
                                "vod_id": link_url,
                                "vod_name": title_clean,
                                "vod_pic": img,
                                "vod_remarks": episode_count
                            })
                        except Exception as e:
                            continue
                    
                    if videos:  # 如果找到了视频，就不继续查找其他列表了
                        break
            
            # 判断是否有下一页
            next_page = soup.find('a', class_='next') or soup.find('a', text=re.compile(r'下一页|Next'))
            has_next = True if next_page else False
            
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 999 if has_next else int(pg)
            result['limit'] = 90
            result['total'] = 999999
            
            self.debugPrint(f"分类页找到的视频数量: {len(videos)}")
            return result
        except Exception as e:
            self.debugPrint(f"获取分类内容异常: {str(e)}")
            return result
    
    def detailContent(self, ids):
        if not ids:
            return {}
            
        video_id = ids[0]  # 视频页面URL
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache"
        }
        
        try:
            self.debugPrint(f"正在请求详情页: {video_id}")
            response = requests.get(video_id, headers=headers, timeout=10)
            if response.status_code != 200:
                self.debugPrint(f"请求失败，状态码: {response.status_code}")
                return {}
            
            html_content = response.text
            self.debugPrint(f"获取到HTML内容，长度: {len(html_content)}")
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 尝试多种方式获取标题
            title = ""
            title_elem = soup.find('h1') or soup.find('h2') or soup.find('title')
            if title_elem:
                title = title_elem.text.strip()
                title = title.replace('[短剧]', '').strip()
                
                # 如果title包含网站名，需要去除
                if ' - ' in title:
                    title = title.split(' - ')[0].strip()
            
            if not title:
                # 尝试从URL中提取标题
                try:
                    url_parts = video_id.rstrip('/').split('/')
                    title = url_parts[-1] or url_parts[-2]
                    title = urllib.parse.unquote(title)
                except:
                    title = "未知短剧"
            
            self.debugPrint(f"提取到的标题: {title}")
            
            # 获取内容描述（如果有的话）
            desc = ""
            content_elem = soup.find('div', class_=lambda x: x and 'content' in x.lower()) or soup.find('article')
            if content_elem:
                # 去掉所有的链接元素
                for a in content_elem.find_all('a'):
                    a.extract()
                
                desc = content_elem.text.strip()
                # 清理描述文本
                desc = re.sub(r'\s+', ' ', desc)
                # 限制长度
                if len(desc) > 200:
                    desc = desc[:200] + "..."
            
            self.debugPrint(f"提取到的描述: {desc[:50]}...")
            
            # 获取网盘链接
            pan_links = []
            link_patterns = [
                r'(https?://pan\.baidu\.com/s/[a-zA-Z0-9_-]+)',  # 百度网盘链接
                r'(https?://www\.aliyundrive\.com/s/[a-zA-Z0-9_-]+)',  # 阿里云盘链接
                r'(https?://www\.123pan\.com/s/[a-zA-Z0-9_-]+)'  # 123云盘链接
            ]
            
            # 先从所有链接中查找
            link_elems = soup.find_all('a')
            for link in link_elems:
                try:
                    href = link.get('href', '')
                    if not href:
                        continue
                        
                    for pattern in link_patterns:
                        if re.search(pattern, href):
                            link_text = link.text.strip() or "网盘链接"
                            pan_links.append(f"{link_text}${href}")
                            break
                except:
                    continue
            
            # 如果没有找到链接，尝试从文本中正则匹配
            if not pan_links:
                text = html_content
                for pattern in link_patterns:
                    matches = re.findall(pattern, text)
                    for match in matches:
                        pan_links.append(f"网盘链接${match}")
            
            # 提取提取码
            extract_code = ""
            code_patterns = [
                r'提取码[：:]\s*([a-zA-Z0-9]{4})',
                r'密码[：:]\s*([a-zA-Z0-9]{4})',
                r'访问码[：:]\s*([a-zA-Z0-9]{4})'
            ]
            
            for pattern in code_patterns:
                code_match = re.search(pattern, html_content)
                if code_match:
                    extract_code = code_match.group(1)
                    break
            
            if extract_code and pan_links:
                # 添加提取码到第一个链接中
                first_link = pan_links[0].split('$')
                if len(first_link) == 2:
                    name, url = first_link
                    name = f"{name}(提取码:{extract_code})"
                    pan_links[0] = f"{name}${url}"
            
            # 如果没有找到网盘链接，使用分享文本
            if not pan_links:
                share_text = "请在浏览器中打开原页面获取网盘链接"
                pan_links.append(f"{share_text}${video_id}")
            
            self.debugPrint(f"提取到的网盘链接数量: {len(pan_links)}")
            
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
            self.debugPrint(f"获取详情页异常: {str(e)}")
            return {}
    
    def searchContent(self, key, quick):
        search_url = f"{self.siteUrl}/search?q={quote_plus(key)}"
        
        headers = {
            "User-Agent": self.userAgent,
            "Referer": self.siteUrl,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache"
        }
        
        try:
            self.debugPrint(f"正在搜索: {search_url}")
            response = requests.get(search_url, headers=headers, timeout=10)
            if response.status_code != 200:
                self.debugPrint(f"搜索请求失败，状态码: {response.status_code}")
                return []
            
            html_content = response.text
            self.debugPrint(f"获取到HTML内容，长度: {len(html_content)}")
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            videos = []
            processed_links = set()  # 用于去重
            
            # 方法1: 查找所有含有短剧关键字的链接
            items = soup.find_all('a')
            
            for item in items:
                try:
                    title = item.text.strip()
                    if not title:
                        continue
                    
                    # 如果标题中包含搜索关键词或带有短剧标识，则认为是有效结果
                    if key.lower() not in title.lower() and '[短剧]' not in title:
                        continue
                    
                    link = item.get('href')
                    if not link or link in processed_links:
                        continue
                    
                    processed_links.add(link)
                    
                    # 清理标题
                    title_clean = title.replace('[短剧]', '').strip()
                    
                    # 提取集数信息
                    episode_match = re.search(r'（(\d+)集）', title_clean)
                    episode_count = ''
                    if episode_match:
                        episode_count = episode_match.group(1) + '集'
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 由于没有直接的图片，使用默认图标
                    img = "https://duanjugou.top/favicon.ico"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title_clean,
                        "vod_pic": img,
                        "vod_remarks": episode_count
                    })
                except Exception as e:
                    self.debugPrint(f"处理搜索结果时出错: {str(e)}")
                    continue
            
            # 如果找不到结果，尝试方法2
            if not videos:
                self.debugPrint("搜索方法1未找到结果，尝试方法2")
                # 尝试查找搜索结果区域
                search_results = soup.find_all(['div', 'ul', 'ol'], class_=lambda x: x and ('result' in x.lower() or 'list' in x.lower()))
                
                for result_area in search_results:
                    links = result_area.find_all('a')
                    for link in links:
                        try:
                            title = link.text.strip()
                            if not title:
                                continue
                                
                            link_url = link.get('href')
                            if not link_url or link_url in processed_links:
                                continue
                                
                            processed_links.add(link_url)
                            
                            title_clean = title.replace('[短剧]', '').strip()
                            
                            # 提取集数信息
                            episode_match = re.search(r'（(\d+)集）', title_clean)
                            episode_count = ''
                            if episode_match:
                                episode_count = episode_match.group(1) + '集'
                            
                            if not link_url.startswith('http'):
                                link_url = urljoin(self.siteUrl, link_url)
                            
                            img = "https://duanjugou.top/favicon.ico"
                            
                            videos.append({
                                "vod_id": link_url,
                                "vod_name": title_clean,
                                "vod_pic": img,
                                "vod_remarks": episode_count
                            })
                        except Exception as e:
                            continue
                    
                    if videos:  # 如果找到了视频，就不继续查找其他区域了
                        break
            
            self.debugPrint(f"搜索结果数量: {len(videos)}")
            return videos
        except Exception as e:
            self.debugPrint(f"搜索异常: {str(e)}")
            return []
    
    def playerContent(self, flag, id, vipFlags):
        # 对于网盘链接，直接返回原始链接让用户在浏览器中打开
        self.debugPrint(f"播放内容 - flag: {flag}, id: {id}")
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

# 用于本地测试
if __name__ == "__main__":
    import sys
    
    spider = Duanjugou()
    
    # 支持的测试命令
    # python py_duanjugou.py home --filter=1
    # python py_duanjugou.py home_video
    # python py_duanjugou.py category --tid=latest --pg=1
    # python py_duanjugou.py detail --ids=https://duanjugou.top/某个详情页地址
    # python py_duanjugou.py search --key=关键词
    
    if len(sys.argv) > 1:
        method = sys.argv[1]
        
        if method == 'home':
            filter_param = False
            for arg in sys.argv:
                if arg.startswith('--filter='):
                    filter_param = arg.split('=')[1] == '1'
            
            result = spider.homeContent(filter=filter_param)
            print(json.dumps(result, ensure_ascii=False, indent=4))
        
        elif method == 'home_video':
            result = spider.homeVideoContent()
            print(json.dumps(result, ensure_ascii=False, indent=4))
        
        elif method == 'category':
            tid = 'latest'
            pg = '1'
            extend = {}
            filter_param = False
            
            for arg in sys.argv:
                if arg.startswith('--tid='):
                    tid = arg.split('=')[1]
                elif arg.startswith('--pg='):
                    pg = arg.split('=')[1]
                elif arg.startswith('--filter='):
                    filter_param = arg.split('=')[1] == '1'
                elif arg.startswith('--extend='):
                    extend_str = arg.split('=')[1]
                    extend = json.loads(extend_str)
            
            result = spider.categoryContent(tid=tid, pg=pg, filter=filter_param, extend=extend)
            print(json.dumps(result, ensure_ascii=False, indent=4))
        
        elif method == 'detail':
            ids = []
            for arg in sys.argv:
                if arg.startswith('--ids='):
                    ids = [arg.split('=')[1]]
            
            if ids:
                result = spider.detailContent(ids=ids)
                print(json.dumps(result, ensure_ascii=False, indent=4))
            else:
                print("Error: No ids provided")
        
        elif method == 'search':
            key = ''
            for arg in sys.argv:
                if arg.startswith('--key='):
                    key = arg.split('=')[1]
            
            if key:
                result = spider.searchContent(key=key, quick=True)
                print(json.dumps(result, ensure_ascii=False, indent=4))
            else:
                print("Error: No key provided")
        
        else:
            print(f"Unsupported method: {method}")
            print("Supported methods: home, home_video, category, detail, search")
    else:
        # 默认测试首页
        result = spider.homeContent(filter=True)
        print(json.dumps(result, ensure_ascii=False, indent=4)) 
