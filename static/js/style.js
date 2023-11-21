// Get references to the buttons by their IDs
        const showButton = document.getElementById('showButton');
        const hiddenButton = document.getElementById('hiddenButton');

        // Add a click event listener to the "showButton"
        showButton.addEventListener('click', () => {
            // Change the style of the "hiddenButton" to display it
            hiddenButton.style.display = 'block';
            showButton.style.disabled = true;
        });