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

						for (var z = 0; z < product.list_vlan.length ;z++) {
							ln_html += '<option value="' +  product.list_vlan[z].id + '">' +   product.list_vlan[z].name + ' - ' +  product.list_vlan[z].ipam.Config[0].Subnet + '</option>';
	    				};

		        		for (var i = 0; i < product.list_network.length ;i++) {
		        			for (var key in product.list_network[i].network_settings) {				
		        				vlan_conn += '<p><span class="label label-primary">' + key  + '</span> --><strong>' + product.list_network[i].network_settings[key].IPAddress + '</strong><p>'
		        			};
	                    	
	                    }

			        	$('#list_network').html(
	                        '<select class="form-control"  name="list_network_connect">' + ln_html +'</select>'  
			            );

			            $('#product_name_info').html(

			            	'<p style="margin-top: 10px;"><strong>'+product.list_network[0].labels["mto.product.name"]+'</strong></p>'
			            );

			            $('#container_connect_info').html(
			            	vlan_conn
			            );

			            $('#container_name_info').html(
			            	'<p style="margin-top: 10px;"><strong>'+product.list_network[0].name+'</strong></p>'
			            );
			            $('#node_name_info').html(
			            	'<p style="margin-top: 10px;"><strong>'+product.list_network[0].host+'</strong></p>'
			            );		            					            					
					} else{

			        	$('#list_network').html(
	                        '<select class="form-control"  name="list_network_disconnect"></select>'  
			            );
			            $('#product_name_info').html(

			            	"<strong> </strong>"
			            );
			            $('#container_connect_info').html(
			            	'<p></p>'
			            );
			            $('#container_name_info').html(
			            	'<p style="margin-top: 10px;"></p>'
			            );
			            $('#node_name_info').html(
			            	'<p style="margin-top: 10px;"></p>'
			            );			            					
					};

		        }
		    });
		}
	);


})

