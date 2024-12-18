function main(item) {
    let url = item.url;
    const id = getQuery.call({ url: url, key: "id" }) || 'zh';

    const n = {
        'zh': 16, // 杭州综合
        'xh': 17, // 西湖明珠
        'sh': 18, // 杭州生活
        'qt': 20, // 青少体育
        'ys': 21, // 杭州影视
        'ds': 22, // 杭州导视
        'r1': 23, // FM90.7MHz
        'r2': 24, // FM89.0MHz
        'r3': 25, // FM105.4MHz
        'r4': 26, // FM91.8MHz
        'r5': 27, // AM954KHz
        'hl': 28, // Hoolo(综合)
        'r6': 31, // FM100.4MHz
        'fy': 32, // 富阳综合
    };

    const requestUrl = 'https://mapi.hoolo.tv/api/v1/channel_detail.php?channel_id=' + n[id];

    let headers = { 'User-Agent': 'Mozilla/5.0' };
    let res;
    try {
        res = get.call({url: requestUrl, headers: JSON.stringify(headers)});
    } catch (e) {
        return JSON.stringify({ error: `获取页面失败: ${e.message}`, url: requestUrl });
    }

    if (!res) {
        return JSON.stringify({ error: "获取页面返回空内容", url: requestUrl });
    }

    let data = JSON.parse(res);
    let m3u8, sd_m3u8;
    for (const stream of data[0].channel_stream) {
        if (stream.stream_name === 'hd') {
            m3u8 = stream.m3u8;
            break;
        } else if (stream.stream_name === 'sd') {
            sd_m3u8 = stream.m3u8;
        }
    }

    m3u8 = m3u8 || sd_m3u8;

    if (m3u8) {
        return JSON.stringify({ url: m3u8 });
    } else {
        return JSON.stringify({ error: "未找到合适的流", response: data });
    }
}
