var rule = {
    title: '九色',
    host: 'https://rfdxxs.qise100.com/',
    url: 'https://rfdxxs.qise100.com/video/category/fyclass/fypage',
    searchUrl: 'https://rfdxxs.qise100.com/search?keywords=**page=fypage',
        //class_parse:'body&&.list&&.col-30;a&&title;a&&data-href;.*/(.*?).html',
    class_name: '最近更新&高清视频&最近加精&当前最热&最近得分&非付费&91原创&10分钟&20分钟&本月讨论&收藏最多&本月最热&上月最热',
    class_url: 'latest&hd&recent-favorite&hot-list&recent-rating&nonpaid&ori&long-list&longer-list&month-discuss&top-favorite&most-favorite&top-list&top-last',
    searchUrl: '',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'MOBILE_UA',
    },
    timeout: 5000,
    //class_parse: '#uk-nav-header li;a&&Text;a&&href;/(.*?)\.html',
    cate_exclude: '',
    play_parse: true,
    lazy: `js:
let kcode=jsp.pdfh(request(input).match(/<iframe(.*?)</iframe>/)[1]);
let kurl=kcode.match(/url=(.*?)\"/)[1];
if (/m3u8|mp4/.test(kurl)) {
input = { jx: 0, parse: 0, url: kurl }
} else {
input = { jx: 0, parse: 1, url: rule.parse_url+kurl }
}`, 
    double: true,
   推荐: '*',
    一级: 'body&&.video-elem;.title&&Text;.img&&style;.text-dark&&Text;a&&href',
    二级: '*',
     搜索: '.s-tab-main&&li;.js-tongjic&&title;img&&src;.hint&&Text;a&&href;.pay&&Text',
}