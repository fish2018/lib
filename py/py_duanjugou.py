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
            
            # 根据网站实际结构，找到首页内容区域
            main_list_section = soup.find('div', class_='erx-list-box')
            if not main_list_section:
                self.debugPrint("找不到内容区域")
                return []
                
            item_list = main_list_section.find('ul', class_='erx-list')
            if not item_list:
                self.debugPrint("找不到内容列表")
                return []
            
            videos = []
            
            items = item_list.find_all('li', class_='item')
            self.debugPrint(f"找到的列表项数量: {len(items)}")
            
            for item in items:
                try:
                    # 获取标题区域
                    a_div = item.find('div', class_='a')
                    if not a_div:
                        continue
                    
                    # 提取链接和标题
                    link_elem = a_div.find('a', class_='main')
                    if not link_elem:
                        continue
                    
                    title = link_elem.text.strip()
                    link = link_elem.get('href')
                    
                    # 提取时间
                    i_div = item.find('div', class_='i')
                    time_text = ""
                    if i_div:
                        time_span = i_div.find('span', class_='time')
                        if time_span:
                            time_text = time_span.text.strip()
                    
                    # 提取集数信息
                    episode_match = re.search(r'（(\d+)集）', title)
                    episode_count = ''
                    if episode_match:
                        episode_count = episode_match.group(1) + '集'
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 使用默认图标
                    img = "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": episode_count if episode_count else time_text
                    })
                    
                    if len(videos) >= 30:  # 限制数量
                        break
                except Exception as e:
                    self.debugPrint(f"处理单个短剧时出错: {str(e)}")
                    continue
            
            self.debugPrint(f"最终找到的视频数量: {len(videos)}")
            return videos
        except Exception as e:
            self.debugPrint(f"获取首页视频异常: {str(e)}")
            return []
    
    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        
        # 根据分类和页码构建URL
        if tid == 'latest':
            # 最新内容
            url = self.siteUrl
            if pg != '1':
                url = f"{self.siteUrl}/page_{pg}.html"
        elif tid == 'hot-day':
            # 24小时热门
            url = f"{self.siteUrl}/home-day-hot.html"
            if pg != '1':
                url = f"{self.siteUrl}/home-day-hot_{pg}.html"
        elif tid == 'hot-week':
            # 一周热门
            url = f"{self.siteUrl}/home-week-hot.html"
            if pg != '1':
                url = f"{self.siteUrl}/home-week-hot_{pg}.html"
        elif tid.startswith('tag-'):
            # 标签过滤
            tag_category = tid.split('-')[1]
            search_tag = ""
            
            if extend and 'tag' in extend:
                search_tag = extend['tag']
            
            if search_tag:
                url = f"{self.siteUrl}/search.php?q={quote_plus(search_tag)}"
                if pg != '1':
                    # 注意：网站可能不支持搜索结果的翻页
                    url = f"{self.siteUrl}/search.php?q={quote_plus(search_tag)}"
            else:
                # 默认返回最新内容
                url = self.siteUrl
                if pg != '1':
                    url = f"{self.siteUrl}/page_{pg}.html"
        else:
            # 默认情况
            url = self.siteUrl
            if pg != '1':
                url = f"{self.siteUrl}/page_{pg}.html"
        
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
            
            # 获取内容区域
            main_list_section = None
            
            # 搜索页和普通页面结构略有不同
            if 'search.php' in url:
                main_list_section = soup.find('div', class_='erx-list-box')
            else:
                content_section = soup.find('div', class_='erx-content')
                if content_section:
                    main_list_section = content_section.find('div', class_='erx-list-box')
            
            if not main_list_section:
                self.debugPrint("找不到内容区域")
                return result
                
            item_list = main_list_section.find('ul', class_='erx-list')
            if not item_list:
                self.debugPrint("找不到内容列表")
                return result
            
            videos = []
            
            items = item_list.find_all('li', class_='item')
            self.debugPrint(f"找到的列表项数量: {len(items)}")
            
            for item in items:
                try:
                    # 获取标题区域
                    a_div = item.find('div', class_='a')
                    if not a_div:
                        continue
                    
                    # 提取链接和标题
                    link_elem = a_div.find('a', class_='main')
                    if not link_elem:
                        continue
                    
                    title = link_elem.text.strip()
                    link = link_elem.get('href')
                    
                    # 提取时间
                    i_div = item.find('div', class_='i')
                    time_text = ""
                    if i_div:
                        time_span = i_div.find('span', class_='time')
                        if time_span:
                            time_text = time_span.text.strip()
                    
                    # 提取集数信息
                    episode_match = re.search(r'（(\d+)集）', title)
                    episode_count = ''
                    if episode_match:
                        episode_count = episode_match.group(1) + '集'
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 使用默认图标
                    img = "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": episode_count if episode_count else time_text
                    })
                except Exception as e:
                    self.debugPrint(f"处理单个短剧时出错: {str(e)}")
                    continue
            
            # 判断是否有下一页
            pagebar = main_list_section.find('div', class_='erx-pagebar')
            has_next = False
            if pagebar:
                # 查找是否有下一页链接
                next_link = pagebar.find('a', title='›')
                if next_link:
                    has_next = True
                    
                # 或者查找最后一页的页码
                last_page_link = pagebar.find('a', title='››')
                if last_page_link:
                    href = last_page_link.get('href', '')
                    page_match = re.search(r'page_(\d+)', href)
                    if page_match:
                        total_pages = int(page_match.group(1))
                        self.debugPrint(f"总页数: {total_pages}")
                        
                        result['pagecount'] = total_pages
                        result['total'] = total_pages * 30  # 估算总数
            
            if 'pagecount' not in result:
                result['pagecount'] = 999 if has_next else int(pg)
                result['total'] = 999 * 30 if has_next else len(videos)
            
            result['list'] = videos
            result['page'] = int(pg)
            result['limit'] = 30
            
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
            
            # 获取标题
            title_elem = soup.find('h1')
            if not title_elem:
                self.debugPrint("找不到标题")
                return {}
                
            title = title_elem.text.strip()
            
            # 获取内容区域
            content_section = soup.find('section', class_='con')
            if not content_section:
                self.debugPrint("找不到内容区域")
                return {}
            
            # 提取网盘链接 - 直接获取第一个外部链接
            network_disk_link = ""
            network_disk_text = "网盘链接"
            
            link_elem = content_section.find('a', rel='external nofollow')
            if link_elem:
                network_disk_link = link_elem.get('href', '')
                network_disk_text = link_elem.text.strip() or "网盘链接"
                
                self.debugPrint(f"找到网盘链接: {network_disk_link}")
            
            # 如果没有找到链接，尝试从文本中匹配
            if not network_disk_link:
                link_patterns = [
                    r'(https?://pan\.baidu\.com/s/[a-zA-Z0-9_-]+)',  # 百度网盘
                    r'(https?://www\.aliyundrive\.com/s/[a-zA-Z0-9_-]+)',  # 阿里云盘
                    r'(https?://www\.123pan\.com/s/[a-zA-Z0-9_-]+)',  # 123云盘
                    r'(https?://pan\.quark\.cn/s/[a-zA-Z0-9_-]+)'  # 夸克网盘
                ]
                
                for pattern in link_patterns:
                    matches = re.search(pattern, html_content)
                    if matches:
                        network_disk_link = matches.group(1)
                        self.debugPrint(f"从文本中匹配到网盘链接: {network_disk_link}")
                        break
            
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
                    self.debugPrint(f"找到提取码: {extract_code}")
                    break
            
            # 构建播放链接
            play_url = f"{network_disk_text}${network_disk_link}"
            if extract_code and network_disk_link:
                play_url = f"{network_disk_text} 提取码:{extract_code}${network_disk_link}"
                
            if not network_disk_link:
                play_url = f"请在浏览器中打开原页面获取网盘链接${video_id}"
            
            # 提取集数信息
            episode_match = re.search(r'（(\d+)集）', title)
            episode_count = ''
            if episode_match:
                episode_count = episode_match.group(1) + '集'
            
            # 构建返回数据
            vod = {
                "vod_id": video_id,
                "vod_name": title,
                "vod_pic": "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png",
                "type_name": "短剧",
                "vod_year": time.strftime("%Y", time.localtime()),
                "vod_area": "中国大陆",
                "vod_remarks": episode_count,
                "vod_actor": "",
                "vod_director": "",
                "vod_content": f"网盘链接：{network_disk_link}" + (f"，提取码：{extract_code}" if extract_code else ""),
                "vod_play_from": "网盘",
                "vod_play_url": play_url
            }
            
            result = {
                'list': [vod]
            }
            return result
        except Exception as e:
            self.debugPrint(f"获取详情页异常: {str(e)}")
            return {}
    
    def searchContent(self, key, quick):
        search_url = f"{self.siteUrl}/search.php?q={quote_plus(key)}"
        
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
            
            # 获取搜索结果列表
            main_list_section = soup.find('div', class_='erx-list-box')
            if not main_list_section:
                self.debugPrint("找不到搜索结果区域")
                return []
                
            item_list = main_list_section.find('ul', class_='erx-list')
            if not item_list:
                self.debugPrint("找不到搜索结果列表")
                return []
            
            videos = []
            
            items = item_list.find_all('li', class_='item')
            self.debugPrint(f"找到的搜索结果数量: {len(items)}")
            
            for item in items:
                try:
                    # 获取标题区域
                    a_div = item.find('div', class_='a')
                    if not a_div:
                        continue
                    
                    # 提取链接和标题
                    link_elem = a_div.find('a', class_='main')
                    if not link_elem:
                        continue
                    
                    title = link_elem.text.strip()
                    link = link_elem.get('href')
                    
                    # 提取时间
                    i_div = item.find('div', class_='i')
                    time_text = ""
                    if i_div:
                        time_span = i_div.find('span', class_='time')
                        if time_span:
                            time_text = time_span.text.strip()
                    
                    # 提取集数信息
                    episode_match = re.search(r'（(\d+)集）', title)
                    episode_count = ''
                    if episode_match:
                        episode_count = episode_match.group(1) + '集'
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 使用默认图标
                    img = "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": episode_count if episode_count else time_text
                    })
                except Exception as e:
                    self.debugPrint(f"处理搜索结果时出错: {str(e)}")
                    continue
            
            self.debugPrint(f"最终找到的搜索结果数量: {len(videos)}")
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
