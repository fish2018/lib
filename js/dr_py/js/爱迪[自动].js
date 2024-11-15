var rule = {
    模板: '自动',
    模板修改: $js.toString(() => {
        muban.自动.二级.tabs = '.playlist h3';
    }),
    title: '爱迪[自动]',
    host: 'https://www.idiitv.com',
    url: '/idys/fyfilter.html',
    filterable: 1,//是否启用分类筛选,
    filter_url: '{{fl.cateId}}{{fl.area}}/page/fypage{{fl.year}}',
    filter: 'H4sIAAAAAAAAA6tWSslMzKvMzEtXsoquVspOrVSyUkpOLEn1TFHSUcpLzE0F8p92tD3fuBvIL0vMKU0FK8wDCbeueNm8AiQM5MCNqdWBynateLJ3zvPOdpiCqgKE3LQ5TzuXI+QqshByzzs2PmtuRcglFiLJLZ/4dOduhFx2BkLuWeOEZw3TkOSSkOzrXI5iZhaSmc86ZjzZ1YmQq0Jy5/Ndq57unYqkLzOntADoUaXa2NpYHbCfizMys0qpEHYQc+AOnr33ya7lQGdDVaQnZyEcvGP90/4NSHIlSHLTl76cvxIhV5SBJLd1+9Ml0xByGeVZYH/UAgBhoV3wBAIAAA==',
    filter_def: {
        dianying: {cateId: 'dianying'},
        dianshiju: {cateId: 'dianshiju'},
        zongyi: {cateId: 'zongyi'},
        dongmna: {cateId: 'dongmna'}
    },
    searchUrl: '/idcz**/page/fypage.html',
}