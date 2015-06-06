var $border_color = "#efefef";
var $grid_color = "#ddd";
var $default_black = "#666";
var $primary = "#575348";
var $secondary = "#A4DB79";
var $orange = "#F38733";

// Mobile Nav
$('#mob-nav').click(function(){
	if($('aside.open').length > 0){
		$( "aside" ).animate({left: "-320px" }, 500 ).removeClass('open');
	} else {
		$( "aside" ).animate({left: "0px" }, 500 ).addClass('open');
	}
});

// Tooltips
$('a').tooltip('hide');

// Slide Bars
$(function() {
  $(document).ready(function() {
    $.slidebars();
  });
});

$(document).ready(function() {
  $('#btnJoinCampaignModal').on('click', function(){
    console.log('reached here');
    console.log($(this).data('id'));
    $.get('/campaign/1/join',function(resp){
        $('#joincampaignmodal .modal-body').html(resp);
        $('#joincampaignmodal').modal('show');
    })
  })

});
