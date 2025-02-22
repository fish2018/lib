var rule ={
            title: '人人影视筷子',
            host: 'https://kuaizi.cc/',
            url: 'https://kuaizi.cc/vodtype/fyclass-fypage/',
            searchUrl: 'https://kuaizi.cc/vodsearch/**----------fypage---/',
            class_parse: '.mdui-toolbar&&.pc_nav;a&&Text;a&&href;.*/(.*?)/',
            searchable: 2,
            quickSearch: 0,
            filterable: 0,
            headers: {
                'User-Agent': 'PC_UA',
            },
            play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '.index_vod;.swiper-slide;a&&title;.lazyload&&data-src;span&&Text;a&&href',
            double: true,
            一级: '.vod_item li;.star-up-name&&Text;.lazy&&data-original;span&&Text;a&&href',
            二级: {
                title: 'h1&&Text',
                img: '.vodlist_thumb&&data-original',
                desc: '.info_text&&.inline_item:eq(0)&&Text;.info_text&&.inline_item:eq(1)&&Text;.info_text&&.inline_item:eq(2)&&Text;.info_text&&.inline_item:eq(3)&&Text',
                content: 'info_text p',
                tabs: '.mdui-panel-item-title',
                lists: '.mdui-panel-item-body:eq(#id) .mdui-btn-raised',
            },
            搜索: '*',
        }