var rule = {
    title: 'JAV SB',
    host: 'https://jav.sb/',
    url: '/javtype/fyclass-fypage.html',
    searchUrl: '/vod/search/fypage/wd/**.html',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://jav.sb/'
    },
    class_name: '日本有碼&日本無碼&FC2-PPV&無碼破解&中文字幕&MGS動画&寫真&國產',
    class_url: 'Censored&Uncensored&FC2-PPV&Mosaic_Removed&CHN_SUB&MGS&Adult_IDOL&Asian_Amateur',
    play_parse: true,
    lazy: $js.toString(() => {
        let html = JSON.parse(request(input).match(/r player_.*?=(.*?)</)[1]);
        let link = html.url;
        input = {parse: 0, url: link, header: rule.headers};
    }),
    一级: '.grid&&.thumbnail;img&&alt;img&&data-src;;a:eq(0)&&href',
    二级: '*',
    搜索: '.search-item .col-17;h1&&Text;img&&src;;a:eq(0)&&href',
}