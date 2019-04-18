vehicle = {}


vehicle.load_purchase_detail = function(vehicle_id) {
    $.get(Urls['fleetmanagement:_load_purchase_detail'](vehicle_id), function(response){
	var content = JSON.parse(response).response_content;
	$('div#purchase_detail').html(content);
    });
}

vehicle.submit_document = function() {
    var el = $(".vehicle_document_upload");
    var vehicle_id = $(el).data('vehicle');
    var form = $(el).closest('form');
    $('form').attrs('action',Urls['fleetmanagement:add_document'](vehicle_id));
};

$( function() {


});
