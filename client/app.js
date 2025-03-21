function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1;
}

function getbedsValue() {
  var uibeds = document.getElementsByName("uibeds");
  for(var i in uibeds) {
    if(uibeds[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var beds = getbedsValue();
  var bathrooms = getBathValue();
  var city = document.getElementById("uicity");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";
  

  $.post(url, {
      sqft: parseFloat(sqft.value),
      beds: beds,
      bath: bathrooms,
      City: city.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " $</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_city_names"; // Adres API
  
  $.get(url, function(data, status) {
      console.log("got response for get_city_names request");
      if (data) {
          var city = data.city;
          var uicity = document.getElementById("uicity");
          $('#uicity').empty();
          
          
          $('#uicity').append('<option value="" disabled="disabled" selected="selected">Choose a City</option>');

          
          for (var i in city) {
              var opt = new Option(city[i], city[i]); 
              $('#uicity').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
