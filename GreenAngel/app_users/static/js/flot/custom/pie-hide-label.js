var $border_color = "#f9f9f9";
var $grid_color = "#eeeeee";
var $default_black = "#c3ddec";
var $default_white = "#ffffff";
var $sky_blue = "#edf5fa";
var $green = "#8ecf67";
var $blue = "#87ceeb";

$(document).ready(function () {
    $.get('/api/mycampaignstat/', function(data) {
        $.plot($("#hideLabelPie"), data, {
            series: {
                pie: {radius: 1, show: true,
                    label: {
                        show: true,
                        radius: 2/3,
                        formatter: function(label, series) {
                            return '<div style="font-size:11px ;text-align:center; padding:2px; color:white;">'+label+'<br/>'+Math.round(series.percent)+'%</div>';
                        },
                        threshold: 0.1,
                    }
                },
            },
            legend:{  
                show: false,
            },
            colors: [$green, $blue, $default_black],

        });

    })
});
 

