var rule = {
    title:'火车36小时',
    host:'https://6m8.36huo165che.xyz/topic/?https://wangbaomen29.buzz/',
    searchUrl: '/vodsearch/-------------.html?wd=**',
    homeUrl:'',
    url:'/vodtype/fyclass-fypage.html',
    headers:{
        'User-Agent':'MOBILE_UA'
    },
    searchable:0,
    quickSearch:0,
    timeout:5000,
      推荐: '.vods&&.vod;a&&title;img&&data-original;div&&Text;a&&href',
    class_name:'国产视频&中文字幕&国产传媒&日本有码&日本无码&欧美无码&强奸乱伦&制服诱惑&直播主播&糖心Vlog&激情动漫&抖阴视频&女优明星&网-曝-门&伦理三级&AV解说&SM调教&萝莉少女&极品媚黑&女同性恋',
    class_url:'6&7&8&9&10&11&12&20&21&22&23&63&24&25&26&30&31&37&32&33',

  //class_parse:'.nav&&a;a&&Text;a&&href',
    limit:5,
    play_parse:true,
    lazy:'',
    一级:'.vods&&.vod;a&&title;img&&data-original;div&&Text;a&&href',
        二级: {
                "title": "h3&&Text;.module-info-tag&&Text",
                "img": ".img&&data-original",
                "desc": ".module-info-item:eq(1)&&Text;.module-info-item:eq(2)&&Text;.module-info-item:eq(3)&&Text",
                "content": ".stui-content__thumb:eq(1)&&Text",
                "tabs": ".stui-content__detail&&a",
                "lists": ".btn-primary:eq(#id) a"
            },
                   搜索: '.vods&&.vod;a&&title;img&&data-original;div&&Text;a&&href',

}