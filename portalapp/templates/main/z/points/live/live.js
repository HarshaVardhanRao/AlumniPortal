document.addEventListener("DOMContentLoaded", function() {
    const alumniForm = document.getElementById('alumniForm');
    const alumniList = document.getElementById('alumniList');

    // Load alumni from localStorage
    loadAlumni();

    alumniForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const concept = document.getElementById('concept').value;
        
        const alumni = {
            name: name,
            concept: concept
        };

        // Save to localStorage
        addAlumni(alumni);
    });

    function addAlumni(alumni) {
        let alumniData = JSON.parse(localStorage.getItem('alumniData')) || [];
        alumniData.push(alumni);
        localStorage.setItem('alumniData', JSON.stringify(alumniData));
        document.getElementById('name').value = '';
        document.getElementById('concept').value = '';
        displayAlumni();
    }

    function displayAlumni() {
        alumniList.innerHTML = '';
        const alumniData = JSON.parse(localStorage.getItem('alumniData')) || [];
        alumniData.forEach((alumni, index) => {
            const div = document.createElement('div');
            div.classList.add('alumni-item');
            div.innerHTML = `${alumni.name} - ${alumni.concept} <button onclick="deleteAlumni(${index})">Delete</button>`;
            alumniList.appendChild(div);
        });
    }

    window.deleteAlumni = function(index) {
        let alumniData = JSON.parse(localStorage.getItem('alumniData')) || [];
        alumniData.splice(index, 1);
        localStorage.setItem('alumniData', JSON.stringify(alumniData));
        displayAlumni();
    }

    function loadAlumni() {
        displayAlumni();
    }
});