var nodes = ([
  {id: 0, label: '0'},
  {id: 1, label: '1'},
  {id: 2, label: '2'},
  {id: 3, label: '3'},
  {id: 4, label: '4'},
]);

var edges = ([
  {from: 0, to: 2, label: '7'},
  {from: 2, to: 0, label: '7'},
]);

var data = {
  nodes: nodes,
  edges: edges,
var container = document.getElementById('mynetwork');
};
var options = {};
var network = new vis.Network(container, data, options);
