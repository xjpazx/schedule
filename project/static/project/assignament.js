$(function(){
  $('#id_activity_fk').change(function(){
    console.log(
      $('select[name="activity_fk"] option:selected').text());
  });
});