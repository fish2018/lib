function main(item) {
  const id = item.url.split("=")[1];
  const channels = {
    hnjs: "280",
    hnyl: "344",
    hndy: "221",
    hnds: "346",
    hndsj: "484",
    hngg: "261",
    hngj: "229",
    jyjs: "316",
    jykt: "287",
    xfpy: "329",
    klcd: "218",
    cpd: "578",
    csxwzh: "269",
    cszfpd: "254",
    csnxpd: "230",
    klg: "267"
  };
  const channelId = channels[id];
  if (!channelId) {
    return "";
  }
  const url = `http://pwlp.bz.mgtv.com/v1/epg/turnplay/getLivePlayUrlMPP?version=PCweb_1.0&platform=1&buss_id=2000001&channel_id=${channelId}`;
  const headers = {};
  const portData = get.call({ url: url, headers: JSON.stringify(headers) });
  const json = JSON.parse(portData);
  const m3u8 = json.data.url;
  return JSON.stringify({ url: m3u8 });
}