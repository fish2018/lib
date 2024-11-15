var rule={
            title: 'CM',
            host: 'https://cmdmw.com/',
            url: 'https://cmdmw.com/mm/fyclass--------fypage---.html',
            searchUrl: 'https://cmdmw.com/video/so**/page/fypage.html',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 0,//是否启用分类筛选,
            headers: {//网站的请求头,完整支持所有的,常带ua和cookies
                'User-Agent': 'MOBILE_UA', // "Cookie": "searchneed=ok"
            },
            class_parse: '.sub-menu li;a&&Text;a&&href;.*/(.*?).html',
  class_name:'短剧&电影&电视剧&综艺&动漫',
  class_url:'dj&dy&dsj&zy&dm',     
      cate_exclude: '明星',
            play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '.row;.a0igltx368;.text-overflow&&title;.lazyload&&data-original;.text-nowrap&&Text;a&&href',
            double: true, // 推荐内容是否双层定位
            一级: '.row .col-xs-4;.text-overflow&&title;.lazyload&&data-original;.text-nowrap&&Text;a&&href',
            二级: {
                "title": "h1&&Text",
                "img": ".myui-content__thumb .lazyload&&data-original",
                "desc": ".lw1xqqybpi li:eq(0)&&Text;.detail-info-text p:eq(0)&&Text;.detail-info-text p:eq(1)&&Text;.lw1xqqybpi li:eq(1)&&Text;.lw1xqqybpi li:eq(2)&&Text",
                "content": ".entry-content&&Text",
                "tabs": ".n4kn6iq3w2 a",
                "lists": ".ewave-playlist-content:eq(#id) a"
            },
            搜索: '.erj15g5vek;.lazyload&&title;.lazyload&&data-original;.i5yvdvghl2&&p:eq(2)&&Text;a&&href;.cr046qcnkh&&Text',
        }
        