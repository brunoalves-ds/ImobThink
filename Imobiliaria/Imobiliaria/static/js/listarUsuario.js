$(filtro).change(function() {
        var baseUrl   = 'http://127.0.0.1:8000/Usuario/';
        var filtro     = $('#filtro');
        var filtro = $(this).val();
        window.location.href = baseUrl + '?filtro=' + filtro;
    });

