var rule = {
    title: '疯AV',
    host: 'https://vipair1.cc/cn/?utm_source=moefuns&utm_medium=link&comesite=moefuns',
    url: 'https://vipair1.cc/cn/list?idx=fypage&sort=fyclass',
    searchUrl: 'https://vipair1.cc/cn/search_result?kw=**',
    searchable: 2,
    quickSearch: 0,
    headers: {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://vipair1.cc/cn/'
    },
    class_name: '巨乳&纪录片&女同志&姐姐&720&HD&ローション・オイル&AV女优&人妻&角色&熟女&按摩&无码&中出&白虎&自拍&乳交&舔鲍&69&口射&美坹&美腿&口交',
    class_url: '1&2&3&A4&&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20&21&22&23',
    play_parse: true,
    lazy: $js.toString(()=>{
    let html =  JSON.parse(request(input).match(/r player_.*?=(.*?)</)[1]);
    let link = html.url
    input={parse:0,url:link,header:rule.headers}
  }),
    一级: 'body&&.oneVideo&&;h5&&Text;img&&src;.fa-heart&&Text;a:eq(0)&&href',
    二级: '*',
    搜索: '.row-space20 .col-17;h1&&Text;img&&src;;a:eq(0)&&href',
}