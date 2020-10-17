document.addEventListener('DOMContentLoaded', () => {

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
