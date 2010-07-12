var MAX_WIDTH = 100; //meters TODO: find out how big biggest dimension of all rooms is.
var METER;

var fakeFloor = [{
                   "name" : "FarLand",
                   "vertices": [[0, 0],[50, 0],[50,50],[20,60],[0,50]],
                   "floor": 1
                 },
                 {
                   "name" : "cptn_corner",
                   "vertices": [[50, 0],[100, 0],[100,100],[50,100]],
                   "floor": 1
                 }
                ];

$(document).ready(paint);
$(window).bind('resize', repaint);

function repaint() {
  $('#map').remove();
  paint();
}

function paint() {
  calculateMeter();
  createCanvas();
  drawRooms();
  drawPeople('Egressia');
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
function fillCircle(x, y, radius, color, ctx) {
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

function drawPeople(area) {
  var ctx = getContext();
  $.ajax({
           url: '/api/locations/',
           data: {area: area},
           success: function(data/*, textStatus, xhr*/){
             for(var i = 0; i < data.length; i++) {
               drawPerson(data[i], ctx);
             }
           }
         });
}

function drawPerson(person, ctx) {
  fillCircle(person.x*METER, person.y*METER, .5*METER, encodeToHex(person.user).substring(0, 7), ctx);
}

function drawRooms(){
  var ctx = getContext();
  var room;
  var first;
  // TODO: Change fakeFloor to make a call to the API for floor data.
  for(var i = 0; i < fakeFloor.length; i++) {
    room = fakeFloor[i];
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
}

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