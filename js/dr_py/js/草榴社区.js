var rule = {
	title: '草榴社区',
    //host: 'caoliusq4.shop',
	host: 'https://kkb.sixnicecaoliusq.xyz/',


url: '/index.php/vod/type/id/fyclass/page/fypage',

	
searchUrl: '/index.php/vod/search/page/fypage/wd/**.html',
	filterable:1,
searchable: 1,
	quickSearch: 1,
	headers: {
		'User-Agent': 'PC_UA',
 
	},
	class_parse: '.stui-header__menu&&a;a&&Text;a&&href;/(\\d+)',
	play_parse: true,
	lazy:'',
limit: 20,
	推荐:'*',
	一级: '.stui-vodlist&&li;h4&&Text;.lazyload&&data-original;;a&&href',
	二级:'*',

	//二级:'*',
	搜索:'*',
}