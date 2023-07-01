const menuActive = document.querySelector('.menu')
const headerButton = document.querySelector('.burger_m')

function interactionMenu() {
    menuActive.classList.toggle('m_hidden')
}

headerButton.addEventListener('click', interactionMenu)
