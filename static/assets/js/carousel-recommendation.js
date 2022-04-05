$(document).ready(function(){
	//Carousel init
		if( $(window).width()>=100 ){
			$( ".carousel-recommendation .row .col-md-2" ).each(function() {
				var offset = parseInt($( this ).attr("data-offset"));
				$(this).css({'transform':'translateX('+offset+'%)', '-webkit-transform':'translateX('+offset+'%)'});
			});
		}
	// ----------------------------------------------------------------------

	$('.carousel-recommendation').on('click', '.btn-right', function(){
		var count = parseInt($('.carousel-recommendation').attr('data-count'));
		var first = parseInt($('.carousel-recommendation').attr('data-first'));
		var last = parseInt($('.carousel-recommendation').attr('data-last'));
		var offset = parseInt($('.carousel-recommendation').attr('data-offset'));
		var coeff = 100;

		//Set marker--------------------------------------
			if( last+1>count ){ var next = 1; }
			else{ var next = last+1; }

			if( first+1>count ){ var prev = 1; }
			else{ var prev = first+1; }
		//Set marker--------------------------------------

		//Move all left-----------------------------------
			$( ".carousel-recommendation .row .col-md-2" ).each(function() {
				var position = parseInt($( this ).attr("data-position"));
				var offset = parseInt($( this ).attr("data-offset"));

				if( position!=count ){
					if( position != 0){
						$(this).css({'transform':'translateX('+(offset-100)+'%)', '-webkit-transform':'translateX('+(offset-100)+'%)'});
						$( this ).attr( "data-offset", (offset-100) );
					}

					//Set new position--------------------
						if( position-1 < 0){ var newposition = 0; }
						else{ var newposition = position-1; }

						$( this ).attr( "data-position", newposition );
					//Set new position--------------------
				}
			});
		//Move all left-----------------------------------

		//Move next---------------------------------------
			//Transition OFF
				$( ".carousel-recommendation .row" ).find('.marker-'+next+'').css({
					'transition': 'none',
					'-webkit-transition': 'none',
					'transform': 'translateX(600%)',
					'-webkit-transform': 'translateX(600%)'
				});

			setTimeout(function(){
				$( ".carousel-recommendation .row" ).find('.marker-'+next+'').css({
					'transition': 'all 0.5s',
					'-webkit-transition': 'all 0.5s',
					'transform': 'translateX(500%)',
					'-webkit-transform': 'translateX(500%)'
				});

				$( ".carousel-recommendation .row" ).find('.marker-'+next+'').attr('data-position',6 );
				$( ".carousel-recommendation .row" ).find('.marker-'+next+'').attr('data-offset',500);
			},10);
		//Move next---------------------------------------


		$('.carousel-recommendation').attr('data-first',prev);
		$('.carousel-recommendation').attr('data-last',next);
	});

	$('.carousel-recommendation').on('click', '.btn-left', function(){
		var count = parseInt($('.carousel-recommendation').attr('data-count'));
		var first = parseInt($('.carousel-recommendation').attr('data-first'));
		var last = parseInt($('.carousel-recommendation').attr('data-last'));
		var offset = parseInt($('.carousel-recommendation').attr('data-offset'));
		var coeff = 100;

		//Set marker--------------------------------------
			if( last-1==0 ){ var next = count; }
			else{ var next = last-1; }

			if( first-1==0 ){ var prev = count; }
			else{ var prev = first-1; }
		//Set marker--------------------------------------

		//Move all right-----------------------------------
			$( ".carousel-recommendation .row .col-md-2" ).each(function() {
				var position = parseInt($( this ).attr("data-position"));
				var offset = parseInt($( this ).attr("data-offset"));

				if( position!=count ){
					if( position != 0){
						$(this).css({'transform':'translateX('+(offset+100)+'%)', '-webkit-transform':'translateX('+(offset+100)+'%)'});
						$( this ).attr( "data-offset", (offset+100) );
					}

					//Set new position--------------------
						var newposition = position+1;

						$( this ).attr( "data-position", newposition );
					//Set new position--------------------
				}
			});
		//Move all right-----------------------------------

		//Move prev---------------------------------------
			//Transition OFF
			$( ".carousel-recommendation .row" ).find('.marker-'+prev+'').css({
				'transition': 'none',
				'-webkit-transition': 'none',
				'transform': 'translateX(-100%)',
				'-webkit-transform': 'translateX(-100%)'
			});

			setTimeout(function(){
				$( ".carousel-recommendation .row" ).find('.marker-'+prev+'').css({
					'transition': 'all 0.5s',
					'-webkit-transition': 'all 0.5s',
					'transform': 'translateX(0%)',
					'-webkit-transform': 'translateX(0%)'
				});

				$( ".carousel-recommendation .row" ).find('.marker-'+prev+'').attr('data-position',1 );
				$( ".carousel-recommendation .row" ).find('.marker-'+prev+'').attr('data-offset',0);
			},10);
		//Move prev---------------------------------------


		$('.carousel-recommendation').attr('data-first',prev);
		$('.carousel-recommendation').attr('data-last',next);
	});
//Reccomendation Carousel
});