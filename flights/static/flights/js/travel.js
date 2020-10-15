document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#book').disabled = true;

    document.querySelector('#first-name').onkeyup = () => {

        if (document.querySelector('#first-name').value.length > 0 && (document.querySelector('#first-name').value).trim() !== '')
            document.querySelector('#book').disabled = false;
        else
            document.querySelector('#book').disabled = true;
    };

    document.querySelector('#book').onclick = () => {
        if (document.querySelector('#first-name').value.length > 0 && (document.querySelector('#first-name').value).trim() !== '')
            document.querySelector('#book').disabled = false;
        else
            document.querySelector('#book').disabled = true;
    }
});
