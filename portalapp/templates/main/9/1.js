function sendOTP(formType) {
    // Generate a more visually appealing OTP with spaces
    const otp = Math.floor(Math.random() * 900000) + 100000;
    const formattedOTP = otp.toString().replace(/\d{2}/g, "$& ");

    // Replace with your actual OTP sending logic (e.g., using an API)
    // For demonstration purposes, we'll log the OTP to the console
    console.log("Generated OTP:", formattedOTP);

    // Store the OTP in session storage for later verification
    sessionStorage.setItem(`${formType}OTP`, otp);

    // Display a message to the user indicating that the OTP has been sent
    alert(`OTP sent successfully. Please enter the following code:\n${formattedOTP}`);
}

// Handle form submissions and OTP verification
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const enteredOTP = document.querySelector("#loginForm input[name='otp']").value;
    const storedOTP = sessionStorage.getItem("loginOTP");

    if (enteredOTP === storedOTP) {
        // OTP verification successful, proceed with login logic
        console.log("Login successful!");
        // Redirect to the dashboard or appropriate page
    } else {
        // OTP verification failed, display an error message
        alert("Invalid OTP. Please try again.");
    }
});

document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const enteredOTP = document.querySelector("#registrationForm input[name='otp']").value;
    const storedOTP = sessionStorage.getItem("registerOTP");

    if (enteredOTP === storedOTP) {
        // OTP verification successful, proceed with registration logic
        console.log("Registration successful!");
        // Redirect to the login page or appropriate page
    } else {
        // OTP verification failed, display an error message
        alert("Invalid OTP. Please try again.");
    }
});