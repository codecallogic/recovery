$('.carousel').carousel({
interval: 3000,
keyboard: true,
pause: 'hover',
wrap: true
});

$('#slider4').on('slide.bs.carousel', function () {
console.log('SLIDE!');
});

$('#slider4').on('slid.bs.carousel', function () {
console.log('SLID!');
});

let add = document.querySelector('.add')

add.addEventListener('keyup'), function(e){
    if(e.keyCode === 13){
        event.preventDefault();
        add.click();
    }
}
  
$(document).ready(function(){

$(".symptomsLabel").on("click", "li", function(){
$(this).toggleClass("completed");
});


$(".symptomsLabel").on("click", "span", function(event){
$(this).parent().fadeOut(500,function(){
$(this).remove();
});
event.stopPropagation();
});

$("input[type='text']").keypress(function(event){
if(event.which === 13){

var todoText = $(this).val();
$(this).val("");

$(".symptomsLabel").append("<li><span><i class='fa fa-trash'></i></span> " + todoText + "</li>")
}
});

$(".fa-plus").click(function(){
$("input[type='text']").fadeToggle();
});


});