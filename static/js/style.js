const menuButton = document.getElementById("menu-button");
const mobileNav = document.getElementById("mobile-nav");

/*
|--------------------------------------------------------------------------
| Menu mobile
|--------------------------------------------------------------------------
*/

if (menuButton && mobileNav) {

    menuButton.addEventListener("click", () => {

        const isOpen =
            mobileNav.classList.toggle("active");

        menuButton.setAttribute(
            "aria-expanded",
            isOpen
        );

        menuButton.textContent =
            isOpen ? "✕" : "☰";

    });


    /*
    |--------------------------------------------------------------------------
    | Fermer le menu après un clic
    |--------------------------------------------------------------------------
    */

    const mobileLinks =
        mobileNav.querySelectorAll("a");


    mobileLinks.forEach(link => {

        link.addEventListener("click", () => {

            mobileNav.classList.remove("active");

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.textContent = "☰";

        });

    });

}


/*
|--------------------------------------------------------------------------
| Animation d'apparition
|--------------------------------------------------------------------------
*/

const animatedElements =
    document.querySelectorAll(
        ".service-card, .project-card, .process-step"
    );


const observer =
    new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add(
                        "visible"
                    );

                    observer.unobserve(
                        entry.target
                    );

                }

            });

        },
        {
            threshold: 0.15
        }
    );


animatedElements.forEach(element => {

    observer.observe(element);

});