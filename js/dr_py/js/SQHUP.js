var rule ={
            title: 'SQHUP',
            host: 'https://txcy-7oo1.txcy-pu.buzz/index.php',
            url: 'https://txcy-7oo1.txcy-pu.buzz/index.php/vodtype/fyclass-fypage.html',
            //searchUrl: 'https://xn--wf3a.atzectj.net/video-keywords-**.html?page=fypage',
            class_name:'MD系列&导演系列& MDS系列&MDX系列&MDXS系列&MDL系列& MMZ系列&港台三级&日韩三级&欧美三级&禁漫天堂&无码AV&成人综艺&国产精选&91制片厂&其他传媒&果冻&麻豆&JVID&SWAG&91原创',
 class_url:'4&5&6&7&8&46&50&53&58&64&74&78&79&87&89&96&100&101&115&116&10&11&12&13&14&15&45&52&65&71&72&75&76&80&81&91&95&97&103&104&105&106&108&17&18&19&20&22&23&24&27&30&31&40&41&42&54&55&61&66&6768&69&74&84&88&92&93&94&102&110&111&112&33&34&36&47&48&59&62&73&82&83&90&109&113&114&117&118',
  
            //class_parse: 'body&&.tx-wide&&.header&&.nav&&.tx-flex-hc&&li;a&&Text;a&&href;.*/(.*?).html',
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
           // 一级: 'body&&.video-item&&li;img&&src;a&&style;a&&Text;a&&data-url',
                一级: 'body&&.tx-wide&&.row&&li;.f-15&&Text;img&&src;img&&alt;a&&href',
            二级: '*',
            搜索: '.s-tab-main&&li;.js-tongjic&&title;img&&src;.hint&&Text;a&&href;.pay&&Text',
        }
        