console.log(geometry);

function addBookmark() {
    var b_lat = document.getElementById('lat').innerHTML;
    var b_lng = document.getElementById('lng').innerHTML;
    
    console.log(b_lat.toString(), b_lng.toString());

    baseUrl = '/addbookmark'
    axios.get(baseUrl, {
        params: {
            latitude: b_lat.toString(),
            longitude: b_lng.toString()
        }
    })
    .catch(function (error) {
        console.log(error);
    });
}