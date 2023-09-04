from utils import callFunctionIfCallable

from .._SettingBoxGenerator import _SettingBoxGenerator

def createSettingBox_Appearance(setting_box_wrapper, config_window, settings, view_variable):
    sbg = _SettingBoxGenerator(config_window, settings)
    createSettingBoxDropdownMenu = sbg.createSettingBoxDropdownMenu
    createSettingBoxSlider = sbg.createSettingBoxSlider

    # 関数名は変えるかもしれない。
    # テーマ変更、フォント変更時、 Widget再生成か再起動かは検討中
    def slider_transparency_callback(value):
        callFunctionIfCallable(view_variable.CALLBACK_SET_TRANSPARENCY, value)

    def optionmenu_appearance_theme_callback(value):
        callFunctionIfCallable(view_variable.CALLBACK_SET_APPEARANCE, value)

    def optionmenu_ui_scaling_callback(value):
        callFunctionIfCallable(view_variable.CALLBACK_SET_UI_SCALING, value)

    def optionmenu_font_family_callback(value):
        callFunctionIfCallable(view_variable.CALLBACK_SET_FONT_FAMILY, value)

    def optionmenu_ui_language_callback(value):
        callFunctionIfCallable(view_variable.CALLBACK_SET_UI_LANGUAGE, value)


    row=0
    config_window.sb__transparency = createSettingBoxSlider(
        parent_widget=setting_box_wrapper,
        for_var_label_text=view_variable.VAR_LABEL_TRANSPARENCY,
        for_var_desc_text=view_variable.VAR_DESC_TRANSPARENCY,
        slider_attr_name="sb__transparency_slider",
        slider_range=view_variable.SLIDER_RANGE_TRANSPARENCY,
        command=lambda value: slider_transparency_callback(value),
        variable=view_variable.VAR_TRANSPARENCY,
    )
    config_window.sb__transparency.grid(row=row)
    row+=1


    config_window.sb__appearance_theme = createSettingBoxDropdownMenu(
        parent_widget=setting_box_wrapper,
        for_var_label_text=view_variable.VAR_LABEL_APPEARANCE_THEME,
        for_var_desc_text=view_variable.VAR_DESC_APPEARANCE_THEME,
        optionmenu_attr_name="sb__optionmenu_appearance_theme",
        dropdown_menu_attr_name="sb__dropdown_appearance_theme",
        dropdown_menu_values=view_variable.LIST_APPEARANCE_THEME,
        command=lambda value: optionmenu_appearance_theme_callback(value),
        variable=view_variable.VAR_APPEARANCE_THEME,
    )
    config_window.sb__appearance_theme.grid(row=row)
    row+=1



    config_window.sb__ui_scaling = createSettingBoxDropdownMenu(
        parent_widget=setting_box_wrapper,
        for_var_label_text=view_variable.VAR_LABEL_UI_SCALING,
        for_var_desc_text=view_variable.VAR_DESC_UI_SCALING,
        optionmenu_attr_name="sb__optionmenu_ui_scaling",
        dropdown_menu_attr_name="sb__dropdown_ui_scaling",
        dropdown_menu_values=view_variable.LIST_UI_SCALING,
        command=lambda value: optionmenu_ui_scaling_callback(value),
        variable=view_variable.VAR_UI_SCALING,
    )
    config_window.sb__ui_scaling.grid(row=row)
    row+=1


    config_window.sb__font_family = createSettingBoxDropdownMenu(
        parent_widget=setting_box_wrapper,
        for_var_label_text=view_variable.VAR_LABEL_FONT_FAMILY,
        for_var_desc_text=view_variable.VAR_DESC_FONT_FAMILY,
        optionmenu_attr_name="sb__optionmenu_font_family",
        dropdown_menu_values=view_variable.LIST_FONT_FAMILY,
        command=lambda value: optionmenu_font_family_callback(value),
        variable=view_variable.VAR_FONT_FAMILY,
    )
    config_window.sb__font_family.grid(row=row)
    row+=1


    config_window.sb__ui_language = createSettingBoxDropdownMenu(
        parent_widget=setting_box_wrapper,
        for_var_label_text=view_variable.VAR_LABEL_UI_LANGUAGE,
        for_var_desc_text=view_variable.VAR_DESC_UI_LANGUAGE,
        optionmenu_attr_name="sb__optionmenu_ui_language",
        dropdown_menu_attr_name="sb__dropdown_ui_language",
        dropdown_menu_values=view_variable.LIST_UI_LANGUAGE,
        command=lambda value: optionmenu_ui_language_callback(value),
        variable=view_variable.VAR_UI_LANGUAGE,
    )
    config_window.sb__ui_language.grid(row=row)
    row+=1