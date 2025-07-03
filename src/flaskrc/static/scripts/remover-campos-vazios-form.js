document.querySelectorAll('form').forEach(form => {
    console.log(form)
    form.addEventListener('submit', function (e) {
    const form = this;
    const inputs = form.querySelectorAll('input, select, textarea');

    inputs.forEach(input => {
    if (input.value.trim() === '') {
        input.removeAttribute('name'); // remove do POST
    }
    });
});
})
