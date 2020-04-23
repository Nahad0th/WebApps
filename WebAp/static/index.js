$(document).ready(function(){
	$('#task_button').click(function(){
		$.get( "/api/get_productive", function( data ) {
		  // clean display paragraph
		  $('#activity_space').text('');
		  var js_obj = JSON.parse(data);
                  $('#activity_space').append($("<p></p>").text(js_obj.activity_name));
                  $('#activity_space').append($("<p></p>").text(js_obj.description));
                  $('#activity_space').append($("<p><img src='" + js_obj.image + "'></p>"));
		 
		});
	});

	$('#random_button').click(function(){
		$.get( "/api/get_rand", function( data ) {
		  // clean display paragraph
		  $('#activity_space').text('');
		  var js_obj = JSON.parse(data);
                  $('#activity_space').append($("<p></p>").text(js_obj.activity_name));
                  $('#activity_space').append($("<p></p>").text(js_obj.description));
                  $('#activity_space').append($("<p><img src='" + js_obj.image + "'></p>"));
		 
		});
	});

        $('#fun_button').click(function(){
		$.get( "/api/get_fun", function( data ) {
		  // clean display paragraph
		  $('#activity_space').text('');
		  var js_obj = JSON.parse(data);
                  $('#activity_space').append($("<p></p>").text(js_obj.activity_name));
                  $('#activity_space').append($("<p></p>").text(js_obj.description));
                  $('#activity_space').append($("<p><img src='" + js_obj.image + "'></p>"));		 
		});
	});
});