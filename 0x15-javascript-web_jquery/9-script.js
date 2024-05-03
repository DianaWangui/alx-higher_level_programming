$(function () {
    url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function (data) {
      $("DIV#hello").text(data.hello);  
    })
})