$(filtro).change(function() {
        var baseUrl   = 'http://webapp158824.ip-45-79-51-149.cloudezapp.io/Usuario/';
        var filtro     = $('#filtro');
        var filtro = $(this).val();
        window.location.href = baseUrl + '?filtro=' + filtro;

    });


