/**
 *  A "Listener" type which helps us detect whether the clear button has been pressed.
 *  After choosing, we then pan over the selected station
 *  and afterwards we call the function which properly processes the given data
 */
// Clear button click
document.getElementById("run").addEventListener("click", function(){
    $('#start').val(null);
    $('#end').val(null);
    $('#trainTime').val(null);
    $('#carTime').val(null);
})
