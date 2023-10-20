// Function to handle form submission
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("predict-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const sequence = formData.get("sequence");

        // Making AJAX request to Django backend
        fetch(`/predict/?sequence=${sequence}`)
            .then(response => response.json())
            .then(data => {
                if (data.predictions !== undefined) {
                    let predictionsHtml = "<p>Predicted receipt counts (scaled) for each month in 2022:</p><ul>";
                    data.predictions.forEach((prediction, index) => {
                        predictionsHtml += `<li>Month ${index + 1}: ${prediction.toFixed(3)}</li>`;
                    });
                    predictionsHtml += "</ul>";
                    resultDiv.innerHTML = predictionsHtml;
                } else {
                    resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                resultDiv.innerHTML = `<p>An error occurred while making the prediction.</p>`;
            });
    });
});
