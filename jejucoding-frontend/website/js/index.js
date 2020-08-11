window.addEventListener('load', function () {
    // var 메뉴가열려있음 = false;
    var menuBtn = document.querySelector('.global-menu-btn');

    menuBtn.addEventListener('click', function () {
        // document.body
        var bodyElem = document.querySelector('body');
        bodyElem.classList.toggle('menu-on');

        // if (메뉴가열려있음) {
        //     bodyElem.classList.remove('menu-on');
        //     메뉴가열려있음 = false;
        // } else {
        //     bodyElem.classList.add('menu-on');
        //     메뉴가열려있음 = true;
        // }

    });
});
