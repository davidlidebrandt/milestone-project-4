$(document).ready(function () {

  $("#update-review-form").submit(function(event) {
    event.preventDefault();
  });


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
    $("#quantity-input").trigger("change");
  });

  $("#decrease-quantity").click(function () {
    currentValue = parseInt($("#quantity-input").val());
    if (currentValue > 1) {
      $("#quantity-input").val(currentValue - 1);
    }
    $("#quantity-input").trigger("change");
  });

  $("#quantity-input").change(function() {
    let val =  parseInt($("#quantity-input").val());
    
    if(val === 1) {
      $("#decrease-quantity").addClass("d-none");
      $("#disabled-minus-button").removeClass("d-none");
    }

    else if(val === 10) {
      $("#disabled-plus-button").removeClass("d-none");
      $("#increase-quantity").addClass("d-none");
    }

    if(val > 1 && val < 10) {
      $("#disabled-minus-button").addClass("d-none");
      $("#decrease-quantity").removeClass("d-none");
      $("#disabled-plus-button").addClass("d-none");
      $("#increase-quantity").removeClass("d-none");
    }
  });

  $("#show-write-review").click(ShowAddReviewModal);

  $("#sort-prize").click(sortByPrize);

  $("#sort-popular").click(sortByPopularity);
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
  get_base_url = window.location.protocol + "//" + window.location.hostname
  if (get_current_url.includes("category")) {
    category = get_current_url.split("=")[1]
    window.location.href = get_base_url + "/products/?category=" + category + "&sort=prize";
  } 
  else if (get_current_url.includes("manufacturer")) {
    manufacturer = get_current_url.split("=")[1]
    window.location.href = get_base_url + "/products/?manufacturer=" + manufacturer + "&sort=prize";
  }
  else {
    window.location.href = get_base_url + "/products/" + "?sort=prize";
  }

}

function sortByPopularity() {
  get_current_url = window.location.href;
  get_base_url = window.location.protocol + "//" + window.location.hostname
  if (get_current_url.includes("category")) {
    category = get_current_url.split("=")[1]
    window.location.href = get_base_url + "/products/?category=" + category + "&sort=units_sold";
  } 
  else if (get_current_url.includes("manufacturer")) {
    manufacturer = get_current_url.split("=")[1]
    window.location.href = get_base_url + "/products/?manufacturer=" + manufacturer + "&sort=units_sold";
  }
  else {
    window.location.href = get_base_url + "/products/" + "?sort=units_sold";
  }
}
