// Function will change label value based of dropdown selected value
function changeLabelValue(dropdown_id, label_id, period_selector_id) {
    const dropdown = document.getElementById(dropdown_id)
    const label = document.getElementById(label_id)
    const period_selector = document.getElementById(period_selector_id)

    dropdown.addEventListener("change", function() {
        if (dropdown.value === "DAILY") {
            period_selector.disabled = true;
            label.textContent = "Typ okresu powtarzalności";
        } else if (dropdown.value === "WEEKLY") {
            period_selector.disabled = false;
            label.textContent = "Numer dnia w tygodniu";
        } else if (dropdown.value === "MONTHLY") {
            period_selector.disabled = false;
            label.textContent = "Numer dnia w miesiącu";
        } else if (dropdown.value === "QUATERLY") {
            period_selector.disabled = false;
            label.textContent = "Numer dnia w kwartale";
        } else if (dropdown.value === "ANNUALLY") {
            period_selector.disabled = false;
            label.textContent = "Numer dnia w roku";
        }
    });
};