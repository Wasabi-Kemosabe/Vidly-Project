function displayMovie(movie) {
    console.log(movie);
    var container = $(".cat-container");
    var li = `
    <div class="card text-center">
        <img src="${movie.image}" class="card-img-top" alt="movie image">
        <div class="card-body">
            <h5 class="card-title">${movie.title}</h5>
            <p class="card-text">${movie.genre.name}</p>
            <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#movie-modal">
                Click here for more info!
            </button>
            <div class="modal fade" id="movie-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">${movie.title}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <p>${movie.description}</p>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Buy/rent movie</button>
                        </div>
                    </div>
                </div>
            </div>
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

// Testing out Git commands