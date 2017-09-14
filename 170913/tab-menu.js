$(document).ready(function() {
  var menu = $('.main-menu>li');
  var span = $('.main-menu span');
  var last_item = $('.sub-menu li:last-child');
  var first_item = $('.sub-menu li:first-child');

  menu.hover(function() {
    $(this).find('.sub-menu>li').toggleClass('sub-menu-active');
  });

  span.focusin(function() {
    $(this).siblings().children().addClass('sub-menu-active');
  });

  last_item.focusout(function() {
    $(this).removeClass('sub-menu-active');
    $(this).siblings().removeClass('sub-menu-active');
  });

  //   first_item.focusout(function() {
  //     $(this).removeClass('sub-menu-active');
  //     $(this).siblings().removeClass('sub-menu-active');
  //   });
});