open_side_panel = function() {
    $('#side_panel').css({ 'width': '20%' }),
        $('#main').css({ 'marginLeft': '20%' }),
        $('#open_icon').css({ 'display': 'none' });
}

close_side_panel = function() {
    $('#side_panel').css({ 'width': '0' }),
        $('#main').css({ 'marginLeft': '0' }),
        $('#open_icon').css({ 'display': 'inline-block' });
}