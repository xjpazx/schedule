$(function () {
    $(document).ready(function () {
        $('#id_activity_fk').change(function () {
            var valor = $('select[name="activity_fk"] option:selected').text();
            $.ajax({
                url: '/schedule/as/schedule/',
                type: 'post',
                dataType: 'json',
                data: {val: valor},
                success: function (data) {
                    console.log(data)
                    const toDel = data.data;
                    console.log(toDel)
                    const opts = OrderedSelectBox.cache.id_employees_from.filter(function (e, i) {
                        return !toDel.includes(e.text)
                    });
                    console.log(opts)
                    OrderedSelectBox.cache.id_employees_from = opts;
                    console.log(OrderedSelectBox.cache.id_employees_from)
                    OrderedSelectBox.redisplay('id_employees_from')
                },
                error: function (error) {
                    console.log(error)
                }
            });
        });
    });

});