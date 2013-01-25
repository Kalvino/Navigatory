$(document).ready(function () {
    $("#itemcarousel").jcarousel({
        visible: 3
    });
    $("#homeCarousel").carousel('cycle', {
        interval: 6000    
    });
    
    $("#detailCarousel").carousel('cycle', {
        interval: 6000    
    });
    $('.activityCarousel').carousel('pause');
    $('.hotelCarousel').carousel('pause');
    
    $(".lightbox").lightBox();
    $("a[rel^=name1]").lightBox();
    $("a[rel^=name2]").lightBox();
    $("a[rel^=name3]").lightBox();
    $("a[rel^=name1-hotel]").lightBox();
    $("a[rel^=name2-hotel]").lightBox();
    $("a[rel^=name3-hotel]").lightBox();
    $("#detailCarousel .carousel-inner a").lightBox();
    $("#homeCarousel .carousel-inner a").lightBox();
    //Date Picker Date Format
    
    function getDateFormat () {
        var $this = $('#selectlang');
        var selectedLang = $('#selectlang').val();
        var defaultFormat = "mm-dd-yy",
            enFormat = "mm-dd-yy",
            frFormat = "dd-mm-yy",
            phFormat = "'Ika' d 'ng' MM', taong' yy",
            otaFormat = "DD, d MM, yy",
            otbFormat = "d MM, yy",
            format;

        if(selectedLang == "enUS" ){
            format = enFormat;
        } else if (selectedLang == "fr"){
            format = frFormat;
        } else if (selectedLang == "ph"){
            format = phFormat;
        } else if (selectedLang == "ota"){
            format = otaFormat;
        } else if (selectedLang == "otb"){
            format = otbFormat;
        } else {
            format = defaultFormat;
        }
        
        $( "#datepicker" ).datepicker('option', 'dateFormat', format );
    }
    
    
    $( "#datepicker" ).datepicker({ firstDay: 1});
    $( "#modalfromdatepicker" ).datepicker({ firstDay: 1});
    $( "#modaltodatepicker" ).datepicker({ firstDay: 1});
    getDateFormat();
    
    $("#selectlang").on('change',function(){
        getDateFormat();
    });
    
    //Add more button for itenararies
    $('#addmore-itineraries').click(function() {
        console.log("Clicked");
        var num     = $('.itinerary-list a').length;
        var newNum  = new Number(num + 1);
 
        var newElem = $('#itinerary' + num).clone().attr('id', '#itinerary' + newNum);
        var newItinerary =  '<a href="#" id="itinerary' + newNum +'" class="add-item-link" data-toggle="modal" data-target="#chooseItineraryPrefrences" > ';
            newItinerary += '<div class="add-item">';
            newItinerary += '<h1>+</h1>';
            newItinerary += '<h3>Add Another itinerary</h3>';
            newItinerary += '</div>';
            newItinerary += '</a>';
       
        $('.itinerary-list').append(newItinerary);
    });
    
    $( "#sortable-itenerary-details" ).sortable({
        update: function(event, ui) {
                    getListNumber();
                },
        placeholder: "tr-ui-state-highlight"
        
    });
    
    $(".upward, .downward, .deleteItem, .plusOne, .minusOne").on('mouseenter', function () {
            $( "#sortable-itenerary-details" ).sortable('disable');
    });
    $(".upward, .downward, .deleteItem, .plusOne, .minusOne").on('mouseleave', function () {
            $( "#sortable-itenerary-details" ).sortable('enable');
    });
    
    //$(".item-place-details").hide();
    
    getListNumber();
    getAverageDrivingHour();
    getAverageDistancePerDay();
    
    hideDetails();
    function showDetails () {  
        $(".showD").on("click", function(){
            var $this = $(this);
            $this.unbind("click");
            $this.addClass("hideD");
            $this.removeClass("showD");
            $this.closest(".item-place-header").siblings(".item-place-details").slideDown("100", function(){
                    $this.val("Hide Details");
                    $this.on("click", hideDetails());
            });
            
         });
    }
    
    function hideDetails() {
        $(".hideD").on("click", function(){
            var $this = $(this);
            $this.unbind("click");
            $this.addClass("showD");
            $this.removeClass("hideD");
            console.log("It works!");
            $this.closest(".item-place-header").siblings(".item-place-details").slideUp("100", function(){
                $this.val("Show Details");
                $this.on("click", showDetails());
            });
        });
    }
    
    //Push items up or down in Personalize page
    $('.upward').click(function(e){
        e.preventDefault();
        var current = $(this).closest('tr');
        current.prev().before(current);
        showChanged(current);
        getListNumber();
      });
    
    $('.downward').click(function(e){
        e.preventDefault();
        var current = $(this).closest('tr');
        current.next().after(current);
        showChanged(current);
        getListNumber();  
    });
    
    function showChanged(current){
        current.css({
            backgroundColor: "#ccc"    
        }).animate({
            backgroundColor: "#fcfbfb"    
        }, 300);
    }
    
    function getListNumber () {
        $(".list-number").each(function(){
            var list = $(this).closest("tr");
            var listPrev = list.prev();
            var listNum
            if (list.index() == 0){
                listNum = parseInt(list.index()) + 1;
            }else{
                listNum = parseInt($(".list-number", listPrev).html()) + parseInt($(".input-smallest", listPrev).val());
            }
            totalNights();
            $(this).html(listNum);
        });
    }
    
    function totalNights() {
        var total = 0;
        $(".input-smallest").each(function(){
            total += parseInt($(this).val());
        });
        
        $(".totalNights").html(total + " Nights");
    }
    
    $('.deleteItem').on('click', function(e){
            e.preventDefault();
            var list = $(this).closest("tr");
            list.remove();
        });
    $(".popBtn").on("click", function() {
        $('#chooseItineraryPrefrences').modal('hide');
    });
    
    $( "#slider" ).slider({
            value:300,
	    min: 100,
	    max: 500,
	    step: 100,
	    slide: function( event, ui ) {
                var slideVal = ui.value;
                var textVal;
                switch (slideVal){
                    case 100:
                        textVal = "Shorter drives, less sites";
                    break;
                    case 200:
                        textVal = "Option 2";
                    break;
                    case 300:
                        textVal = "Option 3";
                    break;
                    case 400:
                        textVal = "Option 4";
                    break;
                    case 500:
                        textVal = "Longer drives, more sites";
                    break;
                }
	    $( "#drivePref" ).html( textVal );
	}    
    });
    $( "#drivePref" ).html("Option 3");
    
    var activeUnit = "km";
    
    $("#km").on("click", function(e){
        e.preventDefault();
        if (activeUnit == "miles"){
            $(".unit").each(function(){
                $(this).html('km');
            });
            $(".value").each(function(){
                var realVal = parseFloat($(this).attr('title')) * parseFloat(1.609344);
                var val = roundNumber(realVal, 2);
                console.log(realVal);
                $(this).attr('title', realVal);
                $(this).html(val);    
            });
            activeUnit = "km";
            console.log(activeUnit);
        }
    });
    $("#miles").on("click", function(e){
        e.preventDefault();
        if (activeUnit == "km"){
            $(".unit").each(function() {
                $(this).html('miles');
            });
            $(".value").each(function(){
                var realVal = parseFloat($(this).attr('title')) * parseFloat(0.621371192);
                var val = roundNumber(realVal, 2);
                console.log(realVal);
                $(this).attr('title', realVal);
                $(this).html(val);    
            });
            activeUnit = "miles";
            console.log(activeUnit);
        }
    });
    
    function roundNumber(num, dec) {
	var result = Math.round(num*Math.pow(10,dec))/Math.pow(10,dec);
	return result;
    }
    $(".plusOne").on("click", function(e){
        e.preventDefault();
        var input = $(this).siblings(".input-smallest");
        console.log(input);
        input.val(parseInt(input.val()) + 1);
        getListNumber();
    });
    $(".minusOne").on("click", function(e){
        e.preventDefault();
        var input = $(this).siblings(".input-smallest");
        console.log(input);
        if (parseInt(input.val()) - 1 > 0){
            input.val(parseInt(input.val()) - 1);
        }
        getListNumber();
    });
    
    function getAverageDrivingHour () {
        var totalHours = 0, avgHour;
        var numberOfTrips = $(".hourValue").length;
        $(".hourValue").each(function() {
            totalHours += parseFloat($(this).html());
            avgHour = totalHours/numberOfTrips;
            $(".avgHour").html(roundNumber(avgHour, 2));
        });
    }
    
    function getAverageDistancePerDay (){
        var totalDrivingDistance = 0, avgDistance;
        var numberOfTrips = $(".value").length;
        $(".value").each(function() {
            totalDrivingDistance += parseFloat($(this).html());
            avgDistance = totalDrivingDistance/numberOfTrips;
            $(".avgDistance").html(roundNumber(avgDistance, 1));
            $(".avgDistance").attr("title", avgDistance);
        });
    }
    
    $(".print").on("click", function (e) {
        e.preventDefault();
        var container = $(this).attr('rel');
	$('.' + container).printArea();
    });
    
});