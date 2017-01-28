  var map;
  var myLocation = {
    'latitude':  47.66,
    'longitude': -122.355,
    // 'url': 'maps1.json'
    'url': 'http://web-apprentice-demo.craic.com/assets/maps/fremont.geojson'
  };
  // GeoJSON has no style information so we need to provide that
  var myStyle = {
    strokeColor: "#000000",
    strokeOpacity: 1,
    strokeWeight: 1,
    fillColor: "#AAAAAA",
    fillOpacity: 0.5
  };
  function initialize() {
    // Create the Google Map
    var myLatlng = new google.maps.LatLng( myLocation.latitude, myLocation.longitude );
    var mapOptions = {
      zoom: 13,
      center: myLatlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
    // Load the geojson from a URL - this is asynchronous, so process the data in a callback function
    var xhr = new XMLHttpRequest();
    xhr.open('GET', myLocation.url, true);
    xhr.onload = function() {
      loadGeoJSON(this.responseText);
    };
    xhr.send();
  }
  function loadGeoJSON(text) {
    // The XMLHttpRequest response is JSON text - so parse it into an Object
    var json = JSON.parse(text);
    var features = new GeoJSON(json, myStyle);
    // Loop through each feature
    for (var i = 0; i < features.length; i++){
      features[i].setMap(map);
    }
  }
  google.maps.event.addDomListener(window, 'load', initialize);