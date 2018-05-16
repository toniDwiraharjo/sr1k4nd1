Array.prototype.contains = function (obj) {
    var i = this.length;
    while (i--) {
        if (this[i].valueOf() === obj.valueOf()) {
            return true;
        }
    }
    return false;
};

Date.prototype.ddmmyyyy = function () {
    var mm = this.getMonth() + 1; // getMonth() is zero-based
    var dd = this.getDate();

    return [
        (dd > 9 ? '' : '0') + dd,
        (mm > 9 ? '' : '0') + mm,
        this.getFullYear()
    ].join('-');
};


var clat = 0.736672;
var clon = 119.992595;
var zoom = 6;
var center = [clat, clon];
var layer;

var map = L.map('map').setView([clat, clon], zoom);
L.tileLayer('http://{s}.sm.mapstack.stamen.com/(terrain-background,$fff[hsl-saturation@60])[soft-light]/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var coastline = L.map('coastline').setView([clat, clon], zoom);
L.tileLayer('https://api.mapbox.com/styles/v1/hendriprayugo/cj1ebiu2r00gb2sn34tjia85e/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiaGVuZHJpcHJheXVnbyIsImEiOiJjaWlpamthNnUwMHE5dWNrcDlodnAxOGgwIn0.OdKW9hysCK29qvhTAfP3xQ', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(coastline);

map.sync(coastline);
coastline.sync(map);

var enabledate = [
    '01-10-2017',
    '02-10-2017',
    '03-10-2017',
    '04-10-2017',
    '05-10-2017',
    '06-10-2017',
    '07-10-2017',
    '08-10-2017',
    '09-10-2017',
    '10-10-2017'
];

$("#datepicker").datepicker({
    dateFormat: 'dd-mm-yy',
    onSelect: function () {
        setTimeout(function () {
            loadimage();
        }, 1000)
    },
    beforeShowDay: function (date) {
        var formated = date.ddmmyyyy();
        console.log(formated);
        if(enabledate.contains(formated)){
            return [true, "","Available"];
        }else {
            return [false,"","unAvailable"];
        }
    }
});

$('.param').click(function () {
    var item = $(this).attr('value');
    $(this).addClass('itemxactive');
    $('.param').not(this).each(function () {
        $(this).removeClass('itemxactive');
    });
    loadimage()
});

$('#datepicker').on('change', function () {
    alert('test');
});

function loadimage() {
    var item = $('.itemxactive').attr('value');
    var time = $('#datepicker').val();
    var t = time.split('-');
    var formated = t[2] + t[1] + t[0];
    try {
        layer.remove();
    } catch (e) {
    }
    var imageUrl = '/static/images/sat/' + item + '.' + formated + '.png',
        imageBounds = [[11, 94], [-11, 141]];
    layer = L.imageOverlay(imageUrl, imageBounds, {opacity: 0.7}).addTo(map);
    $('#lg-src').attr('src', '/static/images/sat/' + item + '.png');
}

setTimeout(function () {
    loadimage();
}, 1000);