import i18n

def get_protect_info(lang):
    menu = f'''{i18n.t('_ProtectInfo_', locale=lang)}\n\n {i18n.t('_ReplyForMenu_', locale=lang)}'''
    return menu