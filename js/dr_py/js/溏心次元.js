var rule ={
            title: '溏心次元',
            host: 'https://txcy-7oo1.txcy-pu.buzz/index.php',
            url: 'https://txcy-7oo1.txcy-pu.buzz/index.php/vodtype/fyclass-fypage.html',
            //searchUrl: 'https://xn--wf3a.atzectj.net/video-keywords-**.html?page=fypage',
            class_name:'MD系列&导演系列& MDS系列&MDX系列&MDXS系列&MDL系列& MMZ系列&MAD系列&MDWP系列&MSD系列&MDM恋爱咖啡&MDUS系列&MXJ系列&MKY系列&MAN系列&MCY系列&MDAG系列&MDHT系列&BLX系列&MPG系列&兔子先生&果冻传媒&皇家华人&吴梦梦无套系列&PsychoPorn色控&蜜桃影像传媒&天美传媒&91制片厂&MSM性梦者&叮叮映画&涩会&豚豚创媒&爱妃传媒&辣椒原创&O-STAR&肉肉传媒&渡边传媒&葵心娱乐&红斯灯影像&麻麻传媒&蝌蚪传媒&Pussy Hunter&桃花源&大鸟十八&疯拍系列&KISS糖果屋&小鹏奇啪行&30天解密麻豆&突袭女优计划&女神羞羞研究所&小哥哥艾理&情趣K歌房&淫欲游戏王&麻豆不回家&女优淫娃培训营&狼人插&女优擂台摔角狂热&恋爱巴士&男女优生死斗&情人劫密室逃脱&换妻&你好同学&禁欲小屋&鲍鱼的胜利&性爱自修室&春游记&心动的性号&情趣大富翁&寻宝吧女神&男优练习生&女神体育祭&麻豆高校&野外露初&乌鸦传媒&精东影业&SWAG&星空无限传媒&大象传媒&大象传媒&MINI传媒&糖心&葫芦影业&天马传媒&CCAV成人头条&性视界传媒&SA国际传媒&香蕉传媒&91茄子&EDmosaic&国产片商&节目企划',
 class_url:'4&5&6&7&8&46&50&53&58&64&74&78&79&87&89&96&100&101&115&116&10&11&12&13&14&15&45&52&65&71&72&75&76&80&81&91&95&97&103&104&105&106&108&17&18&19&20&22&23&24&27&30&31&40&41&42&54&55&61&66&6768&69&74&84&88&92&93&94&102&110&111&112&33&34&36&47&48&59&62&73&82&83&90&109&113&114&117&118&32&3',
  
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
        