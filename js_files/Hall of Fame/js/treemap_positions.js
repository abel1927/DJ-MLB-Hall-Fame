$.getJSON('./data/pos_nac_hall.json', function (data) {
  var chartDom = document.getElementById('chart-positions');
  var myChart = echarts.init(chartDom);
  var option;
  
  var total = 0
  for(var key in data['posiciones']){
    total = total + data['posiciones'][key]
  }

  //function format(oro, total){

  //} 

  var nodes = [];
  for (var key in data['posiciones']) {
      jugadores =  data['posiciones'][key]
      nodes.push(
          {
              name: key + "  " + String(jugadores) + "(" + String(Math.round(jugadores*100/total)) +"%)",
              value: jugadores,
          },
      );
  }
  
  console.log(nodes);

  option = {
    series: [
      {
        type: 'treemap',
        data: nodes,
      }
    ]
  };
  
  myChart.setOption(option);

  $(window).on('resize', resize);

  function resize() {
      setTimeout(function () {

          myChart.resize();
      }, 200);
  }

});
