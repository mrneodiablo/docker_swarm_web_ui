$(document).ready(function(){

	function dawDashBoardCpu(datacpudashboard){
		var ctx = document.getElementById("cpu_dashboard");
		var data = {
					    labels: [
						        "used%",
						        "free%"
						    ],
						    datasets: [
						        {
						            data: datacpudashboard.data,
						            backgroundColor: [
						                "#007FFE",
						                "#2CB304"
						            ],
						        }]
					};
	
		var cpu = new Chart(ctx,{
		    type: 'pie',
		    data: data,
		    animation:{
		        animateScale:true,
		    }	    
		});
	}



	function dawDashBoardRam(dataramdashboard){
		var ctx = document.getElementById("ram_dashboard");
		var data = {
					    labels: [
						        "used%",
						        "free%"
						    ],
						    datasets: [
						        {
						            data: dataramdashboard.data,
						            backgroundColor: [
						                "#007FFE",
						                "#2CB304"
						            ],

						        }]
					};
	
		var ram = new Chart(ctx,{
		    type: 'pie',
		    data: data,
		    animation:{
		        animateScale:true,
		    }
		});
	}

	dawDashBoardCpu(datacpudashboard);
	dawDashBoardRam(dataramdashboard);
})

