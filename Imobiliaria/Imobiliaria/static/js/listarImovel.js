$(document).ready(function () {

    var baseUrl = 'http://localhost:8000/Imovel/';
    var filterTipo = $('#filter-tipo-imovel');
    var filterQuartos = $('#filter-quartos-imovel');
    var filterAndares = $('#filter-andares-imovel');
    var filterStatus = $('#filter-status-imovel');

    $(filterTipo).change(function () {
        var filterTipo = $(this).val();
        window.location.href = baseUrl + '?filterTipo=' + filterTipo;
    });

    $(filterStatus).on('click',function () {
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