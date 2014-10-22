function respond_click() {
	var json = {
        row: $(this).attr("data-row"),
        col: $(this).attr("data-col")
	};
	
    $.ajax({
        url: '/api/push/move',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(json)
    }).done(function (data) {
		var msg = $("#messagebox");
		msg.html(data['msg']);

		if (data['error']) {
			msg.removeClass("info");
			msg.addClass("danger");
		}
		else {
			msg.removeClass("danger");
			msg.addClass("info");	
		}
	});
}



$(document).ready(function () {
	//alert("Getting it done");
	$(".tictacgrid").each(function() {
		$(this).html("a");
		$(this).css("background", "#ff0000");
		$(this).click(respond_click);
	});
});

