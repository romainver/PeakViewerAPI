
console.log('in')
      var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([12.41, 8.82]),
          zoom: 4
        })
      });
      {% if peaks %}
      {% for peak in peaks %}
      console.log('{{peak.coordinates.0}}')
      console.log('{{peak.latitude}}')
      //TODO : Replace long lat by coordinates
       var layer = new ol.layer.Vector({
     source: new ol.source.Vector({
         features: [
             new ol.Feature({
                 geometry: new ol.geom.Point(ol.proj.fromLonLat([{{peak.coordinates.1}}, {{peak.coordinates.0}}])),
                 id:{{peak.id}}
     })]
 })
   });
        map.addLayer(layer);
{%endfor%}


 
 map.on("click", function(e) {
    map.forEachFeatureAtPixel(e.pixel, function (feature, layer) {
      $.get('/getrecords/'+feature.values_.id, function (data){
        console.log(data);
        const chart = Highcharts.chart('chart', {
            
            title: {
                text: 'Temperature Forecast for '+data.peak
            },
            xAxis: {
                type:'datetime'
            },
            yAxis: {
                title: {
                    text: 'Temperature (in °C)'
                }
            },
            series: [{
                type:'line',
                data: data.records,
            }, ]
        });
      });
        
    })
});
 {%endif%}
