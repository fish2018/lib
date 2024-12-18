var rule = {
    模板: '自动',
    模板修改: $js.toString(() => {
        Object.assign(muban.自动.二级, {
            tab_text: 'div--small&&Text',
        });
    }),
    title: '宇航影视[自动]',
    host: 'http://yuhang007.com',
    url: '/index.php/vod/show/id/fyclass/page/fypage.html',
    searchUrl: '/index.php/vod/search/page/fypage/wd/**.html',
    class_parse: '.nav-menu-items&&li;a&&Text;a&&href;/(\\d+)\.html',
    cate_exclude: '今日更新|热榜|资讯',
    搜索: '.module-items .module-search-item;.video-serial&&title;img&&data-src;.video-serial&&Text;.video-serial&&href',
}