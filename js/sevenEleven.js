window.onload = function () {
    setCard();
}

function setCard() {
    var $result = $("#section-list");
    var sectionList = [];
    $.getJSON("./sevenEleven.json", function (dataList) {

        for (var i in dataList) {
            var prefectureNameTag = `<h3 class=\"city-title\"><span>${dataList[i].prefecture_name}</span></h3>`;

            var prefectureUrlTag = `<a href=\"${dataList[i].prefecture_url}\"><button>もっと見る</button></a>`;

            var cardList = [];

            for (var j in dataList[i].product_list) {
                var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_list[j].product_image}\">`;
                var titleTag = `<p class=\"card-title\">${dataList[i].product_list[j].product_name}</p>`;
                var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_list[j].product_price}円(税込)</p><p>発売日${dataList[i].product_list[j].product_date}</p></div>`;
                var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${titleTag + cardTextTag}</div></div>`;
                cardList.push(`<a href=\"${dataList[i].product_list[j].product_url}\">${cardContentTag}</a>`);
            }

            var wrapperTag = `<div class=\"wrapper hokkaido\"><div class=\"card-list\">${cardList.join("")}</div></div>`;

            sectionList.push(`<section>${prefectureNameTag + wrapperTag + prefectureUrlTag}</section>`);

        }
        $result[0].innerHTML = sectionList.join("");
    });
}