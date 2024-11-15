var rule ={
            title: 'X6AV',
            host: 'https://x6av.com/',
            url: 'https://x6av.com/e/action/ListInfo/index.php?page=fypage&classid=fyclass',
            searchUrl: 'https://x6av.com/e/search/result/index.php?page=page&searchid=**
            //class_parse: 'body&&.nav&&.nav-main&&li;a&&Text;a&&href;.*/(.*?)/',
 class_name:'国产&传媒&日韩&动漫&欧美&吃瓜',    
 class_url:'guochan&chuanmei&rihan&dongman&oumei&chigua',      
            searchable: 2,
            quickSearch: 0,
            filterable: 0,
            headers: {
                'User-Agent': 'MOBILE_UA',
            },
            play_parse: true,
                                  lazy: `js:
let kcode=jsp.pdfh(request(input).match(/<iframe(.*?)</iframe>/)[1]);
let kurl=kcode.match(/url=(.*?)\"/)[1];
if (/m3u8|mp4/.test(kurl)) {
input = { jx: 0, parse: 0, url: kurl }
} else {
input = { jx: 0, parse: 1, url: rule.parse_url+kurl }
}`, 
            limit: 6,
            推荐: 'body&&.videos-container&&.th;img&&src;a&&Text;.th-description&&Text;a&&href',
            double: true,
            一级: 'body&&.videos-container&&.th;img&&src;a&&Text;.th-description&&Text;a&&href',
            二级:'*',
            搜索: '*',
        }