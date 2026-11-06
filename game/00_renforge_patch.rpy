
init -999 python:
    try:
        _rf_cur = getattr(store._preferences, "language", None)
        if _rf_cur is not None:
            try:
                _rf_known = renpy.known_languages()
            except:
                _rf_known = None
            if _rf_known is not None:
                _rf_bad = _rf_cur not in _rf_known
            else:
                _rf_bad = (_rf_cur == "japanese_mod")
            if _rf_bad:
                store._preferences.language = None
    except:
        pass

    _renforge_font_map = {
        u"DejaVuSans.ttf": u"logotypejp_corpmin.ttf",
        u"PAC LIBERTAS font.ttf": u"logotypejp_corpmin.ttf",
        u"Postamt.ttf": u"logotypejp_corpmin.ttf",
        u"Renner 500 Medium.ttf": u"logotypejp_corpmin.ttf",
        u"Slidfis.ttf": u"logotypejp_corpmin.ttf",
    }
    try:
        for _src, _dst in _renforge_font_map.items():
            for _b in (False, True):
                for _i in (False, True):
                    config.font_replacement_map[(_src, _b, _i)] = (_dst, _b, _i)
    except: pass
