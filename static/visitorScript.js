        $(document).ready(function () {
            visitorShow();
        });

        function visitorMake() {
            $.ajax({
                type: "POST",
                url: "/visitor_post",
                data: {visitor_give: '샘플데이터'},
                success: function (response) {
                    alert(response["msg"]);
                    window.location.reload();
                }
            })
        }

        function visitorShow() {
            $.ajax({
                type: "GET",
                url: "/visitor_post?visitor_give=샘플데이터",
                data: {},
                success: function (response) {
                    alert(response["msg"]);
                }
            })
        }