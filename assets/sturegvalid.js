// stureg.js

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const passwordField = document.getElementById("dob");

  form.addEventListener("submit", function (event) {
    const password = passwordField.value;
    if (!isValidPassword(password)) {
      event.preventDefault(); // Prevent the form submission
      displayErrorMessage("Password does not meet the criteria.");
    }
  });

  function isValidPassword(password) {
    // Check if the password starts with a capital letter
    if (!/^[A-Z]/.test(password)) {
      return false;
    }

    // Check if the password has a length of 8 characters
    if (password.length !== 8) {
      return false;
    }

    // Check if the password contains at least one special symbol
    if (!/[!@#$%^&*]/.test(password)) {
      return false;
    }

    return true;
  }

  function displayErrorMessage(message) {
    const errorMessageDiv = document.querySelector(".error-message");
    errorMessageDiv.innerHTML = message;
    errorMessageDiv.style.display = "block";
    setTimeout(() => {
      errorMessageDiv.style.display = "none";
    }, 5000); // Hide the error message after 5 seconds
  }
});
