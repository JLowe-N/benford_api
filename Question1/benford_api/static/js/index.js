// File Validation - Client Side
// tsv only preferred, but allowing all files to submit to support extensionless file provided
const reAllowedFiles = /^.*\.tsv$/
// 100MB limit, but would likely need to adjust based on app requirements
const fileSizeLimit = 1024 * 1024 * 100 * 1.024
let existingHints = []


document.getElementById("benfordFileSubmit")
        .addEventListener("click", function checkFileInput(e) {
            while (existingHints.length > 0) {
                hintElement = existingHints.pop()
                hintElement.remove()
            }

            const input = document.getElementById("benfordFileInput");
            const file = input.files[0];
            
            if (!file) {
                addHint("Please select a file before clicking 'Upload'", input);
            } else if (!reAllowedFiles.test(file.name)) {
                addHint("Please ensure you are submitting a CSV or TSV file", input);
                // Will allow to submit any file due to provided 7_2009 file
                // since it has no extension
                return;
            } else if (file.size > fileSizeLimit) {
                let fileSizeMB = Math.round(file.size / 1024 / 1024)
                let fileLimitMB = Math.round(fileSizeLimit / 1024 / 1024)
                addHint("The selected file is " + fileSizeMB + " MB. The API limit is " + fileLimitMB + " MB. Try removing unnecessary columns.", input);
            } else {
                // validations passed, allow form to submit
                return;
            }
            // One of the validations failed
            e.preventDefault();
            
        })

function addHint(text, elementToAppendAfter) {
    const span = document.createElement("span");
    span.classList.add("hint");
    span.textContent = text;
    elementToAppendAfter.insertAdjacentElement('afterend', span);
    existingHints.push(span);
}