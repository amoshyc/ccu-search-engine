---
title: "CCU Search Engine HW2"
date: 2018-03-21T22:15:58+08:00
categories: ["HW"]
tags: []
toc: true
math: false
---

# tl;dr

403410034 資工四 黃鈺程。
這個作業我覺得最有意思的結果是「1999 年的舊資料」與「無效查詢」這兩段。前者表現出了 Google 的**強大**；後候表現出百度的「強大」哈哈哈。另外總得來說，Google 如預期的最強大，Bing 有再努力，Yahoo 感覺在吃老本快不行了，而百度那個真的是搜尋引擎嗎…不只眾所皆知的字詞屏蔽，搜尋結果根本不可信。

# 介紹

因為我平常只用 Google，Google 已經被我調教得很好了 XD，所以在進行這個作業時我使用 Chrome 的無痕視窗並且沒有登入任何帳號，以此來確保公平性。我將從各個方面比較 Google, Yahoo, Bing, Baidu 這四個搜尋引擎。我原先想使用程式自動化查詢，這樣我就可以使用大量的測資來恆量，但很可惜的，Google 會阻檔程式引發的搜尋的樣子：短時間內無法進入大量的查詢，因此我還是使用人工的方式來測量，所以如果我的結果與其他人觀測的結果有所出入，很可能只是我們選了不同關鍵字查詢造成的。

# 相關性與數量

`黃石國家公園景點`：全部都是相關的，但除了 Google 以外，其他的前二都是廣告，尤其是百度最扯，前五個都是。而 Google 做得最好，有把資料抽出來整理成表，而其他的都是搜尋有沒有網站有這個關鍵字。在數量方面，Google 如同預期的遠大於 Bing 與百度，而 Yahoo 並沒有公佈數量（是不是不敢講~）。

![Imgur](https://i.imgur.com/jmk7pkN.png)
![Imgur](https://i.imgur.com/9BGizc8.png)
![Imgur](https://i.imgur.com/CoCfFtM.png)
![Imgur](https://i.imgur.com/LN0Vxqn.png)

# 斷詞

`很難想要查詢什麼`：各家查出來的結果差距很大啊，雖然我也不知道這個詞查下去應該要得到怎樣的結果，不過從結果來看，Google 是最理解這句話的，Bing 跟 Yahoo 幾乎一模一樣，而百度根本亂匹配。

![Imgur](https://i.imgur.com/KfeaLxM.png)
![Imgur](https://i.imgur.com/Flc2LXF.png)
![Imgur](https://i.imgur.com/qQIvoh8.png)
![Imgur](https://i.imgur.com/rUOmRZ6.png)

## 標點符號

`,`：大家都可以抓出這是逗號~除了百度，你連這個也可以打廣告！還是第一個結果那個不是廣告？

![Imgur](https://i.imgur.com/tFwq5Sm.png)
![Imgur](https://i.imgur.com/bnbC9ig.png)
![Imgur](https://i.imgur.com/gzUx2av.png)
![Imgur](https://i.imgur.com/TjmsNPq.png)

# 無效查詢

`asdojvjoiqwjefoiajsdvokmasdif`：給一段無效的字串，預期什麼都查不到……但百度你強，這也搜得到東西

![Imgur](https://i.imgur.com/DJ2tC0I.png)
![Imgur](https://i.imgur.com/B73yAB5.png)
![Imgur](https://i.imgur.com/SXeti2s.png)
![Imgur](https://i.imgur.com/Z5gB0I3.png)

# 以圖搜圖

搜下面這張圖，預計結果 `keroro 共鳴`。

![Imgur](https://i.imgur.com/JKAVZOb.png)

---------------

結果只有 Google 正確判別了，不過百度也不算太差，找到了幾乎相同的圖片。而 Bing 與 Yahoo 不提供「以圖搜圖」，起碼我沒找到就是了。

![Imgur](https://i.imgur.com/qEq7y95.png)
![Imgur](https://i.imgur.com/8bRYzP4.png)


# 自動修正

`線姓代數`：基本的功能，各家都做得不錯，圖就不貼了，都能修正成 `線性代數`。

# 1999年的舊資料

今年一月在 Hacker News 上有一篇 [文章](https://news.ycombinator.com/item?id=16153840) 引起眾人討論。該文章說他觀察到 Google 會丟棄太舊的文章，而 Bing, Duck Duck Go 不會。他網站十年前的文章出現這個現象。今天我再來測試一下，我並不準備使用同一篇，因為他十年前那篇文已引起觀注，現在在 Google, Bing, Yahoo 上都搜得到（是的，百度搜不到）。我拿他更舊的一篇[部落格文](http://inessential.com/1999/12/)來實驗，該文章是 1999 年 12 月寫的，真的古老~

`December 1999 Brent Simmons`：哈哈，竟然只有 Google 搜得到，百度仍然悲劇，Bing, Yahoo 搜到了本人的 LinkedIn 但搜不到他的部落格。有趣的結果~

![Imgur](https://i.imgur.com/sHBouZ4.png)
![Imgur](https://i.imgur.com/xIMyADR.png)
![Imgur](https://i.imgur.com/pJ9hcJ4.png)
![Imgur](https://i.imgur.com/iC5WqiQ.png)

# 頁庫存檔

`Denver Broncos` 維基百科的頁庫存檔：Google 穩定，百度直接死，bing 沒問題，Yahoo 根本連不進去。

![Imgur](https://i.imgur.com/qhPtEZ1.png)
![Imgur](https://i.imgur.com/DciB59A.png)
![Imgur](https://i.imgur.com/6VH5aHQ.png)
![Imgur](https://i.imgur.com/3yCT81z.png)

# 廣告

從之前的圖片你可以發現，Google 根本良心企業，百度, bing, Yahoo 都把廣告做得非常像搜尋結果，其中，百度非常的誇張，常常前五個結果都是廣告，而想到之前百度廣告害死人的新聞，真的覺得百度這企業太可惡了。