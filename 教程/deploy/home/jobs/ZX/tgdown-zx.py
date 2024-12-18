# -*- coding:utf-8 -*-
from asyncio import CancelledError
from telethon.errors import FileReferenceExpiredError
from telethon.tl.types import MessageMediaDocument
import os
import re
import sys
import git
import json
import requests
import subprocess
from typing import Union
import demoji
from telethon import TelegramClient
from tqdm import tqdm
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class TqdmUpTo(tqdm):
    total = None
    now_size = 0
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} [已用时：{elapsed}预计剩余：{remaining}, {rate_fmt}{postfix}]'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unit = 'B'
        self.unit_scale = True
        self.unit_divisor = 1024
        self.bar_format = TqdmUpTo.bar_format

    def update_to(self, current, total):
        """更新进度条
        :param current: 已传输
        :param total: 总大小
        :return:
        """
        self.total = total
        if current != 0:
            self.update(current - self.now_size)
        self.now_size = current
async def GetChatTitle(client: TelegramClient, chat_id: int) -> Union[str, None]:
    entity = await client.get_entity(chat_id)
    return entity.title
async def getHistoryMessage(client: TelegramClient, chat_id: int, from_user=None, limit=5):
    channel_title = await GetChatTitle(client, chat_id)
    if from_user is not None and from_user.isdecimal():
        from_user = int(from_user)
    # 取最近2条消息
    messages = client.iter_messages(chat_id, from_user=from_user, limit=limit)
    return channel_title, messages
async def GetChatId(client: TelegramClient, chat_id: str) -> int:
    # 检测chat_id是id还是昵称
    isId = re.match(r'-?[1-9][0-9]{4,}', chat_id)
    if isId is None:
        entity = await client.get_entity(chat_id)
        chat_id = entity.id
    else:
        chat_id = int(chat_id)
    return chat_id
def shorten_filename(filename, limit=50):
    filename = filename.replace('\n', ' ')
    """返回合适长度文件名，中间用...显示"""
    if len(filename) <= limit:
        return filename
    else:
        return filename[:int(limit / 2) - 3] + '...' + filename[len(filename) - int(limit / 2):]
def GetFileId(message) -> str:
    _id = 'unknown'
    if hasattr(message.media, 'document'):
        _id = message.media.document.id
    elif hasattr(message.media, 'photo'):
        _id = message.media.photo.id
    return str(_id)
def GetFileName(message) -> str:
    # 取名优先级，文件名>描述>ID
    if message.file.name:
        return message.file.name
    file_ext = '.jpg' if message.file.ext in ['.jpe','jpeg'] else message.file.ext
    if len(message.message) != 0:
        sName = shorten_filename(demoji.replace(message.message, '[emoji]'))
        return re.sub(r'[\\/:*?"<>|]', '_', sName) + file_ext
    return GetFileId(message) + file_ext
# fileExist 检查文件是否存在（文件名和大小都相等），如果不存在重名文件加序号
def fileExist(file_path: str, file_size):
    i = 2
    ix = file_path.rfind('.', 1)
    fileName = file_path[:ix]
    fileType = file_path[ix:]
    temp = file_path
    while os.path.exists(temp):
        if os.path.getsize(temp) == file_size:
            return True, temp
        temp = f'{fileName}({i}){fileType}'
        i += 1
    return False, temp
def GetFileSuffix(message) -> list:
    mime_type = 'unknown/unknown'
    if hasattr(message.media, 'document'):
        mime_type = message.media.document.mime_type
    elif hasattr(message.media, 'photo'):
        mime_type = 'image/jpg'
    return mime_type.split('/')
async def download_file(client: TelegramClient, channel_title, channel_id, message, old=False, output='ZX'):
    file_name = GetFileName(message)
    file_path = f'{output}/{file_name}'
    file_size = message.file.size
    ret, file_path = fileExist(file_path, file_size)
    if not ret:
        # 已经判断文件不存在，并且保证了文件名不重复
        download_path = file_path + '.downloading'
        print(f"开始下载：{file_name}")
        try:
            with TqdmUpTo(total=file_size, bar_format=TqdmUpTo.bar_format, desc=file_name[:10]) as bar:
                await message.download_media(download_path, progress_callback=bar.update_to)
        except CancelledError:
            print("取消下载")
            os.remove(download_path)
            sys.exit()
        except FileReferenceExpiredError:
            if old:
                print('重试失败，退出下载')
                exit(1)
            print('下载超时，重试中')
            channelData = await client.get_entity(int(channel_id))
            newMessages = client.iter_messages(entity=channelData, ids=message.id)
            async for newMessage in newMessages:
                await download_file(client, channel_title, channel_id, newMessage, old=True)
        except Exception as e:
            print("下载出错", e.__class__.__name__)
            os.remove(download_path)
        else:
            os.rename(download_path, file_path)
    else:
        print(f"文件已存在：{file_path}")


class TGDown:
    def __init__(self,api_id,api_hash,phone,username,repo,token,filter,local_target=None,channel=None,tdl=False,tip=None):
        self.client = TelegramClient('TG', api_id, api_hash)
        self.phone = phone
        self.registry = 'github.com'
        self.username = username
        self.repo = repo
        self.token = token
        self.branch = 'main'
        self.local_target = local_target
        self.filter = filter
        self.channel = channel
        self.tdl = tdl # 加速下载工具 docs.iyear.me/tdl  先tdl login -T code
        self.tip = tip # 替换set_version里的newname
        self.gh = [
            'https://slink.ltd/https://raw.githubusercontent.com',
            'https://raw.yzuu.cf',
            'https://raw.nuaa.cf',
            'https://raw.kkgithub.com',
            'https://cors.zme.ink/https://raw.githubusercontent.com',
            'https://git.886.be/https://raw.githubusercontent.com',
            'https://gitdl.cn/https://raw.githubusercontent.com',
            'https://ghp.ci/https://raw.githubusercontent.com',
            'https://gh.con.sh/https://raw.githubusercontent.com',
            'https://ghproxy.net/https://raw.githubusercontent.com',
            'https://github.moeyy.xyz/https://raw.githubusercontent.com',
            'https://gh-proxy.com/https://raw.githubusercontent.com',
            'https://ghproxy.cc/https://raw.githubusercontent.com',
            'https://gh.llkk.cc/https://raw.githubusercontent.com',
            'https://gh.ddlc.top/https://raw.githubusercontent.com',
            'https://gh-proxy.llyke.com/https://raw.githubusercontent.com',
        ]
    def in_git_exist(self,file):
        is_exist = False
        file_url = f'https://ghp.ci/https://raw.githubusercontent.com/{self.username}/{self.repo}/{self.branch}/{file}'
        # 发送 HEAD 请求
        response = requests.head(file_url)
        # 检查响应状态码
        if response.status_code == 200:
            is_exist = True
        return is_exist
    def git_clone(self):
        self.domain = f'https://{self.token}@{self.registry}/{self.username}/{self.repo}.git'
        if os.path.exists(self.repo):
            subprocess.call(['rm', '-rf', self.repo])
        try:
            print(f'开始克隆：git clone https://{self.registry}/{self.username}/{self.repo}.git')
            git.Repo.clone_from(self.domain, to_path=self.repo, depth=1)
        except Exception as e:
            try:
                self.registry = 'gitdl.cn'
                self.domain = f'https://{self.token}@{self.registry}/https://github.com/{self.username}/{self.repo}.git'
                if os.path.exists(self.repo):
                    subprocess.call(['rm', '-rf', self.repo])
                repo = git.Repo.clone_from(self.domain, to_path=self.repo, depth=1)
            except Exception as e:
                print(222222, e)
    def get_local_repo(self):
        # 打开本地仓库，读取仓库信息
        repo = git.Repo(self.repo)
        config_writer = repo.config_writer()
        config_writer.set_value('user', 'name', self.username)
        config_writer.set_value('user', 'email', self.username)
        # 设置 http.postBuffer
        config_writer.set_value('http', 'postBuffer', '73400320')
        config_writer.release()
        # 获取远程仓库的引用
        remote = repo.remote(name='origin')
        # 获取远程分支列表
        remote_branches = remote.refs
        # 遍历远程分支，查找主分支
        for branch in remote_branches:
            if branch.name == 'origin/master' or branch.name == 'origin/main':
                self.branch = branch.name.split('/')[-1]
                break
        # print(f"仓库{self.repo} 主分支为: {self.main_branch}")
        return repo
    def reset_commit(self,repo):
        # 重置commit
        try:
            os.chdir(self.repo)
            # print('开始清理git',os.getcwd())
            repo.git.checkout('--orphan', 'tmp_branch')
            repo.git.add(A=True)
            repo.git.commit(m="update")
            repo.git.execute(['git', 'branch', '-D', self.branch])
            repo.git.execute(['git', 'branch', '-m', self.branch])
            repo.git.execute(['git', 'push', '-f', 'origin', self.branch])
        except Exception as e:
            print('git清理异常', e)
    def git_push(self,repo):
        # 推送并重置commit计数
        # 推送
        print(f'开始推送：git push https://{self.registry}/{self.username}/{self.repo}.git')
        try:
            repo.git.add(A=True)
            repo.git.commit(m="update")
            repo.git.push()
            self.reset_commit(repo)
        except Exception as e:
            try:
                repo.git.execute(['git', 'push', '--set-upstream', 'origin', self.branch])
                self.reset_commit(repo)
            except Exception as e:
                print('git推送异常', e)
    def set_version(self,filename,targetjson):
        newname = self.tip
        if not newname:
            # 取包名中的时间串
            match = re.match(self.filter, filename)
            if match:
                newname = f"{match.group(1)}"
        # 载入FongMi.json文件
        with open(f'{self.local_target}/{targetjson}', 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 添加logo
        data["logo"] = "https://gitdl.cn/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/imgs/zx.gif"
        # 查找 "豆瓣" 对象并追加新的对象
        douban_index = next((index for (index, d) in enumerate(data["sites"]) if d["key"] == "Tg | 豆瓣"), None)
        if douban_index is not None:
            data["sites"][douban_index]["ext"]["siteUrl"] = "http://tgsou.fish2018.us.kg"
            data["sites"][douban_index]["ext"]["channelUsername"] = "tgsearchers"
            item = {
              "key": "当前版本",
              "name": newname,
              "type": 3,
              "api": "csp_TgYunDouBanPan",
              "searchable": 0,
              "changeable": 0,
              "ext": {
                "siteUrl": "http://tgsou.fish2018.us.kg",
                "channelUsername": "tgsearchers",
                "commonConfig": "./json/peizhi.json",
                "filter": "./json/douban.json"
              }
            }
            data["sites"].insert(douban_index + 1, item)
        # 查找 "TG搜索|网盘搜索" 对象并更新 "ext"
        tg_search_index = next((index for (index, d) in enumerate(data["sites"]) if d["key"] == "TgYunPan|本地"), None)
        if tg_search_index is not None:
            data["sites"][tg_search_index]["ext"]["siteUrl"] = "http://tgsou.fish2018.us.kg"
            data["sites"][tg_search_index]["ext"]["channelUsername"] = "tgsearchers"
            items = [
                {
                    "key": "lf_js_p2p",
                    "name": "磁力 | lf_p2p",
                    "type": 3,
                    "searchable": 1,
                    "changeable": 1,
                    "quickSearch": 1,
                    "filterable": 1,
                    "api": "https://ghp.ci/https://raw.githubusercontent.com/fish2018/lib/refs/heads/main/js/lf_p2p2_min.js",
                    "ext": "18+"
                }
            ]
            for item in items:
                data["sites"].insert(tg_search_index + 1, item)

        # 将更新后的数据写回FongMi.json文件
        with open(f'{self.local_target}/{targetjson}', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    def readme(self,name,message=''):
        readme = f'{self.repo}/README.md'
        # 读取 README.md 文件内容
        with open(readme, 'r') as file:
            content = file.read()
        # 定义一个函数来替换匹配到的 URL
        def replace_urls(match):
            new_urls = [f"{gh_base}/{self.username}/{self.repo}/{self.branch}/{name}" for gh_base in self.gh]
            return '```bash\n' + '\n'.join(new_urls) + '\n```'
        # 使用正则表达式查找并替换所有匹配的 URL
        new_content = re.sub(
            r'```bash\s*\n(.*?)\s*```',
            replace_urls,
            content,
            flags=re.DOTALL
        )

        # 写回新的 README.md 文件内容
        with open(readme, 'w') as file:
            file.write(new_content)

    async def down_group(self, client: TelegramClient, chat_id, from_user=None):
        chat_id = await GetChatId(client, chat_id)
        channel_title, messages = await getHistoryMessage(client, chat_id, from_user=from_user)
        # 正则表达式
        pattern = self.filter
        async for message in messages:
            if message is None:
                continue
            # 判定消息中是否存在媒体内容 MessageMediaDocument:文件
            if not isinstance(message.media, (MessageMediaDocument)):
                continue
            # 检查文件名是否匹配
            match = re.match(pattern, message.file.name)
            if match:
                is_exist = self.in_git_exist(message.file.name)
                if is_exist:
                    print('没有更新，无需下载')
                    return
                self.git_clone()
                subprocess.call(f'rm -rf {self.repo}/真心*.zip', shell=True)
                if self.tdl:
                    cmd = f'tdl dl -i zip -u https://t.me/{self.channel.split("/")[-1]}/{message.id} -d {self.repo} --template "{{{{ .FileName }}}}"'
                    subprocess.call(f'{cmd}', shell=True)
                else:
                    await download_file(client, channel_title, chat_id, message, self.repo)
                print(f'TG群组({channel_title}) - 本地包{message.file.name}下载完成')
                self.readme(message.file.name,message=message.message)
                # 更新本地目录中的真心包并解压
                if self.local_target:
                    try:
                        print(f'开始更新{self.local_target}目录文件到最新版本')
                        subprocess.call(
                            f'rm -rf {self.local_target}/* && '
                            f'cp -a {self.repo}/{message.file.name} {self.local_target}/ && '
                            f'cd {self.local_target} && '
                            f'unzip -o -q {message.file.name} && '
                            f'rm -rf {message.file.name}',
                            shell=True
                        )
                        # 修改配置
                        with open(f'{self.local_target}/json/peizhi.json', 'r', encoding='utf-8') as f:
                            cfg = json.load(f)
                            cfg["tgPic"] = "true"
                            with open(f'{self.local_target}/json/peizhi.json', 'w+', encoding='utf-8') as file:
                                json.dump(cfg, file, indent=4, ensure_ascii=False)
                        # 添加版本号
                        self.set_version(filename=message.file.name, targetjson='FongMi.json')
                        for file in [f'{self.local_target}/readme-tg.txt', f'{self.local_target}/readme.txt']:
                            with open(file, 'r', encoding='gb2312') as f:
                                content = f.read()
                                with open(file, 'w', encoding='utf-8') as f:
                                    f.write(content)
                    except Exception as e:
                        print(e)
                # 推送
                repo = self.get_local_repo()
                self.git_push(repo)
                print(f'\n-------------下载地址------------------\n\nhttps://raw.yzuu.cf/{self.username}/{self.repo}/{self.branch}/{message.file.name}')
                break

    def run(self):
        with self.client.start(phone=self.phone):
            self.client.loop.run_until_complete(self.down_group(self.client, self.channel))


if __name__ == '__main__':
    api_id = xxx
    api_hash = 'xxx'
    phone = "xxx"
    channel = 'https://t.me/juejijianghu'
    username = 'fish2018'
    repo = 'ZX'
    token = 'xxx'
    local_target = 'z'
    filter = r"真心(.*)\.zip"
    filter2 = r'tgsou(.*)\.zip'
    tdl = True
    tip = None
    TGDown(api_id,api_hash,phone,username,repo,token,filter,local_target,channel,tdl,tip).run()
