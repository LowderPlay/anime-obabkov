style code:
    font "fonts/Hack-Regular.ttf"

screen frontend_screen:
    frame:
        background "#222222"
        padding (0, 0)
        align (0.5, 0.5)
        xysize (1640, 768)

        imagebutton:
            align (0.43, 0.05)
            idle "UI/skip.png"
            action Return(True)

        vbox:
            spacing 5
            for i in elements.values():
                hbox:
                    text "{color=#8B888F}<{/color}{color=#FC618D}[i.name]{/color}" style "code":
                        yalign 0.5
                    if i.name not in ["base", "roof"]:
                        text " {color=#5AD4E6}x{/color}{color=#8B888F}={/color}" style "code":
                            yalign 0.5
                        button:
                            if selected in horizontal or selected == "center":
                                action [SetField(i, "h", selected), SetVariable("selected", "")]
                            else:
                                action SetField(i, "h", "")
                            frame:
                                background "#000000"
                                text "{color=#FCE566}{u}[i.h]{/u}{/color}" style "code"
                    text " {color=#5AD4E6}y{/color}{color=#8B888F}={/color}" style "code":
                        yalign 0.5
                    button:
                        if selected in vertical or selected == "center":
                            action [SetField(i, "v", selected), SetVariable("selected", "")]
                        else:
                            action SetField(i, "v", "")
                        frame:
                            background "#000000"
                            text "{color=#FCE566}{u}[i.v]{/u}{/color}" style "code"
                    text "{color=#8B888F}/>{/color}" style "code":
                        yalign 0.5
        
        hbox:
            align (0.01, 0.99)
            spacing 5
            for i in horizontal + vertical + ["center"]:
                button:
                    if selected != i:
                        action SetVariable("selected", i)
                    else:
                        action SetVariable("selected", "")
                    frame:
                        if selected != i:
                            background "black"
                        text "[i]"

        frame:
            align (1.0, 0.0)
            xysize (768, 768)
            padding (0, 0)
            image "UI/frontend/bg.png"            
            frame:
                align (0.5, 0.5)
                xysize (408, 570)
                padding (0, 0)
                background "#00000000"
                for k, element in elements.items():
                    if not element.is_correct() and element.is_visible():
                        image "UI/frontend/cropped/[element.name].png":
                            align element.get_align()
            
            for k, element in elements.items():
                if element.is_correct() and element.is_visible():
                    if element.name.startswith("window"):
                        $ k = f"window_{element.h}"
                    image "UI/frontend/[k].png"
        imagebutton:
            align (0.5, 0.97)
            idle "UI/frontend/done.png"
            insensitive "UI/frontend/done_inactive.png"
            action [Return(True)] sensitive (check())

define elements = {
    "base": Element("base"),
    "roof": Element("roof"),
    "door": Element("door"),
    "window_left": Element("window"),
    "window_right": Element("window"),
}

define selected = ""

python early:
    horizontal = ["left", "right"]
    vertical = ["top", "bottom"]

    def check():
        return all([e.is_correct() for e in elements.values()]) and elements["window_left"].h != elements["window_right"].h


    def change(a, b):
        print(a, b)
        renpy.restart_interaction()

    class Element:
        def __init__(self, name):
            self.name = name
            self.h = ""
            self.v = ""
        
        def is_correct(self):
            correct = False
            correct |= self.name == "base" and self.v == "bottom"
            correct |= self.name == "roof" and self.v == "top"
            correct |= self.name == "window" and self.h == "left" and self.v == "center"
            correct |= self.name == "window" and self.h == "right" and self.v == "center"
            correct |= self.name == "door" and self.h == "center" and self.v == "bottom"

            return correct

        def is_visible(self):
            return (self.h != "" or self.name in ["base", "roof"]) and self.v != ""

        def get_align(self):
            x, y = 0.0, 0.0

            if self.h == "left":
                x = 0.0
            elif self.h == "center":
                x = 0.5
            elif self.h == "right":
                x = 1.0

            if self.v == "top":
                y = 0.0
            elif self.v == "center":
                y = 0.5 if self.name != "window" else 0.9
            elif self.v == "bottom":
                y = 1.0

            return (x, y)

    
    