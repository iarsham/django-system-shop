$(document).ready(function(){
	$('.carousel').on('click', '.btn-control', function(){
		//Set variables
		var count = parseInt($(this).parents('.carousel').attr('data-count'));
		var current = parseInt($(this).parents('.carousel').attr('data-current'));

		if( current + 1 > count ) { var next = 1; }
		else{ var next = current + 1; }


		//Move
		$(this).parents('.carousel').find('.items .item[data-marker="'+current+'"]').removeClass('active');
		$(this).parents('.carousel').find('.items .item[data-marker="'+next+'"]').addClass('active');


		//Set data
		$(this).parents('.carousel').attr('data-current', next);


		//Set markers
		$(this).parents('.carousel').find('.markers > li').removeClass('active');
		$(this).parents('.carousel').find('.markers > li[data-marker="'+next+'"]').addClass('active');
	});


	// Marker Click
	$('.carousel').on('click', '.markers li', function(){
		//Set variables
		var current = parseInt($(this).parents('.carousel').attr('data-current'));
		var marker = parseInt($(this).attr('data-marker'));

		//Move
		$(this).parents('.carousel').find('.items .item[data-marker="'+current+'"]').removeClass('active');
		$(this).parents('.carousel').find('.items .item[data-marker="'+marker+'"]').addClass('active');


		//Set data
		$(this).parents('.carousel').attr('data-current', marker);


		//Set markers
		$(this).parents('.carousel').find('.markers > li').removeClass('active');
		$(this).parents('.carousel').find('.markers > li[data-marker="'+marker+'"]').addClass('active');
	});
});