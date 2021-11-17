var map;

// Initialize Google Map function.
function initMap() {
    // Setting default values to UF coordinates.
    var options = {
        center: {lat: 29.643, lng: -82.354},
        zoom: 14
    };

    map = new google.maps.Map(document.getElementById('map'), options);

    infowindow = new google.maps.InfoWindow;
    // Ask user for geolocation (current location).
    // User has the option to allow or decline.
    // If user declines or if location is not found, default to UF coordinates.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (pos) {
            var position = {
                lat: pos.coords.latitude,
                lng: pos.coords.longitude
            }
            // Add initial marker.
            var marker = new google.maps.Marker({
                lat: pos.coords.latitude,
                lng: pos.coords.longitude,
                map: map
            });

            infowindow.setPosition(position);
            infowindow.setContent('Current location.');
            infowindow.open(map);

        }, function () {
            handleLocationError('Geolocation failure.', map.center());
            // Add initial marker.
            var marker = new google.maps.Marker({
                lat: 29.643,
                lng: -82.354,
                map: map
            });
        })
    } else {
        handleLocationError('No valid geolocation found.', map.center());
        // Add initial marker.
        var marker = new google.maps.Marker({
            lat: 29.643,
            lng: -82.354,
            map: map
        });
    }

    // Set input variable to equal the search text inputted by the user.
    var input = document.getElementById('search');
    var searchBox = new google.maps.places.SearchBox(input);

    map.addListener('bounds_changed', function () {
        searchBox.setBounds(map.getBounds());
    });

    var markers = [];
    // Create listener event function for search bar to update the map.
    searchBox.addListener('places_changed', function () {
        var places = searchBox.getPlaces();

        // If input isn't a valid place.
        if (places.length == 0) {
            return;
        }
        // Reset marker.
        markers.forEach(function (m) {
            m.setMap(null);
        });
        markers = [];

        var bounds = new google.maps.LatLngBounds();
        places.forEach(function (p) {
            if (!p.geometry) {
                return;
            }
            markers.push(new google.maps.Marker({
                map: map,
                title: p.name,
                position: p.geometry.location
            }));

            if (p.geometry.viewport) {
                bounds.union(p.geometry.viewport);
            } else {
                bounds.extend(p.geometry.location);
            }
        });
        // Update bounds to map.
        map.fitBounds(bounds);

        // For geolocation data to be outputted into body of HTML file.
        var geoplace = searchBox.getPlaces();
        console.log(input.value);
        //document.getElementById('lat_out').innerHTML = input.value.geometry.location.lat();
        //document.getElementById('lng_out').innerHTML = input.value.geometry.location.lng();

        //geolocation API, use input.value
        var geolocation = input.value;
        axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
            params: {
                address: geolocation,
                key: 'AIzaSyDx9BeRyEXjOwbaPxuqYJLdnQMF2u1x36c'
            }
        })
        //error catching.
        .then(function (response) {
            //logging full responses of locations.
            console.log(response);

            //1. PROVIDES: formatted address.
            var formatAddress = response.data.results[0].formatted_address;
            var formatAddress_out = `
            <ul class="list-group">
                <li class="list-group-item"><strong>Place</strong>: ${formatAddress}</li>
            `;

            //PROVIDES: lat/long data. geometry data.
            var lat = response.data.results[0].geometry.location.lat;
            var lng = response.data.results[0].geometry.location.lng;
            //console.log(lat);
            console.log(lng);
            var geometry_out = `
            <ul class="list-group">
                <li class="list-group-item"><strong>Latitude</strong>: ${lat}</li>
                <li class="list-group-item"><strong>Longitude</strong>: ${lng}</li>
            `;

            //output data retrieved from geocode to html body div.
            document.getElementById('format-address').innerHTML = formatAddress_out;
            document.getElementById('geometry').innerHTML = geometry_out;
            
            // Get the solar api data
            let baseUrl = '/api';
            var data = [];
            axios.get(baseUrl, {
                params: {
                    latitude: lat,
                    longitude: lng,
                }
            })
            .then(function (response) {
                let ghi = response.data.outputs.avg_ghi.monthly;
                let dni = response.data.outputs.avg_dni.monthly;
                data = [
                    ['Month', 'Average Direct Normal Irradiance', 'Average Global Horizontal Irradiance'],
                    ['Jan', dni['jan'], ghi['jan']],
                    ['Feb', dni['feb'], ghi['feb']],
                    ['Mar', dni['mar'], ghi['mar']],
                    ['Apr', dni['apr'], ghi['apr']],
                    ['May', dni['may'], ghi['may']],
                    ['Jun', dni['jun'], ghi['jun']],
                    ['Jul', dni['jul'], ghi['jul']],
                    ['Aug', dni['aug'], ghi['aug']],
                    ['Sep', dni['sep'], ghi['sep']],
                    ['Oct', dni['oct'], ghi['oct']],
                    ['Nov', dni['nov'], ghi['nov']],
                    ['Dec', dni['dec'], ghi['dec']]
                ]
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(drawChart);
    
                function drawChart() {
    
                    var chartData = google.visualization.arrayToDataTable(data  );
    
                    var options = {
                    title: 'Solar Data for ' + formatAddress,
                    curveType: 'function',
                    legend: { position: 'bottom' },
                    };
    
                    var chart = new google.visualization.LineChart(document.getElementById('chart'));
    
                    chart.draw(chartData, options);
                }
            });
        })
        .catch(function (error) {
            console.log(error);
        });
    });
};

// Asking user for geolocation fall-back function.
function handleLocationError(content, position) {
    infowindow.setPosition(position);
    infowindow.setContent(content);
    infowindow.open(map);
}