function validateScan() {
    const emailText = document.getElementById("emailText").value.trim();

    if (emailText.length < 10) {
        alert("Email content is too short to analyze!");
        return false;
    }

    document.getElementById("loading").style.display = "block";
    return true;
}
