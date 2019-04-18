$(function() {

    $('.date_field').not('.birth_date').datetimepicker({
	format: 'yyyy-mm-dd',
	minView:'month',
	autoclose: true,
	forceParse:true,
	startView: 4,
    });

    $('.year_field').datetimepicker({
	format: 'yyyy',
	startView: 4,
	minView: 4,
	autoclose: true,
    });

    $('.birth_date').datetimepicker({
	format: 'yyyy-mm-dd',
	minView:'month',
	autoclose: true,
	forceParse:true,
	startView: 4,
    });
    
    $('.date_time_field').datetimepicker({autoclose: true});
    
    // OVERRIDE DATEPICKER HTML
    $('.datetimepicker table.table-condensed').addClass('table').removeClass('table-condensed');
});

