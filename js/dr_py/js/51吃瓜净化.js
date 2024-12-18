// ==UserScript==
// @name         51吃瓜净化
// @namespace    Tianming Buyou
// @version      1.0
// @description  隐藏51吃瓜的广告,净化界面
// @author       天命不又
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 移除广告和不必要的元素
    function removeAds() {
        const articles = document.querySelectorAll('article');
        articles.forEach(article => {
            const meta = article.querySelector('meta[itemprop="name"][content="广告"]');
            const title = article.querySelector('h2.post-card-title[itemprop="headline"]');
            const background = Array.from(article.querySelectorAll('div.blog-background')).find(elem => {
                const backgroundImage = elem.style.backgroundImage;
                return backgroundImage && backgroundImage.includes('data:image/gif');
            });
            if (meta || (title && !title.textContent.trim()) || background) {
                article.remove();
            }
        });
        
            // 移除页脚菜单
    const footMenu = document.getElementById('foot-menu');
    removeElement(footMenu);

    function removeElement(element) {
        if (element) {
            element.remove();
        }
    }  
     
        if (window.location.href.includes('/archives/')) {
            // 移除文章页面内指定的元素
            const elementsToRemove = [
                'blockquote',
                '.content-file',
                '.content-tabs-head',
                '.content-tab-content',
                '.selected',
                '.flash',
                '#comments',
            ];
            elementsToRemove.forEach(selector => {
                document.querySelectorAll(selector).forEach(elem => elem.remove());
            });
        }
    }

    // 在页面加载完毕后执行移除操作
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        removeAds();
    } else {
        document.addEventListener('DOMContentLoaded', removeAds);
    }
})();