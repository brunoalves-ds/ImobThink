$(document).ready(function () {

    var baseUrl = 'http://webapp158824.ip-45-79-51-149.cloudezapp.io/Imovel';
    var filterTipo = $('#filter-tipo-imovel');
    var filterQuartos = $('#filter-quartos-imovel');
    var filterAndares = $('#filter-andares-imovel');
    var filterStatus = $('#filter-status-imovel');

    $(filterTipo).change(function () {
        var filterTipo = $(this).val();
        window.location.href = baseUrl + '?filterTipo=' + filterTipo;
    });

    $(filterStatus).change(function () {
        var filterStatus = $(this).val();
        window.location.href = baseUrl + '?filterStatus=' + filterStatus;
    });

    $(filterQuartos).change(function () {
        var filterQuartos = $(this).val();
        window.location.href = baseUrl + '?filterQuartos=' + filterQuartos;

    });

    $(filterAndares).change(function () {
        var filterAndares = $(this).val();
        window.location.href = baseUrl + '?filterAndares=' + filterAndares;

    });

});
