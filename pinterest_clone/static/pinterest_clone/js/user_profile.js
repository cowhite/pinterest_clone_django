var follow_callback;

$(document).ready(function() {
  return console.log(555);
});

follow_callback = function(res) {
  var $btn, new_follow_dajax, new_unfollow_dajax;
  console.log(res);
  $btn = $("#follow-board-" + res.object_id);
  if (res.increment === 1) {
    $btn.removeClass("btn-primary").addClass("btn-danger");
    new_unfollow_dajax = $btn.attr("onclick");
    $btn.attr("onclick", $btn.attr("follow_dajax"));
    return $btn.attr("follow_dajax", new_unfollow_dajax);
  } else if (res.increment === -1) {
    $btn.removeClass("btn-danger").addClass("btn-primary");
    new_follow_dajax = $btn.attr("onclick");
    $btn.attr("onclick", $btn.attr("follow_dajax"));
    return $btn.attr("follow_dajax", new_follow_dajax);
  } else {
    return window.location.reload();
  }
};
