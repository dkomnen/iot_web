/**
 * Created by David on 4/30/18.
 */
function submitDevices() {
    var myCheckboxes = [];
    $("input:checked").each(function () {
        myCheckboxes.push($(this).val());
    });
    var data = {
        device_ids: myCheckboxes,
        interval: "monthly"
    };
    $.ajax({
        type: "POST",
        url: "api/viking/graph_data",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (data) {
            $('#myResponse').html(data)
        }
    });
    return false;

}