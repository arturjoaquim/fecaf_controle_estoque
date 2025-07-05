function iniciarSelect2(seletor, placeholder, configExtra = {}) {
    $(function () {
        $(seletor).select2({
            placeholder: placeholder,
            allowClear: true,
            ...configExtra
        });
    });
}


const propriedadesAjaxSelect2 = {
    produtos: {
        minimumInputLength: 4,
        ajax: {
            url: "/api/produto/consultar-id-por-nome",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                console.log(params.term)
                return {
                    nomeProduto: params.term
                };
            },
            processResults: function (data) {
                console.log(data)
                return {
                    results: data.map(produto => ({
                        id: produto.idProduto,
                        text: produto.nomeProduto
                    }))
                };
            },
            cache: true
        }
    },
    tiposMovimento: {
        ajax: {
            url: "/api/tipo-movimentacao/consultar-id-por-nome",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                console.log(params.term)
                return {
                    nomeTipoMov: params.term
                };
            },
            processResults: function (data) {
                console.log(data)
                return {
                    results: data.map(tpMov => ({
                        id: tpMov.idTipoMov,
                        text: tpMov.nomeTipoMov
                    }))
                };
            },
            cache: true
        }
    }
}
