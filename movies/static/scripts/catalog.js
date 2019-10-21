function displayMovie(movie) {
    console.log(movie);
    var container = $(".cat-container");
    var li = `<li>${movie.title}</li>`;
    container.append(li);
}

function getData() {
    $.ajax({
        type: "GET",
        url: "/api/movies",
        success: function (res) {
            var movies = res.objects;
            for (let i = 0; i < movies.length; i++) {
                displayMovie(movies[i]);
            }
        },
        error: function (details) {
            console.log("Error on get req", details);
        }
    });
}

function init() {
    console.log("Hello catalog page");
    getData();
}

window.onload = init();