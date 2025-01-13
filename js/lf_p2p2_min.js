import _0x390aa4 from 'assets://js/lib/cheerio.min.js';
import 'assets://js/lib/crypto-js.js';
import { gbkTool } from 'assets://js/lib/gbk.js';
const _0x12b93f = '';
const _0x3987f7 = {
    'pgFail': [],
    'headers': [
        {
            'Referer': _0x12b93f,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
        },
        {
            'Referer': _0x12b93f,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
        },
        {
            'Referer': _0x12b93f,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        },
        {
            'Referer': _0x12b93f,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/115.0.0.0'
        },
        {
            'Referer': _0x12b93f,
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/115.0.0.0'
        }
    ],
    'pic_headers': ['@Referer=' + _0x12b93f],
    'br_requests': [],
    'br_contents': [],
    'player': {},
    'filter': {},
    'second_res': []
};
function _0x50af14(_0x332eae) {
    _0x48072a();
    let _0x1f7cd9 = { 'class': [] };
    if (_0x332eae) {
        _0x1f7cd9.filters = _0x3987f7.filter;
    }
    _0x1f7cd9.class.push({
        'type_id': 'P2P',
        'type_name': '\uD83D\uDFE2 配合搜索源(比如lf_search.js)使用或者单独搜索使用'
    });
    return JSON.stringify(_0x1f7cd9);
}
function _0x4c2491() {
    _0x48072a();
    _0x488c85 = { 'list': _0xe24432 };
    return JSON.stringify(_0x488c85);
}
function _0x1e7494(_0x221c22, _0x524e46, _0x4d40b3, _0xe05446) {
    _0x48072a();
    let _0x496c3e = [];
    _0x524e46 = parseInt(_0x524e46);
    if (_0x29284a(_0x524e46, 1))
        return;
    if (_0x221c22.match(/www\.mp4us\.com/))
        _0x11eff6.category(_0x221c22, _0x496c3e);
    else {
        if (_0x221c22.match(/www\.66ss\.org/))
            _0x522eb9.category(_0x221c22, _0x496c3e);
        else {
            if (_0x221c22.match(/www\.kuba222\.com/) || _0x221c22.match(/kubady#(\d+)/m))
                _0x3c1fc6.category(_0x221c22, _0x496c3e);
            else {
                if (_0x221c22.match(/jp\.netcdn\.space/))
                    _0x4c2007.category(_0x221c22, _0x496c3e);
                else {
                    if (_0x221c22.match(/javmulu\.net/))
                        _0x3796cb.category(_0x221c22, _0x496c3e);
                    else {
                        if (_0x221c22.match(/www\.2bt0\.com/) || _0x221c22.match(/butailing#(\d+)/m))
                            _0xefb5f8.category(_0x221c22, _0x496c3e);
                        else {
                            if (_0x221c22.match(/xunlei8\.cc/))
                                _0x3dd8f6.category(_0x221c22, _0x496c3e);
                            else
                                _0x221c22.match(/missav/) && _0x2d5787.category(_0x221c22, _0x496c3e);
                        }
                    }
                }
            }
        }
    }
    _0x515665 = {
        'list': _0x496c3e,
        'page': _0x524e46,
        'pagecount': 999,
        'limit': 100,
        'total': 999
    };
    return JSON.stringify(_0x515665);
}
async function _0xf39aba(_0x2c2e28, _0x13f856, _0x39a575) {
    _0x48072a();
    try {
        let _0x3b9123 = [];
        let _0x5de82b = 999;
        let _0x4837b0 = [];
        let _0x15848f = [];
        let _0x58aaa4 = [];
        let _0x49032e = [];
        let _0x1e531a = [];
        let _0x12df94 = [];
        let _0x5bb059 = [];
        let _0xd9744f = [];
        false ? (console.log('[提示]'), console.log('[提示][增强模式搜索(18+)]')) : (console.log('[提示]'), console.log('[提示][使用普通模式搜索]'));
        if (_0x13f856) {
            _0x38fe63 = { 'list': [] };
            return JSON.stringify(_0x38fe63);
        }
        _0x39a575 == undefined && (_0x39a575 = '1');
        let _0x500100 = '';
        _0x2c2e28.match(/(\w+-\d+)\s?/m) ? _0x500100 = _0x2c2e28.match(/(\w+-\d+)\s?/m)[1] : _0x500100 = _0x2c2e28;
        let _0x5baeca = {
            'url': 'https://avmoo.cfd/cn/search/' + _0x500100 + '/page/' + _0x39a575,
            'options': {
                'headers': {
                    'Referer': 'https://avmoo.cfd/cn/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                }
            }
        };
        if (!false)
            _0x5baeca = undefined;
        else {
            if (_0x4c2007.fail[_0x2c2e28] && _0x4c2007.fail[_0x2c2e28].stat)
                _0x5baeca = undefined;
            else
                _0x39a575 > 1 && _0x4c2007.fail[_0x2c2e28] && _0x39a575 >= _0x4c2007.fail[_0x2c2e28].fpg && (_0x5baeca = undefined);
        }
        let _0x2b6983 = {
            'url': 'https://javmulu.net/index/search.html?name=' + _0x500100 + '&page=' + _0x39a575,
            'options': {
                'headers': {
                    'Referer': 'https://javmulu.net/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                }
            }
        };
        if (!false)
            _0x2b6983 = undefined;
        else {
            if (_0x3796cb.fail[_0x2c2e28] && _0x3796cb.fail[_0x2c2e28].stat)
                _0x2b6983 = undefined;
            else
                _0x39a575 > 1 && _0x3796cb.fail[_0x2c2e28] && _0x39a575 >= _0x3796cb.fail[_0x2c2e28].fpg && (_0x2b6983 = undefined);
        }
        let _0xe90b18 = '';
        _0x2c2e28.match(/(\w+-?\d+)\s?/m) ? _0x2c2e28.match(/(\w+-\d+)\s?/m) ? _0xe90b18 = _0x2c2e28.match(/(\w+-\d+)\s?/m)[1] : _0xe90b18 = _0x2c2e28.split(' ')[1] : _0xe90b18 = _0x2c2e28;
        let _0x50115a = {
            'url': 'https://missav.ws/cn/search/' + _0xe90b18 + '?page=' + _0x39a575,
            'options': {
                'headers': {
                    'Referer': 'https://missav.ws/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                }
            }
        };
        if (!false)
            _0x50115a = undefined;
        else {
            if (_0x2d5787.fail[_0x2c2e28] && _0x2d5787.fail[_0x2c2e28].stat)
                _0x50115a = undefined;
            else
                _0x39a575 > 1 && _0x2d5787.fail[_0x2c2e28] && _0x39a575 >= _0x2d5787.fail[_0x2c2e28].fpg && (_0x50115a = undefined);
        }
        let _0x46af7a = {
            'url': 'https://www.mp4us.com/search/' + _0x2c2e28 + '-' + _0x39a575 + '.html',
            'options': {
                'headers': {
                    'Referer': 'https://www.mp4us.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                }
            }
        };
        if (_0x11eff6.fail[_0x2c2e28] && _0x11eff6.fail[_0x2c2e28].stat)
            _0x46af7a = undefined;
        else
            _0x39a575 > 1 && _0x11eff6.fail[_0x2c2e28] && _0x39a575 >= _0x11eff6.fail[_0x2c2e28].fpg && (_0x46af7a = undefined);
        _0x39a575 == '1' ? _0x17d66e = {
            'url': 'https://www.66ss.org/e/search/index.php',
            'options': {
                'redirect': 0,
                'headers': {
                    'Referer': 'https://www.66ss.org/',
                    'Content-Type': 'application/x-www-form-urlencoded;',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                },
                'method': 'POST',
                'body': 'show=title&tempid=1&tbname=article&mid=1&dopost=search&submit=&keyboard=' + encodeURI(_0x2c2e28)
            }
        } : _0x17d66e = {
            'url': 'https://www.66ss.org/e/search/result/index.php?page=' + (_0x39a575 - 1) + '&searchid=' + _0x522eb9.searchid,
            'options': {
                'headers': {
                    'Referer': 'https://www.66ss.org/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                }
            }
        };
        if (_0x522eb9.fail[_0x2c2e28] && _0x522eb9.fail[_0x2c2e28].stat)
            _0x17d66e = undefined;
        else
            _0x39a575 > 1 && _0x522eb9.fail[_0x2c2e28] && _0x39a575 >= _0x522eb9.fail[_0x2c2e28].fpg && (_0x17d66e = undefined);
        let _0x12f4b6 = {
            'url': 'https://www.kuba222.com/index.php?m=vod-search-pg-' + _0x39a575 + '-wd-' + _0x2c2e28 + '.html',
            'options': {
                'headers': {
                    'Referer': 'https://www.kuba222.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
                }
            }
        };
        if (_0x3c1fc6.fail[_0x2c2e28] && _0x3c1fc6.fail[_0x2c2e28].stat)
            _0x12f4b6 = undefined;
        else
            _0x39a575 > 1 && _0x3c1fc6.fail[_0x2c2e28] && _0x39a575 >= _0x3c1fc6.fail[_0x2c2e28].fpg && (_0x12f4b6 = undefined);
        _0xefb5f8.md == '' && _0xefb5f8.get_md('https://www.2bt0.com/search.php?sb=' + _0x2c2e28);
        let _0x1dda61 = {
            'url': 'https://www.2bt0.com/search.php?page=' + _0x39a575 + '&sb=' + _0x2c2e28 + '&sg=1',
            'options': {
                'headers': {
                    'Cookie': _0xefb5f8.cookie,
                    'Referer': 'https://www.2bt0.com/',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                },
                'method': 'POST',
                'body': 'md=' + _0xefb5f8.md
            }
        };
        if (_0xefb5f8.fail[_0x2c2e28] && _0xefb5f8.fail[_0x2c2e28].stat)
            _0x1dda61 = undefined;
        else
            _0x39a575 > 1 && _0xefb5f8.fail[_0x2c2e28] && _0x39a575 >= _0xefb5f8.fail[_0x2c2e28].fpg && (_0x1dda61 = undefined);
        let _0x34bb39 = {
            'url': 'https://xunlei8.cc/s/' + encodeURI(_0x2c2e28) + '.html',
            'options': {
                'headers': {
                    'Referer': 'https://xunlei8.cc/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                }
            }
        };
        if (_0x3dd8f6.fail[_0x2c2e28] && _0x3dd8f6.fail[_0x2c2e28].stat)
            _0x34bb39 = undefined;
        else
            _0x39a575 > 1 && (_0x34bb39 = undefined);
        _0x3987f7.br_requests = [
            _0x5baeca,
            _0x2b6983,
            _0x50115a,
            _0x46af7a,
            _0x17d66e,
            _0x12f4b6,
            _0x1dda61,
            _0x34bb39
        ];
        _0x3987f7.br_contents = [];
        let _0x402732 = true;
        for (let _0x54e73d = 0; _0x54e73d < _0x3987f7.br_requests.length; _0x54e73d++) {
            _0x3987f7.br_requests[_0x54e73d] && (_0x402732 = false);
        }
        _0x402732 && (_0x5de82b = _0x39a575 - 1);
        await _0x14ad14(_0x3987f7.br_requests, _0x3987f7.br_contents);
        try {
            _0x11eff6.search(_0x3987f7.br_contents[3], _0x2c2e28, _0x39a575, _0x4837b0);
        } catch (_0x19b419) {
            console.log(_0x19b419.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x19b419.stack);
            _0x4837b0 = [];
        }
        try {
            _0x522eb9.search(_0x3987f7.br_contents[4], _0x2c2e28, _0x39a575, _0x15848f);
        } catch (_0x267740) {
            console.log(_0x267740.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x267740.stack);
            _0x15848f = [];
        }
        try {
            _0x3c1fc6.search(_0x3987f7.br_contents[5], _0x2c2e28, _0x39a575, _0x58aaa4);
        } catch (_0x28b78a) {
            console.log(_0x28b78a.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x28b78a.stack);
            _0x58aaa4 = [];
        }
        try {
            _0xefb5f8.search(_0x3987f7.br_contents[6], _0x2c2e28, _0x39a575, _0x49032e);
        } catch (_0x4a7070) {
            console.log(_0x4a7070.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x4a7070.stack);
            _0x49032e = [];
        }
        try {
            _0x3dd8f6.search(_0x3987f7.br_contents[7], _0x2c2e28, _0x39a575, _0x1e531a);
        } catch (_0x248f15) {
            console.log(_0x248f15.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x248f15.stack);
            _0x1e531a = [];
        }
        try {
            _0x4c2007.search(_0x3987f7.br_contents[0], _0x2c2e28, _0x39a575, _0x12df94);
        } catch (_0x2788d3) {
            console.log(_0x2788d3.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x2788d3.stack);
            _0x12df94 = [];
        }
        try {
            _0x3796cb.search(_0x3987f7.br_contents[1], _0x2c2e28, _0x39a575, _0x5bb059);
        } catch (_0x43dfe4) {
            console.log(_0x43dfe4.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x43dfe4.stack);
            _0x5bb059 = [];
        }
        try {
            _0x2d5787.search(_0x3987f7.br_contents[2], _0x2c2e28, _0x39a575, _0xd9744f);
        } catch (_0x12d043) {
            console.log(_0x12d043.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x12d043.stack);
            _0xd9744f = [];
        }
        _0x38b67e(_0x3b9123, _0x4837b0, _0x15848f, _0x58aaa4, _0x49032e, _0x1e531a, _0x12df94, _0x5bb059, _0xd9744f);
        _0x38fe63 = {
            'list': _0x3b9123,
            'pagecount': _0x5de82b
        };
        return JSON.stringify(_0x38fe63);
    } catch (_0x4e51b0) {
        console.log(_0x4e51b0.toString().replace(/(.*?Error): /, '[$1]: ') + ', ' + _0x4e51b0.stack);
    }
}
function _0x15909a(_0x217ee0) {
    let _0x13164b = [];
    if (_0x217ee0 == 'P2PTest') {
        let _0x3f45e7 = [
            'magnet$magnet:?xt=urn:btih:b038e7f34ae7b479601bc82e5121d28f4e5ea4d7&dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1dygod.org.%e5%b0%8f%e7%be%8e%e4%ba%ba%e9%b1%bc.2023.BD.1080P.%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97.mkv&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce',
            'magnet$magnet:?xt=urn:btih:25DLYXPUOD7D5BGODN2PTVNX5Q4DRB7P&dn=%5B%E9%98%B3%E5%85%89%E7%94%B5%E5%BD%B1-www.dygod.org%5D%E5%AE%89%E4%B9%90%E4%BC%A0-01~04&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&xl=1594081748',
            'https://dy.town/uploads/download/file/15824/%E5%A6%88%E5%A6%88%E7%9A%84%E6%9C%8B%E5%8F%8B.Mother.s.Friend.2015.HD720P.X264.AC3.Korean.CHS.rarbt.torrent',
            'magnet:?xt=urn:btih:5258E0FF7992FD52BD3C71D05F8E9B80598E3654&dn=妈妈的朋友.Mother.s.Friend.2015.HD720P.X264.AC3.Korean.CHS.rarbt',
            'magnet:?xt=urn:btih:EEAA8400C5FC5431F0AC3AE965938848F8F89A31&dn=青春学堂2.寄生和野史.청춘학당2.기생난입야사.2016.HD720P.X264.rarbt',
            'thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjQ3N2RmMjA4YzBiMWVmYmVlYWEzMzg2MWRhMWI1YjUwMzM1OTA4YTJaWg==',
            'magnet:?xt=urn:btih:4EF7643B579538207A80AD78746AC7316A9F9408&dn=The%20Invincible%20Iron%20Man%20(2007)%20720p%20BluRay-LAMA&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.bittor.pw%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Feddie4.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce'
        ];
        let _0x2495b8 = {
            'vod_id': _0x217ee0,
            'vod_play_url': _0x3f45e7[6]
        };
        _0x3a14a9 = { 'list': [_0x2495b8] };
        return JSON.stringify(_0x3a14a9);
    }
    if (_0x217ee0.match(/missav/))
        _0x37ecd3 = JSON.parse(_0x217ee0);
    else
        _0x217ee0.match(/\$\$\$/) ? (_0x4c2007.detail(_0x217ee0, _0x13164b), _0x37ecd3 = _0x13164b[0]) : _0x37ecd3 = JSON.parse(_0x217ee0);
    _0x37ecd3.vod_remarks = '\uD83D\uDFE2 本源仅供学习交流\uFF0C请在24小时后删除\uFF0C谢谢合作\uFF01';
    _0x3a14a9 = { 'list': [_0x37ecd3] };
    return JSON.stringify(_0x3a14a9);
}
function _0x38865a(_0x57e52a, _0x8b5001, _0x22dfb3) {
    let _0x37581f = '';
    let _0x5407f0 = '';
    if (_0x8b5001.match(/akamai-content-network/m)) {
        _0x37581f = JSON.stringify({ 'Referer': 'https://missav.ws/' });
    }
    _0xde8dfb = {
        'parse': '0',
        'jx': '0',
        'header': _0x37581f,
        'playUrl': '',
        'url': _0x8b5001
    };
    if (_0x5407f0) {
        _0xde8dfb.format = _0x5407f0;
    }
    return JSON.stringify(_0xde8dfb);
}
function _0x48072a() {
    setTimeout(() => {
        console.log('[检测]当前的TVBox壳子支持异步\uFF01请尽情享用\uFF01');
    }, 10);
}
async function _0x14ad14(_0x13dabb, _0x41495a, _0x396b89) {
    let _0x937855 = [];
    !_0x396b89 && (_0x396b89 = 3000);
    for (let _0x378bb3 = 0; _0x378bb3 < _0x13dabb.length; _0x378bb3++) {
        if (_0x13dabb[_0x378bb3] == undefined) {
            _0x937855.push({
                'headers': {},
                'content': ''
            });
            continue;
        }
        !_0x13dabb[_0x378bb3].options ? _0x13dabb[_0x378bb3].options = {
            'async': true,
            'timeout': _0x396b89
        } : (_0x13dabb[_0x378bb3].options.async = true, _0x13dabb[_0x378bb3].options.timeout = _0x396b89);
        _0x937855.push(http(_0x13dabb[_0x378bb3].url, _0x13dabb[_0x378bb3].options));
    }
    let _0x2b2c3d = await Promise.all(_0x937855);
    for (let _0x416ed5 = 0; _0x416ed5 < _0x2b2c3d.length; _0x416ed5++) {
        _0x41495a.push(_0x2b2c3d[_0x416ed5]);
    }
    console.log('[提示]全部拿完数据');
}
function _0x29284a(_0x3e1cb2, _0x41bd30, _0x15bf3e) {
    if (_0x3e1cb2 > _0x41bd30)
        return true;
    if (_0x15bf3e && _0x3987f7.pgFail.indexOf(_0x15bf3e) != -1)
        return true;
    return false;
}
function _0x290365(_0x1200b0) {
    let _0x251403 = '';
    let _0x1bef7c = _0x3987f7.headers[0];
    if (_0x3987f7.cacheSubDB[_0x1200b0]) {
        console.log('[页面]已经缓存\uFF0C使用缓存\u3002');
        return _0x3987f7.cacheSubDB[_0x1200b0];
    }
    try {
        _0x251403 = req(_0x1200b0, {
            'headers': _0x1bef7c,
            'timeout': 5000
        }).content;
    } catch {
        _0x251403 = '';
    }
    if (_0x251403) {
        _0x3987f7.cacheSubDB[_0x1200b0] = _0x251403;
        console.log('建立页面缓存(' + _0x1200b0 + ')\u3002');
    }
    return _0x251403;
}
function _0x1df164(_0x27a248, _0x5c614e) {
    if (!_0x27a248)
        return 'https://img2.baidu.com/it/u=651971012,3800349450&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500';
    _0x27a248 = _0x27a248 + '@Referer=' + _0x5c614e;
    return _0x27a248;
}
function _0x3156d8(_0xb49c00, _0x2c36d8) {
    return Math.round(Math.random() * (_0x2c36d8 - _0xb49c00) + _0xb49c00);
}
function _0x261e72(_0x59ec61) {
    var _0x20a216 = '';
    var _0x51c012 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var _0x25cb91 = _0x51c012.length;
    for (var _0x3f0e19 = 0; _0x3f0e19 < _0x59ec61; _0x3f0e19++) {
        _0x20a216 += _0x51c012.charAt(Math.floor(Math.random() * _0x25cb91));
    }
    return _0x20a216;
}
function _0x38b67e() {
    let _0x45b599 = 0;
    for (let _0x24b2b3 = 1; _0x24b2b3 < arguments.length; _0x24b2b3++) {
        arguments[_0x24b2b3].length > _0x45b599 && (_0x45b599 = arguments[_0x24b2b3].length);
    }
    for (let _0x3e79cf = 0; _0x3e79cf < _0x45b599; _0x3e79cf++) {
        for (let _0x82bad0 = 1; _0x82bad0 < arguments.length; _0x82bad0++) {
            _0x3e79cf < arguments[_0x82bad0].length && arguments[0].push(arguments[_0x82bad0][_0x3e79cf]);
        }
    }
}
class _0x326730 {
    constructor(_0xd25447) {
        this.url = _0xd25447;
        this.fail = {};
    }
    ['search'](_0x2809c8, _0x40755d, _0x3bc012, _0x2c2f53) {
        if (_0x2809c8.content == '') {
            console.log('[提示][AVMOO]没有搜索到');
            return;
        }
        let _0x4f91fa = _0x2809c8.content;
        let _0x357283 = _0x390aa4.load(_0x4f91fa);
        if (_0x357283('.alert.alert-danger').length == 1) {
            _0x3bc012 == 1 ? (!this.fail[_0x40755d] && (this.fail[_0x40755d] = {}), this.fail[_0x40755d].stat = true) : (!this.fail[_0x40755d] && (this.fail[_0x40755d] = {}), this.fail[_0x40755d].fpg = _0x3bc012);
            console.log('[提示][AVMOO]没有搜索到');
            return;
        }
        let _0x123cad = _0x357283('#waterfall .item');
        _0x123cad.each(function () {
            _0x2c2f53.push({
                'vod_id': _0x357283('.photo-info date:eq(0)', this).text() + '$$$' + _0x1df164(_0x357283('img', this).attr('src'), 'https://avmoo.cfd/cn/') + '$$$' + _0x357283('a', this).attr('href').replace(/\/\//m, 'https://'),
                'vod_name': _0x357283('.photo-info date:eq(0)', this).text() + ' ' + _0x357283('img', this).attr('title'),
                'vod_pic': _0x1df164(_0x357283('img', this).attr('src'), 'https://avmoo.cfd/cn/'),
                'vod_remarks': _0x357283('.photo-info date:eq(1)', this).text() + ' [AVMOO]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0x291342, _0x26587f) {
        let _0x470442 = _0x291342.split('$$$')[0];
        let _0x259f8c = _0x291342.split('$$$')[1];
        let _0x391b72 = _0x291342.split('$$$')[2];
        let _0x51ecb6 = req('https://btsow.makeup/search/' + _0x470442, {
            'headers': {
                'Referer': 'https://btsow.makeup/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x59068e = _0x390aa4.load(_0x51ecb6);
        let _0x1dd228 = _0x59068e('.data-list [class="row"]');
        _0x1dd228.each(function () {
            _0x26587f.push({
                'vod_id': _0x59068e('a', this).attr('href').replace(/\/\//m, 'https://') + '$$$' + _0x391b72,
                'vod_name': _0x59068e('a .file', this).text() + ' ' + _0x59068e('a .size-date', this).text().replace('Size:', '').replace('Convert Date:', '').replace(/ \/ /, '/'),
                'vod_pic': _0x259f8c,
                'vod_remarks': _0x59068e('a .size-date', this).text().replace('Size:', '').replace('Convert Date:', '').replace(/ \/ /, '/')
            });
        });
    }
    ['detail'](_0x471565, _0x1a5686) {
        let _0x96c571 = _0x471565.split('$$$')[0];
        let _0x547a5e = _0x471565.split('$$$')[1];
        let _0x44cd73 = req(_0x547a5e, {
            'headers': {
                'Referer': 'https://avmoo.cfd/cn/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x34f73b = _0x390aa4.load(_0x44cd73);
        _0x471565 = _0x34f73b('.info p:eq(0)').text().replace('识别码: ', '');
        let _0x18a1bf = _0x34f73b('h3').text();
        let _0x363945 = _0x1df164(_0x34f73b('.bigImage').attr('href'), 'https://avmoo.cfd/cn/');
        let _0x23498c = _0x34f73b('.info p:eq(1)').text().replace('发行时间: ', '');
        let _0x57a670 = _0x34f73b('#avatar-waterfall').text().trim();
        let _0x2e7542 = _0x34f73b('.info p:eq(3)').text().replace('导演: ', '');
        _0x44cd73 = req(_0x96c571, {
            'headers': {
                'Referer': 'https://btsow.makeup/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        _0x34f73b = _0x390aa4.load(_0x44cd73);
        _0x1a5686.push({
            'vod_id': _0x471565,
            'vod_name': _0x18a1bf,
            'vod_pic': _0x363945,
            'type_name': 'AV',
            'vod_year': _0x23498c,
            'vod_area': '日本',
            'vod_remarks': '',
            'vod_actor': _0x57a670,
            'vod_director': _0x2e7542,
            'vod_content': '[FBI WARNING] Federal Law provides severe civil and criminal penalties for the unauthorized reproduction,distribution, or exhibition of copyrighted motion pictures (Title 17,United States Code, Sections 501 and 508). The Federal Bureau of Investigation investigates allegations of criminal copyright infringement(Title 17,United States Code,Section 506).',
            'vod_play_from': _0x34f73b('h3:eq(0)').text(),
            'vod_play_url': _0x34f73b('#magnetLink').text()
        });
    }
}
class _0x227019 {
    constructor(_0x2ed027) {
        this.url = _0x2ed027;
        this.fail = {};
    }
    ['search'](_0x4f1a79, _0xc4714d, _0x523a77, _0x16afaf) {
        if (_0x4f1a79.content == '') {
            console.log('[提示][JAVMULU]没有搜索到');
            return;
        }
        let _0x5d2b18 = _0x4f1a79.content;
        let _0x3e989f = _0x390aa4.load(_0x5d2b18);
        if (_0x5d2b18.match(/location/) || _0x3e989f('#w0 .empty').length == 1) {
            _0x523a77 == 1 ? (!this.fail[_0xc4714d] && (this.fail[_0xc4714d] = {}), this.fail[_0xc4714d].stat = true) : (!this.fail[_0xc4714d] && (this.fail[_0xc4714d] = {}), this.fail[_0xc4714d].fpg = _0x523a77);
            console.log('[提示][JAVMULU]没有搜索到');
            return;
        }
        let _0x59a7d9 = _0x3e989f('.list-view article');
        _0x59a7d9.each(function () {
            _0x16afaf.push({
                'vod_id': 'https://javmulu.net' + _0x3e989f('a', this).attr('href'),
                'vod_name': _0x3e989f('.card-footer h5.text-secondary', this).text(),
                'vod_pic': _0x1df164(_0x3e989f('.card-body img', this).attr('src'), 'https://javmulu.net/'),
                'vod_remarks': _0x3e989f('.card-footer .text-primary', this).text() + ' [JAVMULU]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0xb89d50, _0x3058d5) {
        let _0x4aa6ea = req(_0xb89d50, {
            'headers': {
                'Referer': this.url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x7acc5c = _0x390aa4.load(_0x4aa6ea);
        let _0x4547af = _0x7acc5c('h1.h4').text();
        let _0xc47f0f = _0x1df164(_0x7acc5c('.video-view img:eq(0)').attr('src'), 'https://javmulu.net/');
        let _0x56193a = _0x7acc5c('.list-unstyled.video-info li:eq(1)').text().split(':')[1].split(' ')[0];
        let _0x345bca = '';
        let _0x17fe51 = _0x7acc5c('.card-footer.text-center').text().trim().replace(/\n/, '');
        let _0x52f645 = _0x7acc5c('.list-unstyled.video-info li:eq(3)').text().split(':')[1];
        let _0x5c618c = _0x7acc5c('.col-md-12.col-lg-6 tbody tr');
        _0x5c618c.each(function () {
            let _0x905771 = {
                'vod_name': _0x4547af,
                'vod_pic': _0xc47f0f,
                'vod_year': _0x56193a,
                'vod_remarks': _0x345bca,
                'vod_actor': _0x17fe51,
                'vod_director': _0x52f645
            };
            _0x3058d5.push({
                'vod_id': JSON.stringify(_0x905771),
                'vod_name': _0x7acc5c('td:eq(0)', this).attr('title'),
                'vod_pic': _0xc47f0f,
                'vod_remarks': _0x345bca
            });
        });
    }
}
class _0x231510 {
    constructor(_0x22fe53) {
        this.url = _0x22fe53;
        this.fail = {};
    }
    ['search'](_0x148844, _0x2f8f69, _0x306165, _0x42944b) {
        if (_0x148844.content == '') {
            console.log('[提示][MISSAV]没有搜索到');
            return;
        }
        let _0x83a8a = _0x148844.content;
        let _0x1a374e = _0x390aa4.load(_0x83a8a);
        if (_0x83a8a.match(/未有记录/m)) {
            _0x306165 == 1 ? (!this.fail[_0x2f8f69] && (this.fail[_0x2f8f69] = {}), this.fail[_0x2f8f69].stat = true) : (!this.fail[_0x2f8f69] && (this.fail[_0x2f8f69] = {}), this.fail[_0x2f8f69].fpg = _0x306165);
            console.log('[提示][MISSAV]没有搜索到');
            return;
        }
        let _0x7d576 = _0x1a374e('div.grid.grid-cols-2:eq(0) > div');
        _0x7d576.each(function () {
            _0x42944b.push({
                'vod_id': _0x1a374e('a:eq(0)', this).attr('href'),
                'vod_name': _0x1a374e('a.text-secondary', this).text(),
                'vod_pic': _0x1df164(_0x1a374e('a img', this).attr('data-src'), 'https://missav.ws/'),
                'vod_remarks': _0x1a374e('span.absolute.right-1', this).text() + ' [MissAV]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0x4f03e0, _0x563581) {
        let _0x21d615 = req(_0x4f03e0, {
            'headers': {
                'Referer': this.url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x4973a2 = _0x390aa4.load(_0x21d615);
        let _0x185a30 = _0x4973a2('h1').text();
        let _0x333c6a = _0x21d615.match(/eval\(.*\)/m);
        _0x333c6a = _0x333c6a[0];
        let _0x5c4f65 = _0x333c6a.match(/}\((.*?),(.*?),(.*?),(.*?),(.*?),(.*?)\)/m);
        _0x5c4f65[1] = _0x5c4f65[1].replace(/\\/g, '');
        _0x5c4f65[4] = _0x5c4f65[4].replace(/\.split.*/m, '').replace(/'/g, '');
        _0x333c6a = this.missav_de(_0x5c4f65[1], Number(_0x5c4f65[2]), Number(_0x5c4f65[3]), _0x5c4f65[4], 0, {});
        _0x333c6a = _0x333c6a.split(';');
        let _0x5e8b4d = '';
        let _0x2afd87 = '';
        for (let _0x304bf4 = 0; _0x304bf4 < _0x333c6a.length - 1; _0x304bf4++) {
            let _0x14f55a = _0x333c6a[_0x304bf4].match(/(source.*?)='(.*)'/m);
            _0x14f55a[1] = _0x14f55a[1].replace(/^source$/, 'auto').replace(/^source842$/, '480p').replace(/^source1280$/, '720p').replace(/^sourceFhd$/, '1080p');
            _0x5e8b4d = _0x5e8b4d + '$$$' + _0x14f55a[1];
            _0x2afd87 = _0x2afd87 + '$$$' + _0x185a30 + '$' + _0x14f55a[2];
        }
        _0x5e8b4d = _0x5e8b4d.replace(/^\$\$\$/, '');
        _0x2afd87 = _0x2afd87.replace(/^\$\$\$/, '');
        let _0x50685b = _0x1df164(_0x4973a2('[property="og:image"]').attr('content'), 'https://missav.ws/');
        let _0x366b27 = '';
        let _0x2f6484 = '';
        let _0x39d0e9 = '日本';
        let _0x57e2ae = '';
        let _0x52f9d1 = '';
        let _0x3a7393 = '[FBI WARNING] Federal Law provides severe civil and criminal penalties for the unauthorized reproduction,distribution, or exhibition of copyrighted motion pictures (Title 17,United States Code, Sections 501 and 508). The Federal Bureau of Investigation investigates allegations of criminal copyright infringement(Title 17,United States Code,Section 506).';
        let _0x37a38a = _0x4973a2('.space-y-2 .text-secondary');
        _0x37a38a.each(function () {
            let _0x2e764a = _0x4973a2(this).text();
            if (_0x2e764a.match(/类型/m))
                _0x366b27 = _0x2e764a.replace('类型:', '');
            else {
                if (_0x2e764a.match(/发行日期/m))
                    _0x2f6484 = _0x2e764a.replace('发行日期:', '');
                else {
                    if (_0x2e764a.match(/女优/m))
                        _0x57e2ae = _0x2e764a.replace('女优:', '');
                    else
                        _0x2e764a.match(/导演/m) && (_0x52f9d1 = _0x2e764a.replace('导演:', ''));
                }
            }
        });
        let _0x333af3 = {
            'vod_id': _0x4f03e0,
            'vod_name': _0x185a30,
            'vod_pic': _0x50685b,
            'type_name': _0x366b27,
            'vod_year': _0x2f6484,
            'vod_area': _0x39d0e9,
            'vod_actor': _0x57e2ae,
            'vod_director': _0x52f9d1,
            'vod_content': _0x3a7393,
            'vod_play_from': _0x5e8b4d,
            'vod_play_url': _0x2afd87
        };
        _0x563581.push({
            'vod_id': JSON.stringify(_0x333af3),
            'vod_name': 'M3U8',
            'vod_pic': _0x50685b,
            'vod_remarks': ''
        });
        _0x37a38a = _0x4973a2('.min-w-full tr');
        _0x37a38a.each(function () {
            let _0x1ca22d = {
                'vod_name': _0x185a30,
                'vod_pic': _0x50685b,
                'type_name': _0x366b27,
                'vod_year': _0x2f6484,
                'vod_area': _0x39d0e9,
                'vod_actor': _0x57e2ae,
                'vod_director': _0x52f9d1,
                'vod_content': _0x3a7393
            };
            _0x563581.push({
                'vod_id': JSON.stringify(_0x1ca22d),
                'vod_name': _0x4973a2('td:eq(0) a', this).text(),
                'vod_pic': _0x50685b,
                'vod_remarks': ''
            });
        });
    }
    ['missav_de'](_0x8c5c, _0x3f80b8, _0x5cc9ee, _0x5f0b69, _0x7b7212, _0x1c4797) {
        _0x5f0b69 = _0x5f0b69.split('|');
        _0x7b7212 = function (_0xdf7508) {
            return _0xdf7508.toString(36);
        };
        if (!''.replace(/^/, String)) {
            while (_0x5cc9ee--) {
                _0x1c4797[_0x5cc9ee.toString(_0x3f80b8)] = _0x5f0b69[_0x5cc9ee] || _0x5cc9ee.toString(_0x3f80b8);
            }
            _0x5f0b69 = [function (_0x4b4f4b) {
                    return _0x1c4797[_0x4b4f4b];
                }];
            _0x7b7212 = function () {
                return '\\w+';
            };
            _0x5cc9ee = 1;
        }
        while (_0x5cc9ee--) {
            _0x5f0b69[_0x5cc9ee] && (_0x8c5c = _0x8c5c.replace(new RegExp('\\b' + _0x7b7212(_0x5cc9ee) + '\\b', 'g'), _0x5f0b69[_0x5cc9ee]));
        }
        return _0x8c5c;
    }
}
class _0x2b7842 {
    constructor(_0x3752ca) {
        this.url = _0x3752ca;
        this.fail = {};
    }
    ['search'](_0x5ed4a0, _0x5bb740, _0xf4599b, _0x164d60) {
        if (_0x5ed4a0.content == '') {
            console.log('[提示][MP4电影]没有搜索到');
            return;
        }
        let _0x1c001f = _0x5ed4a0.content;
        let _0x109a1a = _0x390aa4.load(_0x1c001f);
        let _0x3d9dda = _0x109a1a('#list_all ul li');
        if (_0x109a1a('#list_all ul li:eq(0)').text().match(/未搜索到/m)) {
            _0xf4599b == 1 ? (!this.fail[_0x5bb740] && (this.fail[_0x5bb740] = {}), this.fail[_0x5bb740].stat = true) : (!this.fail[_0x5bb740] && (this.fail[_0x5bb740] = {}), this.fail[_0x5bb740].fpg = _0xf4599b);
            console.log('[提示][MP4电影]没有搜索到');
            return;
        }
        _0x3d9dda.each(function () {
            let _0x339ca1 = _0x109a1a('h2 a', this).contents().eq(_0x109a1a('h2 a', this).contents().length - 1).text().match(/((更新|全).*)$/m);
            _0x339ca1 = _0x339ca1 ? _0x339ca1[1] : 'HD';
            if (_0x339ca1.match(/更新至全/m)) {
                _0x339ca1 = _0x339ca1.replace('更新至', '');
            }
            _0x164d60.push({
                'vod_id': 'https://www.mp4us.com/' + _0x109a1a('a', this).attr('href'),
                'vod_name': _0x109a1a('a img', this).attr('alt').replace(/(《|》)/gm, ''),
                'vod_pic': _0x1df164(_0x109a1a('a img', this).attr('data-original'), 'https://www.mp4us.com/'),
                'vod_remarks': _0x339ca1 + ' [MP4电影]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0x618f9a, _0x43b4b2) {
        let _0x2b4f6e = req(_0x618f9a, {
            'headers': {
                'Referer': this.url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x3a8f73 = _0x390aa4.load(_0x2b4f6e);
        let _0xca737c = _0x3a8f73('.article-header .text p:eq(0)').text();
        let _0x50cc7d = _0x1df164(_0x3a8f73('.article-header .pic img').attr('src'), 'https://www.mp4us.com/');
        let _0x150b36 = _0x3a8f73('.article-header .post-meta span:eq(0) a').text();
        let _0x4a272e = _0x3a8f73('.article-header .update_time').text();
        let _0x16a238 = _0x3a8f73('.article-header .text p:eq(4) span').text();
        let _0x3709ca = _0x3a8f73('.article-header .actor .attrs').text();
        let _0x353258 = _0x3a8f73('.article-header .director .attrs').text();
        let _0x5838db = _0x3a8f73('.article-related.info p').text();
        let _0x1e78f3 = _0x3a8f73('.panel.down-list li');
        _0x1e78f3.each(function () {
            let _0x314930 = {
                'vod_name': _0xca737c,
                'vod_pic': _0x50cc7d,
                'type_name': _0x150b36,
                'vod_year': _0x4a272e,
                'vod_area': _0x16a238,
                'vod_actor': _0x3709ca,
                'vod_director': _0x353258,
                'vod_content': _0x5838db
            };
            _0x43b4b2.push({
                'vod_id': JSON.stringify(_0x314930),
                'vod_name': _0x3a8f73('a', this).attr('title'),
                'vod_pic': _0x50cc7d,
                'vod_remarks': ''
            });
        });
    }
}
class _0x3d9a2c {
    constructor(_0x98624a) {
        this.url = _0x98624a;
        this.fail = {};
        this.searchid = '';
    }
    ['search'](_0x502f71, _0x5db3e3, _0x2dd66f, _0x3e0238) {
        if (_0x2dd66f == 1 && !_0x502f71.headers.location) {
            !this.fail[_0x5db3e3] && (this.fail[_0x5db3e3] = {});
            this.fail[_0x5db3e3].stat = true;
            console.log('[提示][6V电影网]没有搜索到');
            return;
        }
        _0x2dd66f == 1 && _0x502f71.headers.location.match(/searchid=(.+)/m) && (this.searchid = _0x502f71.headers.location.match(/searchid=(.+)/m)[1], _0x502f71.content = http('https://www.66ss.org/e/search/result/index.php?page=0&searchid=' + this.searchid, {
            'headers': {
                'Referer': 'https://www.66ss.org/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            'async': false
        }).content);
        if (_0x502f71.content == '') {
            console.log('[提示][6V电影网]没有搜索到');
            return;
        }
        let _0x75cc91 = _0x502f71.content;
        let _0x48af93 = _0x390aa4.load(_0x75cc91);
        let _0x4ee1c4 = _0x48af93('#post_container li');
        if (_0x75cc91.match(/没有搜索到/m) || _0x4ee1c4.length == 0) {
            _0x2dd66f == 1 ? (!this.fail[_0x5db3e3] && (this.fail[_0x5db3e3] = {}), this.fail[_0x5db3e3].stat = true) : (!this.fail[_0x5db3e3] && (this.fail[_0x5db3e3] = {}), this.fail[_0x5db3e3].fpg = _0x2dd66f);
            console.log('[提示][6V电影网]没有搜索到');
            return;
        }
        _0x4ee1c4.each(function () {
            _0x3e0238.push({
                'vod_id': 'https://www.66ss.org' + _0x48af93('a', this).attr('href'),
                'vod_name': _0x48af93('.article h2 a', this).text(),
                'vod_pic': _0x1df164(_0x48af93('a img', this).attr('src'), 'https://www.66ss.org/'),
                'vod_remarks': _0x48af93('.info .info_date', this).text() + ' [6V电影网]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0xda64a, _0xf70298) {
        let _0x33a75a = req(_0xda64a, {
            'headers': {
                'Referer': this.url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x239551 = _0x390aa4.load(_0x33a75a);
        let _0x301493 = _0x239551('#post_content').text();
        let _0x4a0cb1 = _0x239551('#content h1:eq(0)').text().replace(/\[.*?\]/g, '');
        let _0x17e052 = _0x1df164(_0x239551('#post_content img:eq(0)').attr('src'), 'https://www.66ss.org/');
        let _0x44fac4 = _0x301493.match(/◎类　　别　(.*?)◎/m) ? _0x301493.match(/◎类　　别　(.*?)◎/m)[1] : '';
        let _0x3b9811 = _0x301493.match(/◎年　　代　(.*?)◎/m) ? _0x301493.match(/◎年　　代　(.*?)◎/m)[1] : '';
        let _0x8127fd = _0x301493.match(/◎产　　地　(.*?)◎/m) ? _0x301493.match(/◎产　　地　(.*?)◎/m)[1] : '';
        let _0x112290 = _0x301493.match(/◎(主　　演|演　　员)　(.*?)◎/m) ? _0x301493.match(/◎(主　　演|演　　员)　(.*?)◎/m)[2].replace(/　+/g, '') : '';
        let _0x4db338 = _0x301493.match(/◎导　　演　(.*?)◎/m) ? _0x301493.match(/◎导　　演　(.*?)◎/m)[1].replace(/　+/g, '') : '';
        let _0x31656a = _0x301493.match(/◎简　　介　(.*?)【下/m) ? _0x301493.match(/◎简　　介　(.*?)【下/m)[1] : '';
        let _0x16fa2d = _0x239551('#post_content > table a');
        _0x16fa2d.each(function () {
            let _0x202be7 = {
                'vod_name': _0x4a0cb1,
                'vod_pic': _0x17e052,
                'type_name': _0x44fac4,
                'vod_year': _0x3b9811,
                'vod_area': _0x8127fd,
                'vod_actor': _0x112290,
                'vod_director': _0x4db338,
                'vod_content': _0x31656a
            };
            _0xf70298.push({
                'vod_id': JSON.stringify(_0x202be7),
                'vod_name': _0x239551(this).text(),
                'vod_pic': _0x17e052 + '@User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'vod_remarks': ''
            });
        });
    }
}
class _0x31b9c5 {
    constructor(_0x169b1d) {
        this.url = _0x169b1d;
        this.fail = {};
        this.second_res = [];
    }
    ['search'](_0xc88702, _0x545456, _0x116df5, _0x4506bd) {
        if (_0xc88702.content == '') {
            console.log('[提示][酷吧电影]没有搜索到');
            return;
        }
        let _0x294b1c = _0xc88702.content;
        let _0x39f5e1 = _0x390aa4.load(_0x294b1c);
        let _0x3f1418 = _0x39f5e1('.stui-vodlist__media.col-pd:eq(0) li');
        if (_0x3f1418.length == 0) {
            _0x116df5 == 1 ? (!this.fail[_0x545456] && (this.fail[_0x545456] = {}), this.fail[_0x545456].stat = true) : (!this.fail[_0x545456] && (this.fail[_0x545456] = {}), this.fail[_0x545456].fpg = _0x116df5);
            console.log('[提示][酷吧电影]没有搜索到');
            return;
        }
        _0x3f1418.each(function () {
            _0x4506bd.push({
                'vod_id': 'https://www.kuba222.com' + _0x39f5e1('a', this).attr('href'),
                'vod_name': _0x39f5e1('a', this).attr('title'),
                'vod_pic': _0x1df164(_0x39f5e1('a', this).attr('data-original'), 'https://www.kuba222.com'),
                'vod_remarks': _0x39f5e1('.text-right', this).text() + ' [酷吧电影]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0x33c1a7, _0x418aa6) {
        if (_0x33c1a7.match(/kubady#(\d+)/m)) {
            _0x33c1a7 = _0x33c1a7.match(/kubady#(\d+)/m)[1];
            for (let _0x66cff8 = 0; _0x66cff8 < this.second_res[_0x33c1a7].length; _0x66cff8++) {
                _0x418aa6.push(this.second_res[_0x33c1a7][_0x66cff8]);
            }
            false = true;
            return;
        }
        if (false) {
            for (let _0x3149ab = 0; _0x3149ab < _0x3987f7.second_res.length; _0x3149ab++) {
                _0x418aa6.push(_0x3987f7.second_res[_0x3149ab]);
            }
            false = false;
            return;
        }
        let _0xd89ae0 = [];
        let _0x39e48e = req(_0x33c1a7, {
            'headers': {
                'Referer': this.url,
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0xee2398 = _0x390aa4.load(_0x39e48e);
        let _0x281371 = _0xee2398('.stui-content__detail h3.title').text();
        let _0x4ed052 = _0x1df164(_0xee2398('.stui-content__thumb img').attr('data-original'), 'https://www.kuba222.com/');
        let _0x1c660c = _0xee2398('.stui-content__detail .data a:eq(0)').text();
        let _0x27e7c2 = _0xee2398('.stui-content__detail .data a:eq(2)').text();
        let _0x2bab30 = _0xee2398('.stui-content__detail .data a:eq(1)').text();
        let _0x2a863d = _0xee2398('.text-right', this).text();
        let _0x358b60 = _0xee2398('.stui-content__detail .data:eq(2)').text().replace('主演\uFF1A', '');
        let _0x58495f = _0xee2398('.stui-content__detail .data:eq(3)').text().replace('导演\uFF1A', '');
        let _0x57fe8a = _0xee2398('.detail-content').text();
        let _0x5255f4 = _0xee2398('.stui-overflow-list.stui-overflow-list-down script');
        let _0x5eeb94 = 0;
        _0x5255f4.each(function () {
            let _0x1b1384 = _0xee2398(this).text().match(/var GvodUrls1 ="(.*?)"/m)[1];
            _0x1b1384 = _0x1b1384.split('###');
            !_0xd89ae0[_0x5eeb94] && (_0xd89ae0[_0x5eeb94] = []);
            for (let _0x36b2cf = 0; _0x36b2cf < _0x1b1384.length - 1; _0x36b2cf++) {
                let _0x37d8c5 = {
                    'vod_id': _0x1b1384[_0x36b2cf].split('$')[1],
                    'vod_name': _0x281371,
                    'vod_pic': _0x4ed052,
                    'type_name': _0x1c660c,
                    'vod_year': _0x27e7c2,
                    'vod_area': _0x2bab30,
                    'vod_remarks': _0x2a863d,
                    'vod_actor': _0x358b60,
                    'vod_director': _0x58495f,
                    'vod_content': _0x57fe8a,
                    'vod_play_from': _0x1b1384[_0x36b2cf].split('$')[0],
                    'vod_play_url': _0x1b1384[_0x36b2cf].split('$')[1]
                };
                _0xd89ae0[_0x5eeb94].push({
                    'vod_id': JSON.stringify(_0x37d8c5),
                    'vod_name': _0x1b1384[_0x36b2cf].split('$')[0],
                    'vod_pic': _0x4ed052,
                    'vod_remarks': _0x2a863d
                });
            }
            _0x5eeb94++;
        });
        this.second_res = _0xd89ae0;
        _0x5255f4 = _0xee2398('[class="stui-pannel__head bottom-line active clearfix"]');
        _0x5eeb94 = 0;
        _0x5255f4.each(function () {
            _0x418aa6.push({
                'vod_id': 'kubady#' + _0x5eeb94,
                'vod_name': _0xee2398('h3', this).text(),
                'vod_pic': _0x4ed052,
                'vod_remarks': _0x2a863d,
                'vod_tag': 'folder'
            });
            _0x5eeb94++;
        });
        _0x3987f7.second_res = _0x418aa6;
        false = false;
    }
}
class _0x1f79fc {
    constructor(_0x46a16d) {
        this.url = _0x46a16d;
        this.fail = {};
        this.second_res = [];
        this.md = '';
        this.cookie = '';
    }
    ['get_md'](_0x444311) {
        let _0x107579 = req(_0x444311, {
            'headers': {
                'Referer': this.url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            'timeout': 3000
        }).content;
        _0x107579.match(/md: "(.*?)"/m) ? (this.md = _0x107579.match(/md: "(.*?)"/m)[1], console.log('[提示][不太灵]创建MD缓存成功')) : console.log('[提示][不太灵]创建MD缓存失败');
        if (_0x107579.match(/document\.cookie = "(.*?); .*"/m)) {
            this.md = _0x107579.match(/document\.cookie = "(.*?); .*"/m)[1];
            console.log('[提示][不太灵]创建Cookie缓存成功');
        }
    }
    ['search'](_0x5bc0a2, _0x49d7d6, _0x26ff65, _0x604933) {
        if (_0x5bc0a2.content == '') {
            console.log('[提示][不太灵]没有搜索到');
            return;
        }
        let _0x1cd0d8 = _0x5bc0a2.content;
        let _0x2e6813 = _0x390aa4.load(_0x1cd0d8);
        let _0x262c66 = _0x2e6813('#showdiv .masonry_item');
        if (_0x262c66.length == 0) {
            _0x26ff65 == 1 ? (!this.fail[_0x49d7d6] && (this.fail[_0x49d7d6] = {}), this.fail[_0x49d7d6].stat = true) : (!this.fail[_0x49d7d6] && (this.fail[_0x49d7d6] = {}), this.fail[_0x49d7d6].fpg = _0x26ff65);
            console.log('[提示][不太灵]没有搜索到');
            return;
        }
        _0x262c66.each(function () {
            _0x604933.push({
                'vod_id': _0x2e6813('a', this).attr('href').replace(/\./m, 'https://www.2bt0.com'),
                'vod_name': _0x2e6813('h5', this).contents().eq(0).text(),
                'vod_pic': _0x1df164(_0x2e6813('.bgimgcov', this).attr('style').match(/(https:\/\/.*?\.(png|jpg))/m)[1], 'https://www.2bt0.com'),
                'vod_remarks': _0x2e6813('.type--fine-print', this).text().replace(/(\(|\))/gm, '') + ' [不太灵]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0x4c1ac3, _0x7fef9e) {
        if (_0x4c1ac3.match(/butailing#(\d+)/m)) {
            _0x4c1ac3 = _0x4c1ac3.match(/butailing#(\d+)/m)[1];
            for (let _0x4a3991 = 0; _0x4a3991 < this.second_res[_0x4c1ac3].length; _0x4a3991++) {
                _0x7fef9e.push(this.second_res[_0x4c1ac3][_0x4a3991]);
            }
            false = true;
            return;
        }
        if (false) {
            for (let _0x1f2bb3 = 0; _0x1f2bb3 < _0x3987f7.second_res.length; _0x1f2bb3++) {
                _0x7fef9e.push(_0x3987f7.second_res[_0x1f2bb3]);
            }
            false = false;
            return;
        }
        let _0x221f38 = [];
        this.md == '' ? (console.log('[提示]没命中MD缓存'), this.get_md(_0x4c1ac3)) : console.log('[提示]命中MD缓存');
        let _0x3e93cc = req(_0x4c1ac3, {
            'headers': {
                'Cookie': this.cookie,
                'Referer': this.url,
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            'method': 'POST',
            'body': 'md=' + this.md
        }).content;
        let _0x358204 = _0x390aa4.load(_0x3e93cc);
        let _0x240976 = _0x358204('#movie-content .info-title').text().match(/(.*?)(\s*?)\((.*?)\)/m);
        let _0x32f2c1 = _0x240976[1];
        let _0x203dc7 = _0x1df164(_0x358204('#movie-content img:eq(0)').attr('src'), 'https://www.2bt0.com/');
        let _0x3f46c9 = _0x240976[3];
        let _0x470ec7 = _0x358204('#movie-content .tiny-title:eq(-2)').text().replace('上映地区: ', '');
        let _0x171cdd = '';
        let _0x4adbc7 = _0x358204('[itemprop="actor"] [itemprop="name"]').text().replace(/(\w|\s)+/gm, ' ');
        let _0x4ace4e = _0x358204('[itemprop="director"] [itemprop="name"]').text().replace(/(\w|\s)+/gm, ' ');
        let _0x2ea58e = _0x358204('.information-text span').text();
        let _0x4f0626 = _0x358204('.tabs-container .tabs-content > li');
        let _0x55f325 = 0;
        _0x4f0626.each(function () {
            !_0x221f38[_0x55f325] && (_0x221f38[_0x55f325] = []);
            let _0x24b0f2 = _0x358204('.container', this);
            _0x24b0f2.each(function () {
                let _0x2df70a = {
                    'vod_name': _0x32f2c1,
                    'vod_pic': _0x203dc7,
                    'vod_year': _0x3f46c9,
                    'vod_area': _0x470ec7,
                    'vod_remarks': _0x171cdd,
                    'vod_actor': _0x4adbc7,
                    'vod_director': _0x4ace4e,
                    'vod_content': _0x2ea58e
                };
                _0x221f38[_0x55f325].push({
                    'vod_id': JSON.stringify(_0x2df70a),
                    'vod_name': _0x358204('.col-md-12 a.torrent-title', this).text(),
                    'vod_pic': _0x203dc7,
                    'vod_remarks': _0x171cdd
                });
            });
            _0x55f325++;
        });
        this.second_res = _0x221f38;
        _0x4f0626 = _0x358204('.tabs-container .tabs li');
        _0x55f325 = 0;
        _0x4f0626.each(function () {
            _0x7fef9e.push({
                'vod_id': 'butailing#' + _0x55f325,
                'vod_name': _0x358204('span.h5', this).text(),
                'vod_pic': _0x203dc7,
                'vod_remarks': _0x171cdd,
                'vod_tag': 'folder'
            });
            _0x55f325++;
        });
        _0x3987f7.second_res = _0x7fef9e;
        false = false;
    }
}
class _0x52f21c {
    constructor(_0x39500b) {
        this.url = _0x39500b;
        this.fail = {};
    }
    ['search'](_0xc0f1b0, _0x300a63, _0x43ddc0, _0x420e22) {
        if (_0xc0f1b0.content == '') {
            console.log('[提示][迅雷影视]没有搜索到');
            return;
        }
        let _0x462f5b = _0xc0f1b0.content;
        let _0x2fbfd7 = _0x390aa4.load(_0x462f5b);
        let _0x2500ff = _0x2fbfd7('.bf3b11b08 .b59a2b64df1');
        if (_0x2500ff.length == 0) {
            _0x43ddc0 == 1 && (!this.fail[_0x300a63] && (this.fail[_0x300a63] = {}), this.fail[_0x300a63].stat = true);
            console.log('[提示][迅雷影视]没有搜索到');
            return;
        }
        _0x2500ff.each(function () {
            _0x420e22.push({
                'vod_id': 'https://xunlei8.cc' + _0x2fbfd7('a:eq(0)', this).attr('href'),
                'vod_name': _0x2fbfd7('h2 a:eq(0)', this).text(),
                'vod_pic': _0x1df164(_0x2fbfd7('a:eq(0) img', this).attr('src'), 'https://xunlei8.cc/'),
                'vod_remarks': '豆' + _0x2fbfd7('h2 a:eq(1) span', this).text() + ' [迅雷影视]',
                'vod_tag': 'folder'
            });
        });
    }
    ['category'](_0x4bc81d, _0x99516a) {
        let _0x362b7f = req(_0x4bc81d, {
            'headers': {
                'Referer': this.url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        }).content;
        let _0x3a6d68 = _0x390aa4.load(_0x362b7f);
        let _0xef661d = _0x3a6d68('h1').text();
        let _0x578391 = _0x1df164(_0x3a6d68('.ba330 img').attr('src'), 'https://xunlei8.cc/');
        let _0x510650 = '';
        let _0x2e065b = '';
        let _0x123510 = '';
        let _0x304f91 = '';
        let _0x1fad87 = '';
        let _0x43ff8b = _0x3a6d68('.b1f40f7888').text();
        let _0x622d2e = _0x3a6d68('.be998a p');
        _0x622d2e.each(function () {
            let _0x2521ef = _0x3a6d68(this).text();
            let _0x205105 = _0x3a6d68(this).contents();
            if (_0x2521ef.match(/类型/m))
                for (let _0x40871c = 1; _0x40871c < _0x205105.length; _0x40871c++) {
                    _0x510650 = _0x510650 + ' ' + _0x205105.eq(_0x40871c).text();
                }
            else {
                if (_0x2521ef.match(/上映/m))
                    _0x2e065b = _0x2521ef.replace('上映\uFF1A', '');
                else {
                    if (_0x2521ef.match(/地区/m))
                        _0x123510 = _0x2521ef.replace('地区\uFF1A', '');
                    else {
                        if (_0x2521ef.match(/主演/m))
                            for (let _0x1d4151 = 1; _0x1d4151 < _0x205105.length; _0x1d4151++) {
                                _0x304f91 = _0x304f91 + ' ' + _0x205105.eq(_0x1d4151).text();
                            }
                        else {
                            if (_0x2521ef.match(/导演：/m))
                                for (let _0x243993 = 1; _0x243993 < _0x205105.length; _0x243993++) {
                                    _0x1fad87 = _0x1fad87 + ' ' + _0x205105.eq(_0x243993).text();
                                }
                        }
                    }
                }
            }
        });
        _0x622d2e = _0x3a6d68('.bf8243b9 li');
        _0x622d2e.each(function () {
            let _0x3bd4b6 = {
                'vod_name': _0xef661d,
                'vod_pic': _0x578391,
                'type_name': _0x510650,
                'vod_year': _0x2e065b,
                'vod_area': _0x123510,
                'vod_actor': _0x304f91,
                'vod_director': _0x1fad87,
                'vod_content': _0x43ff8b
            };
            _0x99516a.push({
                'vod_id': JSON.stringify(_0x3bd4b6),
                'vod_name': _0x3a6d68('a:eq(0)', this).text(),
                'vod_pic': _0x578391,
                'vod_remarks': ''
            });
        });
    }
}
const _0x4c2007 = new _0x326730('https://avmoo.cfd/cn/');
const _0x3796cb = new _0x227019('https://javmulu.net/');
const _0x2d5787 = new _0x231510('https://missav.ws/');
const _0x11eff6 = new _0x2b7842('https://www.mp4us.com/');
const _0x522eb9 = new _0x3d9a2c('https://www.66ss.org/');
const _0x3c1fc6 = new _0x31b9c5('https://www.kuba222.com/');
const _0xefb5f8 = new _0x1f79fc('https://www.2bt0.com/');
const _0x3dd8f6 = new _0x52f21c('https://xunlei8.cc/');
function _0x1aed4b(_0x95f4e7) {
    _0x48072a();
    if (!false) {
        console.log('[提示]处于生产环境\uFF0C关闭console.log打印日志\u3002');
        console.log = () => {
        };
    }
    console.log();
    console.log('[TVBox调试日志]');
    console.log('[提示]路飞开始调试了\uFF01\uFF01\uFF01');
    console.log('[提示]ext值为: ' + _0x95f4e7);
    if (_0x95f4e7.match(/18\+/)) {
        false = true;
    }
}
export default {
    'init': _0x1aed4b,
    'home': _0x50af14,
    'homeVod': _0x4c2491,
    'category': _0x1e7494,
    'detail': _0x15909a,
    'play': _0x38865a,
    'search': _0xf39aba
};
