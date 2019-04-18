$(function() {


    Morris.Donut({
        element: 'service-km-donut-chart',
        data:[
            {label: "Next Service (KM)", value: 100000},
            {label: "Current Mileage (KM)", value: 92000},
        ],
        resize: true
    });


});
