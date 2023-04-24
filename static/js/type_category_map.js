/**
 * JavaScript code listens for a change in the first select element with ID "id_type". 
 * When a change occurs, it uses a JSON object called "type_to_category" to retrieve 
 * available options for the corresponding category. 
 * 
 * It then creates HTML option elements based on the available options and appends them 
 * to the second select element with ID "id_category". If the available options are not 
 * defined or not an array, it logs a message to the console.
 */

const typeSelect = document.getElementById("id_type");
const categorySelect = document.getElementById("id_category");
const options = JSON.parse(type_to_category);

// disable category fielad based on category fielad value
if (typeSelect.value !== "") {
  categorySelect.disabled = false

} else {
  categorySelect.disabled = true;
  categorySelect.innerHTML = '';
}

typeSelect.addEventListener("change", (event) => {
  const selectedOption = event.target.value;
  const availableOptions = options[selectedOption];

  categorySelect.disabled = false

  if (availableOptions && Array.isArray(availableOptions)) {
    const optionsHTML = availableOptions
      .map((option) => `<option value="${option[0]}">${option[1]}</option>`)
      .join("");
    categorySelect.innerHTML = optionsHTML;
  } else {
    // handle case when availableOptions is not defined or not an array
    console.log("Available options not defined or not an array.");
  }
});