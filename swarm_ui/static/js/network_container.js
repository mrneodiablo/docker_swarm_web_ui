$(document).ready(function() {
	$("#container_name").change(
		function load_ajax(){
		    $.ajax({
		        url : "apigetnetwork", 
		        type : "post", 
		        dateType:"json", 
		        
		        data : { 
		             containerid : $('#container_name').val()
		        },
		        success : function (result){
		        	var product = JSON.parse(result)
					var ln_html = '';
					if (product.status) {
						$('#result').html(result)
		        		for (var i = 0; i < product.list_network.length ;i++) {
	                    	ln_html += '<option value="' +  product.list_network[i].id + '">' +  product.list_network[i].name + " - "+ product.list_network[i].ipam.Config[0].Subnet + '</option>';
	                    }

			        	$('#list_network').html(
	                        '<select class="form-control"  name="list_network">' + ln_html +'</select>'  
			            );
			            $('#product_name').html(

			            	"<strong>"+product.list_network[0].Labels.product+"</strong>"
			            );						
					} else{
			        	$('#list_network').html(
	                        '<select class="form-control"  name="list_network"></select>'  
			            );
			            $('#product_name').html(

			            	"<strong> </strong>"
			            );				
					};

		        }
		    });
		}
	);


})

