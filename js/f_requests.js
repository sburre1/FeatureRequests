$(document).ready(function()
{
    var date_input=$('input[name="targetDate"]'); //our date input has the name "targetDate"
    var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
    date_input.datepicker({
        format: 'mm/dd/yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
    })
})