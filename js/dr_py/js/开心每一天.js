var rule = {
	title: '18JTV',
    host: 'https://new.xfplink.com/18302/',
	
hostJs:`print(HOST);let html=request(HOST,{headers:{"User-Agent":MOBILE_UA}});
	let src = jsp.pdfh(html,"body&&.article-content&&a:eq(2)&&href")||jsp.pdfh(html,"body&&.article-content&&a:eq(2)&&Text");
	if(!src.startsWith('http')){src='https://'+src};print("抓到主页:"+src);HOST=src`,
	

url: '/t/fyclass-fypage/',

	
searchUrl: '/s/nid/1/page/fypage/sid/1/wd/**/',
	filterable:1,
searchable: 1,
	quickSearch: 1,
	headers: {
		'User-Agent': 'PC_UA',
 
	},
	  class_name:'国产&日韩&欧美&伦理&动漫&国产自拍&主播诱惑&探花约炮&偷拍偷窥&乱伦侵犯&网爆吃瓜&短视频&传媒剧情&日韩自拍&日韩无码&中文字幕&av解说&换脸明星&无码字幕&港台伦理&日韩伦理&欧美伦理&剧集动漫&3D动漫&次元动漫&',
   class_url:'1&2&3&4&16&5&6&7&8&9&10&11&12&12&14&15&17&18&19&21&22&23&29&30&31&26&27&28',



	play_parse: true,
	lazy:'',
limit:40,
	推荐:'*',
	一级: '.list li;a&&title;.lazy&&data-original;span&&Text;a&&href',
	
	二级:'*',
	搜索:'*',
}