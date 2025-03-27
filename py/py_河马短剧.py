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
        self.domain = "kuaikaw.cn"
        self.api = "https://www.kuaikaw.cn"
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        self.nextData = None  # 缓存NEXT_DATA数据
        self.cateManual = {}

    def getName(self):
        # 返回爬虫名称
        return "河马短剧"
    
    def init(self, extend=""):
        # 初始化爬虫
        headers = {
            "User-Agent": self.ua,
            "Referer": f"{self.api}/"
        }
        
        # 初始化分类列表 (根据网站最新分类数据)
        self.cateManual = {
            "首页": "home",
            "短剧推荐": "1",
            "最新短剧": "3",
            "短剧精选": "4",
            "青春": "青春",
            "民国": "民国",
            "萌宝": "萌宝",
            "超能": "超能",
            "甜宠": "甜宠",
            "学院": "学院",
            "都市": "都市",
            "穿越": "穿越",
            "古装": "古装",
            "悬疑": "悬疑",
            "创业": "创业"
        }
        
        return {}
    
    def homeContent(self, filter=False):
        """获取首页分类及筛选"""
        result = {}
        # 分类列表，使用已初始化的cateManual
        classes = []
        for k in self.cateManual:
            classes.append({
                'type_name': k,
                'type_id': self.cateManual[k]
            })
        result['class'] = classes
        
        if filter:
            # 筛选项，根据网站实际提供的筛选功能
            filters = {}
            # 全部分类页的筛选项
            filters["all"] = [
                {
                    "key": "sort",
                    "name": "排序",
                    "value": [
                        {"n": "最新", "v": "new"},
                        {"n": "热播", "v": "hot"},
                        {"n": "好评", "v": "score"}
                    ]
                },
                {
                    "key": "year",
                    "name": "年份",
                    "value": [
                        {"n": "全部", "v": ""},
                        {"n": "2024", "v": "2024"},
                        {"n": "2023", "v": "2023"},
                        {"n": "2022", "v": "2022"},
                        {"n": "2021", "v": "2021"},
                        {"n": "2020", "v": "2020"}
                    ]
                }
            ]
            # 其他分类页也使用相同的筛选
            for cate_id in self.cateManual.values():
                if cate_id not in ["home", "hot", "all"]:
                    filters[cate_id] = filters["all"]
            
            result['filters'] = filters
        
        return result
    
    def homeVideoContent(self):
        """获取首页推荐视频内容"""
        url = self.api
        headers = {
            "User-Agent": self.ua,
            "Referer": f"{self.api}/"
        }
        
        videos = []
        try:
            response = requests.get(url, headers=headers)
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
                                "vod_id": book_id,
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
                                    "vod_id": book_id,
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
                            # "vod_id": book_id,
                            "vod_id": f"/{book_id}",
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
            
            videos = unique_videos[:30]  # 只保留前30个
        
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
        url = f"{self.api}/search?searchValue={urllib.parse.quote(search_key)}&page={pg}"
        
        headers = {
            "User-Agent": self.ua,
            "Referer": f"{self.api}/"
        }
        
        try:
            response = requests.get(url, headers=headers)
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
                            "vod_id": book_id,
                            "vod_name": book_name,
                            "vod_pic": cover_url,
                            "vod_remarks": f"{status_desc} {total_chapters}集" if total_chapters else status_desc
                        })
                
                # 构建返回结果
                result = {
                    "list": videos,
                    "page": int(current_page),
                    "pagecount": total_pages,
                    "limit": len(videos),
                    "total": total_pages * len(videos) if videos else 0
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
                            "vod_id": book_id,
                            "vod_name": title,
                            "vod_pic": img_url,
                            "vod_remarks": remark
                        })
                
                # 构建返回结果
                result = {
                    "list": videos,
                    "page": int(pg),
                    "pagecount": 1,  # 无法获取总页数时默认为1
                    "limit": len(videos),
                    "total": len(videos)
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
        url = f"{self.api}/search?searchValue={encoded_key}&page=1"
        
        headers = {
            "User-Agent": self.ua,
            "Referer": f"{self.api}/"
        }
        
        try:
            response = requests.get(url, headers=headers)
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
                        next_page_url = f"{self.api}/search?searchValue={encoded_key}&page={page}"
                        next_page_response = requests.get(next_page_url, headers=headers)
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
                        "vod_id": book_id,
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
                            "vod_id": book_id,
                            "vod_name": title,
                            "vod_pic": img_url,
                            "vod_remarks": remark
                        })
        
        except Exception as e:
            print(f"搜索出错: {e}")
        
        result = {
            "list": search_results
        }
        return result
    
    def detailContent(self, ids):
        # 获取视频详情和剧集列表
        # 传入的ids是一个列表，取第一个元素作为视频ID
        video_id = ids[0]
        video_url = f"{self.api}/episode/{video_id}"
        
        headers = {
            "User-Agent": self.ua,
            "Referer": f"{self.api}/"
        }
        
        try:
            response = requests.get(video_url, headers=headers)
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
                        next_chapter_url = f"{self.api}/episode/{video_id}?page={page}"
                        next_chapter_response = requests.get(next_chapter_url, headers=headers)
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
                        "User-Agent": self.ua,
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
                "User-Agent": self.ua,
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
