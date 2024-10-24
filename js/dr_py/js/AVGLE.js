var rule = {
    title: 'AVGLE',
    host: 'https://avgle.to/zh/',
    url: 'https://avgle.to/zh/vtype/fyclass-fypage.html',
    searchUrl: 'https://avgle.to/zh/vod/search/by/up/wd/**.html',
    class_name: '日本有码&日本无码&FC2-PPV&中文字幕&MGS&国产成人&欧美成人&写真&动画',
    class_url: 'Censored&Uncensored&FC2-PPV&JAV_CHN.SUBs&MGS&Asian_Amateur&Western_Porn&Adult_IDOL&Anime',
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
    lazy: $js.toString(() => {
        let html = JSON.parse(request(input).match(/r player_.*?=(.*?)</)[1]);
        let link = html.url; //log(link)
        var html2 = fetch(link, {
            headers: {
                'Referer': 'https://avgle.to/',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
            },
            method: 'GET',
            onlyHeaders: true
        }); //log(html2)
        var play = JSON.parse(html2).url
        input = {
            parse: 0,
            url: play,
            header: rule.headers
        };
    }),
    double: true,
    // 推荐: '列表1;列表2;标题;图片;描述;链接;详情',
    一级: 'body&&.video-img-box;.title&&Text;img&&data-src;a&&Text;a&&href',
    二级: '*',
    搜索: '.s-tab-main&&li;.js-tongjic&&title;img&&src;.hint&&Text;a&&href;.pay&&Text',
}