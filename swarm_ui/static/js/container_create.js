$(document).ready(function() {
	$("#registry").change(
		function load_ajax(){

			var url = window.location.href
			var arr = url.split("/");
			var api = arr[0]  + arr[1] + "//" + arr[2]
		    $.ajax({
		        url : api + "/swarm/registry/api/listrepo", 
		        type : "post", 
		        dateType:"json", 
		        
		        data : { 
		             registry : $('#registry').val()
		        },
		        success : function (result){
		        	var images = JSON.parse(result)
					var ln_html = '';
					if (images.status) {
						
		        		for (var key in images.data.repo_data) {
		        			for (var i = 0; i < images.data.repo_data[key].data.tags.length; i++) {
		        				ln_html += '<option value="' +  images.data.repo_ip + ":" + images.data.repo_port + "/" + key + ":" + images.data.repo_data[key].data.tags[i] + '">' +  key + ":" + images.data.repo_data[key].data.tags[i] + '</option>';
		        			};

	                    }

			        	$('#list_images').html(
	                        '<select class="form-control"  name="list_images" id="list_images">' + ln_html +'</select>'  
			            );

					} else{
			        	$('#list_images').html(
	                        '<select default="0" name="list_images" id="list_images"></select>'  
			            );		
					};

		        }
		    });
		}
	);



	$("#list_product").change(
		function load_ajax(){

			var url = window.location.href
			var arr = url.split("/");
			var api = arr[0]  + arr[1] + "//" + arr[2]
		    $.ajax({
		        url : api + "/swarm/product/api/inpsect", 
		        type : "post", 
		        dateType:"json", 
		        
		        data : { 
		             product : $('#list_product').val()
		        },
		        success : function (result){

		        	var network = JSON.parse(result)
					var ln_html = '';
					if (network.status) {
						
						for (var i = 0; i < network.data.length ; i++) {
							ln_html += '<option value="' +  network.data[i].vlan + '">' +  network.data[i].vlan + " - " + network.data[i].subnet + '</option>';
						};


			        	$('#list_network').html(
	                        '<select name="list_network" id="list_network" required>' + ln_html +'</select>'  
			            );

					} else{
			        	$('#list_network').html(
	                        '<select name="list_network" id="list_network" required></select>'  
			            );		
					};

		        }
		    });
		}
	);

	$("#container_name").change(function(){
		var container_name = $('#container_name').val()
		$('#hostname').html('<input name="hostname"  id="hostname" class="input ng-pristine ng-valid ng-touched" type="text" placeholder="Hostname" value="' + container_name + '" >')
		$('#hostpath').html('<input name="hostpath"   class="input ng-pristine ng-untouched ng-valid" type="text" placeholder="Host Path" value="'+ "/data/container/" + container_name +'">')			

	});


	$("#cpus").change(
		function load_ajax(){
			var url = window.location.href
			var arr = url.split("/");
			var api = arr[0]  + arr[1] + "//" + arr[2]
		    $.ajax({
		        url : api + "/swarm/node/api/getcpunode", 
		        type : "post", 
		        dateType:"json", 
		        
		        data : { 
		             name : $('#node').val()
		        },
		        success : function (result){
		        	var node = JSON.parse(result)
		        	var cpu_node = node.data
		        	var cpu_set = $('#cpus').val()
		        	if ( Number(cpu_set) > Number(cpu_node) ) {
		        		alert("Chọn số lượng CPU <= số lượng CPU của node")
		        	} 
		        }
		    });
	});
})

