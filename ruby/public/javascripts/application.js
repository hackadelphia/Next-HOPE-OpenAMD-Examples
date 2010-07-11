var METER = 10;
var API = "http://api.hope.net/api/";

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

$(document).ready(function() {
                    drawRooms();
                    drawPeople();
                  });

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

function drawPeople() {
  var ctx = getContext();
  $.ajax({
           url: '/api/locations/',
           data: {user: 'user1'},
           success: function(data/*, textStatus, xhr*/){
             for(var i = 0; i < data.length; i++) {
               drawPerson(data[i], ctx);
             }
           }
         });
}

function drawPerson(person, ctx) {
  fillCircle(person.x*METER, person.y*METER, .5*METER, '#f00', ctx);
}

function drawRooms(){
  var multiplier = 10;
  var canvas = document.getElementById('map');
  if (canvas.getContext){
    var ctx = canvas.getContext('2d');
    var room;
    var first;
    for(var i = 0; i < fakeFloor.length; i++) {
      room = fakeFloor[i];
      if (room.floor === 1) {
        ctx.beginPath();
        first = room.vertices[0];
        ctx.moveTo(first[0], first[1]);
        for (var k = 1; k < room.vertices.length; k++) {
          ctx.lineTo(room.vertices[k][0], room.vertices[k][1]);
        }
        ctx.lineTo(first[0], first[1]);
        ctx.closePath();
        ctx.stroke();
      }
    }
  }
}
