//http://55ck.net跳转域名
var rule = {
    title: '黄色仓库',
    host: 'http://8391ck.cc/',
    url: '/vodtype/fyclass-fypage.html',
    searchUrl: '/vodsearch/**----------fypage---.html',
    class_parse: '.stui-pannel__menu&&a[href*=type];a--span&&Text;a&&href;.*/(\\d+).html',
    hikerListCol: "movie_2",
    hikerClassListCol: "movie_2",
    play_parse: true,
    lazy: $js.toString(() => {
  eval(parseDomForHtml(request(input),".stui-player__video&&script&&Html"));
    var urls = player_aaaa.url;
        input = {parse: 0, url: urls, js: ''};
    }),
    推荐: '*',
    一级: '.stui-vodlist&&li:has(a[href*=/vod]);h4&&Text;.lazyload&&data-original;.pic-text&&Text;a&&href',
    二级: '*',
    搜索: '*',
}