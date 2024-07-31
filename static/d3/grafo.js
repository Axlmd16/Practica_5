var nodes = ([
  {id: 0, label: '0, Simon Bolivar'},
  {id: 1, label: '1, Argelia'},
  {id: 2, label: '2, Estacion "La Tebaida"'},
  {id: 3, label: '3, Terminal'},
  {id: 4, label: '4, Plaza Leon'},
  {id: 5, label: '5, Coliseo "Ciudad de Loja"'},
  {id: 6, label: '6, Cementerio General'},
  {id: 7, label: '7, Hospital Isidro Ayora'},
  {id: 8, label: '8, Conservatorio Salvador Bustamante'},
  {id: 9, label: '9, Parque "Jipiro"'},
  {id: 10, label: '10, Zoologico'},
  {id: 11, label: '11, UNL'},
  {id: 12, label: '12, Laguna "Daniel Alvarez"'},
  {id: 13, label: '13, Estadio "Reyna del Cisne"'},
  {id: 14, label: '14, Mercado Mayorista'},
  {id: 15, label: '15, Cabo Biancho'},
]);

var edges = ([
  {from: 0, to: 1, label: '0.629'},
  {from: 0, to: 3, label: '6.586'},
  {from: 0, to: 13, label: '4.283'},
  {from: 1, to: 0, label: '0.629'},
  {from: 1, to: 4, label: '3.513'},
  {from: 1, to: 2, label: '2.419'},
  {from: 1, to: 9, label: '6.678'},
  {from: 2, to: 1, label: '2.419'},
  {from: 3, to: 0, label: '6.586'},
  {from: 3, to: 4, label: '2.564'},
  {from: 3, to: 5, label: '3.049'},
  {from: 3, to: 9, label: '0.707'},
  {from: 4, to: 1, label: '3.513'},
  {from: 4, to: 3, label: '2.564'},
  {from: 4, to: 7, label: '1.003'},
  {from: 4, to: 9, label: '3.202'},
  {from: 5, to: 3, label: '3.049'},
  {from: 5, to: 10, label: '5.24'},
  {from: 6, to: 13, label: '2.251'},
  {from: 7, to: 4, label: '1.003'},
  {from: 7, to: 12, label: '2.974'},
  {from: 8, to: 9, label: '0.264'},
  {from: 8, to: 14, label: '1.363'},
  {from: 9, to: 1, label: '6.678'},
  {from: 9, to: 3, label: '0.707'},
  {from: 9, to: 4, label: '3.202'},
  {from: 9, to: 8, label: '0.264'},
  {from: 10, to: 5, label: '5.24'},
  {from: 11, to: 12, label: '1.867'},
  {from: 11, to: 15, label: '2.741'},
  {from: 12, to: 7, label: '2.974'},
  {from: 12, to: 11, label: '1.867'},
  {from: 13, to: 0, label: '4.283'},
  {from: 13, to: 6, label: '2.251'},
  {from: 14, to: 8, label: '1.363'},
  {from: 15, to: 11, label: '2.741'},
]);

var data = {
  nodes: nodes,
  edges: edges,
};
var container = document.getElementById('mynetwork');
var options = {};
var network = new vis.Network(container, data, options);
var camino = [15, 11, 12, 7, 4, 9];
network.on('afterDrawing', function(ctx) {
  for (var i = 0; i < camino.length - 1; i++) {
    var node1 = network.getPositions([camino[i]])[camino[i]];
    var node2 = network.getPositions([camino[i + 1]])[camino[i + 1]];
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(node1.x, node1.y);
    ctx.lineTo(node2.x, node2.y);
    ctx.stroke();
  }
});
