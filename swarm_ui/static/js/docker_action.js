$(document).ready(function() {
	$("#submit_pull").click(function(event) {
		var registry = $('#registry').val();
		var image = $('#image').val();
		var tag = $('#tag').val();
		var contents = '<div class="six wide column"><div class="ui icon message"><i class="notched circle loading icon"></i><div class="content"><div class="header ng-binding">Pulling=' + image + ':' + tag + '</div><p>Chờ trong vào phút</p></div></div></div>'
		if (image != "") {
			$('#process_pull').html(contents);
		};
		
		
		
	});


})