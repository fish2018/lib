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
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"

    def init(self, extend=""):
        return {}
    
    def homeContent(self, filter=False):
        # 首页内容，此处省略具体实现
        pass
    
    def homeVideoContent(self):
        # 首页视频内容，此处省略具体实现
        pass
    
    def categoryContent(self, tid, pg, filter, extend):
        # 分类内容，此处省略具体实现
        pass
    
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
                
                # 构建视频信息对象
                vod = {
                    "vod_id": video_id,
                    "vod_name": book_name,
                    "vod_pic": cover_url,
                    "type_name": "",  # 类型名可以从标签中提取
                    "vod_year": "",   # 年份信息可能不可用
                    "vod_area": "",   # 地区信息可能不可用
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
