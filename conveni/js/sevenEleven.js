window.onload = function () {
    setCard();
}

function setCard() {
    var $result = $(".seveneleven");
    var sectionList = [];
    $.getJSON("/sevenEleven.json", function (dataList) {
        for (var i in dataList) {
            var prefectureNameTag = `<div class="title"><h2>${dataList[i].prefecture_name}</h2></div>`;

            var prefectureUrlTag = `<div class="wrapper"><a href=\"${dataList[i].prefecture_url}\"><button>もっと見る</button></a></div>`;

            var cardList = [];

            for (var j in dataList[i].product_list) {
                var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_list[j].product_image}\">`;
                var titleTag = `<p class=\"card-title\">${dataList[i].product_list[j].product_name}</p>`;
                var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_list[j].product_price}円<span>(税込)</span></p><p>発売日<span class="release">${dataList[i].product_list[j].product_date}</span></p></div>`;
                var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${titleTag + cardTextTag}</div></div>`;
                cardList.push(`<a href=\"${dataList[i].product_list[j].product_url}\">${cardContentTag}</a>`);
            }

            var wrapperTag = `<div id="card-list" class="wrapper card-list sevenStyle">${cardList.join("")}</div>`;

            sectionList.push(`<section>${prefectureNameTag + wrapperTag + prefectureUrlTag}</section>`);

        }
        $result[0].innerHTML = sectionList.join("");
    });
}