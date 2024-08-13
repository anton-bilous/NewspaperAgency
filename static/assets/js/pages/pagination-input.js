'use strict';

function goToPage() {
    const searchParams = new URLSearchParams(window.location.search);
    const pageInput = document.getElementById("page-number-input");
    searchParams.set("page", pageInput.value);
    window.location.search = searchParams.toString();
}
