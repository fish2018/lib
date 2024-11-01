var rule = {
            title: '黄仓库',
            //host: 'http://hsck.net/',
            // homeUrl:'/',
  hostJs: $js.toString(() => {
        HOST = 'http://hsck419.cc/';
let html=request('http://hsck419.cc/');
        let strU = html.match(/strU="(.*?)"/)[1];
        let locationU = strU + HOST.rstrip('/') + '/&p=/';
        //log(locationU);
        let resp = request(locationU, {withHeaders: true, redirect: false});
        HOST = JSON.parse(resp).location;
        
    }),
            url: '/vodtype/fyclass-fypage.html',
            searchUrl: '/vodsearch/-------------.html?wd=**',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 0,//是否启用分类筛选,
            headers: {//网站的请求头,完整支持所有的,常带ua和cookies
                'User-Agent': 'MOBILE_UA',
                 'Cookie': 'searchneed=ok',
            },
     class_name:'日韩&国产&欧美&动漫&日本有码&无码中文字幕&有码中文字幕&日本无码&国产视频&欧美高清&动漫剧情&另类视频',
 class_url:'1&2&3&4&7&8&9&10&15&21&22',

 // class_parse: '.stui-header__menu&&li;a&&Text;a&&href',
            play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '*',
            double: true, // 推荐内容是否双层定位
            一级: '.stui-vodlist&&li;h4&&Text;a&&data-original;.pic-text&&Text&&Text;a&&href',
            二级:'*',
               }