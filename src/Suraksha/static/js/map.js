var map 

server_url = "ws://localhost:8000/ws/coordinates"
function initMap(){}
function change_coordinate(){

  lat = document.getElementById("lat").value; 
  lon = document.getElementById("long").value; 
  var c1 = new google.maps.LatLng(lat,lon)
  marker.setPosition(c1)
}

//TODO: Differentiate different markers using different colors, will need to read google documentation

class gps_device {
	constructor(device_name){
		this.device_name = device_name
		this.ws = new WebSocket(server_url+'/'+device_name+'/')
		this.ws.onmessage = this.onmessage.bind(this)
		this.ws.onopen = this.onopen.bind(this)

		//this.marker = new google.maps.Marker({ map: map,})
	}
	 onopen(e){

		let message = { "get_coord":true,}
		this.ws.send(JSON.stringify(message))
	 }

	onmessage(message){
		
		let coords = JSON.stringify(message.data)
		console.log(coords)
		this.ws.send(JSON.stringify({"get_coord":true}))
		//let coord_obj = new google.maps.LatLng(coords["lat"],coords["long"])
		//this.marker.setPosition(coord_obj)
		}

}

window.onload = function(){

	//map = new google.maps.Map(document.getElementById("map"), {  zoom: 1,  center: uluru,});
	//Algorithm flow:
	//1 Map loads
	//2 once the map loads properly, we create the gps device objects for every device_name we fetch from the dom (give same class name)
	
	//TODO: need to revisit map documentation once again 
	new gps_device("device_one")
}


