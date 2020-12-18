document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('.custom-select-wrapper').addEventListener('click', function() {
        this.querySelector('.custom-select').classList.toggle('open');
    })

    for (const option of document.querySelectorAll(".custom-option")) {
    option.addEventListener('click', function() {
        if (!this.classList.contains('selected')) {
            this.parentNode.querySelector('.custom-option.selected').classList.remove('selected');
            this.classList.add('selected');
            this.closest('.custom-select').querySelector('.custom-select__trigger span').textContent = this.textContent;
        }
    })
}
window.addEventListener('click', function(e) {
    const select = document.querySelector('.custom-select')
    if (!select.contains(e.target)) {
        select.classList.remove('open');
    }
});


    document.querySelector('.book-flight-button').disabled = true;

    document.querySelector('.book-flight-button').onclick = () => {

        if (document.querySelector('#first-name').value.length > 0 && (document.querySelector('#first-name').value).trim() !== '')
        {
            if (document.querySelector('#age').value > 0)
            {
                if (document.querySelector('#e-mail').value.length > 0 && (document.querySelector('#e-mail').value).trim() !== '')
                {
                    document.querySelector('#book').disabled = false;
                }
            }
        }

        else {
            document.querySelector('.book-flight-button').disabled = true;
        }
    };
});
