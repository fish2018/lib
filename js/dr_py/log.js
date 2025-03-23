var ws;
var websocketUrl = getWsUrl();
const HEART_BEAT_INTERVAL = 1000;
const reconnectTime = 5000;
var lockReconnect = false;
var heartBeatInterval;

function createWs() {
    ws = new WebSocket(websocketUrl);
    ws.addEventListener('open', (event) => {
        console.log('WebSocket is open now.');
        startHeartBeat();
        addMsg("websocket连接成功，当前时间" + new Date().Format("yyyy-MM-dd hh:mm:ss"));
    });

    ws.addEventListener('message', (event) => {
        console.log('Message from server: ', event.data);
        if (event.data != 'HEARTBEAT') addMsg(event.data);
    });

    ws.addEventListener('error', (error) => {
        console.error('WebSocket encountered error: ', error);
        let msg = "websocket发生错误,连接状态码:" + ws.readyState;
        addMsg(msg);
        reconnect();
    });

    ws.addEventListener('close', (event) => {
        console.log('WebSocket is closed now.');
        addMsg('websocket连接关闭');
        if (heartBeatInterval) clearInterval(heartBeatInterval);
        reconnect();
    });
}

function getWsUrl() {
    let host = location.host;
    let protocol = 'ws';
    let port = location.port;
    return protocol + '://' + host;
}

function reconnect() {
    if (!lockReconnect) {
        lockReconnect = true;
        setTimeout(function () {
            addMsg("正在重连，当前时间" + new Date().Format("yyyy-MM-dd hh:mm:ss"));
            createWs();
            lockReconnect = false;
        }, reconnectTime);
    }
}

function addMsg(msg){
    let f = $('#filter').val();
    if (f.length > 0 && msg.indexOf(f) <= 0) {
        return;
    }
    if(msg && !msg.endsWith('<br>')) {
        msg += '<br>';
    }
    $("#msg").append(msg);
    $("#log").scrollTop($("#log").prop("scrollHeight"));
}

function startHeartBeat() {
    if (ws.readyState === 1) {
        ws.send('HEARTBEAT');
//        console.log('send HEARTBEAT');
    }
    heartBeatInterval = setInterval(() => {
        if (ws.readyState === 1) {
          ws.send('HEARTBEAT');
//          console.log('send HEARTBEAT');
        }
    }, HEART_BEAT_INTERVAL);
}

Date.prototype.Format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1, // 月份
        "d+": this.getDate(), // 日
        "h+": this.getHours(), // 小时
        "m+": this.getMinutes(), // 分
        "s+": this.getSeconds(), // 秒
        "q+": Math.floor((this.getMonth() + 3) / 3), // 季度
        "S": this.getMilliseconds() // 毫秒
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
            return fmt;
}

$(document).ready(function() {
    $('#clearLog').click(function () {
       $("#msg").html('');
    });
    addMsg('websocket初始化中,当前ws服务地址=>  ' + websocketUrl);
    createWs();
});