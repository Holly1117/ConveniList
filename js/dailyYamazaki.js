window.onload = function () {
  setCard();
};

function setCard() {
  var $result = $(".dailyYamazaki");
  var cardList = [];
  $.getJSON("/dailyYamazaki.json", function (dataList) {
    for (var i in dataList) {
      var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_image}\">`;
      var titleTag = `<p class=\"card-title\">${dataList[i].product_name}</p>`;
      var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_price}円<span>(税込)</span></p><p>発売日<span class="release">${dataList[i].product_date}</span></p></div>`;
      var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${
        titleTag + cardTextTag
      }</div></div>`;
      cardList.push(
        `<a href=\"https://www.daily-yamazaki.jp/new/\">${cardContentTag}</a>`
      );
    }
    $result[0].innerHTML = cardList.join("");
  });
}
