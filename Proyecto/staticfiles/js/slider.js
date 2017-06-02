/**
 * directorySlider v0.9 - Loads all images in a specified directory and creates a slide show
 * Author: Justin W. Hall
 * http://www.justinwhall.com/directory-jquery-slider/
 *
 * License: GPL v3
 */
$(function(){
$('.dropdown').on('show.bs.dropdown', function(e){
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  $('.dropdown').on('hide.bs.dropdown', function(e){
    e.preventDefault();
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp(400, function(){
    	$('.dropdown').removeClass('open');
      	$('.dropdown').find('.dropdown-toggle').attr('aria-expanded','false');
    });
    
  });
});
