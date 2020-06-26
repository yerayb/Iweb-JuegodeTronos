$(document).ready(function() {
  //jQuery code...
  $("div.content container > p").click(function () {
    var contenido = $(this).attr("name");
    contenido = "#" + contenido + "personaje";
    $(contenido).slideUp();
  });
  $("div.content container > p").dblclick(function () {
    var contenido = $(this).attr("name");
    contenido = "#" + contenido + "personaje";
    $(contenido).slideDown();
  });
});
