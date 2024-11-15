var rule ={
            title: '熊猫AV',
            host: 'https://www.panda1139.sbs/',
            url: '/index.php/vod/type/fyclass/fypage/.html',
            searchUrl: '/index.php/vod/search/fypage/wd/**.html',
            class_name:'国产传媒&国产3级&探花&欧美&三级&动漫',
  class_url:'12&25&8&4&5&6',
  
            //class_parse: '.sitenav li;a&&Text;a&&href;.*/(.*?).html',
            searchable: 2,
            quickSearch: 0,
            filterable: 0,
            headers: {
                'User-Agent': 'MOBILE_UA',
            },
            play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '*',
            double: true,
            一级: 'body&&.row-m-space8&&li;a&&title;img&&src;.item-auxiliary&&Text;a&&href',
            二级: '*',
            搜索: '.s-tab-main&&li;.js-tongjic&&title;img&&src;.hint&&Text;a&&href;.pay&&Text',
        }