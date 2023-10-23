
var firstDropdown = document.getElementById("category");
var secondDropdown = document.getElementById("activity");

firstDropdown.onchange = function() {
  // Clear the second dropdown
  secondDropdown.innerHTML = "";

  // Get the selected value from the first dropdown
  var selectedValue = firstDropdown.value;

  // Enable the second dropdown
  secondDropdown.disabled = false;

  console.log(selectedValue)

  // Add options to the second dropdown based on the selected value
  if (selectedValue === "recovery") {
    var option = document.createElement("option");
    option.text = "Cold Plunge";
    option.value = "cold_plunge";
    secondDropdown.add(option);

    option = document.createElement("option");
    option.text = "Stretch";
    option.value = "stretch";
    secondDropdown.add(option);

    option = document.createElement("option");
    option.text = "Ice";
    option.value = "ice";
    secondDropdown.add(option);

    option = document.createElement("option");
    option.text = "Sauna";
    option.value = "sauna";
    secondDropdown.add(option);

    option = document.createElement("option");
    option.text = "Steam Room";
    option.value = "steam_room";
    secondDropdown.add(option);

    // Add more options as needed for option1
  } else if (selectedValue === "workout") {
  	    var option = document.createElement("option");
        
        option = document.createElement("option");
        option.text = "Run";
        option.value = "run";
        secondDropdown.add(option);

        option = document.createElement("option");
        option.text = "Resistance Training";
        option.value = "resistance_training";
        secondDropdown.add(option);

        option = document.createElement("option");
        option.text = "Cycling";
        option.value = "cycling";
        secondDropdown.add(option);

        option = document.createElement("option");
        option.text = "Jump Rope";
        option.value = "jump_rope";
        secondDropdown.add(option);
  }
};