$(document).ready(function () {
  $("#delete-review-warn").click(function() {
    $("#delete-review-modal").show();
  });


  $("#cancel-delete-review").click(function() {
    $("#delete-review-modal").hide();
  });


  $("#quantity-input").val("1");
  $("#increase-quantity").click(function () {
    currentValue = parseInt($("#quantity-input").val());
    if (currentValue > 0 && currentValue < 10) {
      $("#quantity-input").val(currentValue + 1);
    }
  });

  $("#decrease-quantity").click(function () {
    currentValue = parseInt($("#quantity-input").val());
    if (currentValue > 1) {
      $("#quantity-input").val(currentValue - 1);
    }
  });

  $("#show-write-review").click(ShowAddReviewModal);

  $("#sort-prize").click(sortByPrize);
});

function ShowAddReviewModal() {
  $(".reviews-div").hide();
  $(".write-reviews-div").show();
  $("#show-reviews").toggleClass("text-decoration-underline");
  $(this).toggleClass("text-decoration-underline");
  $("#show-reviews").click(showReviewModal);
  $(this).off();
}

function showReviewModal() {
  $(".write-reviews-div").hide();
  $(".reviews-div").show();
  $("#show-write-review").toggleClass("text-decoration-underline");
  $(this).toggleClass("text-decoration-underline");
  $("#show-write-review").click(ShowAddReviewModal);
  $(this).off();
}

function sortByPrize() {
  get_current_url = window.location.href;
  if (get_current_url.includes("category")) {
    window.location.href = get_current_url + "&sort=prize";
  } else {
    window.location.href = get_current_url + "?sort=prize";
  }
}
