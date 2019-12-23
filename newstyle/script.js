var Expand = (function() {
    var tile = $('.strips__strip');
    var tileLink = $('.strips__strip > .strip__content');
    var tileText = tileLink.find('.strip__inner-text');
    var stripClose = $('.strip__close');

    var expanded  = false;
    
    var open = function(artid) {

        // var tile = $(this).parent();
        var tile = document.getElementById(artid);
        // var tileText = document.getElementById(artid+"a");
        console.log(expanded);

        if (!expanded) {
            // tile.addClass('strips__strip--expanded');
            tile.classList.add('strips__strip--expanded');
            // add delay to inner text
            tileText.css('transition', 'all .5s .3s cubic-bezier(0.23, 1, 0.32, 1)');
            stripClose.addClass('strip__close--show');
            stripClose.css('transition', 'all .6s 1s cubic-bezier(0.23, 1, 0.32, 1)');
            expanded = true;
        }  else {
            close(artid);
        }
    };

    var close = function(artid) {
        var tile = document.getElementById(artid);
        if (expanded) {
            // tile.removeClass('strips__strip--expanded');
            tile.classList.remove('strips__strip--expanded');
            // remove delay from inner text
            tileText.css('transition', 'all 0.15s 0 cubic-bezier(0.23, 1, 0.32, 1)');
            stripClose.removeClass('strip__close--show');
            stripClose.css('transition', 'all 0.2s 0s cubic-bezier(0.23, 1, 0.32, 1)')
            expanded = false;
        }
    }

    var bindActions = function() {
        tileLink.on('click', open);
        stripClose.on('click', close);
    };

    var init = function() {
        bindActions();
    };

    return {
        init: init,
        open: open
    };

}());

Expand.init();

function deto(artid) {
        Expand.open(artid);
}

