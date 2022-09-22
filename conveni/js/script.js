$(function() {
    //トップに戻るを表示 
    $(window).scroll(function () {
        if ($(window).scrollTop() > 200) {
            $('#go-top').fadeIn();
        } else {
            $('#go-top').fadeOut();
        }
    });

    //スクロール時にふわっと移動する
    var headerHight = 80;
    $('a[href^=#]').click(function(){
        var href= $(this).attr("href");
          var target = $(href == "#" || href == "" ? 'html' : href);
           var position = target.offset().top-headerHight;
        $("html, body").animate({scrollTop:position}, 550, "swing");
           return false;
    });

    //もっと見る
    $(function(){
        $(".more").on("click", function() {
            $(this).toggleClass("on-click");
            $(".txt-hide").slideToggle(300);
        });
    });
});