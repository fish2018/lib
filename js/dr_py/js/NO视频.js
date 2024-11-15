var rule = {
    title: 'NO视频',
    host: 'http://www.novipnoad.net',
    //hostJs: 'print(HOST);let html=request(HOST,{headers:{"User-Agent":MOBILE_UA}});let src = jsp.pdfh(html,"ul&&li&&a&&href");print(src);HOST=src.replace("/index.php","")',
    // homeUrl: '/',

    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
   
    filterable: 0,//是否启用分类筛选,
    url: '/fyclass/',

    headers: {//网站的请求头,完整支持所有的,常带ua和cookies
        'User-Agent':'MOBILE_UA',
        // "Cookie": "searchneed=ok"
    },

    timeout: 5000,
    searchUrl: '/?s={wd}',

    //class_name: '电影&剧集&动画&综艺&音乐&短片',
    //class_url: 'movie&TV&anime&shows&music&short',
    class_parse: 'ul.nav-ul-menu li;a&&Text;a&&href;.*/(.*?)/', 

    play_parse: true,
    lazy: '',
    limit: 6,

    推荐: '*',
    double: true, // 推荐内容是否双层定位
    一级: '.video-item .item-thumbnail;a&&title;img&&src;.module-item-note&&Text;a&&href',
    二级: {
          "title": "h1&&Text;.module-info-tag&&Text",
          "img": ".img&&src",
          "desc": ";;;p.data--span:eq(1)&&Text;p.data--span:eq(2)&&Text",
          "content": ".item-content.toggled&&Text",
          "tabs": ".re-box-head h3",
          "lists": ".play_list_box:eq(#id)&&li",
          "list_url": "a&&href"        
        },
        
    搜索: '.movie-list-body&&.vod-search-list;.a&&Text;.lazyload&&data-original;.module-item-note&&Text;a&&href',
}
