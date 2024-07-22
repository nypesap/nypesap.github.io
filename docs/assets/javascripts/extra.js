document.addEventListener("DOMContentLoaded", () => {
    "use strict";
    // Copied from 
    // https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/blob/66b952c3ae8eae9fdd3b181bfaf9a3e1ee424208/mkdocs_git_revision_date_localized_plugin/js/timeago_mkdocs_material.js

    if (typeof document$ !== "undefined") {
        document$.subscribe(function() {
            const nodes = document.querySelectorAll('.timeago');
            if (nodes.length > 0) {
              const locale = nodes[0].getAttribute('locale');
              timeago.render(nodes, locale);
            }
        })
    } else {
        const nodes = document.querySelectorAll('.timeago');
        if (nodes.length > 0) {
          const locale = nodes[0].getAttribute('locale');
          timeago.render(nodes, locale);
        }
    }
});

document.addEventListener("DOMContentLoaded", () => {
    "use strict";

    if (!window.location.pathname.startsWith("/contact")) {
        return;
    }

    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }

    if (window.location.pathname.startsWith("/contact-success/")) {
        gtag("event", "sign_up_success");
    }

    const form = document.querySelector("#extFormWrapper > form");

    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();

            if (!form.reportValidity()) {
                return;
            }

            gtag("event", "sign_up", { method: "Contact Form" });

            // URL -> base64 -> HEX
            const hexData = "6148523063484d364c79396d62334a74637935316269317a6447463061574d75593239744c325a76636d317a4c7a646a596d49344d6a557a5957457a596a5934596d4d3059574e6b596a45304d44557a4e7a41334d5445315a6a55794e6d51354d7a673d";

            if (!["127.0.0.1", "localhost"].includes(window.location.hostname)) {
                form.action = atob(String.fromCharCode(...hexData.match(/.{1,2}/g).map(byte => parseInt(byte, 16))));
            }

            form.submit();
        });
    }

    const showEmailToggle = document.querySelector("#extShowEmail");

    if (showEmailToggle) {
        showEmailToggle.addEventListener("click", (e) => {
            e.preventDefault();
            gtag("event", "show_email");
            // HTML <a> with mailto: -> base64 -> HEX
            const hexData = "5047456761484a6c5a6a306962574670624852764f6d64795a576375625746735a58647a61326c41626e6c775a584e686343356a62323069506d64795a576375625746735a58647a61326c41626e6c775a584e686343356a623230384c32452b";
            const span = document.createElement("span");
            span.innerHTML = atob(String.fromCharCode(...hexData.match(/.{1,2}/g).map(byte => parseInt(byte, 16))));
            showEmailToggle.replaceWith(span);
        });
    }
});