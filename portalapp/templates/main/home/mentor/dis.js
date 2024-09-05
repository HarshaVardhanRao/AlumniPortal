const profile = JSON.parse(localStorage.getItem('alumniProfile'));
const profileDetails = document.getElementById('profileDetails');

if (profile) {
    profileDetails.innerHTML = `
        <p><strong>Full Name:</strong> ${profile.fullName}</p>
        <p><strong>Email:</strong> ${profile.email}</p>
        <p><strong>Phone:</strong> ${profile.phone}</p>
        <p><strong>Address:</strong> ${profile.address}</p>
        <p><strong>Date of Birth:</strong> ${new Date(profile.dob).toLocaleDateString()}</p>

        <h2>Educational Background</h2>
        <p><strong>Degree(s):</strong> ${profile.degree}</p>
        <p><strong>Graduation Year:</strong> ${profile.gradYear}</p>
        <p><strong>Major:</strong> ${profile.major}</p>
        <p><strong>Honors:</strong> ${profile.honors}</p>

        <h2>Professional Information</h2>
        <p><strong>Job Title:</strong> ${profile.jobTitle}</p>
        <p><strong>Company:</strong> ${profile.company}</p>
        <p><strong>Industry:</strong> ${profile.industry}</p>
        <p><strong>Achievements:</strong> ${profile.achievements}</p>
        <p><strong>LinkedIn:</strong> <a href="${profile.linkedin}">${profile.linkedin}</p>
}
