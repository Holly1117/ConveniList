window.onload = function () {
  setLawsonCard();
  setFamilyMartCard();
  setSevenElevenCard();
  setDailyYamazakiCard();
};

function setLawsonCard() {
  var $result = $(".lawson");
  var cardList = [];
  var displayLimit = 5;
  $.getJSON("/lawson.json", function (dataList) {
    for (var i in dataList) {
      if (i >= displayLimit) break;
      var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_image}\">`;
      var titleTag = `<p class=\"card-title\">${dataList[i].product_name}</p>`;
      var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_price}円<span>(税込)</span></p><p>発売日<span class="release">${dataList[i].product_date}</span></p></div>`;
      var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${
        titleTag + cardTextTag
      }</div></div>`;
      cardList.push(
        `<a href=\"${dataList[i].product_url}\">${cardContentTag}</a>`
      );
    }
    $result[0].innerHTML = cardList.join("");
  });
}

function setFamilyMartCard() {
  var $result = $(".familymart");
  var cardList = [];
  var displayLimit = 5;
  $.getJSON("/familyMart.json", function (dataList) {
    for (var i in dataList) {
      if (i >= displayLimit) break;
      var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_image}\">`;
      var titleTag = `<p class=\"card-title\">${dataList[i].product_name}</p>`;
      var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_price}円<span>(税込)</span></p><p>発売日<span class="release">${dataList[i].product_date}</span></p></div>`;
      var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${
        titleTag + cardTextTag
      }</div></div>`;
      cardList.push(
        `<a href=\"${dataList[i].product_url}\">${cardContentTag}</a>`
      );
    }
    $result[0].innerHTML = cardList.join("");
  });
}

function setDailyYamazakiCard() {
  var $result = $(".dailyYamazaki");
  var cardList = [];
  var displayLimit = 5;
  $.getJSON("/dailyYamazaki.json", function (dataList) {
    for (var i in dataList) {
      if (i >= displayLimit) break;
      var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_image}\">`;
      var titleTag = `<p class=\"card-title\">${dataList[i].product_name}</p>`;
      var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_price}円<span>(税込)</span></p><p>発売日<span class="release">${dataList[i].product_date}</span></p></div>`;
      var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${
        titleTag + cardTextTag
      }</div></div>`;
      cardList.push(
        `<a href=\"${dataList[i].product_url}\">${cardContentTag}</a>`
      );
    }
    $result[0].innerHTML = cardList.join("");
  });
}

function setSevenElevenCard() {
  var $result = $(".seveneleven");
  var sectionList = [];
  var displayLimit = 5;
  var areaLimit = "北海道";
  $.getJSON("/sevenEleven.json", function (dataList) {
    for (var i in dataList) {
      if (dataList[i].prefecture_name != areaLimit) continue;

      var cardList = [];

      for (var j in dataList[i].product_list) {
        if (j >= displayLimit) break;
        var imageTag = `<img class=\"card-img\" src=\"${dataList[i].product_list[j].product_image}\">`;
        var titleTag = `<p class=\"card-title\">${dataList[i].product_list[j].product_name}</p>`;
        var cardTextTag = `<div class=\"card-text\"><p>${dataList[i].product_list[j].product_price}円<span>(税込)</span></p><p>発売日<span class="release">${dataList[i].product_list[j].product_date}</span></p></div>`;
        var cardContentTag = `<div class=\"card\">${imageTag}<div class=\"card-content\">${
          titleTag + cardTextTag
        }</div></div>`;
        cardList.push(
          `<a href=\"${dataList[i].product_list[j].product_url}\">${cardContentTag}</a>`
        );
      }

      var wrapperTag = cardList.join("");

      sectionList.push(wrapperTag);
    }
    $result[0].innerHTML = sectionList.join("");
  });
}
