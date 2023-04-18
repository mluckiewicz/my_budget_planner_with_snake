// Function will change label value based of dropdown selected value
function changeLabelValue(dropdown_id, label_id, period_selector_id) {
    const dropdown = document.getElementById(dropdown_id)
    const label = document.getElementById(label_id)
    const period_selector = document.getElementById(period_selector_id)

    dropdown.addEventListener("change", function() {
        if (dropdown.value === "DAILY") {
            period_selector.value = 1;
            period_selector.disabled = true;
            period_selector.textContent = "Not applicable";
        } else if (dropdown.value === "WEEKLY") {
            period_selector.disabled = false;
            label.textContent = "Day of the week";
            period_selector.placeholder  = "From 1 to 7";
        } else if (dropdown.value === "MONTHLY") {
            period_selector.disabled = false;
            label.textContent = "Day of the week";
            period_selector.placeholder  = "From 1 to 31";
        } else if (dropdown.value === "ANNUALLY") {
            period_selector.disabled = false;
            label.textContent = "Day of the year";
            period_selector.placeholder  = "From 1 to 366";
        }
    });
};