var rule = {
author: '小可乐/240701/第一版',
title: '采集大全',
类型: '影视',
host: 'http://cj.liqinyi.top:666',
hostJs: '',
headers: {'User-Agent': 'MOBILE_UA'},
编码: 'utf-8',
timeout: 5000,

homeUrl: '/',
url: '/index.php/vod/showfyfilter.html',
filter_url: '{{fl.area}}{{fl.by}}{{fl.class}}/id/{{fl.cateId}}{{fl.lang}}{{fl.letter}}/page/fypage{{fl.year}}',
detailUrl: '',
searchUrl: '/index.php/vod/search/page/fypage/wd/**.html',
searchable: 1, 
quickSearch: 1, 
filterable: 1, 

class_name: '电影&剧集&综艺&动漫&短剧&更新',
class_url: '1&2&3&4&5&map',
filter_def: {
1: {cateId: '1'},
2: {cateId: '2'},
3: {cateId: '3'},
4: {cateId: '4'},
5: {cateId: '5'},
map: {cateId: 'map'}
},

play_parse: true,
lazy: `js:
let kcode = JSON.parse(request(input).match(/var player_.*?=(.*?)</)[1]);
let kurl = unescape(base64Decode(kcode.url));
if (/\\.(m3u8|mp4)/.test(kurl)) {
input = { jx: 0, parse: 0, url: kurl };
} else {
input = { jx: 0, parse: 1, url: kurl };
}
`,

limit: 9,
double: false,
推荐: '*',
一级: '.vodlist_thumb;a&&title;a&&data-original;.text_right&&Text;a&&href',
二级: {
title: 'h2.title&&Text;.data--span:eq(0)&&Text',
img: '.content_thumb&&a&&data-original',
desc: '.data:eq(1)&&Text;.data:eq(0)&&a:eq(0)&&Text;.data:eq(0)&&a:eq(1)&&Text;.data--span:eq(-2)&&Text;.data--span:eq(-1)&&Text',
content: '.full_text&&span&&Text',
tabs: '.play_source_tab&&a',
tab_text: 'a&&alt',
lists: '.content_playlist:eq(#id)&&a:not([onclick])',
list_text: 'body&&Text',
list_url: 'a&&href',
},
搜索: '*',

filter: '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'
}