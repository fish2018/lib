var rule = {
    title: '农村少妇',
            host: 'https://brourou.com/',
            url: 'vodlist/fyclass---fyarea-fypage.shtml',
            searchUrl: 'vodlist/--**-latest-fypage.shtml',
            class_parse: 'body&&.pager&&li;a&&Text;a&&href;list/(.*?)---',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'PC_UA',
    },
    timeout: 5000,
    play_parse: true,
    //lazy: '*', 
    lazy: $js.toString(() => {
        let html = request(input);
        if (/m3u8/.test(html)){
            let link = html.match(/http.*?m3u8/)[0];
            input = {parse: 0, url: link, header: rule.headers}
        }else{
            let link = request(pdfh(html,'iframe&&src')).match(/setVideoHLS\(\'(http.*?m3u8)/)[1];
            input = {parse: 0, url:link }
        };
    }),
    
    
    一级: '.row&&.col-xs-12;a&&title;img&&data-original;.duration&&Text;a&&href',
    二级: {
        title: '.page-title&&Text',
        img: '',
        desc: '',
        content: '.list-unstyled&&li',
        tabs: '',
        lists: '.col-md-8&&.playbtn',
  },
    搜索: '*',
}