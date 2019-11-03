
$( document ).ready(function() {


    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn-cliente');
    var searchForm = $('#search-form-cliente');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja realmente deletar ?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn-cliente).on('click', function() {
        searchForm-cliente.submit();
    });
    $(searchBtn-usuario).on('click', function() {
        searchForm-usuario.submit();
    });



});

$(filter).change(function() {
        var baseUrl   = 'http://127.0.0.1:8000/Cliente/';
        var filter     = $('#filter');
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });