/**
 * Created by David on 4/30/18.
 */
var dataSet = [];
var dataLabels = [];
var device_serial_numbers = [];

function drawChart() {
    var chartMin = $("#chart-min").val();
    var chartMax = $("#chart-max").val();
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dataLabels,
            datasets: dataSet
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        //beginAtZero: true
                        suggestedMin: 20,
                        min: parseFloat(chartMin),
                        max: parseFloat(chartMax)
                    }
                }]
            }
        }
    });
}

function submitDevices() {
    dataSet = [];
    dataLabels = [];
    var myCheckboxes = [];
    $("input:checked").each(function () {
        myCheckboxes.push($(this).val());
    });
    var data = {
        device_ids: myCheckboxes,
        interval: $("#interval-select").val(),
        user_id: $("#my-data").data().userId

    };
    $.ajax({
        type: "POST",
        url: "api/viking/graph_data",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (data) {
            device_serial_numbers = data["device_ids"];
            var result_string = "";
            var index = 0;
            for (var key in data) {
                result_string += key + " " + data[key] + "</br>";
                var data_points_map = data[key];
                var data_set = [];
                for (var data_points_key in data_points_map) {
                    data_set.push(data_points_map[data_points_key]);
                    //dataLabels.push(data_points_key)
                    dataLabels.push(new Date(data_points_key * 1000))
                }
                dataSet.push(createDataset(data_set, key, index));
                dataLabels = clearDataLabelDuplicates(dataLabels)
                index++;
            }
            drawChart();
        }
    });
    return false;

}

function addDevice() {
    var data = {
        "serial_number": $("#device_serial_number").val(),
        "name": $("#device_name").val(),
        "device_type": "temperature"
    };
    var user_id = $("#my-data").data().userId;
    console.log(user_id);
    $.ajax({
        type: "POST",
        url: "api/user/" + user_id + "/device",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (data) {

        }
    });
    return false;
}

function showEditDevice(index, device_type) {
    console.log(index);
    $("#device-container-" + index).hide();
    $("#edit-device-container-" + index).show();
    switch (device_type) {
        case "temperature":
            $("#edit-device-container-radio-temperature-" + index).prop("checked", true);
            break;
        case "power":
            $("#edit-device-container-radio-power-" + index).prop("checked", true);
            break;
        case "water":
            $("#edit-device-container-radio-water-" + index).prop("checked", true);
            break;
    }
}

function editDevice(device_id) {
    //var device_id = "5ae8c792e89bdea63b78095a";
    console.log(device_id);
    var data = {
        "serial_number": $("#edit_device_serial_number").val(),
        "name": $("#edit_device_name").val(),
        "device_type": "temperature"
    };
    var user_id = $("#my-data").data().userId;
    console.log(user_id);
    $.ajax({
        type: "POST",
        url: "api/user/" + user_id + "/device/" + device_id,
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (data) {
            location.reload();
            location.href = location.href;
        }
    });
    return false;
}

function createDataset(dataPoints, deviceName, index) {
    return {
        label: deviceName,
        data: dataPoints,
        backgroundColor: [
            getColor(index)
        ],
        borderColor: [
            getColor(index)
        ],
        borderWidth: 1
    }
}

function clearDataLabelDuplicates(dataLabels) {
    var seen = {};
    var out = [];
    var len = dataLabels.length;
    var j = 0;
    for (var i = 0; i < len; i++) {
        var item = dataLabels[i];
        if (seen[item] !== 1) {
            seen[item] = 1;
            out[j++] = item;
        }
    }
    return out;
}

function random_rgba() {
    var o = Math.round, r = Math.random, s = 255;
    return 'rgba(' + o(r() * s) + ',' + o(r() * s) + ',' + o(r() * s) + ',' + r().toFixed(1) + ')';
}

function getColor(index) {
    var colors = [
        "rgba(255,100,100, 0.5)",
        "rgba(100,255,100, 0.5)",
        "rgba(100,100,255, 0.5)",
        "rgba(250,240,0  , 0.5)"

    ];
    return colors[index];
}

function getDeviceStatus() {
    console.log(device_serial_numbers);
    $.ajax({
        type: "POST",
        url: "api/viking/status",
        data: JSON.stringify(device_serial_numbers),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (data) {
            console.log(data);
            for (var key in data) {
                var device = data[key];
                console.log(device);
                if (device["status"] == true) {
                    $("#" + device["serial_number"] + "-status-up").show();
                    $("#" + device["serial_number"] + "-status-down").hide();

                } else {
                    $("#" + device["serial_number"] + "-status-up").hide();
                    $("#" + device["serial_number"] + "-status-down").show();
                }
            }
        }
    });
    return false;
}
