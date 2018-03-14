var increment_result = (data) => {
    if (data['len'] == 0) return;

    var container = $('#result-section > .container');
    var cnt = container.children().length;
    var scroll_target = `a.title[data-id=${cnt + 1}]`

    for (var idx = 0; idx < data['len']; idx++) {
        cnt += 1;
        var item = data['data'][idx];
        var html = `
            <div class="item">
                <a class="title" target="_blank" href=${item.url} data-id=${cnt}>${item.title}</a>
                <span class="url">${item.url}</span>
                <p class="body">${item.body}</p>
            </div>`;
        container.append($(html));
    }

    $.scrollTo(scroll_target, 200, {
        axis: 'y',
        offset: { top: -30 }
    });
}

var submit_query = () => {
    var query = $('#input_input').val();
    if (query == "")
        return;

    $.post('/search', { 'query': query }, (meta) => {
        $('div.meta span.total').html('Total:' + meta['total']);

        $('#result-section > div.container').empty();
        $.post('/more', {}, (ret) => {
            increment_result(ret);
            $.scrollTo($('#result-section'), 200, { axis: 'y' });
        });
    });
}

var init_submit_button = () => {
    $('#submit').click(submit_query);
}

var init_more_button = () => {
    $('#more').click(() => {
        $.post('/more', {}, increment_result);
    });
}

var init_input_field = () => {
    $('#input_input').keypress((e) => {
        if (e.which == 13) {
            submit_query();
            return false;
        }
    });
}

$(() => {
    init_input_field();
    init_submit_button();
    init_more_button();
});