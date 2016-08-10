

$(document).ready(function () {

    //cache
    var packages;
    var services;
    var $packageChoice = $("#id_service_package");
    var $serviceChoice = $("#id_services");
    var $preTaxFinalPrice = $("#id_pre_tax_final")


    //function use the package info to check corresponding box
    function check_service(packageIdSelected) {
        var services = $.grep(packages,function (element, index) {
            return element.pk == packageIdSelected;
        })[0].fields.services;

        // uncheck everything
        $serviceChoice.find("input").prop( "checked", false );
        // check
        for(i=0;i<services.length;i++){
            serviceId = services[i].toString();
            $serviceChoice.find("input[value=" + serviceId + "]").prop( "checked", true );
        }
    }



    //function to update price
    function calculate_price() {
        var preTaxFinal = 0;
        var price = 0;
        var serviceBoxes = $serviceChoice.find("input");
        for(i=0;i<serviceBoxes.length;i++){
            if(serviceBoxes[i].checked){
                price = $.grep(services,function (element, index) {
                    return element.pk == serviceBoxes[i].value;
                })[0].fields.price;
                preTaxFinal += price;
            }
        }
        $preTaxFinalPrice.val(preTaxFinal);
    }
    //get the json that have the package data
    $.ajax({
        type:'GET',
        url:'/structure/packages/json',
        success:function (data) {
            //parse the JSON string
            packages = $.parseJSON(data);
            console.log('success', packages);

            $.ajax({
                type:'GET',
                url:'/structure/services/json',
                success:function (data) {
                    //parse the JSON string
                    services = $.parseJSON(data);
                    console.log('success', services);

            }
    });


        }
    });





    //set up the trigger of choice change
    $packageChoice.on('change', function (e) {
        var optionSelected = $("option:selected", this);
        var packageIdSelected = optionSelected.attr('value');

        check_service(packageIdSelected);
        calculate_price();
    });

    // set up the triiger for calculating price
    $serviceChoice.find(":checkbox").change(function (e) {
        calculate_price();
    });
});