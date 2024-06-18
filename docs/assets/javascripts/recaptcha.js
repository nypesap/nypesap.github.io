function _recaptchaOnShowEmail(token) {
    // HTML <a> with mailto: -> base64 -> HEX
    const hexData = "5047456761484a6c5a6a306962574670624852764f6d64795a576375625746735a58647a61326c41626e6c775a584e686343356a62323069506d64795a576375625746735a58647a61326c41626e6c775a584e686343356a623230384c32452b";
    const emailTag = atob(String.fromCharCode(...hexData.match(/.{1,2}/g).map(byte => parseInt(byte, 16))));

    const emailLocation = document.querySelector("#extEmailLocation");
    const button = document.querySelector(".g-recaptcha#extShowEmail");
    emailLocation.innerHTML = emailTag;
    button.remove();
}
function _recaptchaOnErrorEmail() {
    const button = document.querySelector(".g-recaptcha#extShowEmail");
    const errorWrapper = document.createElement("p");
    errorWrapper.className = "recaptchaError";
    errorWrapper.style = "color: red;";
    errorWrapper.innerText = "There was an error with reCAPTCHA, please try again...";

    // More errors mean that the page didn't freeze, which is good UX
    // perhaps there is a cleaner way, but for now more errors will suffice.
    // if (document.querySelector(`.${errorWrapper.className}`)) {
    //     return;
    // }

    button.before(errorWrapper);
}
function _recaptchaOnSubmitForm(token) {
    const form = document.querySelector("#extFormWrapper > form");
    
    if (!form.reportValidity()) {
        return;
    }
    
    // URL -> base64 -> HEX
    const hexData = "6148523063484d364c79396d62334a74637935316269317a6447463061574d75593239744c325a76636d317a4c7a646a596d49344d6a557a5957457a596a5934596d4d3059574e6b596a45304d44557a4e7a41334d5445315a6a55794e6d51354d7a673d";
    const actionUrl = atob(String.fromCharCode(...hexData.match(/.{1,2}/g).map(byte => parseInt(byte, 16))));
    const responseTextareas = form.querySelectorAll('textarea[name="g-recaptcha-response"]');
    
    for (const el of responseTextareas) {
        el.remove();
    }
    
    form.action = actionUrl;
    form.submit();
}
function _recaptchaOnErrorForm() {
    const button = document.querySelector(".g-recaptcha#extSubmitForm");
    const errorWrapper = document.createElement("p");
    errorWrapper.className = "recaptchaError";
    errorWrapper.style = "color: red;";
    errorWrapper.innerText = "There was an error with reCAPTCHA, please try again...";

    // More errors mean that the page didn't freeze, which is good UX
    // perhaps there is a cleaner way, but for now more errors will suffice.
    // if (document.querySelector(`.${errorWrapper.className}`)) {
    //     return;
    // }

    button.before(errorWrapper);
}