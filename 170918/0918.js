$(document).ready(function() {
  var tab = $('.tab')

  //   tab.click(function() {
  //     $(this).parent().addClass('active').siblings().removeClass('active');
  //   });
  //   tab.focusin(function() {
  //     $(this).parent().addClass('active').siblings().removeClass('active');
  //   })

  tab.on('click focusin', function() {
    $(this).parent().addClass('active').siblings().removeClass('active');
  })
});