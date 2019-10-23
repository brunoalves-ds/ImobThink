
$( document ).ready(function() {

    var deleteBtn = $('.delete-btn');
    
    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja realmente deletar ?');

        if(result) {
            window.location.href = delLink;
        }

    });

});