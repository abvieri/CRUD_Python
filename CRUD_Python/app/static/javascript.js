(function (win, doc) {
    'user strict';

    // confirma se o usuário deseja apagar o dado
    if (doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel');
        for (let i = 0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function (event) {
                if (confirm('Deseja apagar este dado?')) {
                    return true;
                } else {
                    event.preventDefault();
                }
            })
        }
    }

    // Ajax do form
    function sendForm(event) {
        event.preventDefault();
        let data = new FormData(form);
        let ajax = new XMLHttpRequest();
        let token = doc.querySelectorAll('input')[0].value;
        ajax.open('POST', form.action);
        ajax.setRequestHeader("X-CSRFToken", token);
        ajax.onreadystatechange = function () {
            if (ajax.status === 200 && ajax.readyState === 4) {
                let result = doc.querySelectorAll('#result')[0];
                
                result.innerHTML = 'Operação realizada com sucesso!';
                result.classList.add('alert');
                result.classList.add('alert-success');
                setTimeout(() => {
                    result.innerHTML = '';
                    result.classList.remove('alert');
                    result.classList.remove('alert-success');
                }, 3000);
            }
        }
        ajax.send(data);
        form.reset();
    }
    form.addEventListener("submit", sendForm, false);

})(window, document);