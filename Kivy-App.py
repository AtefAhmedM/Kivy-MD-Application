WindowManager:

    SignUp:

        id: singone

        LoginScreen:

            id: loginsc

        RiskEval:

            id: riskevaluation

        SignUptwo:
            id: signtwo

<SignUp>:

    name: "signup"

    FloatLayout:

        MDCard:

            size_hint: None, None

            size: (400, 550)

            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            elevation: 50

            padding: 20

            spacing: 30

        MDLabel:

            text: "Sign-Up"

            bold: True

            halign: "center"

            pos_hint: {"center_x": .5, "center_y": .9}

            font_style: "H4"

        MDTextField:

            id: nameone

            hint_text: "First Name"

            size_hint: None, None

            width: 320

            pos_hint: {"center_x": .5, "center_y": .64}

            required: True

            helper_text_mode: "on_error"

            multiline: False

            line_color_normal: app.theme_cls.accent_color

        MDTextField:

            id: nametwo

            hint_text: "Last Name"

            size_hint: 0.4, None

            pos_hint: {"center_x": .5, "center_y": .56}

            helper_text: "*Required"

            helper_text_mode: "on_focus"

            multiline: False

            line_color_normal: app.theme_cls.accent_color

        MDTextField:

            id: email

            hint_text: "Email Address"

            size_hint: 0.4, None

            pos_hint: {"center_x": .5, "center_y": .48}

            helper_text: "*Required"

            helper_text_mode: "on_focus"

            icon_right: "email"

            email: True

            multiline: False

            line_color_normal: app.theme_cls.accent_color

        MDTextField:

            hint_text: "Phone number"

            size_hint: 0.4, None

            pos_hint: {"center_x": .5, "center_y": .40}

            helper_text: "*Required"

            helper_text_mode: "on_focus"

            icon_right: "phone"

            multiline: False

            max_text_length: 10

            line_color_normal: app.theme_cls.accent_color

        MDTextField:

            id: password

            hint_text: "Password"

            size_hint: 0.4, None

            pos_hint: {"center_x": .5, "center_y": .32}

            helper_text: "*Required"

            helper_text_mode: "on_focus"

            password: True

            icon_right: 'key-variant'

            multiline: False

            line_color_normal: app.theme_cls.accent_color

        MDTextField:

            id: copassword

            hint_text: "Confirm Password"

            size_hint: 0.4, None

            pos_hint: {"center_x": .5, "center_y": .24}

            helper_text: "*Required"

            helper_text_mode: "on_focus"

            password: True

            icon_right: 'key-variant'

            multiline: False

            line_color_normal: app.theme_cls.accent_color

        MDRaisedButton:

            text: "Next"

            halign: "center"

            pos_hint: {"center_x":.5, "center_y":.15}

            theme_text_color: "Custom"

            text_color: 1,1,1,1

            font_size: "16sp"

            on_release: app.root.current = "signuptwo"

        MDTextButton:

            text: "Have an account? Login!"

            font_size: "13sp"

            halign: "center"

            pos_hint: {"center_x": .5, "center_y": .1}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

            on_release: app.root.current = "login"

        MDLabel:

            id: Name

            text: "Info"

            pos_hint: {"center_x": .9, "center_y": .8}

            font_style: "H6"

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDIconButton:

            id: name

            icon: "numeric-1-circle"

            pos_hint: {"center_x": .42, "center_y": .75}

            user_font_size: "35sp"

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDProgressBar:

            id: progress

            size_hint: 0.11, 0.01

            pos_hint: {"center_x": .495, "center_y":.75}

        MDLabel:

            id: Contact

            text: "Submit"

            pos_hint: {"center_x": 1.03, "center_y": .8}

            font_style: "H6"

            theme_text_color: "Custom"

        MDIconButton:

            id: contact

            icon: "numeric-2-circle"

            pos_hint: {"center_x": .57, "center_y": .75}

            user_font_size: "35sp"

            theme_text_color: "Custom"

<SignUptwo>:

    name: "signuptwo"

    MDFloatLayout:

        MDCard:

            size_hint: None, None

            size: (400, 550)

            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            elevation: 50

            padding: 20

            spacing: 30

        MDLabel:

            text: "Sign-Up"

            bold: True

            halign: "center"

            pos_hint: {"center_x": .5, "center_y": .9}

            font_style: "H4"

            MDTextField:

            id: age

            hint_text: "Age"

            helper_text_mode: "on_focus"

            icon_right: "number"

            size_hint: 0.4, None

            pos_hint: {"center_x": .5, "center_y": .57}

            helper_text: "*Required"

            max_text_length: 2

            line_color_normal: app.theme_cls.accent_color

        MDLabel:

            text: "Gender"

            pos_hint: {"center_x": .9, "center_y": .45}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDLabel:

            text: "Yes"

            pos_hint: {"center_x": 1.03, "center_y": .50}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDLabel:

            text: "No"

            pos_hint: {"center_x": 1.13, "center_y": .50}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDLabel:

            text: "Male"

            pos_hint: {"center_x": 1.03, "center_y": .45}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDLabel:

            text: "Female"

            pos_hint: {"center_x": 1.11, "center_y": .45}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, 1

        MDLabel:

            text: "Are you Vaccinated?"

            size_hint: 0.4, None

            pos_hint: {'center_x': .5, "center_y": .50}

            MDCheckbox:

            group: "group"

            size_hint_x: 0.07

            size_hint_y: 0.07

            pos_hint: {'center_x': .59, "center_y": .50}

            on_active: app.check(*args)

        MDCheckbox:

            group: "group"

            size_hint_x: 0.07

            size_hint_y: 0.07

            pos_hint: {'center_x': .69, "center_y": .50}

            on_active: app.check1(*args)

        MDCheckbox:

            group: "group1"

            size_hint_x: 0.07

            size_hint_y: 0.07

            pos_hint: {'center_x': .59, "center_y": .45}

            on_active: app.check2(*args)

        MDCheckbox:

            group: "group1"

            size_hint_x: 0.07

            size_hint_y: 0.07

            pos_hint: {'center_x': .69, "center_y": .45}

            on_active: app.check3(*args)

        MDRaisedButton:

            text: "Submit"

            pos_hint: {"center_x":.5, "center_y":.23}

            on_release: app.root.current = "riskeval"

        MDTextButton:

            text: "Modify Information!"

            font_size: "13sp"

            halign: "center"

            pos_hint: {"center_x": .5, "center_y": .15}

            theme_text_color: "Custom"

            text_color: 0, 0, 0, .6

            on_release: app.root.current = "signup"

        MDLabel:

            id: Name

            text: "Info"

            pos_hint: {"center_x": .9, "center_y": .8}

            font_style: "H6"

            theme_text_color: "Custom"

            text_color: 0,0,1,1

        MDIconButton:

            id: name

            icon: "check-decagram"

            pos_hint: {"center_x": .42, "center_y": .75}

            user_font_size: "35sp"

            theme_text_color: "Custom"

            text_color: 0,0,1,1

        MDProgressBar:

            id: progress

            size_hint_x: .11

            size_hint_y: .01

            pos_hint: {"center_x": .495, "center_y":.75}

            text_color: 0,0,1,1

        MDLabel:

            id: Contact

            text: "Submit"

            pos_hint: {"center_x": 1.03, "center_y": .8}

            font_style: "H6"

            theme_text_color: "Custom"

        MDIconButton:

            id: contact

            icon: "check-decagram"

            pos_hint: {"center_x": .57, "center_y": .75}

            user_font_size: "35sp"

            theme_text_color: "Custom"

<LoginScreen>:

        name: "login"

        MDFloatLayout:

            MDCard:

                size_hint: None, None

                size: (400, 550)

                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                elevation: 50

                padding: 20

                spacing: 30

            MDLabel:

                text: "LoginScreen"

                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                halign: "center"

                theme_text_color: "Custom"

                text_color: 1,1,1,1

                font_size: "35sp"

            MDTextField:

                hint_text: "UserName"

                size_hint: 0.4, None

                pos_hint: {"center_x": .5, "center_y": .6}

                required: True

                helper_text_mode: "on_error"

                icon_right: "account"

                multiline: False

                line_color_normal: app.theme_cls.accent_color

            MDTextField:

                hint_text: "Password"

                size_hint: 0.4, None

                pos_hint: {"center_x": .5, "center_y": .48}

                password: True

                required: True

                helper_text_mode: "on_error"

                icon_right: "eye-off"

                multiline: False

                line_color_normal: app.theme_cls.accent_color

            MDRaisedButton:

                text: "Login"

                pos_hint: {"center_x":.5, "center_y":.2}

                on_release: app.root.current = "riskeval"

                MDLabel:

                text: "Login"

                bold: True

                halign: "center"

                pos_hint: {"center_x": .5, "center_y": .8}

                font_style: "H4"

            MDTextButton:

                text: "Don't have an account? Click to create..."

                font_size: "13sp"

                halign: "center"

                pos_hint: {"center_x": .5, "center_y": .15}

                theme_text_color: "Custom"

                text_color: 0, 0, 0, 1

                on_release: app.root.current = "signup"

        <RiskEval>:

            id: riskevaluation

            name: "riskeval"

            MDFloatLayout:

            ScrollView:

            pos_hint: {'left': 1, 'top': 1}

            size_hint_y: .8

            do_scroll_x: False

            MDToolbar:

                id: toolbar

                title: "Risk Evaluation"

                pos_hint: {'top':1.0}

                md_bg_color: app.theme_cls.accent_color

                MDBottomAppBar:

                md_bg_color: app.theme_cls.accent_color

            MDToolbar:

                icon: 'git'

                type: 'bottom'

                mode: "end"

                MDLabel:

                id: debugarea

                theme_text_color: "Error"

                font_size: "24sp"

                Button:

                text: 'start'

                font_size: 12

                size: 75, 50

                size_hint: None, None

                pos_hint: {"center_x": .5, "center_y": .35}

                on_release: root.do_print()