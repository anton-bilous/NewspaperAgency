'use strict';

function adjustWidth(element) {
    element.style.width = '0px'; // Reset width
    element.style.width = (element.scrollWidth + 1) + 'px'; // Set width based on content
}

document.addEventListener("DOMContentLoaded", function () {
    // Initialize with default width
    const page_input = document.getElementById('current-page-input');
    adjustWidth(page_input);

    page_input.addEventListener("keyup", event => {
        if (event.key === "Enter") {
            const searchParams = new URLSearchParams(window.location.search);
            searchParams.set("page", page_input.value);
            window.location.search = searchParams.toString();
        }
    });
});
