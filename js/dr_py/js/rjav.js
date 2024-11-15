var rule = {
    title: 'RJAV',
    host: 'https://rjav.tv',
    url: '/zh/videotype/fyclass-fypage.html',
    homeUrl: '/zh',
    searchUrl: '/zh/vod/search/page/fypage/wd/**.html',
    headers:{ 'User-Agent': PC_UA},
    searchable: 2,
    quickSearch: 1,
    class_name: 'FC2-PPV&日本無碼&馬賽克破壞&國產&日本有碼&MGS動画&中文字幕&Korean BJ Dance',
    class_url: 'FC2-PPV&JAV_Uncensored&Mosaic_Removed&Asian_Amateur&JAV_Censored&MGS&JAV+CHN.SUBs&Korean_BJ_Dance',
    limit: 6,
    double: true,
    play_parse: true,
    lazy: $js.toString(() => {
        let d = [];
        let url1=jsp.pdfh(request(input),'.info-video-tips script&&Html').replace(/\\/g, '').match(/"url":"(.*?)"/)[1];       
        let aa=JSON.parse(fetch(url1, {headers:{
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "range": "bytes=0-",
            "sec-ch-ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\", \"Microsoft Edge Simulate\";v=\"110\", \"Lemur\";v=\"110\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-fetch-dest": "video",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://rjav.tv/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
          },withHeaders: true,redirect: false})).location 
        input = {
            url: aa,
            parse: 0,
            header: rule.headers
        }
        setResult(d)
    }),
    推荐: '*',
    一级: '.row-space7 li;h2&&Text;img&&src;.ico-right&&Text;a&&href;',
    二级:'*',
    // 二级: {
    // "title": "h2&&Text",
    // "img": "img:eq(0)&&src",
    // "code": ".info-tags:contains('代碼')&&span:eq(1)&&Text",
    // "release_date": ".info-tags:contains('發布日期')&&span:eq(1)&&Text",
    // "duration": ".info-tags:contains('片長')&&span:eq(1)&&Text",
    // "tags": ".info-tags:contains('標籤') a&&Text",
    // "actors": ".info-tags:contains('女優') a&&Text",
    // "play_url": ".row-space20&&div" // 假设视频是通过 iframe 加载的
    // },
    搜索: '.row-space7 li;a&&title;img&&src;.ico-right&&Text;a&&href;',
}