function validateForm() {
    const nom = document.getElementById('nom').value;
    const prenom = document.getElementById('prenom').value;
    let password = document.getElementById('password').value;
    const passwordComfirm = document.getElementById('passwordComfirm').value;
    console.log(nom, prenom, password, passwordComfirm)
    let isValid = true;
    if (nom === '') {
        document.getElementById('nomWarning').textContent = 'Veuillez saisir votre nom.';
        isValid = false;
    } else {
        document.getElementById('nomWarning').textContent = '';
    }
    if (prenom === '') {
        document.getElementById('prenomWarning').textContent = 'Veuillez saisir votre prénom.';
        isValid = false;
    } else {
        document.getElementById('prenomWarning').textContent = '';
    }
    if (password === '') {
        document.getElementById('passwordWarning').textContent = 'Veuillez saisir votre mot de passe.';
        isValid = false;
    } else if (passwordComfirm !== password) {
        document.getElementById('passwordWarning').textContent = '';
        document.getElementById('passwordComfirmWarning').textContent = 'Les mots de passe ne correspondent pas.';
        isValid = false;
    } else {
        document.getElementById('passwordComfirmWarning').textContent = '';
    }
    if (isValid) {
        password = CryptoJS.SHA256(password).toString(CryptoJS.enc.Hex);
        document.getElementById('password').value = password;
        return true;
    } else {
        return false;
    }
}