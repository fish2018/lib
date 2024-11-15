var rule ={
            title: 'avtoday',
            host: 'https://avtoday.io',
            url: '/catalog/fyclass?page=fypage',
            searchUrl: 'https://avtoday.io/search?s=**',
            //class_parse: '.nav a;script&&Text;a&&href;.*/(.*?).html',
  class_name:'无码&制服&丝袜&萝莉&多人&动长腿',
  class_url:'无码&制服&丝袜&4萝莉&多人&长腿',
  
                      searchable: 2,
            quickSearch: 0,
            filterable: 0,
            //编码:'GBK',
            headers: {
                'User-Agent': 'MOBILE_UA',
                'Referer': 'https://avtoday.io'
            },
            play_parse: true,
                      lazy: `js:
let kcode=jsp.pdfh(request(input), 'iframe&&src').replace(/^\\./ ,rule.host);
let kurl=request(kcode).match(/m3u8_url = '(.*?)'/)[1];
if (/m3u8|mp4/.test(kurl)) {
input = {parse: 0, url: kurl, header: rule.headers};
} else {
input = { jx: 0, parse: 1, url: rule.parse_url+kurl }
}`, 
            limit: 6,
            推荐: '.album&&.row;.row&&.thumbnail;.video-title&&Text;img&&src;.video-duration&&Text;a&&href',
            double:true, // 推荐内容是否双层定位
            double: true,
            一级: `js:
            pdfh = jsp.pdfh, pdfa = jsp.pdfa, pd = jsp.pd;
    var d = [];
    let html = request(input, {});
    var list = pdfa(html, '.album&&.thumbnail');
    for (var i = 0; i < list.length; i++) {
        d.push({
            title: pdfh(list[i], '.video-title&&a&&Text'),
            desc: pdfh(list[i], '.video-duration&&Text'),
            pic_url: pdfh(list[i], 'img&&src').replace(/^\\./ ,rule.host),
            url: pdfh(list[i], 'a&&href').replace(/^\\./ ,rule.host),           
        });
    }
setResult(d);`,
            二级: '*',
            搜索: '*',
        }