const toggleSkills = document.getElementById("toggleSkills");
      const skillsOptions = document.getElementById("skillsOptions");

      toggleSkills.addEventListener("change", () => {
        if (toggleSkills.checked) {
          skillsOptions.style.display = "block";
        } else {
          skillsOptions.style.display = "none";
        }
});
const registrationForm = document.getElementById("registrationForm");

      registrationForm.addEventListener("submit", (e) => {
        e.preventDefault();

        // Perform registration logic here

        // Reset form values
        registrationForm.reset();
});