// Careful. This returns a Promise. Proper usage is:

// loadPrivateKey(...).then(
//    privateKey => console.log(privateKey) // RESOVE
//    reason => console.log(reason) // REJECT
//).catch(
//    err => console.log(err)
//)
const loadPrivateKey = (async(privateKeyArmored, passphrase) => {
    let privateKey = await openpgp.decryptKey({
      privateKey: await openpgp.readPrivateKey({ armoredKey: privateKeyArmored }),
      passphrase
    });
    return privateKey
})

const loadPrivateKeyLocal = async () => loadPrivateKey(
    localStorage['privateKeyArmored'],localStorage['privateKeyPassphrase'] 
)

const enableTooltips = () => {
    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))      
    let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
}

const loadPublicKey = (async(key_data) => {
    let publicKey = await openpgp.readKey({
        armoredKey: key_data
    });
    return publicKey
    
})

const generateKeyPair = (async (name, email, passphrase) => {
    const date = new Date().toISOString()
    const { privateKey, publicKey, revocationCertificate } = await openpgp.generateKey({
        type: 'ecc', 
        curve: 'curve25519', 
        userIDs: [{ name, email, comment: "ETSD Generated Key, " + date }], 
        passphrase, 
        format: 'armored' 
    });

    return {
        privateKey,
        publicKey
    }
})

const downloadBlob = (blob, filename) => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename || 'download';
    const clickHandler = () => {
        setTimeout(() => {
        URL.revokeObjectURL(url);
        this.removeEventListener('click', clickHandler);
        }, 150);
    };
    a.addEventListener('click', clickHandler, false);
    a.click();
    return a;
}

const downloadKey = (keyString, filename) => downloadBlob(new Blob([keyString], {type :'application/pgp-keys'}), filename)

const jqDisable = (sel) => $(sel).prop({'disabled': true})
const jqEnable = (sel) => $(sel).prop({'disabled': false})