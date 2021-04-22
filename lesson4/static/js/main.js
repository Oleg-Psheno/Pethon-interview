$.get( "/ajax_handler", function( data ) {
  let out = ``
  let dat = JSON.parse(data);
  dat.forEach(function (item){
    out += `<div class="item col-4">
            <p>Наименование товара - ${item.fields.name}</p>
            <p>Остаток на складе  - ${item.fields.quantity}</p>
            <p>${item.fields.description}</p>
               <br>
           </div>`
  });
  $( "#test" ).html( out );
});


$(document).ready(function($) {
	$('.popup-open').click(function() {
		$('.popup-fade').fadeIn();
		return false;
	});

	$('.popup-close').click(function() {
		$(this).parents('.popup-fade').fadeOut();
		return false;
	});

	$(document).keydown(function(e) {
		if (e.keyCode === 27) {
			e.stopPropagation();
			$('.popup-fade').fadeOut();
		}
	});

	$('.popup-fade').click(function(e) {
		if ($(e.target).closest('.popup').length == 0) {
			$(this).fadeOut();
		}
	});
});
// $( function() {
//     $( "#dial-form" ).dialog({
//       autoOpen: false,
//       show: {
//         effect: "blind",
//         duration: 1000
//       },
//       hide: {
//         effect: "explode",
//         duration: 1000
//       }
//     });
//
//     $( "#opener" ).on( "click", function() {
//       $( "#dial-form" ).dialog( "open" );
//     });
//   } );
