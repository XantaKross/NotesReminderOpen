// Get the elements from the HTML
const tbox = document.getElementById('Text_Box');
const positive = document.getElementById("Add");
const negative = document.getElementById("Discard");
const comment = document.getElementById("Comment");

// Hide and clear the elements initially
tbox.value = '';
tbox.style.display = 'none';
comment.style.display = 'none';

// Add click event listener to the positive button
positive.addEventListener("click", function(event) {
     if (tbox.style.display === 'none') {
        // Show the input box and buttons
        tbox.style.display = 'inline-block';
        comment.style.display = 'inline-block';

        comment.innerText = "Enter task format as 'Task, Deadline'"
        positive.innerText = 'Enter';
        negative.innerText = 'Discard';

        boolean = 1; // added.
        tbox.focus(); // set focus to the input box
    }

    else {
        // Hide the input box and buttons
        tbox.style.display = 'none';
        comment.style.display = 'none';

        positive.innerText = '+';
        negative.innerText = 'x';

        // Get the value of tbox and call the showTable() function
        const task = tbox.value.trim();
        if (task !== '') {
            showTable(task);
        }
        tbox.value = ''; // clear the input box
    }
});

// Add click event listener to the negative button
negative.addEventListener("click", function(event) {
     if (tbox.style.display === 'none') {
        // Show the input box and buttons
        tbox.style.display = 'inline-block';
        comment.style.display = 'inline-block';

        comment.innerText = "Type priority to be deleted."
        positive.innerText = 'Enter';
        negative.innerText = 'Discard';

        boolean = 0; // removed.
        tbox.focus(); // set focus to the input box
    }

    else {
        // Hide the input box and buttons
        tbox.style.display = 'none';
        comment.style.display = 'none';

        positive.innerText = '+';
        negative.innerText = 'x';

        // Get the value of tbox and call the removeTable() function
        const task = tbox.value.trim();
        if (task !== '') {
            showTable(task);
        }
        tbox.value = ''; // clear the input box
    }
});
