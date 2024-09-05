document.getElementById("profileForm").addEventListener("submit", saveProfile);
document.getElementById("viewProfiles").addEventListener("click", viewProfiles);

function saveProfile(e) {
    e.preventDefault();

    let profiles = JSON.parse(localStorage.getItem("profiles")) || [];

    const profile = {
        fullName: document.getElementById("fullName").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        address: document.getElementById("address").value,
        dob: document.getElementById("dob").value,
        degree: document.getElementById("degree").value,
        graduationYear: document.getElementById("graduationYear").value,
        major: document.getElementById("major").value,
        honors: document.getElementById("honors").value,
        jobTitle: document.getElementById("jobTitle").value,
        company: document.getElementById("company").value,
        industry: document.getElementById("industry").value,
        achievements: document.getElementById("achievements").value,
        linkedin: document.getElementById("linkedin").value,
        clubs: document.getElementById("clubs").value,
        leadership: document.getElementById("leadership").value,
        projects: document.getElementById("projects").value,
        volunteer: document.getElementById("volunteer").value,
        hobbies: document.getElementById("hobbies").value,
        projectsInitiatives: document.getElementById("projectsInitiatives").value,
        memories: document.getElementById("memories").value,
        impact: document.getElementById("impact").value,
        advice: document.getElementById("advice").value,
        profilePicture: document.getElementById("profilePicture").value
    };

    profiles.push(profile);
    localStorage.setItem("profiles", JSON.stringify(profiles));
    alert("Profile saved successfully!");
    document.getElementById("profileForm").reset();
}

function viewProfiles() {
    const profileList = document.getElementById("profileList");
    profileList.innerHTML = "";
  
    profiles.forEach((profile) => {
      const profileItem = document.createElement("li");
      profileItem.innerHTML = `
        <div>
          <strong>Full Name:</strong> ${profile.fullName}
          <br>
          <strong>Email:</strong> ${profile.email}
          <br>
          <br>
          <img src="${profile.profilePicture}" alt="Profile Picture" width="100">
        </div>
      `;
      profileList.appendChild(profileItem);
    });
  }