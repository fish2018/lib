#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 短剧狗爬虫 - 全网免费短剧网盘合集

import sys
import requests
from urllib.parse import urljoin, quote
import re
from bs4 import BeautifulSoup

# 修复导入路径问题
sys.path.append('../../')
try:
    from base.spider import Spider
except ImportError:
    # 定义一个基础接口类，用于本地测试
    class Spider:
        def init(self, extend=""):
            pass

class Spider(Spider):
    def __init__(self):
        self.siteUrl = 'https://duanjugou.top'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
    def getName(self):
        return "短剧狗"
    
    def init(self, extend=""):
        # 分类配置 - 添加推荐分类和热门标签
        self.cateManual = {
            "娇妻": "search.php?q=%E5%A8%87%E5%A6%BB",
            "总裁": "search.php?q=%E6%80%BB%E8%A3%81",
            "都市": "search.php?q=%E9%83%BD%E5%B8%82",
            "穿越": "search.php?q=%E7%A9%BF%E8%B6%8A",
            "闪婚": "search.php?q=%E9%97%AA%E5%A9%9A",
            "神医": "search.php?q=%E7%A5%9E%E5%8C%BB"
        }
        
        # Pyramid应用必要配置项
        self.api = ""  # API地址，本地运行时不需要
        self.key = "py_短剧狗"  # 插件唯一标识
        self.name = "短剧狗|网盘"  # 插件名称
        self.type = 3  # 插件类型 - 3为视频
        self.searchable = 1  # 是否可搜索
        self.quickSearch = 1  # 是否可快速搜索
        self.filterable = 1  # 是否可筛选
        self.changeable = 0  # 是否可换源
        
        # 过滤器配置
        if extend:
            self.extend = extend
        else:
            self.extend = {
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
                            {"n": "千金", "v": "千金"},
                            {"n": "公主", "v": "公主"},
                            {"n": "女王", "v": "女王"}
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
                            {"n": "老公", "v": "老公"},
                            {"n": "赘婿", "v": "赘婿"}
                        ]
                    }
                ]
            }
        return
    
    def isVideoFormat(self, url):
        # 对于网盘链接，不是直接的视频格式
        return False
    
    def manualVideoCheck(self):
        # 不需要手动检查
        return False
    
    def homeContent(self, filter):
        result = {}
        
        # 构建分类列表
        classes = []
        for k in self.cateManual:
            classes.append({
                'type_id': self.cateManual[k],
                'type_name': k
            })
        
        result['class'] = classes
        
        # 处理过滤器
        if filter:
            result['filters'] = self.extend
        
        # 获取首页推荐视频
        try:
            result['list'] = self.homeVideoContent()['list']
        except:
            result['list'] = []
        
        return result
    
    def fetch(self, url, headers=None):
        """统一的网络请求接口"""
        if headers is None:
            headers = {
                "User-Agent": self.userAgent,
                "Referer": self.siteUrl,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
            }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"请求异常: {url}, 错误: {str(e)}")
            return None
    
    def homeVideoContent(self):
        url = self.siteUrl
        
        try:
            print(f"获取首页内容：{url}")  # 调试输出
            response = self.fetch(url)
            if not response:
                return {'list': []}
            
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 根据网站实际结构，找到首页内容区域
            main_list_section = soup.find('div', class_='erx-list-box')
            if not main_list_section:
                print(f"未找到erx-list-box容器")
                return {'list': []}
                
            item_list = main_list_section.find('ul', class_='erx-list')
            if not item_list:
                print(f"未找到erx-list列表")
                return {'list': []}
            
            videos = []
            
            items = item_list.find_all('li', class_='item')
            print(f"首页找到 {len(items)} 个项目")  # 调试输出
            
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
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 使用默认图标
                    img = "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": time_text
                    })
                except Exception as e:
                    print(f"处理单个短剧时出错: {str(e)}")
                    continue
            
            print(f"首页解析完成，共获取到 {len(videos)} 个视频")  # 调试输出
            return {'list': videos}
        except Exception as e:
            print(f"获取首页内容时出错: {str(e)}")
            return {'list': []}
    
    def categoryContent(self, tid, pg, filter, extend):
        # 构建请求URL
        url = f"{self.siteUrl}"
        
        # 先进行id判断和处理，确保能处理各种格式的分类ID
        print(f"接收到分类ID: {tid}")  # 调试输出
        
        # 检查是否只传递了分类名称（如"娇妻"），而非完整ID
        original_tid = tid
        for k, v in self.cateManual.items():
            if tid == k:  # 如果传入的是分类名称，转换为对应的ID
                tid = v
                print(f"将分类名称 '{original_tid}' 转换为对应ID: {tid}")
                break
        
        if tid == "home" or tid == "latest" or tid == "推荐":
            # 首页内容 - 重用homeVideoContent方法
            print(f"处理首页分类")
            result = self.homeVideoContent()
            # 添加分页信息
            result['page'] = pg
            result['pagecount'] = 1
            result['limit'] = 20
            result['total'] = len(result['list'])
            return result
        elif tid == "hot-day":
            url = f"{self.siteUrl}/sort/hot-day.html"
        elif tid == "hot-week":
            url = f"{self.siteUrl}/sort/hot-week.html"
        elif tid.startswith("tag-"):
            # 对于标签类别，需要检查是否有特定标签
            url = f"{self.siteUrl}/tags.html"
            
            # 处理过滤器
            if "tag" in extend and extend["tag"]:
                tag = extend["tag"]
                url = f"{self.siteUrl}/tags/{tag}.html"
        elif tid.startswith("search.php"):
            # 这是搜索类分类，直接使用完整URL
            print(f"处理搜索类分类: {tid}")
            url = f"{self.siteUrl}/{tid}"
        elif tid in ["娇妻", "总裁", "都市", "穿越", "闪婚", "神医"]:
            # 直接处理标签关键词
            keyword = tid
            encoded_keyword = quote(keyword)
            url = f"{self.siteUrl}/search.php?q={encoded_keyword}"
            print(f"处理标签关键词: {keyword}, URL: {url}")
        elif tid.startswith("%"):
            # 处理直接传入URL编码部分的情况
            # 先尝试解码，看是否是中文关键词
            try:
                # 这里不能直接解码，因为应用可能传入的是已编码的字符串如%E7%A9%BF%E8%B6%8A
                # 我们需要特殊处理，通过查找原始映射来匹配
                found = False
                for k, v in self.cateManual.items():
                    if v.endswith(tid):
                        print(f"找到匹配的分类: {k}")
                        url = f"{self.siteUrl}/{v}"
                        found = True
                        break
                
                if not found:
                    # 如果没找到匹配，则作为中文关键词处理
                    # 注意：这可能是一个错误的编码字符串，我们直接用于搜索
                    url = f"{self.siteUrl}/search.php?q={tid}"
                    print(f"未找到匹配，直接使用编码串作为关键词: {tid}")
            except Exception as e:
                print(f"处理URL编码部分时出错: {str(e)}")
                # 作为通用关键词处理
                url = f"{self.siteUrl}/search.php?q={tid}"
        else:
            # 最后尝试编码关键词搜索
            try:
                # 尝试将分类ID作为关键词进行搜索
                encoded_keyword = quote(tid)
                url = f"{self.siteUrl}/search.php?q={encoded_keyword}"
                print(f"尝试将未知分类ID作为关键词搜索: {tid}, URL: {url}")
            except:
                print(f"未能处理的分类ID: {tid}")
                url = self.siteUrl
        
        # 处理分页
        if pg > 1:
            if "?" in url:
                url = f"{url}&page={pg}"
            else:
                url = f"{url}?page={pg}"
        
        print(f"分类请求最终URL: {url}")  # 调试输出
        
        try:
            # 确保使用正确的User-Agent
            headers = {
                "User-Agent": self.userAgent,
                "Referer": self.siteUrl,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
            }
            
            response = self.fetch(url, headers)
            if not response:
                print(f"请求失败，返回None")
                return {'list': [], 'page': pg, 'pagecount': 1, 'limit': 20, 'total': 0}
            
            print(f"请求状态码: {response.status_code}")
            
            html_content = response.text
            
            # 打印HTML内容的前100个字符，帮助调试
            print(f"HTML内容片段: {html_content[:100]}...")
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 查找分类标题，帮助判断是否进入了正确的页面
            title_tag = soup.find('title')
            if title_tag:
                print(f"页面标题: {title_tag.text.strip()}")
            
            # 根据网站实际结构，找到分类内容区域
            main_list_section = soup.find('div', class_='erx-list-box')
            if not main_list_section:
                print(f"未找到erx-list-box容器")
                return {'list': [], 'page': pg, 'pagecount': 1, 'limit': 20, 'total': 0}
                
            item_list = main_list_section.find('ul', class_='erx-list')
            if not item_list:
                print(f"未找到erx-list列表")
                return {'list': [], 'page': pg, 'pagecount': 1, 'limit': 20, 'total': 0}
            
            videos = []
            
            items = item_list.find_all('li', class_='item')
            print(f"找到 {len(items)} 个项目")  # 调试输出
            
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
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 使用默认图标
                    img = "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": time_text
                    })
                except Exception as e:
                    print(f"处理单个短剧时出错: {str(e)}")
                    continue
            
            print(f"成功解析 {len(videos)} 个视频")  # 调试输出
            
            # 获取分页信息
            try:
                pager = soup.find('div', class_='pagebar')
                if pager:
                    page_text = pager.text
                    max_page_match = re.search(r'共(\d+)页', page_text)
                    if max_page_match:
                        max_page = int(max_page_match.group(1))
                        print(f"检测到总页数: {max_page}")
                    else:
                        max_page = pg
                else:
                    max_page = pg
            except Exception as e:
                print(f"获取分页信息出错: {str(e)}")
                max_page = pg
            
            result = {
                'list': videos,
                'page': pg,
                'pagecount': max_page,
                'limit': 20,
                'total': len(videos) * max_page
            }
            
            print(f"分类内容获取完成，返回 {len(videos)} 个视频，共 {max_page} 页")
            
            return result
        except Exception as e:
            print(f"获取分类内容时出错: {str(e)}")
            import traceback
            print(traceback.format_exc())  # 打印完整错误堆栈
            return {'list': [], 'page': pg, 'pagecount': 1, 'limit': 20, 'total': 0}
    
    def detailContent(self, ids):
        # 解析详情页面URL
        url = ids[0]
        if not url.startswith('http'):
            url = urljoin(self.siteUrl, url)
            
        try:
            response = self.fetch(url)
            if not response:
                return {}
                
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 查找页面主体内容 - 使用erx-wrap类而不是article
            main_content = soup.find('div', class_='erx-wrap')
            if not main_content:
                print(f'无法找到erx-wrap容器')
                return {}
            
            # 尝试找到标题 - 从页面标题获取
            title = '未知标题'
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.text.strip()
                # 去掉网站名称
                title = title.split('_')[0].strip()
            
            # 网盘分类关键字
            pan_domains = {
                "百度网盘": ["pan.baidu.com"],
                "阿里云盘": ["alipan.com", "aliyundrive.com"],
                "夸克网盘": ["pan.quark.cn"],
                "迅雷网盘": ["pan.xunlei.com"],
                "天翼云盘": ["cloud.189.cn"],
                "移动云盘": ["caiyun.139.com"],
                "UC网盘": ["drive.uc.cn"],
                "115网盘": ["115cdn.com", "115.com", "anxia.com"],
                "PikPak": ["mypikpak.com"],
                "123网盘": ["123684.com", "123685.com", "123912.com", "123pan.com", "123pan.cn", "123592.com"]
            }

            # 获取网盘链接和下载链接
            pan_links = []
            download_links = []
            
            # 使用正则表达式查找所有可能的链接 - 改进版本，排除末尾的...
            link_pattern = re.compile(r"((?!https?://t\.me)(?:https?://[^\s'\"<>【】\n\.]+(?:\.[^\s'\"<>【】\n\.]+)+(?:/[^\s'\"<>【】\n\.]*)?|magnet:\?xt=urn:btih:[a-zA-Z0-9]+))")
            all_links = link_pattern.findall(html_content)
            
            # 链接去重和清理
            link_map = {}  # 用于去重
            
            # 清理链接函数
            def clean_link(link):
                # 移除尾部非URL字符
                clean = re.sub(r'[\'">].*$', '', link)
                # 移除末尾的省略号
                clean = re.sub(r'\.{3,}$', '', clean)
                # 标准化链接 - 移除URL末尾的斜杠
                clean = clean.rstrip('/')
                return clean
            
            # 处理从正则表达式找到的链接
            for link in all_links:
                clean_link_str = clean_link(link)
                if clean_link_str and len(clean_link_str) > 10:  # 确保链接有效
                    base_url = clean_link_str.split('?')[0]  # 用于基本去重
                    if base_url not in link_map:
                        link_map[base_url] = clean_link_str
            
            # 查找页面中的所有链接元素
            a_tags = main_content.find_all('a', href=True)
            for a in a_tags:
                href = a.get('href', '').strip()
                # 过滤非法链接并清理
                if href and not href.startswith('#') and not href.startswith('javascript:'):
                    clean_href = clean_link(href)
                    if clean_href and len(clean_href) > 10:
                        base_url = clean_href.split('?')[0]
                        if base_url not in link_map:
                            link_map[base_url] = clean_href
            
            # 转换去重后的链接映射为列表
            cleaned_links = list(link_map.values())
            
            # 处理所有找到的链接
            for href in cleaned_links:
                # 跳过无效链接
                if not href or href == '#' or href.startswith('javascript:'):
                    continue
                
                # 获取链接文本（如果是从a标签提取的）
                text = ""
                for a in a_tags:
                    if clean_link(a.get('href', '')) == href:
                        text = a.text.strip()
                        break
                
                # 如果没有链接文本，使用默认文本
                if not text:
                    text = "链接"
                
                # 检查是否是磁力链接
                if href.startswith('magnet:'):
                    download_links.append({
                        'name': f"{text or '磁力链接'}",
                        'url': href
                    })
                    continue
                
                # 检查是否是网盘链接
                is_pan_link = False
                for pan_name, domains in pan_domains.items():
                    if any(domain in href for domain in domains):
                        pan_links.append({
                            'name': f"{text or pan_name}",
                            'url': href
                        })
                        is_pan_link = True
                        break
                
                # 如果不是已知的网盘链接，检查是否是其他类型的下载链接
                if not is_pan_link and re.search(r'(ed2k|thunder|ftp):', href):
                    download_links.append({
                        'name': f"{text or '下载链接'}",
                        'url': href
                    })
            
            # 提取网盘密码 - 在整个页面内容中查找
            pwd_pattern = re.compile(r'提取码[:：]\s*([a-zA-Z0-9]{4})')
            pwd_match = pwd_pattern.search(html_content)
            pwd = pwd_match.group(1) if pwd_match else ''
            
            # 构建播放列表
            vod_play_from = []
            vod_play_url = []
            
            if pan_links:
                vod_play_from.append('网盘链接')
                play_urls = []
                for i, link in enumerate(pan_links):
                    play_urls.append(f"{link['name']}${link['url']}")
                vod_play_url.append('#'.join(play_urls))
            
            if download_links:
                vod_play_from.append('下载链接')
                play_urls = []
                for i, link in enumerate(download_links):
                    play_urls.append(f"{link['name']}${link['url']}")
                vod_play_url.append('#'.join(play_urls))
            
            # 提取简介 - 使用整个内容区域
            content_text = main_content.text.strip()
            # 清理文本
            content_text = re.sub(r'\s+', ' ', content_text)
            
            # 限制简介长度
            description = content_text[:500] + '...' if len(content_text) > 500 else content_text
            
            # 如果有提取码，添加到简介中
            if pwd:
                description = f"提取码: {pwd}\n\n{description}"
            
            vod = {
                'vod_id': ids[0],
                'vod_name': title,
                'vod_pic': 'https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png',
                'type_name': '短剧',
                'vod_year': '',
                'vod_area': '',
                'vod_remarks': '',
                'vod_actor': '',
                'vod_director': '',
                'vod_content': description
            }
            
            if vod_play_from:
                vod['vod_play_from'] = '$$$'.join(vod_play_from)
                vod['vod_play_url'] = '$$$'.join(vod_play_url)
            
            return {
                'list': [vod]
            }
        except Exception as e:
            print(f"获取详情内容时出错: {str(e)}")
            return {}
    
    def searchContent(self, key, quick, pg=1):
        # 对搜索关键词进行URL编码
        try:
            encoded_key = quote(key)
            url = f"{self.siteUrl}/search.php?q={encoded_key}"
            print(f"搜索关键词: {key}, 编码后: {encoded_key}")
            print(f"搜索URL: {url}")
        except Exception as e:
            print(f"编码搜索关键词时出错: {str(e)}")
            return {'list': []}
        
        # 处理分页
        if pg > 1:
            url = f"{url}&page={pg}"
        
        try:
            # 确保使用正确的请求头
            headers = {
                "User-Agent": self.userAgent,
                "Referer": self.siteUrl,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
            }
            
            response = self.fetch(url, headers)
            if not response:
                print(f"搜索请求失败，URL: {url}")
                return {'list': []}
            
            print(f"搜索请求状态码: {response.status_code}")
            
            html_content = response.text
            
            # 打印HTML内容的前100个字符，帮助调试
            print(f"搜索HTML内容片段: {html_content[:100]}...")
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 查找搜索结果列表
            main_list_section = soup.find('div', class_='erx-list-box')
            if not main_list_section:
                print(f"未找到搜索结果erx-list-box容器")
                return {'list': []}
                
            item_list = main_list_section.find('ul', class_='erx-list')
            if not item_list:
                print(f"未找到搜索结果erx-list列表")
                return {'list': []}
            
            videos = []
            
            items = item_list.find_all('li', class_='item')
            print(f"搜索结果找到 {len(items)} 个项目")
            
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
                    
                    if not link.startswith('http'):
                        link = urljoin(self.siteUrl, link)
                    
                    # 使用默认图标
                    img = "https://duanjugou.top/zb_users/theme/erx_Special/images/logo.png"
                    
                    videos.append({
                        "vod_id": link,
                        "vod_name": title,
                        "vod_pic": img,
                        "vod_remarks": time_text
                    })
                except Exception as e:
                    print(f"处理搜索结果时出错: {str(e)}")
                    continue
            
            print(f"搜索成功解析 {len(videos)} 个视频结果")
            return {'list': videos}
        except Exception as e:
            print(f"搜索内容时出错: {str(e)}")
            import traceback
            print(traceback.format_exc())  # 打印完整错误堆栈
            return {'list': []}
    
    def searchContentPage(self, key, quick, pg=1):
        return self.searchContent(key, quick, pg)
    
    def playerContent(self, flag, id, vipFlags):
        # 对于网盘链接，直接返回原始链接让用户在浏览器中打开
        return {
            "parse": 0,
            "url": id,
            "header": {
                "User-Agent": self.userAgent
            }
        }
    
    def localProxy(self, param):
        # 当前场景不需要本地代理
        return None
    
    def destroy(self):
        # 资源回收
        pass 
