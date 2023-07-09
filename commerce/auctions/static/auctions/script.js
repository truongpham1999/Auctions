$(document).ready(function(){
    $("#listingForm").submit(function(e){
        var title = $("#titleInput").val();
        var description = $("#descriptionInput").val();
        var startBid = $("#startBidInput").val();
        var category = $("#categoryInput").val();
        
        if (title == "" || description == "" || startBid == "" || category == "ALL") {
            e.preventDefault();
            
            // Create an alert message
            var alertDiv = $('<div class="alert alert-danger" role="alert">All fields are required!</div>');
            
            // Append alert to the form
            $("#listingForm").prepend(alertDiv);

            // Automatically remove the alert after 5 seconds
            setTimeout(function() {
                $(alertDiv).remove();
            }, 5000);
        }
    });

    // Validation for categoryForm
    $("#categoryForm").submit(function(e){
        var category = $("#category").val();
        
        if (category == "") {
            e.preventDefault();
            
            // Create an alert message
            var alertDiv = $('<div class="alert alert-danger" role="alert">Category is required!</div>');
            
            // Append alert to the form
            $("#categoryForm").prepend(alertDiv);

            // Automatically remove the alert after 5 seconds
            setTimeout(function() {
                $(alertDiv).remove();
            }, 5000);
        }
    });

    $("#bidForm").submit(function(e){
        var addedBid = parseFloat($("#addedBidInput").val());
        var startBid = parseFloat($("#startBidInput").val());
        var currentBid = parseFloat($("#currentBidInput").val());
        
        if (addedBid <= startBid || addedBid <= currentBid) {
            e.preventDefault();
            
            // Create an alert message
            var alertDiv = $('<div class="alert alert-danger" role="alert">Your bid must be higher than the starting bid and the current bid!</div>');
            
            // Append alert to the form
            $(this).prepend(alertDiv);

            // Automatically remove the alert after 5 seconds
            setTimeout(function() {
                alertDiv.remove();
            }, 5000);
        }
    });

    $("#commentForm").submit(function(e){
        var comment = $("#commentInput").val();
        
        if (comment.trim() === "") {
            e.preventDefault();
            
            // Create an alert message
            var alertDiv = $('<div class="alert alert-danger" role="alert">Comment cannot be empty!</div>');
            
            // Append alert to the form
            $(this).prepend(alertDiv);

            // Automatically remove the alert after 5 seconds
            setTimeout(function() {
                alertDiv.remove();
            }, 5000);
        }
    });
});
