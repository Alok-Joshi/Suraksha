var map 
server_url = "ws://localhost:8000/ws/coordinates"
function initMap(){

	const uluru = { lat: -25.344, lng: 131.031 };
	map = new google.maps.Map(document.getElementById("map"),{zoom :16, center: uluru})
	var device_elements = document.getElementsByClassName("device-card")
	var dm = new device_manager(map)
	for(let i =0; i<device_elements.length; ++i){
		{
		    dm.add_device(device_elements[i])	
			
		}
}
}
	
window.initMap = initMap

class device_manager{
	  constructor(map){
		  this.devices = {}
		  this.map = map
		  this.clicked_device = null
		  this.clicked_div = null
	  }

	 add_device(device_element){
		 var new_device = new gps_device(device_element.id,this.map)
		 this.devices[device_element.id] = new_device
		 device_element.addEventListener('click',() => { this.set_color(device_element); this.device_clicked(device_element.id); });

	 } 
	 set_color(device_element){
		 if(this.clicked_div){
			 this.clicked_div.style.backgroundColor = 'white'
		 }

		 device_element.style.backgroundColor = 'blue'
		 this.clicked_div = device_element
	 }
	 

	 device_clicked(device_id){
	   if(this.clicked_device){
		   this.clicked_device.is_focused  = false
	   }

	   this.devices[device_id].is_focused = true
	   this.clicked_device = this.devices[device_id]
	 }
}

class gps_device {
	constructor(device_id,map){
		this.device_id = device_id
		this.ws = new WebSocket(server_url+'/'+device_id+'/')
		this.ws.onmessage = this.onmessage.bind(this)
		this.ws.onopen = this.onopen.bind(this)
		this.map = map
		this.marker = new google.maps.Marker({ map: this.map,})
		this.is_focused = false
	}

	 onopen(e){

		let message = { "get_coord":true,}
		this.ws.send(JSON.stringify(message))
	 }

	onmessage(message){

		if (message.data === "null"){
			console.log(message.data)
			this.ws.send(JSON.stringify({"get_coord":true}))
			return
		}

		var coords = JSON.parse(message.data)
		if(typeof(coords) == "string"){
			coords = JSON.parse(coords)
		}

		let coord_obj = new google.maps.LatLng(coords.lat,coords["long"])
		this.marker.setPosition(coord_obj)
		if(this.is_focused){
			this.map.setCenter(coord_obj)
		}
		this.ws.send(JSON.stringify({"get_coord":true}))

		}

}

