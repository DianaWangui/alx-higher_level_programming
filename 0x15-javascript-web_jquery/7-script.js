// $(function () {}); is a shortcut for $(document).ready(function() {});
$("document").ready(function() {
    url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
    $.get(url, function(data){
        $("#character").text(data.name)
    });
});