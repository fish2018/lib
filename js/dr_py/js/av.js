var rule ={
            title: 'avtoday',
            host: 'https://avtoday.io/',
            url: 'https://avtoday.io/catalog/fyclass?page=fypage',
            searchUrl: 'https://avtoday.io/search?s=**',
            class_parse: '.nav a;script&&Text;a&&href;.*/(.*?).html',
  class_name:'无码&制服&丝袜&萝莉&多人&动长腿',
  class_url:'无码&制服&丝袜&4萝莉&多人&长腿',
  
                      searchable: 2,
            quickSearch: 0,
            filterable: 0,
            //编码:'GBK',
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
            limit: 6,    图片来源: '@Referer=https://avtoday.io/@User-Agent=Mozilla/5.0 (Linux; Android 12; TAS-AN00 Build/HUAWEITAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36',
            推荐: '.album;.thumbnail;.video-title&&a&&Text;img&&src;.video-duration&&Text;a:eq(0)&&href',
            double: true,
            一级: '.album .thumbnail;.video-title&&a&&Text;.video-card&&img img&&src;.video-duration&&Text;a:eq(0)&&href',
            二级: '*',
            搜索: '*',
        }