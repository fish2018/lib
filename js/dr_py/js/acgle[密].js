var rule = {
    author:'嗷呜',
    title: 'ACGLE',
    host: 'https://www.avgle.pro/',
    url: '/category/fyclass/p/fypage.html',
    searchUrl: '/search/**.html',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://www.avgle.pro/'
    },
   class_name: '國產自拍&中文字幕&日本有碼&國產情色&微拍福利&日本無碼&國產精品&強姦亂倫&歐美精品&制服誘惑&蘿莉少女&成人動漫&美女主播&亞洲有碼&國產主播&國產視頻&巨乳美乳&歐美極品&空姐模特&無碼專區&自拍偷拍&騎兵有碼&動漫精品&抖陰視頻&日韓無碼&AV明星&歐美情色&女同性戀&國產傳媒&三級倫理&熟女人妻&亞洲無碼',
    class_url: '263&48&269&119&306&270&249&13&260&92&103&274&264&105&268&304&93&266&5&254&98&261&86&25&259&401&265&115&390&84&267&64&45',
    play_parse: true,
    lazy: $js.toString(() => {
        let html = JSON.parse(request(input).match(/r player_.*?=(.*?)</)[1]);
        let link = html.url;
        input = {parse: 0, url: link, header: rule.headers};
    }),
    一级: '#videos .card;img&&alt;img&&src;;.visited&&a&&href',
    二级: '*',
    搜索: '.search-item .col-17;h1&&Text;img&&src;;a:eq(0)&&href',
}