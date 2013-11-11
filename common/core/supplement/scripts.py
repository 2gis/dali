class Scripts(object):
    disable_animation = """
        var _s = document.createElement("style");
        _s.type = "text/css";
        _s.textContent = "* {                               \
            -o-transition-property:         none !important;\
            -moz-transition-property:       none !important;\
            -ms-transition-property:        none !important;\
            -webkit-transition-property:    none !important;\
            transition-property:            none !important;\
            -webkit-animation:              none !important;\
            -moz-animation:                 none !important;\
            -o-animation:                   none !important;\
            -ms-animation:                  none !important;\
            animation:                      none !important;\
        }";
        document.getElementsByTagName("head")[0].appendChild(_s);
    """

    hide_elements = """
        var _n = document.querySelectorAll('%s');
        for (var i = 0; i < _n.length; i++) {
            _n[i].style.visibility = 'hidden';
        }
    """
