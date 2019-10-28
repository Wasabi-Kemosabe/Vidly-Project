function displayMovie(movie) {
    console.log(movie);
    var container = $(".cat-container");
    var li = `
    <div class="card text-center">
        <img src="${movie.image}" class="card-img-top" alt="movie image">
        <div class="card-body">
            <h5 class="card-title">${movie.title}</h5>
            <p class="card-text">${movie.genre.name}</p>
            <a href="#" class="btn btn-primary">Click here for details!</a>
        </div>
    </div>
    `;
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