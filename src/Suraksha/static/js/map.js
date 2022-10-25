var map 
server_url = "ws://localhost:8000/ws/coordinates"
device_map = {} //maps the device 
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
	  }

	 add_device(device_element){
		 var new_device = new gps_device(device_element.id,this.map)
		 this.devices[device_element.id] = new_device
		 device_element.addEventListener('click',() => { this.set_color(device_element); this.device_clicked(device_element.id); });

	 } 
	 set_color(device_element){
		 this.reset_all_divs()
		 device_element.style.backgroundColor = 'blue'
	 }

	 reset_all_divs(){
		 //Sets color of all divs to white 
	
			for (let device_id in this.devices){
				document.getElementById(device_id).style.backgroundColor = 'white'
			}
	 }

	 device_clicked(device_id){
	   this.devices[device_id].set_focus()
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
		this.current_coords = null
	}
	 set_focus(){
		 //Called when someone clicks on the gps device div
		 this.map.setCenter(this.current_coords,16)
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
		this.current_coords = new google.maps.LatLng(coords.lat,coords["long"])
		this.ws.send(JSON.stringify({"get_coord":true}))

		}

}

