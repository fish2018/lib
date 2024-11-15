	var rule = {
            title: '综合直播',
            host: 'https://buap.770xx.vip/',

     hostJs:'print(HOST);let html=request(HOST,{headers:{"User-Agent":PC_UA}});HOST = jsp.pdfh(html,".login-txt&&a&&href");log(HOST);',
	
	
            
          url:'fyclassfyfilter.html',
	filterable:1,
	filter_url:'{{fl.cateId}}/{{fl.class}}',
	filter: {
		
"zb/?ju=yzzb/zb":[
{
"key":"class",
"name":"直播列表",
"value":[
{"n":"亚洲直播","v":"gwzb"},
{"n":"中文直播","v":"cnzb"},
{"n":"日本直播","v":"ryzb"},
{"n":"越南直播","v":"yyzb"},
{"n":"欧美直播","v":"omzb"},
{"n":"俄国直播","v":"egzb"},
{"n":"乌克兰直播","v":"wkl"}
]
}],
"zb/?ju=xxj/zb":[
{
"key":"class",
"name":"",
"value":[
{"n":"卡哇伊直播","v":"kwy"},
{"n":"咪狐直播","v":"mh"},
{"n":"蜜桃直播","v":"mt"},
{"n":"小妲己直播","v":"xdj"},
{"n":"LOVE直播","v":"love"},
{"n":"番茄直播","v":"fq"},
{"n":"77直播","v":"qq"},
{"n":"依依直播","v":"yy"},
{"n":"日出直播","v":"rc"},
{"n":"彩虹直播","v":"ch"},
{"n":"久久直播","v":"jj"}
]
},
{
"key":"class",
"name":"",
"value":[
{"n":"亚米直播","v":"ym"},
{"n":"恋蝶直播","v":"ld"},
{"n":"夜妖姬直播","v":"yyj"},
{"n":"套路直播","v":"tl"},
{"n":"樱花直播","v":"yh"},
{"n":"享色直播","v":"xs"},
{"n":"红浪漫直播","v":"hlm"},
{"n":"金鱼直播","v":"jy"},
{"n":"桃花直播","v":"th"},
{"n":"花房直播","v":"hf"},
{"n":"小仙女直播","v":"xxn"}
]
},
{
"key":"class",
"name":"",
"value":[
{"n":"视觉秀直播","v":"sjx"},
{"n":"小天使直播","v":"xts"},
{"n":"彩云直播","v":"cy"},
{"n":"咪咪直播","v":"mm"},
{"n":"娇媚直播","v":"jm"},
{"n":"黄瓜直播","v":"hg"},
{"n":"色趣直播","v":"sq"},
{"n":"糯米直播","v":"nm"},
{"n":"小蜜蜂直播","v":"xmf"},
{"n":"小红帽直播","v":"xhm"},
{"n":"桃花运直播","v":"thy"}
]
},
{
"key":"class",
"name":"",
"value":[
{"n":"苦瓜直播","v":"kg"},
{"n":"爱爱你直播","v":"aan"},
{"n":"樱花雨直播","v":"yh"},
{"n":"盘他直播","v":"pt"},
{"n":"夜色直播","v":"ys"},
{"n":"蝴蝶直播","v":"hd"},
{"n":"小天仙直播","v":"xtx"},
{"n":"杏趣直播","v":"xq"},
{"n":"小坏蛋直播","v":"xhd"},
{"n":"飘雪直播","v":"px"},
{"n":"樱桃直播","v":"yt"},
{"n":"奥斯卡直播","v":"ask"},
{"n":"兔女郎直播","v":"tnl"},
{"n":"花仙子直播","v":"hxz"},
{"n":"小性感直播","v":"xxg"}
]
}]
},



  searchUrl: '/sa**/page/fypage.html',
            searchable: 2,
            quickSearch: 0,
            
            headers: {
                'User-Agent': 'MOBILE_UA',
                 'Cookie': 'searchneed=ok',
            },
 class_name:'外国直播&中国直播',
 class_url:'zb/?ju=yzzb/zb&zb/?ju=xxj/zb',
            play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '*',
            double: true, 
            一级: '.list-videos&&.item;a&&title;img&&data-original;.duration&&Text;a&&href',
            二级:'*',
            搜索:'*',
               }