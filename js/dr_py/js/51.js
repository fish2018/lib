// ==UserScript==
// @name         51吃瓜净化
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  净化51吃瓜界面
// @icon         https://www.51cg1.com/favicon.ico
// @author       文心
// @match        https://www.51cg1.com/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    const hideArticles = () => {
        const articlesToHide = [
            '/archives/136677/',
            '/archives/137882/',
            '/archives/111682/'
            // 在这里继续添加新的archives链接
        ];
        articlesToHide.forEach(archive => {
            const article = document.querySelector(`article a[href*="${archive}"]`);
            if (article) {
                article.closest('article').style.display = 'none';
            }
        });
    };

    const hideElements = () => {
        const elementsToHide = [
            '#index > article:nth-child(2)',
            'ul.navbar-nav:nth-of-type(2)',
            '#foot-menu',
            '#footer',
            'div.post-content:nth-child(4)',
            'div.horizontal-banner:nth-child(2)',
            '.content-tabs',
            'div.line:nth-child(3)',
            'div.line:nth-child(5)',
            '#comments',
            '.flash',
            '.article-ads-btn',
            '.post > div:nth-child(10)',
            'div.post-content blockquote',
        ];
        elementsToHide.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(element => {
                element.style.display = 'none';
            });
        });
    };

    hideArticles();
    hideElements();
})();