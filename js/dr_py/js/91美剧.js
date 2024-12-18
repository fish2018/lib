var rule={
            title: '91美剧',
            host: 'https://mjw21.com/', // homeUrl:'/',
         //   url: '/fyclass/page/fyfilter',
      url:'/category/all_mj/fyclass/page/fypage',      
            searchUrl: '/vodsearch/**----------fypage---.html',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 0,//是否启用分类筛选,
            headers: {//网站的请求头,完整支持所有的,常带ua和cookies
                'User-Agent': 'MOBILE_UA', // "Cookie": "searchneed=ok"
            },
          //  class_parse: '.nav&&.menu-item;a&&Text;a&&href;.*/(.*?).html',
cate_exclude: '明星',
class_name:'科幻片&剧情片&动作片&喜剧片&动画片&奇幻片&恐怖片&悬疑片',
class_url:'kehuanpian&juqingpian&dongzuooian&xijupian&donghuapian&qihuanpian&kongbupian&xuanyipian',  
              play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '*',
            double: true, // 推荐内容是否双层定位
          一级: '.m-movies&&.u-movie;h2;img&&data-original;.zhuangtai&&Text;a&&href',
             // 一级: '.video-content&&.u-movie;h2;img&&data-original;.zhuangtai&&Text;a&&href',
            二级: {
                "title": "h2&&Text;.module-info-tag&&Text",
                "img": ".lazyload&&data-original",
                "desc": ".video_info&&br&&Text;.video_info:eq(1)br&&Text;.video_info:eq(2)br&&Text;.video_info:eq(3)br&&Text;.video_info:eq(4)br&&Text;.video_info:eq(5)br&&Text",
                "content": ".jianjie",
                "tabs": "h4",
                "lists": ".vlink:eq(#id) a"
            },
            搜索: 'body .module-item;.module-card-item-title&&Text;.lazyload&&data-original;.module-item-note&&Text;a&&href;.module-info-item-content&&Text',
        }