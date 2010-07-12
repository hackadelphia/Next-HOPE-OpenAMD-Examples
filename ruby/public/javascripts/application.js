var MAX_WIDTH = 100; //meters TODO: find out how big biggest dimension of all rooms is.
var METER;
var cache = {};

var fakeFloor =

$(document).ready(paint);
$(window).bind('resize', repaint);

function repaint() {
  $('#map').remove();
  paint(true);
}

function paint(useCache) {
  if (useCache === undefined) {
    useCache = false;
  }
  calculateMeter();
  createCanvas();
  drawMap(useCache);
  drawPeople('Egressia', useCache);
}

function calculateMeter() {
  METER = (window.innerWidth > window.innerHeight) ? (window.innerHeight-20)/MAX_WIDTH : (window.innerWidth-20)/MAX_WIDTH;
}

function createCanvas() {
  $('<canvas id="map" width="'+(window.innerWidth-20)+'" height="'+(window.innerHeight-20)+'"></canvas>').appendTo('#container');
}

/**
 * color = hex, e.g. '#fff'
 */
function fillCircle(x, y, radius, color) {
  var ctx = getContext();
  ctx.beginPath();
  ctx.fillStyle = color;
  ctx.arc(x, y, radius, 0, Math.PI*2, true);
  ctx.fill();
  ctx.closePath();
}

function getContext() {
  var canvas = document.getElementById('map');
  if (canvas.getContext) {
    return canvas.getContext('2d');
  } else {
    throw "Canvas is not supported in this browser!";
  }
}

function drawPeople(area, useCache) {
  var ctx = getContext();
  if (useCache && cache && cache.people) {
    peopleRenderer(cache.people);
  } else {
    $.ajax({
             url: '/api/locations/',
             data: {area: area},
             success: function(data){
               cache.people = data;
               peopleRenderer(cache.people);
             }
           });
  }
}

function peopleRenderer(data) {
  for(var i = 0; i < data.length; i++) {
    drawPerson(data[i]);
  }
}

function drawPerson(person) {
  fillCircle(person.x*METER, person.y*METER, .5*METER, encodeToHex(person.user).substring(0, 7));
}

function drawMap(useCache){
  if (useCache && cache && cache.map){
    mapRenderer(cache.map);
  } else {
    $.get('/api/map/', {}, function(data){
            cache.map = data;
            mapRenderer(cache.map);
          });
  }
}

function mapRenderer(map) {
  for(var i = 0; i < map.length; i++) {
    drawRoom(map[i]);
  }
}

function drawRoom(room) {
  var ctx = getContext();
  var first;
  if (room.floor === 1) {
    ctx.beginPath();
    first = room.vertices[0];
    ctx.moveTo(first[0]*METER, first[1]*METER);
    for (var k = 1; k < room.vertices.length; k++) {
      ctx.lineTo(room.vertices[k][0]*METER, room.vertices[k][1]*METER);
    }
    ctx.lineTo(first[0]*METER, first[1]*METER);
    ctx.closePath();
    ctx.stroke();
  }
}

/**
 * Todo: come up with cool way to generate hexcolors from user ids.
 */
function encodeToHex(str){
    var r="";
    var e=str.length;
    var c=0;
    var h;
    while(c<e){
        h=str.charCodeAt(c++).toString(16);
        while(h.length<3) h="0"+h;
        r+=h;
    }
    return r;
}