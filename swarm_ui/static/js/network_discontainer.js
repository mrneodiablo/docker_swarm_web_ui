$(document).ready(function() {
	$("#container_name").change(
		function load_ajax(){
			var url = window.location.href
			var arr = url.split("/");
			var api = arr[0]  + arr[1] + "//" + arr[2]			
		    $.ajax({
		        url : api +  "/swarm/networks/api/getnetwork",
		        type : "post", 
		        dateType:"json", 
		        
		        data : { 
		             containerid : $('#container_name').val()
		        },
		        success : function (result){
		        	var product = JSON.parse(result)
					var ln_html = '';
					var vlan_conn = '';
					if (product.status) {

		        		for (var i = 0; i < product.list_network.length ;i++) {
		        			for (var key in product.list_network[i].network_settings) {

		        				ln_html += '<option value="' +  product.list_network[i].network_settings[key].NetworkID + '">' +  key + '</option>';

		        				vlan_conn += '<p><span class="label label-primary">' + key  + '</span> --><strong>' + product.list_network[i].network_settings[key].IPAddress + '</strong><p>'
		        			};
	                    	
	                    }

			        	$('#list_network').html(
	                        '<select class="form-control"  name="list_network_disconnect">' + ln_html +'</select>'  
			            );
			            $('#product_name').html(

			            	"<h3>"+product.list_network[0].labels["mto.product.name"]+"</h3>"
			            );

			            $('#container_connect').html(
			            	vlan_conn
			            );			            					
					} else{

			        	$('#list_network').html(
	                        '<select class="form-control"  name="list_network_disconnect"></select>'  
			            );
			            $('#product_name').html(

			            	"<strong> </strong>"
			            );
			            $('#container_connect').html(
			            	'<p></p>'
			            );				
					};

		        }
		    });
		}
	);


})

