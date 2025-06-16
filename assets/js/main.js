// This script runs after the entire HTML document has been loaded.
document.addEventListener('DOMContentLoaded', function() {
  // Find all the buttons that have the class 'filter-btn'.
  const filterButtons = document.querySelectorAll('.filter-btn');
  // Find all the project links.
  const projects = document.querySelectorAll('.card-list-item-link');

  // If there are no filter buttons on the page, stop the script.
  if (!filterButtons.length) {
    return;
  }

  // Add a 'click' event listener to each filter button.
  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      // When a button is clicked, first remove the 'active' class from all buttons.
      filterButtons.forEach(btn => btn.classList.remove('active'));
      // Then, add the 'active' class to the button that was just clicked.
      this.classList.add('active');

      // Get the filter value from the 'data-filter' attribute of the clicked button.
      const filter = this.getAttribute('data-filter');

      // Go through each project to decide whether to show or hide it.
      projects.forEach(project => {
        // Get the tags for the project from its 'data-tags' attribute and split them into an array.
        const tags = project.getAttribute('data-tags').split(',');

        // Check if the filter is 'all' or if the project's tags include the current filter.
        if (filter === 'all' || tags.includes(filter)) {
          // If it's a match, make the project visible.
          project.style.display = 'block';
        } else {
          // If it's not a match, hide the project.
          project.style.display = 'none';
        }
      });
    });
  });
});
